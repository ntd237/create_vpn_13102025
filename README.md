# 🌐 VPN CONNECTION TOOL

## 📝 Mô Tả

**VPN Connection Tool** là công cụ CLI đơn giản giúp bạn kết nối VPN miễn phí chỉ bằng một dòng lệnh. Chỉ cần nhập tên quốc gia, tool sẽ tự động:
- 🔍 Tìm server VPN tốt nhất
- ⬇️ Tải cấu hình VPN
- 🔌 Kết nối tự động đến VPN
- 🔄 Tự động kết nối lại khi bị ngắt

## ✨ Tính Năng

- 🚀 **Kết nối siêu nhanh**: Chỉ cần 1 lệnh để kết nối VPN
- 🌍 **Nhiều quốc gia**: Hỗ trợ hơn 50 quốc gia trên toàn cầu
- 🆓 **Hoàn toàn miễn phí**: Sử dụng VPN Gate (dịch vụ VPN miễn phí công cộng)
- 🔄 **Auto-reconnect**: Tự động kết nối lại khi mất kết nối
- 📊 **Kiểm tra trạng thái**: Xem trạng thái kết nối và IP hiện tại
- 🛡️ **Không cần đăng ký**: Không cần tạo tài khoản hay đăng nhập
- ⚡ **Server tối ưu**: Tự động chọn server nhanh nhất và ổn định nhất

## 📋 Yêu Cầu

### Phần mềm cần thiết:
- **Python 3.8+**
- **OpenVPN**: Phải cài đặt trước khi sử dụng tool

### Cài đặt OpenVPN:

**Windows:**
1. Tải OpenVPN từ: https://openvpn.net/community-downloads/
2. Chọn bản "Windows Installer (NSIS)"
3. Cài đặt với các tùy chọn mặc định

**Kiểm tra OpenVPN đã cài đặt:**
```bash
# Mở Command Prompt
"C:\Program Files\OpenVPN\bin\openvpn.exe" --version
```

## 🚀 Cài Đặt

### Bước 1: Clone hoặc tải code
```bash
cd create_vpn_13102025
```

### Bước 2: Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### Bước 3: Kiểm tra cài đặt
```bash
python vpn_tool.py --version
```

## 🎮 Sử Dụng

### 1️⃣ Xem danh sách quốc gia có VPN

```bash
python vpn_tool.py list
```

**Output mẫu:**
```
🌍 Đang tải danh sách servers...

📋 Tìm thấy 45 quốc gia:

  • Australia            (AU)  - 5 server(s) - Speed: 15.2 Mbps
  • Japan                (JP)  - 23 server(s) - Speed: 45.8 Mbps
  • Korea Republic of    (KR)  - 12 server(s) - Speed: 38.5 Mbps
  • Thailand             (TH)  - 8 server(s) - Speed: 25.3 Mbps
  • United Kingdom       (GB)  - 4 server(s) - Speed: 12.7 Mbps
  • United States        (US)  - 15 server(s) - Speed: 35.2 Mbps
  • Viet Nam             (VN)  - 3 server(s) - Speed: 8.5 Mbps
  ...
```

### 2️⃣ Kết nối VPN đến quốc gia

```bash
# Cú pháp
python vpn_tool.py connect <MÃ_QUỐC_GIA>

# Ví dụ: Kết nối VPN Nhật Bản
python vpn_tool.py connect JP

# Ví dụ: Kết nối VPN Mỹ
python vpn_tool.py connect US

# Ví dụ: Kết nối VPN Hàn Quốc
python vpn_tool.py connect KR
```

**Output mẫu:**
```
🔍 Tìm kiếm VPN server tốt nhất cho JP...

Chọn server: vpn123456.opengw.net (Japan)
Speed: 45.8 Mbps, Uptime: 25 ms
✅ Đã tải config: vpn_configs\JP_vpn123456.opengw.net.ovpn

🔌 Đang kết nối VPN...

==================================================
✅ OpenVPN đã được khởi động thành công!
==================================================

📌 LƯU Ý QUAN TRỌNG:
   • OpenVPN đang chạy trong background (process độc lập)
   • Bạn có thể đóng cửa sổ này, VPN vẫn hoạt động
   • Cửa sổ OpenVPN console sẽ mở riêng (có thể minimize)

💡 LỆNH HỮU ÍCH:
   • Kiểm tra: python vpn_tool.py status
   • Ngắt kết nối: python vpn_tool.py disconnect

⏳ Đợi khoảng 10-30 giây để VPN kết nối hoàn tất.
   Sau đó chạy 'status' để xác nhận.
```

> 💡 **Giải thích**: OpenVPN sẽ mở một cửa sổ console riêng và chạy trong background. Tool này chỉ khởi động kết nối, sau đó bạn có thể đóng tool. VPN vẫn sẽ tiếp tục hoạt động cho đến khi bạn chạy lệnh `disconnect`.

