"""
VPN Connection Tool - GUI Entry Point
Chạy file này để khởi động giao diện đồ họa.
"""

import sys
import ctypes

def is_admin():
    """Kiểm tra xem script có đang chạy với quyền admin không."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """Request admin privileges và restart script."""
    if sys.platform == 'win32':
        try:
            # Get the command to run
            script = sys.argv[0]
            params = ' '.join([script] + sys.argv[1:])
            
            # Request admin elevation
            ctypes.windll.shell32.ShellExecuteW(
                None, 
                "runas",  # Run as admin
                sys.executable,  # python.exe
                params,
                None,
                1  # SW_SHOWNORMAL
            )
            sys.exit(0)
        except Exception as e:
            print(f"Lỗi khi request admin: {e}")
            sys.exit(1)

if __name__ == '__main__':
    # Kiểm tra admin rights
    if not is_admin():
        print("⚠️  App cần quyền Administrator để kết nối VPN")
        print("🔄 Đang request admin privileges...")
        run_as_admin()
    else:
        print("✅ App đang chạy với quyền Administrator")
        from vpn_gui import main
        main()
