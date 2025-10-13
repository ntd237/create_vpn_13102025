"""
VPN Connection Tool - PyQt5 GUI
Giao diện đồ họa cho công cụ kết nối VPN.
"""

import sys
import time
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QComboBox, QFrame, QTextEdit, QMessageBox,
    QGroupBox
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QFont, QIcon

from core import VPNCore
from utils import load_config, format_server_info


class VPNWorker(QThread):
    """
    Worker thread để thực hiện các tác vụ VPN trong background.
    Tránh UI bị đóng băng khi connect/disconnect.
    """
    # Signals để giao tiếp với main thread
    finished = pyqtSignal(bool, str)  # (success, message)
    progress = pyqtSignal(str)  # Progress message
    
    def __init__(self, vpn_core, action, country_code=None):
        """
        Khởi tạo worker.
        
        Args:
            vpn_core: Instance của VPNCore
            action: 'connect' hoặc 'disconnect'
            country_code: Mã quốc gia (nếu action='connect')
        """
        super().__init__()
        self.vpn_core = vpn_core
        self.action = action
        self.country_code = country_code
    
    def run(self):
        """Chạy action trong background thread."""
        try:
            if self.action == 'connect':
                # Download config
                self.progress.emit(f"🔍 Đang tìm server tốt nhất cho {self.country_code}...")
                config_path = self.vpn_core.download_config(self.country_code)
                
                if not config_path:
                    self.finished.emit(False, f"Không tìm thấy server cho {self.country_code}")
                    return
                
                # Connect
                self.progress.emit("🔌 Đang kết nối VPN...")
                success = self.vpn_core.connect(config_path, require_admin=True)
                
                if success:
                    self.finished.emit(True, "✅ Đã khởi động VPN thành công!")
                else:
                    self.finished.emit(False, "❌ Kết nối thất bại. Thử chạy app với quyền Admin.")
                    
            elif self.action == 'disconnect':
                self.progress.emit("🔌 Đang ngắt kết nối...")
                success = self.vpn_core.disconnect()
                
                if success:
                    self.finished.emit(True, "✅ Đã ngắt kết nối VPN")
                else:
                    self.finished.emit(False, "❌ Không thể ngắt kết nối")
                    
        except Exception as e:
            self.finished.emit(False, f"Lỗi: {str(e)}")


