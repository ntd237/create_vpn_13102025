# 🖥️ GUI VERSION - DESKTOP APPLICATION

## 📝 Giới Thiệu

**VPN Connection Tool GUI** là phiên bản giao diện đồ họa (Desktop) dựa trên PyQt5. Dễ sử dụng với các nút bấm trực quan và hiển thị trạng thái real-time.

---

## ✨ Tính Năng

### UI Components
- 🖱️ **Click & Connect**: Chọn quốc gia và click để kết nối
- 📊 **Real-time Status**: Hiển thị trạng thái kết nối và IP công khai
- 🌍 **Dropdown Selection**: Danh sách quốc gia với tốc độ server
- 📝 **Activity Log**: Nhật ký hoạt động real-time
- 🔄 **Auto Refresh**: Tự động cập nhật status mỗi 3 giây

### Technical Features
- ✅ **Background Processing**: QThread → UI không đóng băng
- ✅ **Hidden Console**: OpenVPN chạy ngầm, không hiện cửa sổ
- ✅ **Clean Exit**: Hỏi disconnect trước khi thoát
- ✅ **Error Handling**: MessageBox notifications
- ✅ **Modern UI**: Professional styling

---

## 🎨 Giao Diện

```
┌────────────────────────────────────────────────────────────┐
│              🌐 VPN Connection Tool                        │
│           Kết nối VPN miễn phí dễ dàng                     │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  ╔══════════════════════════════════════════════════════╗ │
│  ║ Điều Khiển                                           ║ │
│  ╠══════════════════════════════════════════════════════╣ │
│  ║  Chọn quốc gia: [Japan (JP) - 1279.6 Mbps    ▼]     ║ │
│  ║                                                      ║ │
│  ║  [🔌 Kết Nối]  [🔄 Làm Mới]  [⛔ Ngắt Kết Nối]      ║ │
│  ║    (Green)       (Blue)          (Red)              ║ │
│  ╚══════════════════════════════════════════════════════╝ │
│                                                            │
│  ╔══════════════════════════════════════════════════════╗ │
│  ║ Trạng Thái Kết Nối                                   ║ │
│  ╠══════════════════════════════════════════════════════╣ │
│  ║  Trạng thái:  🟢 ĐANG KẾT NỐI                       ║ │
│  ║  IP công khai: 123.45.67.89                         ║ │
│  ╚══════════════════════════════════════════════════════╝ │
│                                                            │
│  ╔══════════════════════════════════════════════════════╗ │
│  ║ Nhật Ký Hoạt Động                                    ║ │
│  ╠══════════════════════════════════════════════════════╣ │
│  ║ [09:15:32] 🔄 Đang tải danh sách quốc gia...        ║ │
│  ║ [09:15:35] ✅ Đã tải 10 quốc gia khả dụng           ║ │
│  ║ [09:16:20] 🔌 Bắt đầu kết nối VPN đến JP...         ║ │
│  ║ [09:16:25] 🔌 Đang kết nối VPN...                   ║ │
│  ║ [09:16:35] ✅ Đã khởi động VPN thành công!          ║ │
│  ╚══════════════════════════════════════════════════════╝ │
└────────────────────────────────────────────────────────────┘

Kích thước: 800x700 pixels
```

---

## 📋 Yêu Cầu

### Phần Mềm:
- **Python 3.8+**
- **PyQt5 >= 5.15.0**
- **OpenVPN** (bắt buộc)

### Hệ Điều Hành:
- ✅ Windows 10/11 (primary)
- ⚠️ Linux/Mac (experimental)

---

## 🚀 Cài Đặt & Chạy

### Bước 1: Cài Dependencies
```bash
pip install -r requirements.txt
```

Hoặc chỉ GUI dependencies:
```bash
pip install PyQt5>=5.15.0 requests>=2.28.0 pyyaml>=6.0 psutil>=5.9.0
```

### Bước 2: Cài OpenVPN
```
Tải từ: https://openvpn.net/community-downloads/
Cài vào: C:\Program Files\OpenVPN\
```

### Bước 3: Chạy GUI
```bash
# Method 1: Entry point
python main_gui.py

# Method 2: Direct
python vpn_gui.py
```

### Recommended: Chạy Với Admin
```bash
# Chuột phải PowerShell → "Run as Administrator"
cd D:\Workspace\Tools\create_vpn
python main_gui.py
```

