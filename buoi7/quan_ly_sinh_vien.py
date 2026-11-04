"""
DO AN CHUONG 1 - QUAN LY SINH VIEN
Bam sat yeu cau Buoi 7: list + dict, ham, menu console, try-except.
"""


danh_sach_sinh_vien = [
    {"mssv": "001", "ho_ten": "Nguyen Van An", "lop": "DH14C5", "nam_sinh": 2006, "diem_tb": 8.2},
    {"mssv": "002", "ho_ten": "Tran Thi Binh", "lop": "DH14C5", "nam_sinh": 2006, "diem_tb": 7.5},
    {"mssv": "003", "ho_ten": "Le Minh Chau", "lop": "DH14C5", "nam_sinh": 2006, "diem_tb": 9.0},
    {"mssv": "004", "ho_ten": "Pham Quoc Dung", "lop": "DH14C5", "nam_sinh": 2005, "diem_tb": 6.8},
]


def tim_sinh_vien_theo_mssv(mssv):
    """Tra ve sinh vien theo MSSV, khong tim thay thi tra None."""
    for sinh_vien in danh_sach_sinh_vien:
        if sinh_vien["mssv"] == mssv:
            return sinh_vien
    return None


def xep_loai(diem_tb):
    if diem_tb >= 8.5:
        return "Gioi"
    if diem_tb >= 7.0:
        return "Kha"
    if diem_tb >= 5.0:
        return "Trung binh"
    return "Yeu"


def nhap_so_nguyen(loi_nhac, min_value=None, max_value=None):
    """Nhap so nguyen an toan bang try-except."""
    while True:
        try:
            gia_tri = int(input(loi_nhac))
            if min_value is not None and gia_tri < min_value:
                print(f"-> Gia tri phai >= {min_value}, vui long nhap lai.")
                continue
            if max_value is not None and gia_tri > max_value:
                print(f"-> Gia tri phai <= {max_value}, vui long nhap lai.")
                continue
            return gia_tri
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so nguyen.")


def nhap_diem_tb(loi_nhac="Nhap diem trung binh (0-10): "):
    while True:
        try:
            diem = float(input(loi_nhac))
            if 0 <= diem <= 10:
                return diem
            print("-> Diem phai nam trong khoang 0-10, vui long nhap lai.")
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so.")


def hien_thi_danh_sach():
    print("\n" + "=" * 92)
    print(f"{'MSSV':<10}{'Ho ten':<24}{'Lop':<12}{'Nam sinh':<12}{'Diem TB':<12}{'Xep loai':<15}")
    print("-" * 92)
    if len(danh_sach_sinh_vien) == 0:
        print("-> Danh sach sinh vien dang trong.")
    else:
        for sv in danh_sach_sinh_vien:
            print(
                f"{sv['mssv']:<10}{sv['ho_ten']:<24}{sv['lop']:<12}"
                f"{sv['nam_sinh']:<12}{sv['diem_tb']:<12.1f}{xep_loai(sv['diem_tb']):<15}"
            )
    print("=" * 92)


def them_sinh_vien(mssv, ho_ten, lop, nam_sinh, diem_tb):
    if tim_sinh_vien_theo_mssv(mssv) is not None:
        print(f"-> MSSV {mssv} da ton tai, khong the them.")
        return False

    danh_sach_sinh_vien.append({
        "mssv": mssv,
        "ho_ten": ho_ten,
        "lop": lop,
        "nam_sinh": nam_sinh,
        "diem_tb": diem_tb,
    })
    print(f"-> Da them sinh vien {mssv} thanh cong.")
    return True


def sua_sinh_vien(mssv):
    sv = tim_sinh_vien_theo_mssv(mssv)
    if sv is None:
        print(f"-> Khong tim thay sinh vien {mssv}.")
        return False

    print(f"-> Dang sua sinh vien: {sv['ho_ten']}")
    ho_ten = input(f"Ho ten moi [{sv['ho_ten']}]: ").strip()
    lop = input(f"Lop moi [{sv['lop']}]: ").strip().upper()
    nam_sinh = nhap_so_nguyen(f"Nam sinh moi [{sv['nam_sinh']}]: ", 1900, 2100)
    diem_tb = nhap_diem_tb(f"Diem TB moi [{sv['diem_tb']}]: ")

    if ho_ten:
        sv["ho_ten"] = ho_ten.title()
    if lop:
        sv["lop"] = lop
    sv["nam_sinh"] = nam_sinh
    sv["diem_tb"] = diem_tb
    print(f"-> Da cap nhat sinh vien {mssv} thanh cong.")
    return True


