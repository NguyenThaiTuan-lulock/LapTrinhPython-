
print("=== BÀI 1.1 ===")
ho_ten = input("Nhap ho ten: ")
nam_sinh = int(input("Nhap nam sinh: "))
diem_tb = float(input("Nhap diem trung binh: "))

print("Kieu du lieu:", type(ho_ten), type(nam_sinh), type(diem_tb))

print("=== BÀI 1.2 ===")
print("Python", "la", "ngon", "ngu", "lap trinh", sep="-")
print("Python", "la", "ngon", "ngu", "lap trinh", sep=", ")
print("Python", "la", "ngon", "ngu", "lap trinh", sep="\n")
print("Dong 1", end=" | ")
print("Dong 2")

print("\n=== BÀI 1.3 - 3 CÁCH ĐỊNH DẠNG CHUỖI ===")
# f-string
print(f"Ho ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb:.2f}")

# str.format()
print("Ho ten: {} - Nam sinh: {} - DTB: {:.2f}".format(ho_ten, nam_sinh, diem_tb))

# toán tử %
print("Ho ten: %s - Nam sinh: %d - DTB: %.2f" % (ho_ten, nam_sinh, diem_tb))


print("=== BÀI 2.1 ===")
# Chú thích một dòng: khai báo thông tin sinh viên
"""
Chú thích/docstring nhiều dòng:
Chương trình quản lý điểm sinh viên - Buổi 2
"""
ho_ten_mau = "Tran Thi B"  # biến lưu họ tên
print("Ho ten mau:", ho_ten_mau)

print("=== BÀI 2.2 ===")
s1 = 'Xin chao'
s2 = "Ban co khoe khong?"
s3 = '''Day la
mot chuoi
nhieu dong'''
s4 = "Duong dan: C:\\Python\\data"
s5 = r"Duong dan raw: C:\Python\data"
s6 = "Toi ten la \"Nam\", con ban ten gi?"

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)