class VPNMainWindow(QMainWindow):
    """
    Cửa sổ chính của VPN GUI application.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VPN Connection Tool")
        self.setGeometry(100, 100, 800, 700)
        
        # Initialize VPN core
        try:
            config = load_config()
            config_dir = config.get('paths', {}).get('config_dir', 'vpn_configs')
        except:
            config_dir = 'vpn_configs'
        
        self.vpn_core = VPNCore(config_dir=config_dir)
        self.countries = {}
        self.worker = None
        
        # Apply global styles
        self.apply_global_styles()
        
        # Setup UI
        self.setup_ui()
        
        # Start status timer
        self.status_timer = QTimer()
        self.status_timer.timeout.connect(self.update_status)
        self.status_timer.start(3000)  # Update mỗi 3 giây
        
        # Load countries in background
        self.load_countries()
    
    def apply_global_styles(self):
        """Áp dụng stylesheet toàn cục."""
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F8FAFC;
            }
            QLabel {
                color: #0F172A;
            }
            QLabel#title {
                font-size: 24px;
                font-weight: 700;
                color: #0F172A;
            }
            QLabel#section-title {
                font-size: 16px;
                font-weight: 600;
                color: #0F172A;
                margin-bottom: 8px;
            }
            QLabel#status-label {
                font-size: 14px;
                color: #475569;
            }
            QLabel#status-value {
                font-size: 14px;
                font-weight: 600;
            }
            QPushButton {
                background-color: #64748B;
                color: #FFFFFF;
                border: none;
                border-radius: 6px;
                padding: 10px 24px;
                font-size: 14px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #475569;
            }
            QPushButton:pressed {
                background-color: #334155;
            }
            QPushButton:disabled {
                background-color: #CBD5E1;
                color: #64748B;
            }
            QPushButton#connect-button {
                background-color: #10B981;
            }
            QPushButton#connect-button:hover {
                background-color: #059669;
            }
            QPushButton#connect-button:pressed {
                background-color: #047857;
            }
            QPushButton#refresh-button {
                background-color: #2563EB;
            }
            QPushButton#refresh-button:hover {
                background-color: #1E40AF;
            }
            QPushButton#refresh-button:pressed {
                background-color: #1E3A8A;
            }
            QPushButton#danger-button {
                background-color: #EF4444;
            }
            QPushButton#danger-button:hover {
                background-color: #DC2626;
            }
            QComboBox {
                border: 1px solid #CBD5E1;
                border-radius: 6px;
                padding: 8px 12px;
                font-size: 14px;
                background: #FFFFFF;
                min-width: 200px;
            }
            QComboBox:focus {
                border: 2px solid #2563EB;
            }
            QComboBox::drop-down {
                border: none;
                width: 30px;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 5px solid #64748B;
                margin-right: 10px;
            }
            QTextEdit {
                border: 1px solid #E2E8F0;
                border-radius: 6px;
                padding: 12px;
                font-size: 12px;
                background: #FFFFFF;
                font-family: 'Consolas', 'Courier New', monospace;
            }
            QFrame#card {
                background: #FFFFFF;
                border: 1px solid #E2E8F0;
                border-radius: 8px;
                padding: 16px;
            }
            QGroupBox {
                font-size: 14px;
                font-weight: 600;
                color: #0F172A;
                border: 1px solid #E2E8F0;
                border-radius: 8px;
                margin-top: 12px;
                padding-top: 12px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 8px;
                background: #FFFFFF;
            }
        """)
    
    def setup_ui(self):
        """Thiết lập giao diện chính."""
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(24, 24, 24, 24)
        main_layout.setSpacing(20)
        
        # Header
        header = self.create_header()
        main_layout.addWidget(header, 0)  # No stretch
        
        # Control panel
        control_panel = self.create_control_panel()
        main_layout.addWidget(control_panel, 0)  # No stretch
        
        # Status display
        status_display = self.create_status_display()
        main_layout.addWidget(status_display, 0)  # No stretch
        
        # Log output - chiếm hết space còn lại
        log_output = self.create_log_output()
        main_layout.addWidget(log_output, 1)  # Stretch factor = 1
    
    def create_header(self):
        """Tạo header với logo và title."""
        header = QFrame()
        header.setObjectName("card")
        
        layout = QVBoxLayout(header)
        
        title = QLabel("🌐 VPN Connection Tool")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        subtitle = QLabel("Kết nối VPN miễn phí - Author: NTD237")
        subtitle.setStyleSheet("font-size: 14px; color: #64748B;")
        subtitle.setAlignment(Qt.AlignCenter)
        layout.addWidget(subtitle)
        
        return header
    
    def create_control_panel(self):
        """Tạo panel điều khiển với buttons."""
        group = QGroupBox("Điều Khiển")
        layout = QVBoxLayout(group)
        layout.setSpacing(12)
        
        # Country selection
        country_layout = QHBoxLayout()
        country_label = QLabel("Chọn quốc gia:")
        country_label.setObjectName("section-title")
        self.country_combo = QComboBox()
        self.country_combo.addItem("Đang tải danh sách...")
        self.country_combo.setEnabled(False)
        
        country_layout.addWidget(country_label)
        country_layout.addWidget(self.country_combo)
        country_layout.addStretch()
        
        layout.addLayout(country_layout)
        
        # Buttons - Sắp xếp lại: Kết Nối → Làm Mới → Ngắt Kết Nối
        button_layout = QHBoxLayout()
        button_layout.setSpacing(12)
        
        # Connect button - Màu xanh lá
        self.connect_btn = QPushButton("🔌 Kết Nối VPN")
        self.connect_btn.setObjectName("connect-button")
        self.connect_btn.setEnabled(False)
        self.connect_btn.clicked.connect(self.on_connect)
        button_layout.addWidget(self.connect_btn)
        
        # Refresh button - Màu xanh dương
        self.refresh_btn = QPushButton("🔄 Làm Mới")
        self.refresh_btn.setObjectName("refresh-button")
        self.refresh_btn.clicked.connect(self.load_countries)
        button_layout.addWidget(self.refresh_btn)
        
        # Disconnect button - Màu đỏ
        self.disconnect_btn = QPushButton("⛔ Ngắt Kết Nối")
        self.disconnect_btn.setObjectName("danger-button")
        self.disconnect_btn.clicked.connect(self.on_disconnect)
        button_layout.addWidget(self.disconnect_btn)
        
        layout.addLayout(button_layout)
        
        return group
    
    def create_status_display(self):
        """Tạo display hiển thị trạng thái."""
        group = QGroupBox("Trạng Thái Kết Nối")
        layout = QVBoxLayout(group)
        layout.setSpacing(8)
        
        # Connection status
        status_layout = QHBoxLayout()
        status_layout.addWidget(QLabel("Trạng thái:"))
        self.status_label = QLabel("🔴 CHƯA KẾT NỐI")
        self.status_label.setObjectName("status-value")
        self.status_label.setStyleSheet("color: #EF4444; font-weight: 700;")
        status_layout.addWidget(self.status_label)
        status_layout.addStretch()
        layout.addLayout(status_layout)
        
        # IP address
        ip_layout = QHBoxLayout()
        ip_layout.addWidget(QLabel("IP công khai:"))
        self.ip_label = QLabel("N/A")
        self.ip_label.setObjectName("status-value")
        ip_layout.addWidget(self.ip_label)
        ip_layout.addStretch()
        layout.addLayout(ip_layout)
        
        return group
    
    def create_log_output(self):
        """Tạo text area cho log output."""
        group = QGroupBox("Nhật Ký Hoạt Động")
        layout = QVBoxLayout(group)
        
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        # Không set height cố định, để nó tự expand
        layout.addWidget(self.log_text)
        
        return group
    
    def log(self, message: str):
        """
        Ghi log vào text area.
        
        Args:
            message: Nội dung log
        """
        timestamp = time.strftime("%H:%M:%S")
        self.log_text.append(f"[{timestamp}] {message}")
    
    def load_countries(self):
        """Load danh sách quốc gia từ VPN Gate."""
        self.log("🔄 Đang tải danh sách quốc gia...")
        self.country_combo.clear()
        self.country_combo.addItem("Đang tải...")
        self.country_combo.setEnabled(False)
        self.connect_btn.setEnabled(False)
        self.refresh_btn.setEnabled(False)
        
        # Load trong background thread
        class CountryLoader(QThread):
            finished = pyqtSignal(dict)
            error = pyqtSignal(str)
            
            def __init__(self, vpn_core):
                super().__init__()
                self.vpn_core = vpn_core
            
            def run(self):
                try:
                    countries = self.vpn_core.list_countries()
                    self.finished.emit(countries)
                except Exception as e:
                    self.error.emit(str(e))
        
        self.country_loader = CountryLoader(self.vpn_core)
        self.country_loader.finished.connect(self.on_countries_loaded)
        self.country_loader.error.connect(self.on_countries_error)
        self.country_loader.start()
    
    def on_countries_loaded(self, countries):
        """Callback khi load countries thành công."""
        self.countries = countries
        self.country_combo.clear()
        
        # Sort và add vào combo
        sorted_countries = sorted(
            countries.items(),
            key=lambda x: x[1][0]['country']
        )
        
        for country_code, servers in sorted_countries:
            best_server = servers[0]
            speed_mbps = best_server['speed'] / 1000000
            label = f"{best_server['country']} ({country_code}) - {speed_mbps:.1f} Mbps"
            self.country_combo.addItem(label, country_code)
        
        self.country_combo.setEnabled(True)
        self.connect_btn.setEnabled(True)
        self.refresh_btn.setEnabled(True)

        self.log(f"✅ Đã tải {len(countries)} quốc gia khả dụng")
        self.log("💡 Lưu ý: VPN Gate API chỉ trả về top 100 servers tốt nhất")
        self.log("   Danh sách quốc gia thay đổi theo thời gian. Nhấn 'Làm Mới' để cập nhật.")
    
    def on_countries_error(self, error):
        """Callback khi load countries thất bại."""
        self.log(f"❌ Lỗi khi tải danh sách: {error}")
        self.country_combo.clear()
        self.country_combo.addItem("Lỗi - Thử lại")
        self.refresh_btn.setEnabled(True)
        
        QMessageBox.warning(
            self,
            "Lỗi",
            f"Không thể tải danh sách quốc gia:\n{error}\n\nThử lại bằng nút 'Làm Mới'"
        )
    
    def on_connect(self):
        """Xử lý khi nhấn nút Connect."""
        country_code = self.country_combo.currentData()
        if not country_code:
            return
        
        self.log(f"🔌 Bắt đầu kết nối VPN đến {country_code}...")
        
        # Disable buttons
        self.connect_btn.setEnabled(False)
        self.disconnect_btn.setEnabled(False)
        self.refresh_btn.setEnabled(False)
        self.country_combo.setEnabled(False)
        
        # Start worker thread
        self.worker = VPNWorker(self.vpn_core, 'connect', country_code)
        self.worker.progress.connect(self.log)
        self.worker.finished.connect(self.on_operation_finished)
        self.worker.start()
    
    def on_disconnect(self):
        """Xử lý khi nhấn nút Disconnect."""
        self.log("🔌 Bắt đầu ngắt kết nối VPN...")
        
        # Disable buttons
        self.connect_btn.setEnabled(False)
        self.disconnect_btn.setEnabled(False)
        self.refresh_btn.setEnabled(False)
        
        # Start worker thread
        self.worker = VPNWorker(self.vpn_core, 'disconnect')
        self.worker.progress.connect(self.log)
        self.worker.finished.connect(self.on_operation_finished)
        self.worker.start()
    
    def on_operation_finished(self, success, message):
        """Callback khi operation hoàn thành."""
        self.log(message)
        
        # Re-enable buttons
        self.connect_btn.setEnabled(True)
        self.disconnect_btn.setEnabled(True)
        self.refresh_btn.setEnabled(True)
        self.country_combo.setEnabled(True)
        
        # Update status ngay
        self.update_status()

        # KHÔNG hiển thị popup notification
        # Trạng thái đã được hiển thị trong cửa sổ chính và log
        # if success:
        #     QMessageBox.information(self, "Thành công", message)
        # else:
        #     QMessageBox.warning(self, "Thất bại", message)
    
    
    def update_status(self):
        """Cập nhật trạng thái kết nối."""
        status = self.vpn_core.get_status()
        
        if status['connected']:
            self.status_label.setText("🟢 ĐANG KẾT NỐI")
            self.status_label.setStyleSheet("color: #10B981; font-weight: 700;")
            
            ip = status.get('ip_address', 'N/A')
            self.ip_label.setText(ip)
        else:
            self.status_label.setText("🔴 CHƯA KẾT NỐI")
            self.status_label.setStyleSheet("color: #EF4444; font-weight: 700;")
            self.ip_label.setText("N/A")
    
    def closeEvent(self, event):
        """Xử lý khi đóng cửa sổ (nút X)."""
        # Stop timer
        self.status_timer.stop()
        
        # Nếu VPN đang kết nối, hỏi có muốn ngắt không
        if self.vpn_core.is_connected():
            reply = QMessageBox.question(
                self,
                "Xác nhận",
                "VPN đang kết nối. Bạn có muốn ngắt kết nối trước khi thoát không?",
                QMessageBox.Yes | QMessageBox.Cancel
            )
            
            if reply == QMessageBox.Cancel:
                # Không đóng cửa sổ, tiếp tục chạy
                self.status_timer.start(3000)  # Restart timer
                event.ignore()
                return
            elif reply == QMessageBox.Yes:
                # Ngắt kết nối VPN
                self.vpn_core.disconnect()
        
        # Đóng cửa sổ
        event.accept()


def main():
    """Entry point cho GUI application."""
    app = QApplication(sys.argv)
    
    # Set application font
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    
    # Create và show window
    window = VPNMainWindow()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
