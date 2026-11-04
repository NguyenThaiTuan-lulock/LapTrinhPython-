import pandas as pd

# 1. Đọc file CSV và xem tổng quan
df = pd.read_csv("Buoi11/diem_sinh_vien.csv")
print("--- 5 dòng đầu ---")
print(df.head())
print("Số dòng, số cột:", df.shape)
print("Tên các cột:", df.columns.tolist())

# 2. Thống kê theo môn học
print("\n--- Điểm trung bình theo môn học ---")
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()
print(diem_trung_binh_mon)

print("Điểm trung bình toàn bộ:", df["diem"].mean())
print("Điểm cao nhất:", df["diem"].max())
print("Điểm thấp nhất:", df["diem"].min())

# 3. Tính điểm trung bình (DTB) từng sinh viên & lọc đạt/không đạt
print("\n--- Điểm trung bình của từng sinh viên ---")
diem_tb_sv = df.groupby("ho_ten")["diem"].mean().round(2)
print(diem_tb_sv)

# Lọc sinh viên đạt (DTB >= 5.0) và không đạt
sinh_vien_dat = diem_tb_sv[diem_tb_sv >= 5.0]
sinh_vien_khong_dat = diem_tb_sv[diem_tb_sv < 5.0]

print("\nSinh viên đạt:")
print(sinh_vien_dat)
print("\nSinh viên không đạt:")
print(sinh_vien_khong_dat)