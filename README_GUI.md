# 🖥️ VPN CONNECTION TOOL - GUI VERSION

## 📝 Giới Thiệu

**VPN Connection Tool GUI** là phiên bản giao diện đồ họa (Desktop) của công cụ kết nối VPN. Dễ sử dụng với các nút bấm trực quan và hiển thị trạng thái real-time.

## ✨ Tính Năng GUI

- 🖱️ **Click & Connect**: Chỉ cần chọn quốc gia và click "Kết Nối"
- 📊 **Status Display Real-time**: Hiển thị trạng thái kết nối và IP công khai
- 🌍 **Dropdown Country Selection**: Danh sách quốc gia với tốc độ server
- 📝 **Activity Log**: Nhật ký hoạt động chi tiết
- 🔄 **Auto Refresh**: Tự động cập nhật trạng thái mỗi 3 giây
- 🎨 **Modern UI**: Giao diện đẹp mắt, chuyên nghiệp với PyQt5

## 🖼️ Giao Diện

```
┌──────────────────────────────────────────────────────────┐
│         🌐 VPN Connection Tool                           │
│      Kết nối VPN miễn phí dễ dàng                        │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  Điều Khiển                                              │
│  ┌────────────────────────────────────────────────────┐ │
│  │  Chọn quốc gia: [Japan (JP) - 1279.6 Mbps ▼]      │ │
│  │                                                    │ │
│  │  [🔌 Kết Nối VPN] [⛔ Ngắt Kết Nối] [🔄 Làm Mới]   │ │
│  └────────────────────────────────────────────────────┘ │
│                                                          │
│  Trạng Thái Kết Nối                                     │
│  ┌────────────────────────────────────────────────────┐ │
│  │  Trạng thái:  🟢 ĐANG KẾT NỐI                      │ │
│  │  IP công khai: 123.45.67.89                        │ │
│  └────────────────────────────────────────────────────┘ │
│                                                          │
│  Nhật Ký Hoạt Động                                      │
│  ┌────────────────────────────────────────────────────┐ │
│  │ [09:15:32] 🔄 Đang tải danh sách quốc gia...       │ │
│  │ [09:15:35] ✅ Đã tải 10 quốc gia khả dụng          │ │
│  │ [09:16:20] 🔌 Bắt đầu kết nối VPN đến JP...        │ │
│  │ [09:16:22] 🔍 Đang tìm server tốt nhất cho JP...   │ │
│  │ [09:16:25] 🔌 Đang kết nối VPN...                  │ │
│  │ [09:16:35] ✅ Đã khởi động VPN thành công!         │ │
│  └────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────┘
```

## 📋 Yêu Cầu

### Phần mềm:
- **Python 3.8+**
- **OpenVPN** (bắt buộc)
- **PyQt5** (GUI framework)

### Hệ điều hành:
- ✅ Windows 10/11 (primary)
- ⚠️ Linux/Mac (chưa test đầy đủ)

## 🚀 Cài Đặt

### Bước 1: Cài OpenVPN
```
Tải từ: https://openvpn.net/community-downloads/
Cài vào: C:\Program Files\OpenVPN\
```

### Bước 2: Cài Dependencies
```bash
# Cài tất cả dependencies (bao gồm PyQt5)
pip install -r requirements.txt

# Hoặc cài riêng PyQt5
pip install PyQt5>=5.15.0
```

### Bước 3: Chạy GUI
```bash
python main_gui.py
```

Hoặc:
```bash
python vpn_gui.py
```

## 🎮 Hướng Dẫn Sử Dụng

### 1️⃣ Khởi động GUI

```bash
# Chạy với quyền Administrator (khuyến nghị)
# Chuột phải PowerShell/CMD → "Run as Administrator"
python main_gui.py
```

> ⚠️ **Quan trọng**: OpenVPN cần quyền Administrator. Chạy app với "Run as Administrator" để tránh lỗi.

### 2️⃣ Chọn Quốc Gia

1. Đợi app tải danh sách quốc gia (vài giây)
2. Click vào dropdown "Chọn quốc gia"
3. Chọn quốc gia bạn muốn (có tốc độ hiển thị)

### 3️⃣ Kết Nối VPN

1. Sau khi chọn quốc gia
2. Click nút **"🔌 Kết Nối VPN"**
3. Đợi 10-30 giây để kết nối
4. Trạng thái sẽ chuyển sang **🟢 ĐANG KẾT NỐI**
5. IP công khai sẽ hiển thị

> 💡 **Lưu ý**: 
> - OpenVPN sẽ mở cửa sổ console riêng (có thể minimize)
> - Xem log trong phần "Nhật Ký Hoạt Động"
> - Nếu thất bại, đảm bảo chạy với quyền Admin

### 4️⃣ Kiểm Tra Trạng Thái

- Trạng thái tự động cập nhật mỗi 3 giây
- **🟢 ĐANG KẾT NỐI**: VPN hoạt động tốt
- **🔴 CHƯA KẾT NỐI**: VPN không hoạt động
- IP công khai hiển thị khi đã kết nối

### 5️⃣ Ngắt Kết Nối

1. Click nút **"⛔ Ngắt Kết Nối"**
2. VPN sẽ được ngắt an toàn
3. Trạng thái chuyển về **🔴 CHƯA KẾT NỐI**

### 6️⃣ Làm Mới Danh Sách

- Click **"🔄 Làm Mới"** để reload danh sách quốc gia
- Hữu ích khi danh sách servers cũ hoặc có lỗi

## 🎨 Giao Diện Chi Tiết

### Components