---

## 🎮 Hướng Dẫn Sử Dụng

### 1. Khởi Động
- Chạy `python main_gui.py`
- App tự động load danh sách quốc gia (3-5 giây)

### 2. Chọn Quốc Gia
- Click dropdown "Chọn quốc gia"
- Chọn quốc gia (hiển thị tốc độ server)

### 3. Kết Nối VPN
- Click nút **"🔌 Kết Nối VPN"** (màu xanh lá)
- Đợi 10-30 giây
- Status chuyển sang **🟢 ĐANG KẾT NỐI**
- IP công khai hiển thị

### 4. Kiểm Tra Trạng Thái
- Status tự động update mỗi 3 giây
- **🟢 ĐANG KẾT NỐI**: VPN hoạt động
- **🔴 CHƯA KẾT NỐI**: VPN đã ngắt

### 5. Làm Mới Danh Sách
- Click **"🔄 Làm Mới"** (màu xanh dương)
- Reload danh sách servers mới

### 6. Ngắt Kết Nối
- Click **"⛔ Ngắt Kết Nối"** (màu đỏ)
- VPN được ngắt an toàn

### 7. Đóng App
- Click nút X
- App hỏi có muốn disconnect không
- Chọn Yes/No/Cancel

---

## 🎨 Design Highlights

### Color Scheme
```yaml
# Primary Actions
Connect Button:    #10B981 (Green - Go, Success)
Refresh Button:    #2563EB (Blue - Active, Reload)
Disconnect Button: #EF4444 (Red - Danger, Stop)

# Status Colors
Connected:    #10B981 (Green)
Disconnected: #EF4444 (Red)

# UI Colors
Background:   #F8FAFC (Light gray)
Card:         #FFFFFF (White)
Border:       #E2E8F0 (Light gray)
Text Primary: #0F172A (Dark)
Text Secondary: #475569 (Gray)
```

### Typography
```yaml
Header Title:     24px, Bold
Section Title:    16px, Semi-bold
Body Text:        14px, Regular
Button Text:      14px, Semi-bold
Log Text:         12px, Monospace
```

### Layout
```yaml
Window Size:      800x700 pixels
Padding:          24px
Card Spacing:     20px
Button Spacing:   12px
Log Height:       200px minimum (expandable)
```

---

## 🔧 Technical Architecture

### Threading Model
```
Main Thread (UI)
├── Render components
├── Handle user input
├── Update display
└── QTimer (status updates every 3s)

Worker Thread (VPNWorker)
├── Fetch countries list
├── Download config files
├── Connect VPN
└── Disconnect VPN
```

### Signal/Slot Communication
```python
# Worker → Main Thread
worker.finished.emit(success: bool, message: str)
worker.progress.emit(message: str)

# Timer → Status Update
timer.timeout.connect(update_status)

# Buttons → Actions
connect_btn.clicked.connect(on_connect)
disconnect_btn.clicked.connect(on_disconnect)
refresh_btn.clicked.connect(load_countries)
```

### Background Processing
```python
class VPNWorker(QThread):
    """Worker thread cho VPN operations"""
    finished = pyqtSignal(bool, str)
    progress = pyqtSignal(str)
    
    def run(self):
        # Long-running VPN operations
        # Không block UI thread
```

---

## 🐛 Troubleshooting

### ❌ Lỗi: "OpenVPN chưa được cài đặt"

**Giải pháp**:
```bash
# Kiểm tra OpenVPN
Test-Path "C:\Program Files\OpenVPN\bin\openvpn.exe"

# Nếu False → Cài OpenVPN
https://openvpn.net/community-downloads/
```

### ❌ Dropdown "Đang tải..." không load

**Nguyên nhân**: Không kết nối được VPN Gate API

**Giải pháp**:
1. Check internet connection
2. Click nút "Làm Mới"
3. Tắt VPN/Proxy khác nếu đang bật
4. Check Firewall không chặn Python

### ❌ Status vẫn "CHƯA KẾT NỐI" sau khi connect

**Nguyên nhân**: Cần thời gian để VPN establish

**Giải pháp**:
1. Đợi 30-60 giây
2. Status sẽ tự động update
3. Xem Activity Log có lỗi gì không

### ❌ "Kết nối thất bại" khi connect

**Nguyên nhân**: Thiếu quyền Administrator

