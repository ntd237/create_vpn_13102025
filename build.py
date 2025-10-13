"""
Script tự động build VPN Connection Tool thành file .exe
"""

import subprocess
import sys
import os
import shutil
from pathlib import Path


def print_step(step_num, message):
    """In step với format đẹp."""
    print(f"\n{'='*60}")
    print(f"BƯỚC {step_num}: {message}")
    print(f"{'='*60}\n")


def run_command(cmd, description):
    """Chạy command với error handling."""
    print(f"▶ {description}...")
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        print(f"✅ {description} - Thành công!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Thất bại!")
        print(f"Error: {e.stderr}")
        return False


def main():
    """Main build process."""
    print("\n" + "="*60)
    print("VPN CONNECTION TOOL - BUILD SCRIPT")
    print("="*60)

    # Set environment variables để tránh MemoryError với Conda
    os.environ['PYINSTALLER_COMPILE_BOOTLOADER'] = '0'
    os.environ['PYINSTALLER_DISABLE_CONDA_SUPPORT'] = '1'
    print("\n💡 Đã set environment variables để tối ưu memory usage")
    
    # Bước 1: Check dependencies
    print_step(1, "Kiểm tra dependencies")
    
    if not run_command(
        "python --version",
        "Kiểm tra Python"
    ):
        print("❌ Python chưa được cài đặt!")
        sys.exit(1)
    
    # Bước 2: Install dependencies
    print_step(2, "Cài đặt dependencies")
    
    if not run_command(
        "pip install -r requirements.txt",
        "Cài đặt tất cả dependencies"
    ):
        print("❌ Không thể cài dependencies!")
        sys.exit(1)
    
    # Bước 3: Clean old builds
    print_step(3, "Dọn dẹp builds cũ")
    
    dirs_to_clean = ['build', 'dist']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            print(f"▶ Xóa thư mục {dir_name}/...")
            shutil.rmtree(dir_name)
            print(f"✅ Đã xóa {dir_name}/")
    
    # Bước 4: Build với PyInstaller
    print_step(4, "Build file .exe với PyInstaller")

    # Try với spec file trước
    success = run_command(
        "pyinstaller vpn_tool.spec --clean",
        "Build .exe từ spec file"
    )

    # Nếu fail, thử alternative method
    if not success:
        print("\n⚠️ Build với spec file thất bại!")
        print("💡 Đang thử alternative method (direct build)...\n")

        # Alternative: Build trực tiếp với command line options
        alt_cmd = (
            "pyinstaller --onefile --windowed "
            "--name VPN_Connection_Tool "
            "--add-data config.yaml;. "
            "--hidden-import PyQt5.QtCore "
            "--hidden-import PyQt5.QtGui "
            "--hidden-import PyQt5.QtWidgets "
            "--hidden-import requests "
            "--hidden-import yaml "
            "--hidden-import psutil "
            "--exclude-module matplotlib "
            "--exclude-module numpy "
            "--exclude-module pandas "
            "--exclude-module scipy "
            "--exclude-module PIL "
            "--exclude-module tkinter "
            "--exclude-module IPython "
            "--exclude-module jupyter "
            "--uac-admin "
            "--clean "
            "main_gui.py"
        )

        if not run_command(alt_cmd, "Build .exe với alternative method"):
            print("❌ Build thất bại với cả 2 methods!")
            print("\n💡 Gợi ý:")
            print("   1. Tăng RAM available (đóng apps khác)")
            print("   2. Tạo virtual environment mới với ít packages hơn")
            print("   3. Sử dụng Python environment thay vì Conda")
            sys.exit(1)

        print("✅ Build thành công với alternative method!")
    
    # Bước 5: Verify output
    print_step(5, "Kiểm tra kết quả")
    
    exe_path = Path("dist/VPN_Connection_Tool.exe")
    if exe_path.exists():
        size_mb = exe_path.stat().st_size / (1024 * 1024)
        print(f"✅ Build thành công!")
        print(f"\n📦 Thông tin file:")
        print(f"   Đường dẫn: {exe_path.absolute()}")
        print(f"   Kích thước: {size_mb:.2f} MB")
        print(f"\n💡 Hướng dẫn:")
        print(f"   1. File .exe nằm trong thư mục: dist/")
        print(f"   2. Chuột phải vào file → 'Run as Administrator'")
        print(f"   3. Hoặc gửi file này cho người khác, họ chỉ cần chạy!")
        print(f"\n⚠️ Lưu ý:")
        print(f"   - File cần quyền Administrator để kết nối VPN")
        print(f"   - OpenVPN vẫn cần được cài đặt trên máy đích")
    else:
        print("❌ Không tìm thấy file .exe!")
        sys.exit(1)
    
    # Bước 6: Create package
    print_step(6, "Tạo package phân phối")
    
    package_dir = Path("dist/VPN_Tool_Package")
    if package_dir.exists():
        shutil.rmtree(package_dir)
    
    package_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy exe
    shutil.copy2(exe_path, package_dir / "VPN_Connection_Tool.exe")
    
    # Copy config
    if Path("config.yaml").exists():
        shutil.copy2("config.yaml", package_dir / "config.yaml")
    
    # Create README
    readme_content = """# VPN Connection Tool

## Cài Đặt

### Yêu Cầu:
- Windows 10/11
- OpenVPN (tải từ: https://openvpn.net/community-downloads/)

### Cách Sử Dụng:
1. Cài đặt OpenVPN (nếu chưa có)
2. Chuột phải vào "VPN_Connection_Tool.exe"
3. Chọn "Run as Administrator"
4. Chọn quốc gia và click "Kết Nối VPN"

## Lưu Ý:
- Bắt buộc chạy với quyền Administrator
- OpenVPN sẽ chạy ngầm trong background
- Xem log trong ứng dụng để biết trạng thái

## Hỗ Trợ:
- Email: ntd237.work@gmail.com
- GitHub: https://github.com/ntd237
"""
    
    with open(package_dir / "README.txt", 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"✅ Đã tạo package tại: {package_dir.absolute()}")
    print(f"\n📦 Nội dung package:")
    print(f"   - VPN_Connection_Tool.exe ({size_mb:.2f} MB)")
    print(f"   - config.yaml")
    print(f"   - README.txt")
    
    print("\n" + "="*60)
    print("✅ BUILD HOÀN TẤT!")
    print("="*60)
    print(f"\n📦 Package sẵn sàng phân phối tại:")
    print(f"   {package_dir.absolute()}")
    print(f"\n💡 Có thể zip thư mục này và gửi cho người khác!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Build bị hủy bởi người dùng")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Lỗi không mong đợi: {e}")
        sys.exit(1)