#### 1. Header
- **Title**: "🌐 VPN Connection Tool"
- **Subtitle**: "Kết nối VPN miễn phí dễ dàng"

#### 2. Điều Khiển Panel
- **Dropdown**: Chọn quốc gia với tốc độ server
- **Kết Nối**: Nút màu xanh để kết nối VPN
- **Ngắt Kết Nối**: Nút màu đỏ để disconnect
- **Làm Mới**: Reload danh sách servers

#### 3. Trạng Thái Panel
- **Status**: Hiển thị trạng thái kết nối real-time
  - 🟢 Màu xanh = Đang kết nối
  - 🔴 Màu đỏ = Chưa kết nối
- **IP Address**: Hiển thị IP công khai hiện tại

#### 4. Nhật Ký Panel
- Log tất cả activities
- Timestamp cho mỗi event
- Auto-scroll xuống dưới
- Font monospace dễ đọc

## ⚙️ Tính Năng Nâng Cao

### Background Processing

GUI sử dụng **QThread** để xử lý VPN operations trong background:
- ✅ UI không bị đóng băng khi connect/disconnect
- ✅ Progress messages realtime
- ✅ User có thể cancel operations (ESC/X)

### Auto Status Update

- Timer tự động check status mỗi 3 giây
- Update trạng thái và IP address
- Không ảnh hưởng performance

### Clean Exit

Khi đóng app:
1. Hỏi user có muốn disconnect VPN không
2. Nếu Yes → ngắt VPN trước khi thoát
3. Nếu No → giữ VPN chạy
4. Cancel → không thoát

## 🛠️ Troubleshooting

### ❌ Lỗi: "OpenVPN chưa được cài đặt"

**Giải pháp**:
1. Cài OpenVPN từ: https://openvpn.net/community-downloads/
2. Restart app

### ❌ Lỗi: "Kết nối thất bại"

**Nguyên nhân**: Thiếu quyền Administrator

**Giải pháp**:
1. Đóng app
2. Chuột phải vào PowerShell/CMD → "Run as Administrator"
3. Chạy lại: `python main_gui.py`

### ❌ Dropdown "Đang tải..." mãi không xong

**Nguyên nhân**: Không thể kết nối VPN Gate API

**Giải pháp**:
1. Kiểm tra internet connection
2. Click nút "Làm Mới"
3. Tắt VPN/Proxy nếu đang bật
4. Kiểm tra Firewall không chặn Python

### ❌ Status vẫn "CHƯA KẾT NỐI" sau khi connect

**Nguyên nhân**: Cần thời gian để VPN thiết lập

**Giải pháp**:
1. Đợi 30-60 giây
2. Status sẽ tự động update
3. Kiểm tra OpenVPN console có lỗi gì không

### ⚠️ App bị lag/đóng băng

**Nguyên nhân**: Ít khi xảy ra (QThread đã xử lý)

**Giải pháp**:
1. Đợi operation hoàn thành
2. Nếu không phản hồi → kill process
3. Chạy lại với quyền Admin

### 🔍 Debug Mode

Xem log chi tiết:
```bash
python vpn_gui.py -v
```

Hoặc xem file log:
```bash
type vpn_tool.log
```

## 🌟 So Sánh CLI vs GUI

| Feature | CLI | GUI |
|---------|-----|-----|
| Dễ sử dụng | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Visual feedback | ❌ | ✅ Real-time |
| Status display | Text only | Visual + Icons |
| Background ops | ❌ Exit khi done | ✅ QThread |
| User-friendly | Terminal users | Everyone |
| Speed | Nhanh hơn | Hơi chậm hơn |

**Khuyến nghị**:
- **CLI**: Cho power users, scripting, automation
- **GUI**: Cho người dùng thông thường, visual learners

## 📊 Technical Details

### Architecture

```
vpn_gui.py (GUI Layer)
    │
    ├─> VPNWorker (QThread)
    │     │
    │     └─> core.py (VPN Logic)
    │           │
    │           └─> OpenVPN Process
    │
    └─> QTimer (Status Updates)
          │
          └─> core.py.get_status()
```

### Threading Model

- **Main Thread**: UI rendering, user interactions
- **Worker Thread**: VPN connect/disconnect operations
- **Timer Thread**: Status updates mỗi 3 giây

### Signals & Slots

```python
# Worker → Main Thread communication
worker.finished.emit(success, message)
worker.progress.emit(message)

# Timer → Status Update
timer.timeout.connect(update_status)
```

## 🎓 Best Practices

### Sử Dụng Hiệu Quả

1. **Luôn chạy với Admin rights** - Tránh lỗi kết nối
2. **Đợi load countries xong** - Trước khi connect
3. **Kiểm tra OpenVPN console** - Nếu có lỗi
4. **Đóng app đúng cách** - Để disconnect VPN properly
5. **Xem log khi có vấn đề** - Debug dễ dàng

### Tối Ưu Performance

- Không spam click buttons - Đợi operation complete
- Đóng OpenVPN console nếu không cần xem log
- Restart app nếu chạy lâu (>1 giờ)

## 📄 License

MIT License - Tự do sử dụng và chỉnh sửa

## 👤 Tác Giả

- **Tên**: ntd237
- **Email**: ntd237.work@gmail.com
- **GitHub**: https://github.com/ntd237

## 🙏 Credits

- **PyQt5**: GUI Framework
- **VPN Gate**: Free VPN Service
- **OpenVPN**: VPN Client

---

## 🔗 Tham Khảo

- CLI Version: Xem `README.md`
- Installation Guide: Xem `INSTALL.md`
- Quick Start: Xem `QUICKSTART.md`

---

**Enjoy the beautiful GUI! 🎨✨**
