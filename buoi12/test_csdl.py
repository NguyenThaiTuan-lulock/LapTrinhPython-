"""
test_csdl.py - Kiem thu module csdl_sinh_vien.py doc lap (chua can giao dien).
Dung file DB tam rieng nen KHONG anh huong den sinh_vien.db that.
Chay:  python test_csdl.py
"""
import os
import csdl_sinh_vien as db

db.TEN_FILE_CSDL = "test_sinh_vien.db"
if os.path.exists(db.TEN_FILE_CSDL):
    os.remove(db.TEN_FILE_CSDL)

db.tao_bang_neu_chua_co()

print("1) Them 5 sinh vien")
db.them_sinh_vien("SV001", "Nguyen Van An", "CNTT1", 8.5)
db.them_sinh_vien("SV002", "Tran Thi Binh", "CNTT1", 7.0)
db.them_sinh_vien("SV003", "Le Van Cuong", "KTPM1", 9.0)
db.them_sinh_vien("SV004", "Pham Thi Dung", "KHMT1", 6.5)
db.them_sinh_vien("SV005", "Hoang Van Em", "CNTT1", 7.5)
for dong in db.lay_toan_bo_sinh_vien():
    print("  ", dong)
assert len(db.lay_toan_bo_sinh_vien()) == 5

print("\n2) Them trung ma SV phai bi tu choi")
try:
    db.them_sinh_vien("SV001", "Trung Ma", "CNTT1", 5)
    raise AssertionError("Phai nem ValueError khi trung ma SV")
except ValueError as loi:
    print("   Bat duoc loi dung:", loi)
assert len(db.lay_toan_bo_sinh_vien()) == 5

print("\n3) Danh dau da dong hoc phi id=1")
db.danh_dau_da_dong_hoc_phi(1)
assert db.lay_toan_bo_sinh_vien()[0][5] == 1
assert db.lay_toan_bo_sinh_vien()[1][5] == 0

print("4) Cap nhat id=2 (doi ten, lop, diem)")
db.cap_nhat_sinh_vien(2, "SV002", "Tran Thi Binh Minh", "KTPM1", 8.0)
sv2 = db.lay_toan_bo_sinh_vien()[1]
print("  ", sv2)
assert sv2[2] == "Tran Thi Binh Minh" and sv2[3] == "KTPM1" and sv2[4] == 8.0

print("5) Cap nhat thanh ma da ton tai phai bi tu choi")
try:
    db.cap_nhat_sinh_vien(2, "SV003", "X", "CNTT1", 5)
    raise AssertionError("Phai nem ValueError khi sua thanh ma trung")
except ValueError:
    print("   Bat duoc loi dung")

print("6) Tim kiem")
assert len(db.tim_kiem_sinh_vien("Van")) == 3        # An, Cuong, Em
assert len(db.tim_kiem_sinh_vien("SV004")) == 1
assert len(db.tim_kiem_sinh_vien("CNTT1")) == 2      # SV001, SV005 (SV002 da chuyen sang KTPM1)
print("  ", [d[1] for d in db.tim_kiem_sinh_vien("CNTT1")])

print("7) Xoa id=3")
db.xoa_sinh_vien(3)
assert len(db.lay_toan_bo_sinh_vien()) == 4

print("\n8) Thong ke theo lop (lop, so luong, diem TB):")
thong_ke = db.thong_ke_theo_lop()
print("  ", thong_ke)

os.remove(db.TEN_FILE_CSDL)
print("\nTEST PASS - module csdl_sinh_vien hoat dong dung")