def xoa_sinh_vien(mssv):
    sv = tim_sinh_vien_theo_mssv(mssv)
    if sv is None:
        print(f"-> Khong tim thay sinh vien {mssv}.")
        return False

    danh_sach_sinh_vien.remove(sv)
    print(f"-> Da xoa sinh vien {mssv} - {sv['ho_ten']}.")
    return True


def tim_kiem_sinh_vien(tu_khoa):
    tu_khoa = tu_khoa.lower()
    ket_qua = [
        sv for sv in danh_sach_sinh_vien
        if tu_khoa in sv["mssv"].lower()
        or tu_khoa in sv["ho_ten"].lower()
        or tu_khoa in sv["lop"].lower()
    ]

    if len(ket_qua) == 0:
        print("-> Khong tim thay sinh vien phu hop.")
        return

    print(f"\n-> Tim thay {len(ket_qua)} sinh vien:")
    for sv in ket_qua:
        print(
            f"  {sv['mssv']} - {sv['ho_ten']} - {sv['lop']} - "
            f"Diem TB: {sv['diem_tb']:.1f} - {xep_loai(sv['diem_tb'])}"
        )


def thong_ke():
    print("\nTHONG KE SINH VIEN")
    if len(danh_sach_sinh_vien) == 0:
        print("-> Chua co du lieu.")
        return

    tong_diem = sum(sv["diem_tb"] for sv in danh_sach_sinh_vien)
    diem_tb_lop = tong_diem / len(danh_sach_sinh_vien)
    sinh_vien_gioi = sum(1 for sv in danh_sach_sinh_vien if xep_loai(sv["diem_tb"]) == "Gioi")
    sinh_vien_kha = sum(1 for sv in danh_sach_sinh_vien if xep_loai(sv["diem_tb"]) == "Kha")
    sinh_vien_tb = sum(1 for sv in danh_sach_sinh_vien if xep_loai(sv["diem_tb"]) == "Trung binh")
    sinh_vien_yeu = sum(1 for sv in danh_sach_sinh_vien if xep_loai(sv["diem_tb"]) == "Yeu")

    print(f"-> Tong so sinh vien: {len(danh_sach_sinh_vien)}")
    print(f"-> Diem trung binh chung: {diem_tb_lop:.2f}")
    print(f"-> Gioi: {sinh_vien_gioi}")
    print(f"-> Kha: {sinh_vien_kha}")
    print(f"-> Trung binh: {sinh_vien_tb}")
    print(f"-> Yeu: {sinh_vien_yeu}")


def hien_thi_menu():
    print("\n===== QUAN LY SINH VIEN =====")
    print("1. Hien thi danh sach")
    print("2. Them sinh vien")
    print("3. Sua sinh vien")
    print("4. Xoa sinh vien")
    print("5. Tim kiem sinh vien")
    print("6. Thong ke")
    print("0. Thoat")


def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban: ").strip()

        if lua_chon == "1":
            hien_thi_danh_sach()

        elif lua_chon == "2":
            mssv = input("Nhap MSSV: ").strip().upper()
            ho_ten = input("Nhap ho ten: ").strip().title()
            lop = input("Nhap lop: ").strip().upper()
            nam_sinh = nhap_so_nguyen("Nhap nam sinh: ", 1900, 2100)
            diem_tb = nhap_diem_tb()
            them_sinh_vien(mssv, ho_ten, lop, nam_sinh, diem_tb)

        elif lua_chon == "3":
            mssv = input("Nhap MSSV can sua: ").strip().upper()
            sua_sinh_vien(mssv)

        elif lua_chon == "4":
            mssv = input("Nhap MSSV can xoa: ").strip().upper()
            xoa_sinh_vien(mssv)

        elif lua_chon == "5":
            tu_khoa = input("Nhap MSSV, ho ten hoac lop can tim: ").strip()
            tim_kiem_sinh_vien(tu_khoa)

        elif lua_chon == "6":
            thong_ke()

        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break

        else:
            print("-> Lua chon khong hop le, vui long chon lai.")


if __name__ == "__main__":
    chay_chuong_trinh()
