# 🌐 VPN CONNECTION TOOL

## 📝 Giới Thiệu

**VPN Connection Tool** là công cụ kết nối VPN miễn phí với **3 chế độ sử dụng**:

1. 🖥️ **GUI (Desktop App)** - Giao diện đồ họa đẹp mắt, dễ sử dụng
2. ⌨️ **CLI (Command Line)** - Dành cho power users và automation  
3. 📦 **Standalone .EXE** - File độc lập, không cần cài Python

---

## ✨ Tính Năng Chính

- 🌍 **50+ Quốc Gia**: Hỗ trợ kết nối VPN đến hơn 50 quốc gia
- 🆓 **Hoàn Toàn Miễn Phí**: Sử dụng VPN Gate (public free VPN)
- 🚀 **Kết Nối Nhanh**: Tự động chọn server tốt nhất
- 🔄 **Auto-Reconnect**: Tự động kết nối lại khi mất kết nối
- 📊 **Real-time Status**: Hiển thị trạng thái và IP công khai
- 🛡️ **Không Cần Đăng Ký**: Không cần tạo tài khoản

---

## 🎯 Chọn Chế Độ Phù Hợp

### 🖥️ GUI Mode (Khuyến Nghị cho người dùng thông thường)

**Phù hợp cho**:
- ✅ Người dùng muốn giao diện đơn giản, click chuột
- ✅ Visual learners (thích thấy interface)
- ✅ Không quen với terminal/command line

**Chạy**:
```bash
python main_gui.py
```

---

### ⌨️ CLI Mode (Dành cho power users)

**Phù hợp cho**:
- ✅ Power users, developers
- ✅ Automation, scripting
- ✅ Remote server (không có GUI)

**Chạy**:
```bash
python vpn_tool.py list
python vpn_tool.py connect JP
```

