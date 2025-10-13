# 📦 BUILD TO .EXE

## 🎯 Mục Đích

Đóng gói VPN Connection Tool thành file **VPN_Connection_Tool.exe** standalone (50-80MB) để phân phối. Người dùng chỉ cần:
1. Cài OpenVPN
2. Chạy .exe với quyền Admin
3. Sử dụng!

---

## 🚀 BUILD NHANH (3 Bước)

### Bước 1: Cài Dependencies
```bash
cd D:\Workspace\Tools\create_vpn
pip install -r requirements.txt
```

### Bước 2: Fix Lỗi Pathlib (Nếu Dùng Conda)
```bash
# Gỡ các package pathlib thừa (conflict với PyInstaller)
pip uninstall pathlib pathlib2 pathlib-abc -y
```

### Bước 3: Chạy Build Script
```bash
python build.py
```

**Kết quả**: File `.exe` nằm trong `dist/VPN_Tool_Package/VPN_Connection_Tool.exe`

---

## 📊 Build Output

### Package Structure:
```
dist/
├── VPN_Connection_Tool.exe          # Single executable
└── VPN_Tool_Package/                # Distribution package
    ├── VPN_Connection_Tool.exe      # Main app (50-80MB)
    ├── config.yaml                  # Config file
    └── README.txt                   # User instructions
```

### File Size: ~50-80 MB
```
Total: ~60 MB
├── Python Runtime: ~10 MB
├── PyQt5 Libraries: ~40 MB
├── Other Libraries: ~5 MB
└── App Code: ~5 MB
```

---

## 🛠️ Build Thủ Công (Nếu Cần)

### Method 1: Sử dụng Spec File
```bash
# Cài PyInstaller
pip install PyInstaller>=5.0.0

# Build từ spec file
pyinstaller vpn_tool.spec --clean

# Kết quả trong dist/
```

### Method 2: Lệnh Trực Tiếp
```bash
pyinstaller main_gui.py \
  --name "VPN_Connection_Tool" \
  --onefile \
  --windowed \
  --uac-admin \
  --add-data "config.yaml:." \
  --hidden-import PyQt5.QtCore \
  --hidden-import PyQt5.QtGui \
  --hidden-import PyQt5.QtWidgets \
  --exclude-module matplotlib \
  --exclude-module numpy
```

---

## 📋 Build Script Features

Script `build.py` tự động thực hiện:

1. ✅ **Check Python**: Kiểm tra Python version
2. ✅ **Install Dependencies**: Cài tất cả requirements
3. ✅ **Clean Old Builds**: Xóa build/dist cũ
4. ✅ **Run PyInstaller**: Build từ spec file
5. ✅ **Verify Output**: Kiểm tra .exe đã tạo
6. ✅ **Create Package**: Tạo package phân phối với README

**Output Example**:
```
============================================================
VPN CONNECTION TOOL - BUILD SCRIPT
============================================================

BƯỚC 1: Kiểm tra dependencies
✅ Kiểm tra Python - Thành công!

BƯỚC 2: Cài đặt dependencies
✅ Cài đặt tất cả dependencies - Thành công!

BƯỚC 3: Dọn dẹp builds cũ
✅ Đã xóa build/
✅ Đã xóa dist/

BƯỚC 4: Build file .exe với PyInstaller
✅ Build .exe từ spec file - Thành công!

BƯỚC 5: Kiểm tra kết quả
✅ Build thành công!

📦 Thông tin file:
   Đường dẫn: D:\...\dist\VPN_Connection_Tool.exe
   Kích thước: 62.5 MB

BƯỚC 6: Tạo package phân phối
✅ Đã tạo package tại: dist\VPN_Tool_Package

============================================================
✅ BUILD HOÀN TẤT!
============================================================
```

---

## ⚙️ Spec File Config

File `vpn_tool.spec` chứa config cho PyInstaller:

```python
# Entry point
['main_gui.py']

# Include data files
datas=[
    ('config.yaml', '.'),
]

# Hidden imports (auto-detect không được)
hiddenimports=[
    'PyQt5.QtCore',
    'PyQt5.QtGui',
    'PyQt5.QtWidgets',
    'requests',
    'yaml',
    'psutil',
]

# Exclude unused libraries (giảm size)
excludes=[
    'matplotlib',
    'numpy',
    'pandas',
    'scipy',
    'PIL',
    'tkinter',
]

# EXE config
name='VPN_Connection_Tool'
console=False        # GUI only, không hiện console
uac_admin=True       # Yêu cầu Admin rights
upx=True            # Nén với UPX
```

---

## 🐛 Troubleshooting

### ❌ Lỗi: "pathlib package is obsolete"

**Nguyên nhân**: Có package `pathlib` cũ trong môi trường

**Giải pháp**:
```bash
pip uninstall pathlib pathlib2 pathlib-abc -y
python build.py
```

### ❌ Lỗi: "PyInstaller not found"

