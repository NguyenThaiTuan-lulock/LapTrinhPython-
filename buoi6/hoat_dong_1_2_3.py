
print("Bài tập 1.1: Các hàm toán học cơ bản")
def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bscnn(a, b):
    return a * b // uscln(a, b)

def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def kiem_tra_so_hoan_thien(n):
    if n <= 0:
        return False
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n

print("THỬ NGHIỆM HOẠT ĐỘNG 1.1 (3 BỘ DỮ LIỆU) ")
# Bộ dữ liệu 1
print(f"USCLN(24, 36): {uscln(24, 36)} | BSCNN(4, 6): {bscnn(4, 6)}")
print(f"Nguyên tố (29): {kiem_tra_nguyen_to(29)} | Hoàn thiện (28): {kiem_tra_so_hoan_thien(28)}")

# Bộ dữ liệu 2
print(f"USCLN(17, 13): {uscln(17, 13)} | BSCNN(12, 18): {bscnn(12, 18)}")
print(f"Nguyên tố (15): {kiem_tra_nguyen_to(15)} | Hoàn thiện (6): {kiem_tra_so_hoan_thien(6)}")

# Bộ dữ liệu 3
print(f"USCLN(100, 75): {uscln(100, 75)} | BSCNN(8, 14): {bscnn(8, 14)}")
print(f"Nguyên tố (2): {kiem_tra_nguyen_to(2)} | Hoàn thiện (12): {kiem_tra_so_hoan_thien(12)}\n")


def in_loi_chao(ten):
    print(f"Xin chao, {ten}!")
    return  

def chia_lay_thuong_du(a, b):
    return a // b, a % b  

print("Bài tập 1.2  return không giá trị và trả về nhiều giá trị:")
in_loi_chao("An")
thuong, du = chia_lay_thuong_du(17, 5)
print(f"17 chia 5 -> Thương: {thuong}, Dư: {du}\n")

print("Hoạt động 2: Tham số mặc định & tham số từ khóa")
def gioi_thieu(ten, tuoi=18, lop="Chua ro"):
    print(f"Ten: {ten} - Tuoi: {tuoi} - Lop: {lop}")

gioi_thieu("An")                             
gioi_thieu("Binh", 20)                       
gioi_thieu("Chi", lop="CNTT01")               
gioi_thieu(ten="Dung", lop="CNTT02", tuoi=19) 
print()


print("Hoạt động 3: Tham số linh hoạt - *args và **kwargs")
def tinh_tong(*args):
    tong = 0
    for so in args:
        tong += so
    return tong

print("Tổng (1, 2, 3):", tinh_tong(1, 2, 3))
print("Tổng (5, 10, 15, 20, 25):", tinh_tong(5, 10, 15, 20, 25))
print("Tổng không truyền số:", tinh_tong())
print()


def in_thong_tin(ho_ten, tuoi, **kwargs):
    print(f"Ho ten: {ho_ten} - Tuoi: {tuoi}")
    for khoa, gia_tri in kwargs.items():
        print(f"  {khoa}: {gia_tri}")

in_thong_tin("Nguyen Thai Tuan", 20, lop="CNTT01", que_quan="Ha Noi")
in_thong_tin("Tran Thi B", 21, email="b@example.com")