**Chi tiết**: Xem phần [CLI Usage](#%EF%B8%8F-cli-usage) bên dưới

---

### 📦 Standalone .EXE (Phân phối cho người khác)

**Phù hợp cho**:
- ✅ Chia sẻ tool cho người không biết Python
- ✅ Chạy trên máy không có Python
- ✅ Standalone, all-in-one file

**Tạo .exe**:
```bash
python build.py
```

**Chi tiết**: Xem [BUILD.md](BUILD.md)

---

## 📋 Yêu Cầu Hệ Thống

### Phần Mềm Bắt Buộc:
- **Python 3.8+** (nếu chạy từ source)
- **OpenVPN** (bắt buộc cho tất cả modes)

### Hệ Điều Hành:
- ✅ Windows 10/11 (fully supported)
- ⚠️ Linux/Mac (experimental)

---

## 🚀 Quick Start

### Cài Đặt

#### Bước 1: Cài OpenVPN
```
Download: https://openvpn.net/community-downloads/
Install to: C:\Program Files\OpenVPN\
```

#### Bước 2: Clone Repository
```bash
git clone https://github.com/ntd237/vpn_connection_tool_13102025.git
cd vpn_connection_tool_13102025
```

#### Bước 3: Cài Dependencies
```bash
pip install -r requirements.txt
```

### Chạy GUI (Khuyến Nghị)
```bash
python main_gui.py
```

### Hoặc Chạy CLI
```bash
python vpn_tool.py list
python vpn_tool.py connect JP
```

---

## 🖥️ GUI Usage

### Khởi Động
```bash
# Chạy với quyền Administrator (recommended)
python main_gui.py
```

### Workflow
1. **Chọn quốc gia** từ dropdown
2. Click **"Kết Nối VPN"** (nút xanh lá)
3. Đợi 10-30 giây
4. Status → 🟢 **ĐANG KẾT NỐI**
5. Sử dụng VPN
6. Click **"Ngắt Kết Nối"** (nút đỏ) khi xong

### Exit Behavior (Quan Trọng)

**Khi click nút X đóng cửa sổ**:

- Nếu **VPN đang kết nối** → Hiện dialog:
  ```
  ┌────────────────────────────────────────┐
  │ VPN đang kết nối.                      │
  │ Bạn có muốn ngắt kết nối trước khi     │
  │ thoát không?                           │
  │                                        │
  │     [Yes]          [Cancel]            │
  └────────────────────────────────────────┘
  ```
  - **Yes**: Ngắt VPN → Đóng app
  - **Cancel**: Giữ kết nối → KHÔNG đóng app

- Nếu **VPN chưa kết nối** → App đóng ngay

**Nguyên tắc đơn giản**: 
- Click X khi VPN ON → Hỏi disconnect
- Click X khi VPN OFF → Đóng luôn

### Giao Diện

```
┌─────────────────────────────────────────────┐
│         🌐 VPN Connection Tool              │
│      Kết nối VPN miễn phí - Author: NTD237  │
├─────────────────────────────────────────────┤
│  Chọn quốc gia: [Japan (JP) ▼]             │
│  [🔌 Kết Nối]  [🔄 Refresh]  [⛔ Ngắt]      │
├─────────────────────────────────────────────┤
│  Trạng thái: 🟢 ĐANG KẾT NỐI               │
│  IP: 123.45.67.89                           │
├─────────────────────────────────────────────┤
│  Nhật Ký:                                   │
│  [09:16:35] ✅ Kết nối thành công!          │
└─────────────────────────────────────────────┘
```

---

## ⌨️ CLI Usage

### 1. Xem Danh Sách Quốc Gia
```bash
python vpn_tool.py list
```

**Output**:
```
📋 Tìm thấy 10 quốc gia:
  • Japan           (JP)  - 45 servers - 1279.6 Mbps
  • Korea           (KR)  - 34 servers - 702.1 Mbps
  • United States   (US)  - 15 servers - 214.6 Mbps
  ...
```

### 2. Kết Nối VPN
```bash
# Cú pháp
python vpn_tool.py connect <COUNTRY_CODE>

# Ví dụ
python vpn_tool.py connect JP    # Nhật Bản
python vpn_tool.py connect US    # Mỹ
python vpn_tool.py connect KR    # Hàn Quốc
```

**Với Admin rights** (recommended):
```bash
python vpn_tool.py connect JP --admin
```

### 3. Kiểm Tra Trạng Thái
```bash
python vpn_tool.py status
```

**Output**:
```
📊 TRẠNG THÁI KẾT NỐI VPN
========================================
🟢 Trạng thái: ĐANG KẾT NỐI
🌐 IP công khai: 123.45.67.89
========================================
```

### 4. Ngắt Kết Nối
```bash
python vpn_tool.py disconnect
```

### 5. Auto-Reconnect Mode
```bash
python vpn_tool.py auto-reconnect JP
# Tự động kết nối lại khi bị ngắt
# Nhấn Ctrl+C để dừng
```

---

## 📦 Build Standalone .EXE

### Quick Build 

```bash
# 1. Cài dependencies (nếu chưa)
pip install -r requirements.txt

# 2. Fix pathlib error (nếu dùng conda)
pip uninstall pathlib pathlib2 pathlib-abc -y

# 3. Build
python build.py
```

### Output
```
dist/VPN_Tool_Package/
├── VPN_Connection_Tool.exe  (50-80MB)
├── config.yaml
└── README.txt
```

### Phân Phối
- Gửi file `.exe` cho người khác
- Họ chỉ cần:
  1. Cài OpenVPN
  2. Run as Administrator
  3. Sử dụng!

**Chi tiết đầy đủ**: [BUILD.md](BUILD.md)

---

## 🛠️ Troubleshooting

### ❌ "OpenVPN chưa được cài đặt"

**Giải pháp**:
1. Cài OpenVPN: https://openvpn.net/community-downloads/
2. Restart terminal/app

### ❌ "Kết nối thất bại" hoặc "Disconnect ngay"

**Nguyên nhân**: Thiếu quyền Administrator

**Giải pháp**:
```bash
# GUI: Chuột phải PowerShell → "Run as Administrator"
python main_gui.py

# CLI: Thêm --admin flag
python vpn_tool.py connect JP --admin
```

### ❌ GUI: Dropdown không load quốc gia

**Giải pháp**:
1. Check internet connection
2. Click nút "Làm Mới"
3. Tắt VPN/Proxy khác nếu đang bật

### ❌ Build .exe: "pathlib package is obsolete"

**Giải pháp**:
```bash
pip uninstall pathlib pathlib2 pathlib-abc -y
python build.py
```

### ❌ VPN kết nối nhưng không truy cập được Internet

**Giải pháp**:
```bash
# Ngắt và kết nối lại
python vpn_tool.py disconnect
python vpn_tool.py connect JP

# Hoặc flush DNS
ipconfig /flushdns
```

---

## 📊 So Sánh Các Chế Độ

| Feature | GUI | CLI | .EXE |
|---------|-----|-----|------|
| **Dễ sử dụng** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Visual feedback** | ✅ Real-time | ❌ Text only | ✅ Real-time |
| **Automation** | ❌ | ✅ | ❌ |
| **Cần Python** | ✅ | ✅ | ❌ |
| **Cần OpenVPN** | ✅ | ✅ | ✅ |
| **Tốc độ** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **File size** | ~2MB | ~2MB | 35-45MB |

---

## 📁 Cấu Trúc Dự Án

```
vpn_connection_tool_13102025/
├── main_gui.py          # GUI entry point
├── vpn_gui.py           # GUI implementation (PyQt5)
├── vpn_tool.py          # CLI interface
├── core.py              # VPN logic (shared)
├── utils.py             # Helper utilities (shared)
├── config.yaml          # Configuration
├── requirements.txt     # Python dependencies
│
├── build.py             # Build script for .exe
├── vpn_tool.spec        # PyInstaller config
│
├── README.md            # This file
├── BUILD.md             # Build documentation

```

---

## 🔒 Bảo Mật & Lưu Ý

### ⚠️ Quan Trọng

- ✅ VPN Gate là dịch vụ miễn phí, community-driven
- ⚠️ **KHÔNG** sử dụng cho banking, thanh toán nhạy cảm
- ⚠️ Server do tình nguyện viên vận hành
- ✅ Tốt cho: xem video, browse web, bypass geo-restriction
- ❌ Không phù hợp cho: công việc quan trọng, tài chính

### 🛡️ Khuyến Nghị

- Chỉ dùng cho browsing, streaming thông thường
- Không gửi thông tin nhạy cảm qua VPN miễn phí
- Luôn sử dụng HTTPS cho sites quan trọng
- Đối với công việc nghiêm túc → dùng VPN trả phí

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📞 Support

- **Tác giả**: ntd237
- **Email**: ntd237.work@gmail.com
- **GitHub**: https://github.com/ntd237

---

## 📄 License

Copyright (c) 2025 ntd237

Permission is hereby granted **only upon obtaining explicit authorization from the author (ntd237)**, to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

