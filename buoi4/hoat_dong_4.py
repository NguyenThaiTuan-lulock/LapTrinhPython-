print("Bai tap 4.1 - ep kieu tuong minh:")
chuoi_so = "25"
so = int(chuoi_so)
print(so, type(so))

so_thuc = float("3.14")
print(so_thuc, type(so_thuc))

danh_sach = list((1, 2, 3))
bo_ba = tuple([4, 5, 6])
tap_hop = set([1, 2, 2, 3, 3, 3])
tu_dien = dict([("a", 1), ("b", 2)])
print(danh_sach, bo_ba, tap_hop, tu_dien)

print("Bai tap 4.2 - Truong hop gay loi khi ep kieu:")
print('int("abc") gay ValueError vi "abc" khong bieu dien mot so nguyen.')
print('int("3.14") gay ValueError vi chuoi co dau thap phan.')

# Hai dong duoi day duoc giu o dang chu thich de chuong trinh van chay thanh cong.
# int("abc")
# int("3.14")

so_hop_le = int(float("3.14"))
print("Ep qua float truoc:", so_hop_le)

print("Bai tap 4.3 - Chuyen đoi ngam đinh:")
ket_qua = 5 + 2.5
print(ket_qua, type(ket_qua))

ket_qua_2 = "Diem: " + str(8.5)
print(ket_qua_2)