"""Hoạt động 5 - Nạp giao diện Qt Designer từ form_dang_nhap.ui."""
import sys
from pathlib import Path
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class CuaSoDangNhap(QWidget):
    def __init__(self):
        super().__init__()
        tep_giao_dien = Path(__file__).with_name("form_dang_nhap.ui")
        uic.loadUi(str(tep_giao_dien), self)
        self.nut_dang_nhap.clicked.connect(self.xu_ly_dang_nhap)

    def xu_ly_dang_nhap(self):
        tai_khoan = self.o_nhap_tai_khoan.text().strip()
        mat_khau = self.o_nhap_mat_khau.text()

        if not tai_khoan or not mat_khau:
            QMessageBox.critical(
                self,
                "Lỗi",
                "Vui lòng nhập đầy đủ tài khoản và mật khẩu.",
            )
            return

        # Bài thực hành chỉ minh họa giao diện và signal-slot,
        # chưa xác thực với cơ sở dữ liệu hay hệ thống tài khoản thật.
        QMessageBox.information(
            self,
            "Thành công",
            f"Xin chào {tai_khoan}, đăng nhập thành công!",
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = CuaSoDangNhap()
    cua_so.show()
    sys.exit(app.exec_())
