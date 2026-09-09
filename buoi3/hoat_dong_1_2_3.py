print("Bai 1.1 - Khai bao & truy cap")

diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]

print("Danh sach diem:", diem_so)
print("Phan tu dau tien:", diem_so[0])
print("Phan tu cuoi cung:", diem_so[-1])
print("Cac phan tu tu vi tri 1 den truoc 4:", diem_so[1:4])
print("Lay cac phan tu voi step = 2:", diem_so[::2])
print("Dao nguoc danh sach:", diem_so[::-1])


print("Bai 1.2 - cac phuong thuc thuong dung")

ten_sv = ["An", "Binh", "Chi"]
print("Danh sach ban dau:", ten_sv)

ten_sv.append("Dung")
print("Sau append('Dung'):", ten_sv)
ten_sv.insert(1, "Em")
print("Sau insert(1, 'Em'):", ten_sv)

ten_sv.remove("Chi")
print("Sau remove('Chi'):", ten_sv)
pop_ra = ten_sv.pop()
print("Sau pop():", ten_sv)
print("Phan tu vua bi xoa:", pop_ra)

ten_sv.sort()
print("Sau sort():", ten_sv)

ten_sv.reverse()
print("Sau reverse():", ten_sv)

ten_sv.extend(["Giang", "Hoa"])
print("Sau extend(['Giang', 'Hoa']):", ten_sv)

print("Bai 2.1 - Duyet list bang for")

diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]

tong = 0
for diem in diem_so:
    print("Diem:", diem)
    tong = tong + diem

print("Tong diem:", tong)
print("Diem trung binh:", round(tong / len(diem_so), 2))


print("bai 2.2 - List long nhau (ma tran)")

ma_tran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("In ma tran theo tung hang:")
for hang in ma_tran:
    print(hang)

print("In tung phan tu cua ma tran:")
for hang in ma_tran:
    for phan_tu in hang:
        print(phan_tu, end=" ")
    print()

# Yeu cau bo sung: tinh tong tat ca phan tu bang 2 vong for long nhau
tong_ma_tran = 0
for hang in ma_tran:
    for phan_tu in hang:
        tong_ma_tran = tong_ma_tran + phan_tu

print("Tong tat ca phan tu trong ma tran:", tong_ma_tran)


print("Bai 3.1 -  Loc so chan/le")

day_so = list(range(1, 21))

so_chan = [x for x in day_so if x % 2 == 0]
so_le = [x for x in day_so if x % 2 != 0]

print("Day so:", day_so)
print("So chan:", so_chan)
print("So le:", so_le)


print("Bai 3.2 - Bien doi phan tu ")

diem_so = [8.5, 7.0, 9.2, 6.5, 5.5]

diem_cong = [round(diem + 0.5, 2) for diem in diem_so]

print("Diem ban dau:", diem_so)
print("Diem sau khi cong 0.5:", diem_cong)
