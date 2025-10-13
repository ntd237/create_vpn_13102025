"""
Module xử lý logic VPN cốt lõi.
Độc lập với CLI interface, có thể tái sử dụng.
"""

import os
import json
import subprocess
import time
import requests
from typing import List, Dict, Optional
import logging

logger = logging.getLogger(__name__)


# === CẤU HÌNH ===
PROTONVPN_API = "https://api.protonvpn.ch/vpn/logicals"
FREEVPN_API = "https://www.vpngate.net/api/iphone/"  # Backup: VPN Gate (public free VPN)
CONFIG_EXTENSION = ".ovpn"


class VPNCore:
    """Class quản lý kết nối VPN."""
    
    def __init__(self, config_dir: str = "vpn_configs"):
        """
        Khởi tạo VPN Core.
        
        Args:
            config_dir: Thư mục lưu config files
        """
        self.config_dir = config_dir
        self.current_process = None
        self.pid_file = os.path.join(config_dir, 'vpn.pid')
        self._ensure_config_dir()
    
    def _ensure_config_dir(self):
        """Tạo thư mục config nếu chưa có."""
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir)
            logger.info(f"Đã tạo thư mục config: {self.config_dir}")
    
    def fetch_vpngate_servers(self) -> List[Dict]:
        """
        Lấy danh sách VPN servers miễn phí từ VPN Gate.
        VPN Gate là dịch vụ hoàn toàn miễn phí, không cần đăng ký.
        
        Returns:
            List các server info dạng dict
            
        Raises:
            Exception: Nếu không thể fetch được servers
        """
        try:
            logger.info("Đang tải danh sách servers từ VPN Gate...")
            # Bypass proxy để tránh lỗi connection
            response = requests.get(FREEVPN_API, timeout=10, proxies={'http': None, 'https': None})
            response.raise_for_status()
            
            # Parse CSV response (skip header)
            lines = response.text.strip().split('\n')
            servers = []
            
            # Skip first 2 lines (headers) and last line (*END)
            for line in lines[2:-1]:
                parts = line.split(',')
                if len(parts) >= 15:
                    servers.append({
                        'hostname': parts[0],
                        'ip': parts[1],
                        'country': parts[5],
                        'country_code': parts[6],
                        'speed': int(parts[4]) if parts[4].isdigit() else 0,
                        'uptime': int(parts[10]) if parts[10].isdigit() else 0,
                        'score': int(parts[2]) if parts[2].isdigit() else 0,
                        'config_data': parts[14]  # Base64 encoded .ovpn
                    })
            
            # Sắp xếp theo tốc độ và uptime
            servers.sort(key=lambda x: (x['speed'], x['uptime']), reverse=True)
            
            logger.info(f"✅ Tìm thấy {len(servers)} servers khả dụng")
            return servers
            
        except Exception as e:
            logger.error(f"Lỗi khi fetch servers: {e}")
            raise
    
    def list_countries(self) -> Dict[str, List[Dict]]:
        """
        Lấy danh sách quốc gia có VPN servers.
        
        Returns:
            Dict với key là country code, value là list servers
        """
        servers = self.fetch_vpngate_servers()
        
        countries = {}
        for server in servers:
            country = server['country_code']
            if country not in countries:
                countries[country] = []
            countries[country].append(server)
        
        return countries
    
    def download_config(self, country_code: str) -> Optional[str]:
        """
        Tải config file cho quốc gia chỉ định.
        Chọn server tốt nhất (nhanh nhất, uptime cao).
        
        Args:
            country_code: Mã quốc gia (VD: US, JP, UK)
            
        Returns:
            Đường dẫn file config đã tải, hoặc None nếu thất bại
        """
        try:
            countries = self.list_countries()
            country_code = country_code.upper()
            
            if country_code not in countries:
                logger.error(f"Không tìm thấy servers cho quốc gia: {country_code}")
                available = ', '.join(sorted(countries.keys()))
                logger.info(f"Các quốc gia khả dụng: {available}")
                return None
            
            # Chọn server tốt nhất
            server = countries[country_code][0]
            logger.info(f"Chọn server: {server['hostname']} ({server['country']})")
            logger.info(f"Speed: {server['speed']/1000000:.1f} Mbps, Uptime: {server['uptime']} ms")
            
            # Decode config data (base64)
            import base64
            config_data = base64.b64decode(server['config_data']).decode('utf-8')
            
            # Lưu file config
            config_filename = f"{country_code}_{server['hostname']}{CONFIG_EXTENSION}"
            config_path = os.path.join(self.config_dir, config_filename)
            
            with open(config_path, 'w', encoding='utf-8') as f:
                f.write(config_data)
            
            logger.info(f"✅ Đã tải config: {config_path}")
            return config_path
            
        except Exception as e:
            logger.error(f"Lỗi khi tải config: {e}")
            return None
    
    def connect(self, config_path: str, require_admin: bool = False) -> bool:
        """
        Kết nối VPN sử dụng config file.
        
        Args:
            config_path: Đường dẫn file .ovpn
            require_admin: Có yêu cầu quyền admin không
            
        Returns:
            True nếu thành công, False nếu thất bại
        """
        if not os.path.exists(config_path):
            logger.error(f"File config không tồn tại: {config_path}")
            return False
        
        try:
            # Kiểm tra OpenVPN có được cài đặt
            openvpn_cmd = self._find_openvpn()
            if not openvpn_cmd:
                logger.error("❌ OpenVPN chưa được cài đặt!")
                logger.info("Vui lòng cài đặt OpenVPN: https://openvpn.net/community-downloads/")
                return False
            
            logger.info(f"Đang kết nối VPN: {config_path}")
            
            # Tạo lệnh kết nối
            cmd = [openvpn_cmd, '--config', config_path]
            
            if require_admin:
                logger.warning("⚠️  Cần quyền Administrator để kết nối VPN")
            
            # Chạy OpenVPN process ẩn (không hiện console)
            # Trên Windows: CREATE_NO_WINDOW để chạy ngầm
            if os.name == 'nt':  # Windows
                # CREATE_NO_WINDOW = 0x08000000 - Chạy process không hiện cửa sổ
                CREATE_NO_WINDOW = 0x08000000
                self.current_process = subprocess.Popen(
                    cmd,
                    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | CREATE_NO_WINDOW,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
            else:  # Linux/Mac
                self.current_process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    start_new_session=True
                )
            
            # Lưu PID để quản lý sau
            with open(self.pid_file, 'w') as f:
                f.write(str(self.current_process.pid))
            
            logger.info(f"Đã khởi động OpenVPN process (PID: {self.current_process.pid})")
            
            # Đợi một chút để kiểm tra kết nối
            logger.info("Đang chờ OpenVPN khởi động...")
            for i in range(10):  # Check trong 10 giây
                time.sleep(1)
                if self.is_connected():
                    logger.info("✅ Đã kết nối VPN thành công!")
                    return True
                # Kiểm tra process còn chạy không
                if self.current_process.poll() is not None:
                    logger.error("OpenVPN process đã dừng. Kiểm tra quyền admin hoặc config file.")
                    return False
            
            logger.warning("⚠️  OpenVPN đang chạy nhưng chưa kết nối xong.")
            logger.info("🔍 Chạy 'vpn_tool.py status' sau ít phút để kiểm tra.")
            return True
                
        except Exception as e:
            logger.error(f"Lỗi khi kết nối: {e}")
            return False
    
    def disconnect(self) -> bool:
        """
        Ngắt kết nối VPN hiện tại.
        
        Returns:
            True nếu thành công
        """
        try:
            # Đọc PID từ file nếu có
            if os.path.exists(self.pid_file):
                try:
                    with open(self.pid_file, 'r') as f:
                        pid = int(f.read().strip())
                    
                    import psutil
                    if psutil.pid_exists(pid):
                        proc = psutil.Process(pid)
                        proc.terminate()
                        proc.wait(timeout=5)
                        logger.info(f"✅ Đã ngắt OpenVPN process (PID: {pid})")
                    
                    os.remove(self.pid_file)
                except Exception as e:
                    logger.warning(f"Không thể kill process từ PID file: {e}")
            
            # Fallback: kill tất cả OpenVPN processes
            killed = self._kill_openvpn_processes()
            if killed:
                logger.info(f"✅ Đã ngắt {killed} kết nối VPN")
            else:
                logger.info("ℹ️  Không có kết nối VPN nào đang hoạt động")
            
            self.current_process = None
            return True
                    
        except Exception as e:
            logger.error(f"Lỗi khi ngắt kết nối: {e}")
            return False
    
    def is_connected(self) -> bool:
        """
        Kiểm tra VPN có đang kết nối không.
        
        Returns:
            True nếu đang kết nối
        """
        # Kiểm tra process còn chạy
        if self.current_process and self.current_process.poll() is None:
            return True
        
        # Kiểm tra có OpenVPN process nào đang chạy
        import psutil
        for proc in psutil.process_iter(['name']):
            try:
                if 'openvpn' in proc.info['name'].lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        return False
    
    def get_status(self) -> Dict:
        """
        Lấy trạng thái kết nối VPN chi tiết.
        
        Returns:
            Dict chứa thông tin status
        """
        connected = self.is_connected()
        
        status = {
            'connected': connected,
            'process_running': self.current_process is not None,
            'ip_address': self._get_public_ip() if connected else None
        }
        
        return status
    
    def _find_openvpn(self) -> Optional[str]:
        """
        Tìm OpenVPN executable.
        
        Returns:
            Đường dẫn đến openvpn.exe hoặc None
        """
        # Các vị trí thường gặp trên Windows
        possible_paths = [
            r"C:\Program Files\OpenVPN\bin\openvpn.exe",
            r"C:\Program Files (x86)\OpenVPN\bin\openvpn.exe",
            "openvpn"  # Trong PATH
        ]
        
        for path in possible_paths:
            try:
                result = subprocess.run(
                    [path, '--version'],
                    capture_output=True,
                    timeout=2
                )
                if result.returncode == 0:
                    return path
            except:
                continue
        
        return None
    
    def _kill_openvpn_processes(self) -> int:
        """
        Kill tất cả OpenVPN processes.
        
        Returns:
            Số process đã kill
        """
        import psutil
        killed = 0
        
        for proc in psutil.process_iter(['name', 'pid']):
            try:
                if 'openvpn' in proc.info['name'].lower():
                    proc.terminate()
                    killed += 1
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        return killed
    
    def _get_public_ip(self) -> Optional[str]:
        """
        Lấy địa chỉ IP công khai hiện tại.
        
        Returns:
            IP address hoặc None
        """
        try:
            response = requests.get('https://api.ipify.org?format=json', timeout=5, proxies={'http': None, 'https': None})
            return response.json().get('ip')
        except:
            return None
