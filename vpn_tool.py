"""
VPN Connection Tool - CLI Interface
Công cụ kết nối VPN miễn phí, đơn giản.
"""

import argparse
import sys
import time
import logging
from typing import Optional

from core import VPNCore
from utils import (
    load_config, 
    setup_logging, 
    validate_country_code,
    format_server_info,
    check_admin_rights,
    print_banner
)


# === CẤU HÌNH TOÀN CỤC ===
CONFIG_FILE = "config.yaml"
VERSION = "1.0.0"


def parse_arguments():
    """
    Phân tích tham số dòng lệnh.
    
    Returns:
        Namespace chứa các arguments
    """
    parser = argparse.ArgumentParser(
        description='VPN Connection Tool - Free VPN connection made easy',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Usage examples:
  %(prog)s list                    # List all available VPN countries
  %(prog)s connect US              # Connect VPN to USA
  %(prog)s connect JP --admin      # Connect to Japan with admin rights
  %(prog)s status                  # Check connection status
  %(prog)s disconnect              # Disconnect VPN
  %(prog)s auto-reconnect US       # Auto reconnect when disconnected
        '''
    )
    
    parser.add_argument(
        'command',
        choices=['list', 'connect', 'disconnect', 'status', 'auto-reconnect'],
        help='Command to execute'
    )
    
    parser.add_argument(
        'country',
        nargs='?',
        help='Country code (e.g.: US, JP, UK, KR, SG)'
    )
    
    parser.add_argument(
        '--admin',
        action='store_true',
        help='Run with Administrator privileges (Windows)'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show detailed output'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version=f'%(prog)s {VERSION}'
    )
    
    return parser.parse_args()


def list_countries(vpn_core: VPNCore):
    """
    Liệt kê tất cả quốc gia có VPN servers.
    
    Args:
        vpn_core: Instance của VPNCore
    """
    try:
        print("\n🌍 Đang tải danh sách servers...\n")
        countries = vpn_core.list_countries()
        
        print(f"📋 Tìm thấy {len(countries)} quốc gia:\n")
        
        # Sắp xếp theo tên quốc gia
        sorted_countries = sorted(
            countries.items(),
            key=lambda x: x[1][0]['country']
        )
        
        for country_code, servers in sorted_countries:
            best_server = servers[0]  # Server tốt nhất
            print(f"  • {best_server['country']:20} ({country_code})  "
                  f"- {len(servers)} server(s) - "
                  f"Speed: {best_server['speed']/1000000:.1f} Mbps")
        
        print(f"\n💡 Sử dụng: vpn_tool.py connect <MÃ_QUỐC_GIA>\n")
        
    except Exception as e:
        logging.error(f"Lỗi khi liệt kê servers: {e}")
        sys.exit(1)


def connect_vpn(vpn_core: VPNCore, country_code: str, require_admin: bool = False):
    """
    Kết nối VPN đến quốc gia chỉ định.
    
    Args:
        vpn_core: Instance của VPNCore
        country_code: Mã quốc gia
        require_admin: Có yêu cầu quyền admin không
    """
    # Validate mã quốc gia
    if not validate_country_code(country_code):
        logging.error(f"❌ Mã quốc gia không hợp lệ: {country_code}")
        logging.info("Mã quốc gia phải là 2 ký tự chữ (VD: US, JP, UK)")
        sys.exit(1)
    
    # Kiểm tra quyền admin nếu cần
    if require_admin and not check_admin_rights():
        logging.warning("⚠️  Tool không chạy với quyền Administrator!")
        logging.info("Thử kết nối bình thường trước...")
    
    try:
        # Tải config
        print(f"\n🔍 Tìm kiếm VPN server tốt nhất cho {country_code.upper()}...\n")
        config_path = vpn_core.download_config(country_code)
        
        if not config_path:
            logging.error(f"❌ Không thể tải config cho {country_code.upper()}")
            logging.info("\n💡 Xem danh sách quốc gia: vpn_tool.py list")
            sys.exit(1)
        
        # Kết nối
        print(f"\n🔌 Đang kết nối VPN...\n")
        success = vpn_core.connect(config_path, require_admin)
        
        if success:
            print("\n" + "="*50)
            print("✅ OpenVPN đã được khởi động thành công!")
            print("="*50)
            print("\n📌 LƯU Ý QUAN TRỌNG:")
            print("   • OpenVPN đang chạy trong background (process độc lập)")
            print("   • Bạn có thể đóng cửa sổ này, VPN vẫn hoạt động")
            print("   • Cửa sổ OpenVPN console sẽ mở riêng (có thể minimize)")
            print("\n💡 LỆNH HỮU ÍCH:")
            print("   • Kiểm tra: python vpn_tool.py status")
            print("   • Ngắt kết nối: python vpn_tool.py disconnect")
            print("\n⏳ Đợi khoảng 10-30 giây để VPN kết nối hoàn tất.")
            print("   Sau đó chạy 'status' để xác nhận.\n")
        else:
            logging.error("\n❌ Kết nối VPN thất bại!")
            if not require_admin:
                logging.info("💡 Thử lại với quyền admin: vpn_tool.py connect {} --admin".format(country_code))
            sys.exit(1)
            
    except Exception as e:
        logging.error(f"Lỗi khi kết nối: {e}")
        sys.exit(1)


def disconnect_vpn(vpn_core: VPNCore):
    """
    Ngắt kết nối VPN.
    
    Args:
        vpn_core: Instance của VPNCore
    """
    try:
        print("\n🔌 Đang ngắt kết nối VPN...\n")
        success = vpn_core.disconnect()
        
        if success:
            print("✅ Đã ngắt kết nối VPN!\n")
        else:
            logging.error("❌ Không thể ngắt kết nối")
            sys.exit(1)
            
    except Exception as e:
        logging.error(f"Lỗi khi ngắt kết nối: {e}")
        sys.exit(1)


def check_status(vpn_core: VPNCore):
    """
    Kiểm tra trạng thái kết nối VPN.
    
    Args:
        vpn_core: Instance của VPNCore
    """
    try:
        status = vpn_core.get_status()
        
        print("\n📊 TRẠNG THÁI KẾT NỐI VPN\n")
        print("=" * 40)
        
        if status['connected']:
            print("🟢 Trạng thái: ĐANG KẾT NỐI")
            if status['ip_address']:
                print(f"🌐 IP công khai: {status['ip_address']}")
        else:
            print("🔴 Trạng thái: CHƯA KẾT NỐI")
        
        print("=" * 40)
        print()
        
    except Exception as e:
        logging.error(f"Lỗi khi kiểm tra status: {e}")
        sys.exit(1)


def auto_reconnect(vpn_core: VPNCore, country_code: str, interval: int = 10):
    """
    Tự động kết nối lại khi mất kết nối.
    
    Args:
        vpn_core: Instance của VPNCore
        country_code: Mã quốc gia
        interval: Khoảng thời gian kiểm tra (giây)
    """
    print(f"\n🔄 Chế độ tự động kết nối lại đã BẬT")
    print(f"   Quốc gia: {country_code.upper()}")
    print(f"   Kiểm tra mỗi: {interval}s")
    print("   Nhấn Ctrl+C để dừng\n")
    
    # Kết nối lần đầu
    connect_vpn(vpn_core, country_code)
    
    try:
        while True:
            time.sleep(interval)
            
            if not vpn_core.is_connected():
                logging.warning("⚠️  Mất kết nối! Đang kết nối lại...")
                connect_vpn(vpn_core, country_code)
            else:
                logging.info("✅ VPN vẫn đang kết nối")
                
    except KeyboardInterrupt:
        print("\n\n🛑 Dừng auto-reconnect")
        disconnect_vpn(vpn_core)


def main():
    """Entry point chính của công cụ."""
    try:
        # Print banner
        print_banner()
        
        # Parse arguments
        args = parse_arguments()
        
        # Load config
        try:
            config = load_config(CONFIG_FILE)
        except FileNotFoundError:
            logging.warning(f"⚠️  Không tìm thấy {CONFIG_FILE}, sử dụng config mặc định")
            config = {}
        
        # Setup logging
        logger = setup_logging(config)
        
        if args.verbose:
            logger.setLevel(logging.DEBUG)
        
        # Khởi tạo VPN Core
        config_dir = config.get('paths', {}).get('config_dir', 'vpn_configs')
        vpn_core = VPNCore(config_dir=config_dir)
        
        # Xử lý commands
        if args.command == 'list':
            list_countries(vpn_core)
            
        elif args.command == 'connect':
            if not args.country:
                logging.error("❌ Thiếu mã quốc gia!")
                logging.info("💡 Sử dụng: vpn_tool.py connect <MÃ_QUỐC_GIA>")
                logging.info("💡 Xem danh sách: vpn_tool.py list")
                sys.exit(1)
            
            connect_vpn(vpn_core, args.country, args.admin)
            
        elif args.command == 'disconnect':
            disconnect_vpn(vpn_core)
            
        elif args.command == 'status':
            check_status(vpn_core)
            
        elif args.command == 'auto-reconnect':
            if not args.country:
                logging.error("❌ Thiếu mã quốc gia!")
                logging.info("💡 Sử dụng: vpn_tool.py auto-reconnect <MÃ_QUỐC_GIA>")
                sys.exit(1)
            
            reconnect_interval = config.get('connection', {}).get('reconnect_interval', 10)
            auto_reconnect(vpn_core, args.country, reconnect_interval)
        
        return 0
        
    except KeyboardInterrupt:
        print("\n\n👋 Đã hủy bởi người dùng")
        return 0
        
    except Exception as e:
        logging.error(f"❌ Lỗi không mong đợi: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
