
import math

print("=== BÀI 3.1 ===")
so_nguyen = 15
so_thuc = 4.2
so_phuc = 3 + 4j
print(type(so_nguyen), type(so_thuc), type(so_phuc))
print(float(so_nguyen))  # ép int -> float
print(int(so_thuc))      # ép float -> int, cắt phần thập phân

print("=== BÀI 3.2 ===")
a = -7
b = 2.6789
c, d = 17, 5
print(abs(a))
print(round(b))
print(round(b, 2))
print(pow(c, 2))
print(divmod(c, d))
print("c ** 2 =", c ** 2)
print("pow(c, 2) == c ** 2 ?", pow(c, 2) == c ** 2)

print("=== BÀI 3.3 ===")
a, b, c = 1, -3, 2
delta = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)
print(f"Delta = {delta}")
print(f"Nghiem x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")

print("=== BÀI 4.1 ===")
cau = "Lap trinh Python rat thu vi"
print(cau[0])
print(cau[-1])
print(cau[4:10])
print(cau[:8])
print(cau[11:])
print(cau[::-1])
print("Chuoi dao nguoc:", cau[::-1])
print("cau co phai palindrome?", cau == cau[::-1])

print("=== BÀI 4.2 ===")
ten = "Nam"
ten_moi = "T" + ten[1:]
print("Ten ban dau:", ten)
print("Ten moi:", ten_moi)

print("=== BÀI 4.3 ===")
cau = " Toi dang HOC Python rat vui "
print(cau.strip())
print(cau.strip().upper())
print(cau.strip().lower())
print(cau.strip().replace("HOC", "hoc"))
print(cau.strip().split())
print(len(cau.strip().split()))
print(cau.count("o"))
print(cau.find("Python"))
print(cau.strip().startswith("Toi"))
print(cau.strip().endswith("vui"))
print("-".join(["Python", "that", "thu", "vi"]))

print("=== BÀI 4.4 ===")
ho_ten_tho = " nguyen   van   an "
ho_ten_sach = " ".join(ho_ten_tho.split()).title()
print(ho_ten_sach)