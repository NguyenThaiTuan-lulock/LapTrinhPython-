#  Hoạt động 3: Vòng lặp for
print(" Hoat đong 3: Duyet for")
# for voi range()
print("Duyet range:")
for i in range(1, 6):
    print(i)

# for duyet list
print("\nDuyet list:")
diem_so = [8.5, 7.0, 9.2, 6.5]
for diem in diem_so:
    print("Diem:", diem)

# for duyet tuple
print("\nDuyet tuple:")
toa_do = (3, 5)
for gia_tri in toa_do:
    print(gia_tri)

# for duyet dictionary
print("\nDuyet dictionary:")
diem_mon = {"Toan": 8.0, "Ly": 7.5}
for mon, diem in diem_mon.items():
    print(mon, "-", diem)

# for duyet string
print("\nDuyet string:")
ten = "Python"
for ky_tu in ten:
    print(ky_tu)

# Bài tập vận dụng – Bảng cửu chương
print("\n Bang cuu chuong ")
n = 5
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# --- Bài tập 4.1 – Tính giai thừa của n ---
print("\n Bai 4.1: Giai thua ")
n = 5
giai_thua = 1
i = 1
while i <= n:
    giai_thua = giai_thua * i
    i += 1
print(f"{n}! = {giai_thua}")


print("\n Bai 4.2: Tong cac chu so ")
so = 4527
so_tam = so
tong_chu_so = 0
while so_tam > 0:
    chu_so = so_tam % 10
    tong_chu_so += chu_so
    so_tam = so_tam // 10
print(f"Tong cac chu so cua {so} la: {tong_chu_so}")