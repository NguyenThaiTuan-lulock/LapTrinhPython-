"""
ung_dung_sinh_vien.py
Giao dien Tkinter cho ung dung Quan ly Sinh vien.
Moi thao tac du lieu deu goi lai cac ham trong csdl_sinh_vien.py.
"""
import tkinter as tk
from tkinter import ttk, messagebox

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.ticker import MaxNLocator

import csdl_sinh_vien as db

DANH_SACH_LOP = ["CNTT1", "CNTT2", "KTPM1", "KHMT1", "HTTT1", "Khác"]


class UngDungSinhVien(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quản lý Sinh viên")
        self.geometry("820x660")
        self.resizable(False, False)

        self.du_lieu_hien_tai = {}     # {id: dòng dữ liệu} đang hiển thị trong bảng
        self.id_dang_sua = None        # id sinh viên đang được chọn để sửa
        self.tu_khoa_loc = ""          # từ khóa tìm kiếm hiện tại ("" = hiện tất cả)
        self.cua_so_thong_ke = None

        db.tao_bang_neu_chua_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach()

    # ------------------------------------------------------------------ GIAO DIỆN
    def khoi_tao_giao_dien(self):
        # ---- Khung nhập liệu
        khung_nhap = tk.LabelFrame(self, text="Thông tin sinh viên", padx=10, pady=5)
        khung_nhap.pack(pady=(10, 5), padx=10, fill="x")

        tk.Label(khung_nhap, text="Mã SV:").grid(row=0, column=0, sticky="w", pady=5)
        self.o_ma_sv = tk.Entry(khung_nhap, width=28)
        self.o_ma_sv.grid(row=0, column=1, padx=(5, 20), pady=5)

        tk.Label(khung_nhap, text="Họ tên:").grid(row=0, column=2, sticky="w", pady=5)
        self.o_ho_ten = tk.Entry(khung_nhap, width=34)
        self.o_ho_ten.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(khung_nhap, text="Lớp:").grid(row=1, column=0, sticky="w", pady=5)
        self.chon_lop = ttk.Combobox(khung_nhap, values=DANH_SACH_LOP,
                                     width=25, state="readonly")
        self.chon_lop.current(0)
        self.chon_lop.grid(row=1, column=1, padx=(5, 20), pady=5)

        tk.Label(khung_nhap, text="Điểm TB (0-10):").grid(row=1, column=2, sticky="w", pady=5)
        self.o_diem = tk.Entry(khung_nhap, width=34)
        self.o_diem.grid(row=1, column=3, padx=5, pady=5)

        khung_nut_form = tk.Frame(khung_nhap)
        khung_nut_form.grid(row=2, column=0, columnspan=4, pady=8)

        tk.Button(khung_nut_form, text="Thêm sinh viên", bg="#2e8b57", fg="white",
                  width=16, command=self.xu_ly_them).grid(row=0, column=0, padx=5)
        self.nut_cap_nhat = tk.Button(khung_nut_form, text="Cập nhật", bg="#1f6fb2",
                                      fg="white", width=16, state="disabled",
                                      command=self.xu_ly_cap_nhat)
        self.nut_cap_nhat.grid(row=0, column=1, padx=5)
        tk.Button(khung_nut_form, text="Làm mới form", width=16,
                  command=self.lam_moi_form).grid(row=0, column=2, padx=5)

        # ---- Khung tìm kiếm
        khung_tim = tk.LabelFrame(self, text="Tìm kiếm (mã SV, họ tên hoặc lớp)",
                                  padx=10, pady=5)
        khung_tim.pack(pady=5, padx=10, fill="x")

        self.o_tim = tk.Entry(khung_tim, width=50)
        self.o_tim.pack(side="left", padx=(0, 10))
        self.o_tim.bind("<Return>", lambda _e: self.xu_ly_tim_kiem())
        tk.Button(khung_tim, text="Tìm", width=10,
                  command=self.xu_ly_tim_kiem).pack(side="left", padx=5)
        tk.Button(khung_tim, text="Hiện tất cả", width=12,
                  command=self.xu_ly_hien_tat_ca).pack(side="left", padx=5)

        # ---- Khung bảng danh sách (Treeview)
        khung_bang = tk.LabelFrame(self, text="Danh sách sinh viên", padx=5, pady=5)
        khung_bang.pack(pady=5, padx=10, fill="both", expand=True)

        cot = ("ma_sv", "ho_ten", "lop", "diem_tb", "hoc_phi")
        self.bang = ttk.Treeview(khung_bang, columns=cot, show="headings",
                                 selectmode="browse", height=12)
        tieu_de = {"ma_sv": ("Mã SV", 110, "w"), "ho_ten": ("Họ tên", 260, "w"),
                   "lop": ("Lớp", 90, "center"), "diem_tb": ("Điểm TB", 90, "center"),
                   "hoc_phi": ("Học phí", 110, "center")}
        for ten_cot, (nhan, rong, can_le) in tieu_de.items():
            self.bang.heading(ten_cot, text=nhan)
            self.bang.column(ten_cot, width=rong, anchor=can_le)
        self.bang.tag_configure("da_dong", background="#e6f4ea")
        self.bang.pack(side="left", fill="both", expand=True)
        self.bang.bind("<<TreeviewSelect>>", self.khi_chon_dong)

        thanh_cuon = ttk.Scrollbar(khung_bang, orient="vertical", command=self.bang.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.bang.configure(yscrollcommand=thanh_cuon.set)

        # ---- Dòng tổng kết
        self.nhan_tong = tk.Label(self, text="", anchor="w")
        self.nhan_tong.pack(padx=12, fill="x")

        # ---- Khung nút thao tác
        khung_nut = tk.Frame(self)
        khung_nut.pack(pady=8)
        tk.Button(khung_nut, text="Đánh dấu đã đóng học phí", bg="#1f6fb2", fg="white",
                  command=self.xu_ly_dong_hoc_phi).grid(row=0, column=0, padx=5)
        tk.Button(khung_nut, text="Xóa sinh viên", bg="#c62828", fg="white",
                  command=self.xu_ly_xoa).grid(row=0, column=1, padx=5)
        tk.Button(khung_nut, text="Thống kê theo lớp", bg="#ef8a00", fg="white",
                  command=self.xu_ly_thong_ke).grid(row=0, column=2, padx=5)

    # ------------------------------------------------------------------ TIỆN ÍCH
    def tai_lai_danh_sach(self):
        """Đọc lại dữ liệu từ CSDL (có áp dụng bộ lọc tìm kiếm) và vẽ lại bảng."""
        for dong in self.bang.get_children():
            self.bang.delete(dong)

        if self.tu_khoa_loc:
            ket_qua = db.tim_kiem_sinh_vien(self.tu_khoa_loc)
        else:
            ket_qua = db.lay_toan_bo_sinh_vien()

        self.du_lieu_hien_tai = {}
        so_da_dong = 0
        for id_sv, ma_sv, ho_ten, lop, diem_tb, da_dong in ket_qua:
            self.du_lieu_hien_tai[id_sv] = (id_sv, ma_sv, ho_ten, lop, diem_tb, da_dong)
            trang_thai = "Đã đóng" if da_dong == 1 else "Chưa đóng"
            so_da_dong += da_dong
            self.bang.insert("", tk.END, iid=str(id_sv),
                             values=(ma_sv, ho_ten, lop, f"{diem_tb:.2f}", trang_thai),
                             tags=("da_dong",) if da_dong == 1 else ())

        tong = len(ket_qua)
        tieu_de = f"Đang lọc theo \"{self.tu_khoa_loc}\" - " if self.tu_khoa_loc else ""
        self.nhan_tong.config(
            text=f"{tieu_de}Tổng: {tong} sinh viên  |  Đã đóng học phí: {so_da_dong}  |  "
                 f"Chưa đóng: {tong - so_da_dong}")

    def lay_id_dang_chon(self):
        """Trả về id sinh viên đang chọn trong bảng, hoặc None nếu chưa chọn."""
        lua_chon = self.bang.selection()
        return int(lua_chon[0]) if lua_chon else None

    def lam_moi_form(self):
        self.o_ma_sv.delete(0, tk.END)
        self.o_ho_ten.delete(0, tk.END)
        self.o_diem.delete(0, tk.END)
        self.chon_lop.current(0)
        self.id_dang_sua = None
        self.nut_cap_nhat.config(state="disabled")
        if self.bang.selection():
            self.bang.selection_remove(self.bang.selection())

    def khi_chon_dong(self, _su_kien=None):
        """Chọn một dòng trong bảng -> đổ dữ liệu lên form để sửa."""
        id_sv = self.lay_id_dang_chon()
        if id_sv is None or id_sv not in self.du_lieu_hien_tai:
            return
        _, ma_sv, ho_ten, lop, diem_tb, _ = self.du_lieu_hien_tai[id_sv]

        self.o_ma_sv.delete(0, tk.END)
        self.o_ma_sv.insert(0, ma_sv)
        self.o_ho_ten.delete(0, tk.END)
        self.o_ho_ten.insert(0, ho_ten)
        self.o_diem.delete(0, tk.END)
        self.o_diem.insert(0, f"{diem_tb:g}")
        self.chon_lop.set(lop if lop in DANH_SACH_LOP else "Khác")

        self.id_dang_sua = id_sv
        self.nut_cap_nhat.config(state="normal")

    def doc_du_lieu_form(self):
        """Kiểm tra dữ liệu nhập. Trả về (ma_sv, ho_ten, lop, diem) hoặc None nếu lỗi."""
        ma_sv = self.o_ma_sv.get().strip()
        ho_ten = " ".join(self.o_ho_ten.get().split())   # bỏ khoảng trắng thừa
        lop = self.chon_lop.get()
        diem_chuoi = self.o_diem.get().strip().replace(",", ".")

        if ma_sv == "" or ho_ten == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ mã sinh viên và họ tên.")
            return None
        if diem_chuoi == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập điểm trung bình.")
            return None
        try:
            diem = float(diem_chuoi)
        except ValueError:
            messagebox.showerror("Lỗi", "Điểm trung bình phải là một con số (ví dụ 8.5).")
            return None
        if not 0 <= diem <= 10:
            messagebox.showerror("Lỗi", "Điểm trung bình phải nằm trong khoảng từ 0 đến 10.")
            return None
        return ma_sv, ho_ten, lop, round(diem, 2)

    # ------------------------------------------------------------------ XỬ LÝ SỰ KIỆN
    def xu_ly_them(self):
        du_lieu = self.doc_du_lieu_form()
        if du_lieu is None:
            return
        try:
            db.them_sinh_vien(*du_lieu)
        except ValueError as loi:           # trùng mã sinh viên
            messagebox.showerror("Lỗi", str(loi))
            return
        self.lam_moi_form()
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thành công", f"Đã thêm sinh viên: {du_lieu[1]}")

    def xu_ly_cap_nhat(self):
        if self.id_dang_sua is None:
            messagebox.showerror("Lỗi", "Vui lòng chọn một sinh viên trong danh sách để cập nhật.")
            return
        du_lieu = self.doc_du_lieu_form()
        if du_lieu is None:
            return
        try:
            db.cap_nhat_sinh_vien(self.id_dang_sua, *du_lieu)
        except ValueError as loi:
            messagebox.showerror("Lỗi", str(loi))
            return
        self.lam_moi_form()
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thành công", f"Đã cập nhật sinh viên: {du_lieu[1]}")

    def xu_ly_xoa(self):
        id_sv = self.lay_id_dang_chon()
        if id_sv is None:
            messagebox.showerror("Lỗi", "Vui lòng chọn một sinh viên trong danh sách để xóa.")
            return
        ho_ten = self.du_lieu_hien_tai[id_sv][2]
        if not messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xóa sinh viên \"{ho_ten}\"?"):
            return
        db.xoa_sinh_vien(id_sv)
        self.lam_moi_form()
        self.tai_lai_danh_sach()

    def xu_ly_dong_hoc_phi(self):
        id_sv = self.lay_id_dang_chon()
        if id_sv is None:
            messagebox.showerror("Lỗi", "Vui lòng chọn một sinh viên để đánh dấu đã đóng học phí.")
            return
        if self.du_lieu_hien_tai[id_sv][5] == 1:
            messagebox.showinfo("Thông báo", "Sinh viên này đã đóng học phí rồi.")
            return
        db.danh_dau_da_dong_hoc_phi(id_sv)
        self.tai_lai_danh_sach()
        if self.bang.exists(str(id_sv)):            # giữ lại dòng đang chọn
            self.bang.selection_set(str(id_sv))

    def xu_ly_tim_kiem(self):
        self.tu_khoa_loc = self.o_tim.get().strip()
        self.lam_moi_form()
        self.tai_lai_danh_sach()
        if self.tu_khoa_loc and not self.du_lieu_hien_tai:
            messagebox.showinfo("Thông báo", "Không tìm thấy sinh viên nào phù hợp.")

    def xu_ly_hien_tat_ca(self):
        self.o_tim.delete(0, tk.END)
        self.tu_khoa_loc = ""
        self.lam_moi_form()
        self.tai_lai_danh_sach()

    def xu_ly_thong_ke(self):
        du_lieu = db.thong_ke_theo_lop()
        if not du_lieu:
            messagebox.showinfo("Thông báo", "Chưa có dữ liệu sinh viên để thống kê.")
            return

        cac_lop = [dong[0] for dong in du_lieu]
        so_luong = [dong[1] for dong in du_lieu]
        diem_tb = [dong[2] for dong in du_lieu]

        if self.cua_so_thong_ke is not None and self.cua_so_thong_ke.winfo_exists():
            self.cua_so_thong_ke.destroy()
        cua_so = tk.Toplevel(self)
        cua_so.title("Thống kê sinh viên theo lớp")
        self.cua_so_thong_ke = cua_so

        hinh = Figure(figsize=(10, 4.4), dpi=100)
        # Biểu đồ 1: số lượng sinh viên mỗi lớp
        truc1 = hinh.add_subplot(1, 2, 1)
        cot1 = truc1.bar(cac_lop, so_luong, color="cornflowerblue", width=0.5)
        truc1.bar_label(cot1)
        truc1.set_title("SỐ LƯỢNG SINH VIÊN THEO LỚP", fontweight="bold", fontsize=11)
        truc1.set_xlabel("Lớp")
        truc1.set_ylabel("Số sinh viên")
        truc1.yaxis.set_major_locator(MaxNLocator(integer=True))
        truc1.set_ylim(0, max(so_luong) + 1)
        truc1.grid(axis="y", linestyle="--", alpha=0.5)
        truc1.set_axisbelow(True)

        # Biểu đồ 2: điểm trung bình mỗi lớp
        truc2 = hinh.add_subplot(1, 2, 2)
        cot2 = truc2.bar(cac_lop, diem_tb, color="seagreen", width=0.5)
        truc2.bar_label(cot2, fmt="%.2f")
        truc2.set_title("ĐIỂM TRUNG BÌNH THEO LỚP", fontweight="bold", fontsize=11)
        truc2.set_xlabel("Lớp")
        truc2.set_ylabel("Điểm TB")
        truc2.set_ylim(0, 10)
        truc2.grid(axis="y", linestyle="--", alpha=0.5)
        truc2.set_axisbelow(True)
        hinh.tight_layout()

        khung_ve = FigureCanvasTkAgg(hinh, master=cua_so)
        khung_ve.draw()
        thanh_cong_cu = NavigationToolbar2Tk(khung_ve, cua_so)   # có nút lưu ảnh PNG
        thanh_cong_cu.update()
        khung_ve.get_tk_widget().pack(side="top", fill="both", expand=True)


if __name__ == "__main__":
    ung_dung = UngDungSinhVien()
    ung_dung.mainloop()
