danh_sach_sv = [
    (8.5, "An"),
    (7.0, "Binh"),
    (9.2, "Chi"),
    (6.5, "Dung")
]

print("DANH SACH SINH VIEN BAN DAU")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")


# Them sinh vien moi
danh_sach_sv.append((8.0, "Em"))

print(" SAU KHI THEM SINH VIEN EM ")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")


# Xoa sinh vien Binh
danh_sach_sv.remove((7.0, "Binh"))

print(" SAU KHI XOA SINH VIEN BINH ")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")


# Sua diem cho sinh vien o vi tri 0
danh_sach_sv[0] = (9.0, danh_sach_sv[0][1])

print(" SAU KHI SUA DIEM CUA AN THANH 9.0")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")


# Kiem tra sinh vien Chi co trong danh sach hay khong
print(
    "\nChi co trong danh sach khong?",
    (9.2, "Chi") in danh_sach_sv
)


# Sap xep tang dan theo diem
danh_sach_sv.sort()

print(" SAP XEP THEO DIEM TANG DAN")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")


# Sap xep giam dan theo diem
danh_sach_sv.sort(reverse=True)

print("SAP XEP THEO DIEM GIAM DAN")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")
