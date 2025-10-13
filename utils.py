"""
Helper utilities cho VPN tool.
"""

import os
import logging
import yaml
from typing import Dict, Any


def load_config(config_path: str = "config.yaml") -> Dict[str, Any]:
    """
    Đọc file cấu hình YAML.
    
    Args:
        config_path: Đường dẫn file config
        
    Returns:
        Dict chứa cấu hình
        
    Raises:
        FileNotFoundError: Nếu file không tồn tại
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"File config không tồn tại: {config_path}")
    
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    return config


def setup_logging(config: Dict[str, Any]) -> logging.Logger:
    """
    Thiết lập logging theo config.
    
    Args:
        config: Dict cấu hình
        
    Returns:
        Logger đã được cấu hình
    """
    import sys
    
    log_config = config.get('logging', {})
    log_level = getattr(logging, log_config.get('level', 'INFO'))
    log_format = log_config.get('format', '%(asctime)s - %(levelname)s - %(message)s')
    
    # Setup UTF-8 encoding cho console trên Windows
    if sys.platform == 'win32':
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.detach())
    
    # Setup root logger
    logging.basicConfig(
        level=log_level,
        format=log_format,
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(
                config.get('paths', {}).get('log_file', 'vpn_tool.log'),
                encoding='utf-8'
            )
        ]
    )
    
    return logging.getLogger(__name__)


def validate_country_code(country_code: str) -> bool:
    """
    Validate mã quốc gia.
    
    Args:
        country_code: Mã quốc gia cần validate
        
    Returns:
        True nếu hợp lệ
    """
    if not country_code:
        return False
    
    # Mã quốc gia phải là 2 ký tự chữ
    if len(country_code) != 2:
        return False
    
    if not country_code.isalpha():
        return False
    
    return True


def format_server_info(server: Dict) -> str:
    """
    Format thông tin server để hiển thị.
    
    Args:
        server: Dict chứa server info
        
    Returns:
        String đã format
    """
    speed_mbps = server.get('speed', 0) / 1000000
    uptime = server.get('uptime', 0)
    
    return (
        f"🌍 {server.get('country', 'Unknown')} ({server.get('country_code', '??')})\n"
        f"   Server: {server.get('hostname', 'N/A')}\n"
        f"   IP: {server.get('ip', 'N/A')}\n"
        f"   Speed: {speed_mbps:.1f} Mbps\n"
        f"   Uptime: {uptime} ms\n"
        f"   Score: {server.get('score', 0)}"
    )


def check_admin_rights() -> bool:
    """
    Kiểm tra có quyền Administrator không.
    
    Returns:
        True nếu đang chạy với quyền admin
    """
    import ctypes
    import os
    
    if os.name == 'nt':  # Windows
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            return False
    else:  # Linux/Mac
        return os.geteuid() == 0


def print_banner():
    """In banner khi khởi động tool."""
    banner = """
    =========================================
        VPN CONNECTION TOOL v1.0
        Ket noi VPN mien phi de dang
    =========================================
    """
    print(banner)
