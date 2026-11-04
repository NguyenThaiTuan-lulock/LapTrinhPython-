"""Hoạt động 2 - QLabel, QPushButton, QLineEdit, QComboBox."""
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QVBoxLayout,
)


class FormThongTin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ví dụ widget cơ bản")
        self.resize(340, 260)

        self.o_nhap_ten = QLineEdit()
        self.o_nhap_ten.setPlaceholderText("Nhập họ tên...")

        self.chon_thanh_pho = QComboBox()
        self.chon_thanh_pho.addItems(["Hà Nội", "Đà Nẵng", "TP.HCM", "Huế"])

        nut_xac_nhan = QPushButton("Xác nhận")
        self.nhan_ket_qua = QLabel("")
        nut_xac_nhan.clicked.connect(self.xu_ly_xac_nhan)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Họ tên:"))
        layout.addWidget(self.o_nhap_ten)
        layout.addWidget(QLabel("Thành phố:"))
        layout.addWidget(self.chon_thanh_pho)
        layout.addWidget(nut_xac_nhan)
        layout.addWidget(self.nhan_ket_qua)
        self.setLayout(layout)

    def xu_ly_xac_nhan(self):
        ten = self.o_nhap_ten.text().strip()
        thanh_pho = self.chon_thanh_pho.currentText()
        if not ten:
            self.nhan_ket_qua.setText("Vui lòng nhập họ tên.")
            return
        self.nhan_ket_qua.setText(f"Xin chào {ten}, đến từ {thanh_pho}!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = FormThongTin()
    cua_so.show()
    sys.exit(app.exec_())