**Giải pháp**:
1. Đóng app
2. Chuột phải PowerShell/CMD → "Run as Administrator"
3. Chạy lại: `python main_gui.py`

### ❌ OpenVPN console hiện lên

**Đã fix**: Version 2.0.2+ OpenVPN chạy ngầm hoàn toàn

**Nếu vẫn thấy**: Update code mới nhất

### ❌ App bị lag/freeze

**Nguyên nhân**: Worker thread có vấn đề

**Giải pháp**:
1. Đợi operation hoàn thành
2. Nếu không phản hồi → Kill process và restart
3. Chạy với Admin rights

---

## 💡 Tips & Tricks

### Keyboard Shortcuts
- **Enter**: Trong dropdown → Chọn quốc gia
- **Space**: Trên button → Click
- **Escape**: Trong dropdown → Đóng dropdown
- **Alt+F4**: Đóng app

### Performance
- Không spam click buttons
- Đợi operation complete trước khi action mới
- Restart app nếu chạy quá lâu (>1 giờ)

### Workflow Tối Ưu
1. Khởi động app (1 lần/ngày)
2. Load countries (tự động)
3. Chọn quốc gia
4. Connect
5. Minimize app (để chạy background)
6. Sử dụng VPN
7. Quay lại app để disconnect

---

## 🆚 CLI vs GUI

| Feature | CLI | GUI |
|---------|-----|-----|
| **Ease of Use** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Visual Feedback** | Text only | ✅ Visual + Icons |
| **Status Display** | Manual check | ✅ Auto-update |
| **Background Ops** | Blocks | ✅ QThread |
| **User-Friendly** | Terminal users | Everyone |
| **Speed** | Faster | Slightly slower |
| **Automation** | ✅ Easy | Limited |

**Recommendation**:
- **GUI**: Cho người dùng thông thường, visual learners
- **CLI**: Cho power users, scripting, automation

---

## 📊 File Structure

```python
# vpn_gui.py (~540 lines)
├── VPNWorker(QThread)           # Background operations
├── VPNMainWindow(QMainWindow)   # Main window
│   ├── __init__()              # Setup
│   ├── apply_global_styles()   # CSS styling
│   ├── setup_ui()              # Create UI
│   ├── create_header()         # Header section
│   ├── create_control_panel()  # Controls section
│   ├── create_status_display() # Status section
│   ├── create_log_output()     # Log section
│   ├── load_countries()        # Fetch countries
│   ├── on_connect()            # Connect handler
│   ├── on_disconnect()         # Disconnect handler
│   ├── update_status()         # Status updater
│   └── closeEvent()            # Exit handler

# main_gui.py (~7 lines)
└── Entry point → vpn_gui.main()
```

---

## 🎓 Advanced

### Custom Styling
Edit stylesheet trong `apply_global_styles()`:
```python
self.setStyleSheet("""
    QPushButton#connect-button {
        background-color: #10B981;  /* Đổi màu */
        font-size: 16px;            /* Đổi size */
    }
""")
```

### Change Window Size
```python
# In __init__()
self.setGeometry(100, 100, 1000, 800)  # x, y, width, height
```

### Add Features
```python
# Add new button
new_btn = QPushButton("New Feature")
new_btn.clicked.connect(self.on_new_feature)

# Add to layout
button_layout.addWidget(new_btn)
```

---

## 📦 Standalone .exe

Để tạo file `.exe` standalone, xem **BUILD.md**

Quick command:
```bash
python build.py
```

---

## ✅ GUI Checklist

Khi chạy GUI, kiểm tra:

- [ ] ✅ App khởi động không lỗi
- [ ] ✅ Load countries thành công
- [ ] ✅ Dropdown hiển thị quốc gia + speed
- [ ] ✅ 3 buttons: Green, Blue, Red
- [ ] ✅ Click Connect → Status update
- [ ] ✅ OpenVPN không hiện console
- [ ] ✅ Activity Log hiển thị messages
- [ ] ✅ Status auto-update mỗi 3s
- [ ] ✅ Disconnect hoạt động
- [ ] ✅ Exit app hỏi disconnect

---

## 📞 Support

- 📖 Installation: `INSTALL.md`
- ⚡ Quick Start: `QUICKSTART.md`
- 📦 Build .exe: `BUILD.md`
- 📝 Main README: `README.md`

---

**Enjoy the beautiful GUI! 🎨✨**
