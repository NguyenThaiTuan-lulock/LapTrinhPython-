"""Hoạt động 6 - Mini project To-do list viết bằng PyQt5."""
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QListWidget,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
)


class UngDungToDo(QWidget):
    def __init__(self):
        super().__init__()
        # Mỗi phần tử gồm (nội dung công việc, trạng thái hoàn thành).
        self.danh_sach_cong_viec = []
        self.khoi_tao_giao_dien()

    def khoi_tao_giao_dien(self):
        self.setWindowTitle("Ứng dụng Ghi chú công việc - PyQt")
        self.resize(460, 430)

        tieu_de = QLabel("TO-DO LIST (PyQt)")
        tieu_de.setStyleSheet("font-size: 18px; font-weight: bold; padding: 6px;")

        self.o_nhap_cong_viec = QLineEdit()
        self.o_nhap_cong_viec.setPlaceholderText("Nhập công việc mới...")
        self.o_nhap_cong_viec.returnPressed.connect(self.them_cong_viec)

        nut_them = QPushButton("Thêm")
        nut_them.clicked.connect(self.them_cong_viec)

        hang_nhap_lieu = QHBoxLayout()
        hang_nhap_lieu.addWidget(self.o_nhap_cong_viec)
        hang_nhap_lieu.addWidget(nut_them)

        self.danh_sach_hien_thi = QListWidget()

        nut_hoan_thanh = QPushButton("Đánh dấu hoàn thành")
        nut_hoan_thanh.clicked.connect(self.danh_dau_hoan_thanh)

        nut_xoa = QPushButton("Xóa công việc")
        nut_xoa.clicked.connect(self.xoa_cong_viec)

        hang_nut_thao_tac = QHBoxLayout()
        hang_nut_thao_tac.addWidget(nut_hoan_thanh)
        hang_nut_thao_tac.addWidget(nut_xoa)

        layout_chinh = QVBoxLayout()
        layout_chinh.addWidget(tieu_de)
        layout_chinh.addLayout(hang_nhap_lieu)
        layout_chinh.addWidget(self.danh_sach_hien_thi)
        layout_chinh.addLayout(hang_nut_thao_tac)
        self.setLayout(layout_chinh)

    def lam_moi_danh_sach(self):
        self.danh_sach_hien_thi.clear()
        for noi_dung, da_hoan_thanh in self.danh_sach_cong_viec:
            tien_to = "[Đã xong] " if da_hoan_thanh else "[Chưa xong] "
            self.danh_sach_hien_thi.addItem(tien_to + noi_dung)

    def them_cong_viec(self):
        noi_dung = self.o_nhap_cong_viec.text().strip()
        if not noi_dung:
            QMessageBox.critical(
                self,
                "Lỗi",
                "Vui lòng nhập nội dung công việc trước khi thêm.",
            )
            return

        self.danh_sach_cong_viec.append((noi_dung, False))
        self.o_nhap_cong_viec.clear()
        self.lam_moi_danh_sach()

    def xoa_cong_viec(self):
        vi_tri = self.danh_sach_hien_thi.currentRow()
        if vi_tri < 0:
            QMessageBox.critical(
                self,
                "Lỗi",
                "Vui lòng chọn một công việc trong danh sách để xóa.",
            )
            return

        self.danh_sach_cong_viec.pop(vi_tri)
        self.lam_moi_danh_sach()

    def danh_dau_hoan_thanh(self):
        vi_tri = self.danh_sach_hien_thi.currentRow()
        if vi_tri < 0:
            QMessageBox.critical(
                self,
                "Lỗi",
                "Vui lòng chọn một công việc để đánh dấu hoàn thành.",
            )
            return

        noi_dung, _ = self.danh_sach_cong_viec[vi_tri]
        self.danh_sach_cong_viec[vi_tri] = (noi_dung, True)
        self.lam_moi_danh_sach()
        self.danh_sach_hien_thi.setCurrentRow(vi_tri)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = UngDungToDo()
    cua_so.show()
    sys.exit(app.exec_())