### 3️⃣ Kết nối với quyền Admin (nếu cần)

```bash
# Nếu kết nối bình thường không được, thử với quyền admin
python vpn_tool.py connect JP --admin
```

> ⚠️ **Lưu ý**: Một số VPN yêu cầu quyền Administrator. Nếu kết nối thất bại, hãy:
> 1. Mở Command Prompt/PowerShell **với quyền Administrator**
> 2. Chạy lại lệnh với flag `--admin`

### 4️⃣ Kiểm tra trạng thái kết nối

```bash
python vpn_tool.py status
```

**Output mẫu:**
```
📊 TRẠNG THÁI KẾT NỐI VPN

========================================
🟢 Trạng thái: ĐANG KẾT NỐI
🌐 IP công khai: 123.45.67.89
========================================
```

### 5️⃣ Ngắt kết nối VPN

```bash
python vpn_tool.py disconnect
```

**Output:**
```
🔌 Đang ngắt kết nối VPN...

✅ Đã ngắt kết nối VPN!
```

### 6️⃣ Tự động kết nối lại (Auto-reconnect)

```bash
# Tự động kết nối lại khi bị mất kết nối
python vpn_tool.py auto-reconnect JP
```

**Output:**
```
🔄 Chế độ tự động kết nối lại đã BẬT
   Quốc gia: JP
   Kiểm tra mỗi: 10s
   Nhấn Ctrl+C để dừng

✅ VPN vẫn đang kết nối
✅ VPN vẫn đang kết nối
⚠️  Mất kết nối! Đang kết nối lại...
🔌 Đang kết nối VPN...
✅ Kết nối VPN thành công!
```

> Nhấn **Ctrl+C** để dừng auto-reconnect và ngắt kết nối

### 7️⃣ Hiển thị chi tiết (Verbose mode)

```bash
# Thêm flag -v để xem chi tiết quá trình
python vpn_tool.py connect JP -v
```

## ⚙️ Tùy Chọn CLI

| Lệnh | Mô tả | Ví dụ |
|------|-------|-------|
| `list` | Liệt kê tất cả quốc gia có VPN | `python vpn_tool.py list` |
| `connect <COUNTRY>` | Kết nối VPN đến quốc gia | `python vpn_tool.py connect US` |
| `disconnect` | Ngắt kết nối VPN | `python vpn_tool.py disconnect` |
| `status` | Kiểm tra trạng thái kết nối | `python vpn_tool.py status` |
| `auto-reconnect <COUNTRY>` | Tự động kết nối lại | `python vpn_tool.py auto-reconnect JP` |

### Flags:
| Flag | Mô tả |
|------|-------|
| `--admin` | Chạy với quyền Administrator |
| `-v, --verbose` | Hiển thị chi tiết quá trình |
| `--version` | Hiển thị phiên bản tool |

## 🌍 Mã Quốc Gia Phổ Biến

| Quốc gia | Mã | Quốc gia | Mã |
|----------|-----|----------|-----|
| 🇺🇸 Mỹ | US | 🇯🇵 Nhật Bản | JP |
| 🇰🇷 Hàn Quốc | KR | 🇬🇧 Anh | GB |
| 🇩🇪 Đức | DE | 🇫🇷 Pháp | FR |
| 🇸🇬 Singapore | SG | 🇹🇭 Thái Lan | TH |
| 🇨🇦 Canada | CA | 🇦🇺 Úc | AU |
| 🇻🇳 Việt Nam | VN | 🇮🇩 Indonesia | ID |

> Xem danh sách đầy đủ: `python vpn_tool.py list`

## 📊 Ví Dụ Sử Dụng Thực Tế

### Ví dụ 1: Truy cập nội dung từ Nhật Bản
```bash
# Kết nối VPN Nhật
python vpn_tool.py connect JP

# Kiểm tra IP
python vpn_tool.py status

# Truy cập websites Nhật
# (Mở browser và vào các trang web)

# Ngắt kết nối
python vpn_tool.py disconnect
```

### Ví dụ 2: Gaming với VPN ổn định
```bash
# Kết nối với auto-reconnect để game không bị disconnect
python vpn_tool.py auto-reconnect SG

# Chơi game...
# Tool sẽ tự động kết nối lại nếu VPN bị ngắt

# Nhấn Ctrl+C khi xong
```

### Ví dụ 3: Workflow hàng ngày
```bash
# Sáng: Kết nối VPN
python vpn_tool.py connect US -v

# Làm việc cả ngày...

# Tối: Ngắt kết nối
python vpn_tool.py disconnect
```

## ⚙️ Cấu Hình Nâng Cao

File `config.yaml` chứa các tùy chọn cấu hình:

```yaml
# Cấu hình kết nối
connection:
  timeout: 30                # Thời gian timeout (giây)
  max_retries: 3            # Số lần retry
  auto_reconnect: true      # Tự động reconnect
  reconnect_interval: 10    # Khoảng thời gian check (giây)

# Đường dẫn
paths:
  config_dir: "vpn_configs"  # Thư mục lưu .ovpn files
  log_file: "vpn_tool.log"   # File log

# Logging
logging:
  level: "INFO"              # DEBUG, INFO, WARNING, ERROR
  format: "%(asctime)s - %(levelname)s - %(message)s"

# VPN Settings
vpn:
  protocol: "udp"            # udp hoặc tcp
  require_admin: false       # Thử không dùng admin trước
```

**Chỉnh sửa config:**
1. Mở file `config.yaml`
2. Thay đổi các giá trị theo nhu cầu
3. Lưu file và chạy lại tool

## 🛠️ Troubleshooting

### ❌ Lỗi: "OpenVPN chưa được cài đặt"
**Nguyên nhân**: Chưa cài OpenVPN hoặc không tìm thấy trong PATH

**Giải pháp:**
1. Cài đặt OpenVPN: https://openvpn.net/community-downloads/
2. Đảm bảo cài vào thư mục mặc định: `C:\Program Files\OpenVPN\`
3. Khởi động lại Command Prompt

### ❌ Lỗi: "Không tìm thấy servers cho quốc gia XXX"
**Nguyên nhân**: Mã quốc gia không đúng hoặc không có server

**Giải pháp:**
1. Chạy `python vpn_tool.py list` để xem danh sách
2. Sử dụng đúng mã 2 ký tự (VD: US, JP, KR)
3. Thử quốc gia khác nếu không có server

### ❌ Lỗi: "Kết nối VPN thất bại" hoặc "OpenVPN bị disconnect ngay"
**Nguyên nhân**: Thiếu quyền Administrator, firewall chặn, hoặc config không hợp lệ

**Giải pháp:**

1. **Chạy với quyền Administrator** (Giải pháp chính):
   ```bash
   # Chuột phải vào PowerShell/CMD → "Run as Administrator"
   # Sau đó chạy:
   python vpn_tool.py connect US --admin
   ```

2. **Kiểm tra OpenVPN console**:
   - Khi connect, một cửa sổ console sẽ mở ra
   - Xem log để biết lỗi cụ thể
   - Thường gặp: "ERROR: Cannot open TUN/TAP dev" → cần admin rights

3. **Tạm tắt Firewall/Antivirus** để test

4. **Thử server khác**: 
   ```bash
   python vpn_tool.py connect JP
   ```

### ⚠️ VPN kết nối nhưng không truy cập được Internet
**Nguyên nhân**: DNS hoặc routing issue

**Giải pháp:**
1. Ngắt và kết nối lại: 
   ```bash
   python vpn_tool.py disconnect
   python vpn_tool.py connect US
   ```
2. Kiểm tra DNS settings trong Windows
3. Flush DNS cache: `ipconfig /flushdns`

### 🐌 VPN chậm
**Giải pháp:**
1. Chọn quốc gia gần hơn
2. Chạy `python vpn_tool.py list` và chọn server có Speed cao
3. Thử kết nối vào thời điểm khác (ít người dùng hơn)

### 📝 Xem log chi tiết
```bash
# Xem file log
type vpn_tool.log

# Hoặc chạy với verbose
python vpn_tool.py connect US -v
```

## 🔒 Bảo Mật & Lưu Ý

### ⚠️ Quan trọng:
- ✅ VPN Gate là dịch vụ miễn phí, community-driven
- ⚠️ **KHÔNG** sử dụng cho các giao dịch nhạy cảm (banking, thanh toán)
- ⚠️ Server do tình nguyện viên vận hành, có thể bị ngắt bất kỳ lúc nào
- ✅ Tốt cho: truy cập nội dung bị chặn địa lý, bảo vệ privacy cơ bản
- ❌ Không phù hợp cho: công việc quan trọng, giao dịch tài chính

### 🛡️ Khuyến nghị:
- Chỉ sử dụng cho browsing web, xem video, download thông thường
- Không gửi thông tin nhạy cảm (password, credit card) qua VPN miễn phí
- Sử dụng HTTPS cho các trang web quan trọng
- Đối với công việc nghiêm túc, hãy dùng VPN trả phí đáng tin cậy

## 📄 Giấy Phép

MIT License - Tự do sử dụng, chỉnh sửa, phân phối

## 👤 Tác Giả

- **Tên**: ntd237
- **Email**: ntd237.work@gmail.com
- **GitHub**: https://github.com/ntd237

## 🙏 Credits

- **VPN Gate**: https://www.vpngate.net/ - Dịch vụ VPN miễn phí công cộng
- **OpenVPN**: https://openvpn.net/ - VPN client open-source

## 📞 Hỗ Trợ

Nếu gặp vấn đề, vui lòng:
1. Kiểm tra phần Troubleshooting ở trên
2. Xem log file: `vpn_tool.log`
3. Liên hệ qua email: ntd237.work@gmail.com

---

**Happy VPN-ing! 🚀**
