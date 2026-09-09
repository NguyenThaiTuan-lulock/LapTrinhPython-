import math

print("BAI 4.1 - KHAI BAO & TINH BAT BIEN ")
toa_do = (3, 5)
print("Toa do:", toa_do)
print("Kieu du lieu:", type(toa_do))
print("Tuple la kieu du lieu bat bien.")
print("Neu viet toa_do[0] = 10 thi Python se bao loi TypeError.")

print(" BAI 4.2 - UNPACKING TUPLE")

x, y = toa_do
print("x =", x, "- y =", y)
a, b = 10, 20
print("Truoc khi doi: a =", a, "- b =", b)

a, b = b, a
print("Sau khi doi: a =", a, "- b =", b)

print("BAI 4.3 - TRA VE NHIEU GIA TRI")
c, d = 17, 5
thuong_du = divmod(c, d)
thuong, du = thuong_du

print("Ket qua divmod:", thuong_du)
print(f"{c} chia {d} duoc thuong {thuong}, du {du}")

print("HOAT DONG 5 - KHOANG CACH GIUA HAI DIEM")

diem_a = (2, 3)
diem_b = (7, 8)
xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
print(
    f"Khoang cach giua {diem_a} va {diem_b} la:",
    round(khoang_cach, 2)
)

print("KHOANG CACH CAC DIEM DEN GOC TOA DO (0, 0)")
cac_diem = [(0, 0), (3, 4), (6, 8)]

for diem in cac_diem:
    x, y = diem
    khoang_cach_goc = math.sqrt(x ** 2 + y ** 2)
    print(
        f"Khoang cach tu {diem} den (0, 0) la:",
        round(khoang_cach_goc, 2)
    )
