kho_hang = [
    ("Ban phim", 250000, 10),
    ("Chuot", 150000, 20),
    ("Man hinh", 2500000, 5)
]

print(" KHO HANG BAN DAU ")
for ten, gia, so_luong in kho_hang:
    print(f"{ten:<12} - Gia: {gia:>10,} VND - SL: {so_luong}")


# Them san pham moi
kho_hang.append(("Tai nghe", 300000, 15))

print("SAU KHI THEM TAI NGHE")
for ten, gia, so_luong in kho_hang:
    print(f"{ten:<12} - Gia: {gia:>10,} VND - SL: {so_luong}")


# Xoa san pham Chuot
kho_hang.remove(("Chuot", 150000, 20))

print(" SAU KHI XOA CHUOT ")
for ten, gia, so_luong in kho_hang:
    print(f"{ten:<12} - Gia: {gia:>10,} VND - SL: {so_luong}")


# Hien thi danh sach kho hang
print(" DANH SACH KHO HANG HIEN TAI")
for ten, gia, so_luong in kho_hang:
    print(f"{ten:<12} - Gia: {gia:>10,} VND - SL: {so_luong}")


# Tinh tong gia tri kho hang
tong_gia_tri = 0

for ten, gia, so_luong in kho_hang:
    tong_gia_tri = tong_gia_tri + gia * so_luong

print(f"\nTong gia tri kho hang: {tong_gia_tri:,} VND")
