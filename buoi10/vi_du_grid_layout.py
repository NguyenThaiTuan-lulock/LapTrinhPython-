"""Bài 1.2 - Minh họa QGridLayout và QHBoxLayout."""
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QGridLayout,
    QHBoxLayout,
)


class ViDuGridLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ví dụ QHBoxLayout và QGridLayout")
        self.resize(360, 200)

        # QGridLayout sắp xếp widget theo hàng và cột.
        grid = QGridLayout()
        grid.addWidget(QLabel("Họ tên:"), 0, 0)
        grid.addWidget(QLabel("Tuổi:"), 1, 0)

        # QHBoxLayout sắp xếp các nút theo chiều ngang.
        hang_nut = QHBoxLayout()
        nut_dong_y = QPushButton("Đồng ý")
        nut_huy = QPushButton("Hủy")
        nut_dong_y.clicked.connect(self.dong_y)
        nut_huy.clicked.connect(self.close)
        hang_nut.addWidget(nut_dong_y)
        hang_nut.addWidget(nut_huy)
        grid.addLayout(hang_nut, 2, 0, 1, 2)

        self.setLayout(grid)

    def dong_y(self):
        print("Bạn đã nhấn Đồng ý.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = ViDuGridLayout()
    cua_so.show()
    sys.exit(app.exec_())
