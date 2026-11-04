"""Hoạt động 3 - Signal/slot và một signal kết nối nhiều slot."""
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
)


class ViDuSignalSlot(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ví dụ Signal - Slot")
        self.resize(360, 180)

        self.o_nhap = QLineEdit()
        self.o_nhap.setPlaceholderText("Nhập nội dung cần hiển thị...")
        nut_hien_thi = QPushButton("Hiển thị nội dung")
        self.nhan_ket_qua = QLabel("Chưa có nội dung")

        layout = QVBoxLayout()
        layout.addWidget(self.o_nhap)
        layout.addWidget(nut_hien_thi)
        layout.addWidget(self.nhan_ket_qua)
        self.setLayout(layout)

        # Một signal clicked kết nối với hai slot.
        nut_hien_thi.clicked.connect(self.hien_thi_noi_dung)
        nut_hien_thi.clicked.connect(lambda: print("Nút vừa được bấm!"))

    def hien_thi_noi_dung(self):
        noi_dung = self.o_nhap.text()
        self.nhan_ket_qua.setText(f"Bạn vừa nhập: {noi_dung}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = ViDuSignalSlot()
    cua_so.show()
    sys.exit(app.exec_())
