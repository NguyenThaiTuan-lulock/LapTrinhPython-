def them_sach(danh_sach, ma, ten, gia, soluong):
    """a) Them mot cuon sach gom Ma sach, Ten sach, Gia, So luong vao danh_sach"""
    sach_moi = {
        "MaSach": ma,
        "TenSach": ten,
        "Gia": float(gia),
        "SoLuong": int(soluong)
    }
    danh_sach.append(sach_moi)

def tim_kiem_theo_ten(danh_sach, tu_khoa):
    """b) Tra ve danh sach cac sach co TenSach chua tu_khoa"""
    ket_qua = []
    tu_khoa_thuong = tu_khoa.strip().lower()
    for sach in danh_sach:
        if tu_khoa_thuong in sach["TenSach"].lower():
            ket_qua.append(sach)
    return ket_qua

def tong_gia_tri_kho_sach(danh_sach):
    """c) Tra ve tong gia tri kho sach = tong (Gia * SoLuong) cua tat ca sach"""
    tong = 0
    for sach in danh_sach:
        tong += sach["Gia"] * sach["SoLuong"]
    return tong

def hien_thi_danh_sach(danh_sach):
    """Ham phu tro in danh sach ra man hinh"""
    if not danh_sach:
        print("-> Danh sach trong")
        return
    print(f"{'Ma sach':<10} | {'Ten sach':<32} | {'Gia':>10} | {'So luong':>8}")
    print("-" * 68)
    for s in danh_sach:
        print(f"{s['MaSach']:<10} | {s['TenSach']:<32} | {s['Gia']:>10,.0f} | {s['SoLuong']:>8}")

def main():
    danh_sach = [
        {"MaSach": "S01", "TenSach": "Lap trinh Python co ban", "Gia": 95000, "SoLuong": 40},
        {"MaSach": "S02", "TenSach": "Cau truc du lieu va giai thuat", "Gia": 120000, "SoLuong": 6},
        {"MaSach": "S03", "TenSach": "Nhap mon tri tue nhan tao", "Gia": 150000, "SoLuong": 25}
    ]

    while True:
        print("\n==== QUAN LY DANH SACH THU VIEN ====")
        print("1. Them sach")
        print("2. Tim kiem theo ten")
        print("3. Xem tong gia tri kho sach")
        print("4. Thoat chuong trinh")
        print("=====================================")

        chon = input("Nhap lua chon cua ban (1-4): ").strip()

        if chon == "1":
            print("\n--- Them sach moi ---")
            ma = input("Nhap ma sach: ").strip()
            ten = input("Nhap ten sach: ").strip()
            if not ma or not ten:
                print("-> Loi: Ma sach va Ten sach khong duoc de trong")
                continue
            try:
                gia = float(input("Nhap gia sach: "))
                soluong = int(input("Nhap so luong: "))
                if gia < 0 or soluong < 0:
                    print("-> Loi: Gia va so luong phai >= 0!")
                    continue
                them_sach(danh_sach, ma, ten, gia, soluong)
                print("-> Da them sach thanh cong! Danh sach hien tai:")
                hien_thi_danh_sach(danh_sach)
            except ValueError:
                print("-> Loi: Gia hoac So luong nhap khong hop le!")

        elif chon == "2":
            print("\n--- Tim kiem sach theo ten ---")
            tu_khoa = input("Nhap tu khoa ten sach can tim: ")
            kq = tim_kiem_theo_ten(danh_sach, tu_khoa)
            if kq:
                print(f"-> Tim thay {len(kq)} cuon sach phu hop:")
                hien_thi_danh_sach(kq)
            else:
                print("-> Khong tim thay cuon sach nao phu hop.")

        elif chon == "3":
            tong_tien = tong_gia_tri_kho_sach(danh_sach)
            print(f"\n-> Tong gia tri kho sach hien tai: {tong_tien:,.0f} VND")

        elif chon == "4":
            print("\nDa thoat chuong trinh. Tam biet")
            break
        else:
            print("-> Lua chon khong hop le, vui long nhap so tu 1 den 4.")

if __name__ == "__main__":
    main()