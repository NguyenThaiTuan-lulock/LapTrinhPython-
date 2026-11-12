"""
test_giao_dien.py - Kiem thu giao dien Tkinter bang cach mo phong thao tac nguoi dung
(khong can click chuot that). Dung file DB tam rieng.
Chay:  python test_giao_dien.py
"""
import os
from tkinter import messagebox

import csdl_sinh_vien as db

db.TEN_FILE_CSDL = "test_gui_sinh_vien.db"
if os.path.exists(db.TEN_FILE_CSDL):
    os.remove(db.TEN_FILE_CSDL)

# --- Chan cac hop thoai de test khong bi dung lai cho bam OK; ghi lai noi dung de kiem tra
nhat_ky = []
messagebox.showerror = lambda tieu_de, noi_dung, **kw: nhat_ky.append(("loi", noi_dung))
messagebox.showinfo = lambda tieu_de, noi_dung, **kw: nhat_ky.append(("info", noi_dung))
messagebox.askyesno = lambda tieu_de, noi_dung, **kw: True

from ung_dung_sinh_vien import UngDungSinhVien   # import SAU khi da vo hieu hoa hop thoai

app = UngDungSinhVien()
app.update()


def nhap(ma, ten, lop, diem):
    app.lam_moi_form()
    app.o_ma_sv.insert(0, ma)
    app.o_ho_ten.insert(0, ten)
    app.chon_lop.set(lop)
    app.o_diem.insert(0, diem)


def so_dong():
    return len(app.bang.get_children())


print("1) Them 3 sinh vien hop le")
nhap("SV001", "Nguyễn Văn An", "CNTT1", "8.5");  app.xu_ly_them()
nhap("SV002", "Trần Thị Bình", "CNTT1", "7,5");  app.xu_ly_them()   # dau phay van duoc chap nhan
nhap("SV003", "Lê Văn Cường", "KTPM1", "9");     app.xu_ly_them()
assert so_dong() == 3, so_dong()

print("2) Validate: de trong ma/ten")
nhap("", "", "CNTT1", "5");  app.xu_ly_them()
assert nhat_ky[-1][0] == "loi" and so_dong() == 3

print("3) Validate: diem khong phai so / ngoai khoang")
nhap("SV010", "Test", "CNTT1", "abc");  app.xu_ly_them()
assert nhat_ky[-1][0] == "loi"
nhap("SV010", "Test", "CNTT1", "11");   app.xu_ly_them()
assert nhat_ky[-1][0] == "loi" and so_dong() == 3

print("4) Validate: trung ma sinh vien")
nhap("SV001", "Nguoi Trung", "CNTT1", "5");  app.xu_ly_them()
assert nhat_ky[-1][0] == "loi" and "đã tồn tại" in nhat_ky[-1][1] and so_dong() == 3

print("5) Chon dong -> form tu dien; sua ten + diem; cap nhat")
app.lam_moi_form()
app.bang.selection_set("1"); app.update()
assert app.o_ma_sv.get() == "SV001" and app.id_dang_sua == 1
assert str(app.nut_cap_nhat["state"]) == "normal"
app.o_ho_ten.delete(0, "end"); app.o_ho_ten.insert(0, "Nguyễn Văn An (đã sửa)")
app.o_diem.delete(0, "end");   app.o_diem.insert(0, "9.5")
app.xu_ly_cap_nhat()
assert db.lay_toan_bo_sinh_vien()[0][2] == "Nguyễn Văn An (đã sửa)"
assert db.lay_toan_bo_sinh_vien()[0][4] == 9.5

print("6) Danh dau da dong hoc phi")
app.bang.selection_set("2"); app.update()
app.xu_ly_dong_hoc_phi()
assert db.lay_toan_bo_sinh_vien()[1][5] == 1
assert "da_dong" in app.bang.item("2", "tags")

print("7) Tim kiem")
app.o_tim.insert(0, "KTPM1"); app.xu_ly_tim_kiem()
assert so_dong() == 1
app.xu_ly_hien_tat_ca()
assert so_dong() == 3
app.o_tim.insert(0, "khong-co-ai"); app.xu_ly_tim_kiem()
assert so_dong() == 0 and nhat_ky[-1][0] == "info"
app.xu_ly_hien_tat_ca()

print("8) Xoa khi chua chon -> bao loi; chon roi xoa")
app.lam_moi_form()
app.xu_ly_xoa()
assert nhat_ky[-1][0] == "loi" and so_dong() == 3
app.bang.selection_set("3"); app.update()
app.xu_ly_xoa()
assert so_dong() == 2

print("9) Thong ke -> mo cua so bieu do")
app.xu_ly_thong_ke(); app.update()
assert app.cua_so_thong_ke.winfo_exists()

print("10) Du lieu van con sau khi dong va mo lai ung dung")
app.destroy()
app2 = UngDungSinhVien(); app2.update()
assert len(app2.bang.get_children()) == 2
app2.destroy()

os.remove(db.TEN_FILE_CSDL)
print("\nTEST PASS - toan bo chuc nang cua giao dien hoat dong dung")