**Giải pháp**:
```bash
pip install PyInstaller>=5.0.0
```

### ❌ Lỗi: "Failed to execute script"

**Nguyên nhân**: Thiếu hidden imports

**Giải pháp**: Thêm vào `hiddenimports` trong `vpn_tool.spec`:
```python
hiddenimports=[
    'PyQt5.QtCore',
    'PyQt5.QtGui',
    'PyQt5.QtWidgets',
    # Thêm module bị thiếu ở đây
]
```

### ❌ File .exe quá lớn (>100MB)

**Giải pháp**: Thêm vào `excludes` trong spec file:
```python
excludes=[
    'matplotlib',
    'numpy',
    'pandas',
    'scipy',
    'PIL',
    'tkinter',
    'unittest',
    'xml',
]
```

### ❌ .exe không chạy trên máy khác

**Nguyên nhân**: Thiếu Visual C++ Redistributable

**Giải pháp**: User cài:
```
https://aka.ms/vs/17/release/vc_redist.x64.exe
```

### ❌ Antivirus chặn .exe

**Nguyên nhân**: False positive (PyInstaller .exe thường bị nghi ngờ)

**Giải pháp**:
1. Add exception trong antivirus
2. Hoặc upload lên VirusTotal để verify
3. Hoặc code signing (cần certificate)

---

## 🧪 Testing

### Test Trên Máy Build:
```bash
# Chạy .exe
dist\VPN_Connection_Tool.exe

# Hoặc chuột phải → "Run as Administrator"
```

### Checklist:
- [ ] Build completes without errors
- [ ] .exe size < 100MB
- [ ] .exe runs successfully
- [ ] UAC admin prompt appears
- [ ] GUI loads correctly
- [ ] All features work (list, connect, disconnect, status)
- [ ] No console window appears
- [ ] OpenVPN runs in background

### Test Trên Máy Clean Windows:
1. Copy `.exe` sang máy khác
2. Cài OpenVPN
3. Run as Administrator
4. Test all features

---

## 📤 Phân Phối

### Option 1: Gửi Trực Tiếp .exe
- File: `VPN_Connection_Tool.exe` (~60MB)
- User: Chỉ cần OpenVPN + Run as Admin

### Option 2: Gửi Package (Recommended)
```bash
# Zip package
Compress-Archive -Path "dist\VPN_Tool_Package" -DestinationPath "VPN_Tool.zip"
```

Package chứa:
- `VPN_Connection_Tool.exe`
- `config.yaml`
- `README.txt` (hướng dẫn)

### Hướng Dẫn Cho User:

**Yêu Cầu**:
- Windows 10/11
- OpenVPN: https://openvpn.net/community-downloads/

**Cách Dùng**:
1. Cài OpenVPN (nếu chưa có)
2. Chuột phải `.exe` → **"Run as Administrator"**
3. Chọn quốc gia → Click "Kết Nối VPN"
4. Sử dụng!

---

## 🎨 Customization

### Thêm Icon:
```python
# Trong vpn_tool.spec
icon='icon.ico'  # File .ico (256x256)
```

### Đổi Tên:
```python
name='MyVPNTool'
```

### Thêm Data Files:
```python
datas=[
    ('config.yaml', '.'),
    ('assets/*', 'assets'),
    ('docs/*', 'docs'),
]
```

---

## 💡 Best Practices

### 1. Build Trong Virtual Environment
```bash
python -m venv build_env
build_env\Scripts\activate
pip install -r requirements.txt
python build.py
```

### 2. Test Trên VM
- Build và test trên clean Windows VM
- Đảm bảo không có dependencies thừa

### 3. Version Control
- Add `/build` và `/dist` vào `.gitignore`
- Chỉ commit source code và spec file

### 4. Automated Testing
```bash
# Test script tự động
dist\VPN_Connection_Tool.exe --test
```

---

## 📊 Build Checklist

Trước khi phân phối:

- [ ] ✅ Build thành công không lỗi
- [ ] ✅ File size hợp lý (< 100MB)
- [ ] ✅ Test trên máy build: OK
- [ ] ✅ Test trên máy clean: OK
- [ ] ✅ UAC admin prompt hoạt động
- [ ] ✅ Tất cả features OK
- [ ] ✅ Không có console window
- [ ] ✅ OpenVPN chạy ẩn
- [ ] ✅ README.txt rõ ràng
- [ ] ✅ Config file included

---

## 🚀 Quick Commands

```bash
# Full build process
pip install -r requirements.txt
pip uninstall pathlib pathlib2 pathlib-abc -y
python build.py

# Clean and rebuild
rmdir /s /q build dist
python build.py

# Test exe
dist\VPN_Connection_Tool.exe

# Create distribution zip
Compress-Archive -Path "dist\VPN_Tool_Package" -DestinationPath "VPN_Tool.zip"
```

---

**Build thành công và sẵn sàng phân phối! 🎉**
