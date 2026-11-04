import numpy as np

# Khai báo list Python thuần và chuyển sang mảng NumPy (ndarray)
diem_list = [8.5, 7.0, 9.2, 6.5, 5.5]
diem_array = np.array(diem_list)

print("Kiểu dữ liệu:", type(diem_list), type(diem_array))

# Phép toán vector hóa: cộng trực tiếp 0.5 vào TOÀN BỘ mảng mà không cần vòng lặp
diem_cong_them = diem_array + 0.5
print("Mảng sau khi cộng 0.5 (NumPy):", diem_cong_them)

# So sánh với cách làm bằng list thuần (phải dùng list comprehension)
diem_cong_them_list = [diem + 0.5 for diem in diem_list]
print("List sau khi cộng 0.5 (List comprehension):", diem_cong_them_list)

# Các hàm thống kê cơ bản
print("Trung bình:", np.mean(diem_array))
print("Lớn nhất:", np.max(diem_array))
print("Nhỏ nhất:", np.min(diem_array))
print("Độ lệch chuẩn:", round(np.std(diem_array), 2))

# Thao tác với ma trận 2 chiều
ma_tran = np.array([[1, 2, 3], [4, 5, 6]])
print("Ma tran:\n", ma_tran)
print("Kích thước (shape):", ma_tran.shape)
print("Ma tran nhân 2:\n", ma_tran * 2)