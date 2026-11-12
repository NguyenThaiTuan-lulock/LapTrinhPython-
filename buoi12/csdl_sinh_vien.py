"""
csdl_sinh_vien.py
Module thao tac CSDL SQLite cho ung dung Quan ly Sinh vien.
Module nay KHONG biet gi ve giao dien - chi nhan du lieu vao va tra du lieu ra.
"""
import os
import sys
import sqlite3


def lay_thu_muc_chay():
    """Tra ve thu muc dat file .db:
    - canh file .exe neu da dong goi bang PyInstaller
    - canh file .py neu chay binh thuong"""
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


TEN_FILE_CSDL = os.path.join(lay_thu_muc_chay(), "sinh_vien.db")


def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)


def _truy_van(cau_lenh, tham_so=()):
    """Chay cau lenh SELECT, tra ve danh sach dong."""
    ket_noi = ket_noi_csdl()
    try:
        con_tro = ket_noi.cursor()
        con_tro.execute(cau_lenh, tham_so)
        return con_tro.fetchall()
    finally:
        ket_noi.close()


def _thuc_thi_ghi(cau_lenh, tham_so=()):
    """Chay cau lenh INSERT/UPDATE/DELETE va commit."""
    ket_noi = ket_noi_csdl()
    try:
        con_tro = ket_noi.cursor()
        con_tro.execute(cau_lenh, tham_so)
        ket_noi.commit()
    finally:
        ket_noi.close()


def tao_bang_neu_chua_co():
    _thuc_thi_ghi("""
        CREATE TABLE IF NOT EXISTS sinh_vien (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ma_sv TEXT NOT NULL UNIQUE,
            ho_ten TEXT NOT NULL,
            lop TEXT NOT NULL,
            diem_tb REAL NOT NULL DEFAULT 0,
            da_dong_hoc_phi INTEGER NOT NULL DEFAULT 0
        )
    """)


def them_sinh_vien(ma_sv, ho_ten, lop, diem_tb):
    """Them sinh vien moi. Nem ValueError neu ma sinh vien da ton tai."""
    try:
        _thuc_thi_ghi(
            "INSERT INTO sinh_vien (ma_sv, ho_ten, lop, diem_tb, da_dong_hoc_phi) "
            "VALUES (?, ?, ?, ?, 0)",
            (ma_sv, ho_ten, lop, diem_tb)
        )
    except sqlite3.IntegrityError:
        raise ValueError(f"Mã sinh viên '{ma_sv}' đã tồn tại.")


def lay_toan_bo_sinh_vien():
    return _truy_van(
        "SELECT id, ma_sv, ho_ten, lop, diem_tb, da_dong_hoc_phi "
        "FROM sinh_vien ORDER BY id"
    )


def tim_kiem_sinh_vien(tu_khoa):
    """Tim theo ma SV, ho ten hoac lop.
    Luu y: LIKE cua SQLite chi khong phan biet hoa/thuong voi chu cai ASCII (a-z)."""
    mau = f"%{tu_khoa}%"
    return _truy_van(
        "SELECT id, ma_sv, ho_ten, lop, diem_tb, da_dong_hoc_phi FROM sinh_vien "
        "WHERE ma_sv LIKE ? OR ho_ten LIKE ? OR lop LIKE ? ORDER BY id",
        (mau, mau, mau)
    )


def cap_nhat_sinh_vien(id_sv, ma_sv, ho_ten, lop, diem_tb):
    """Sua thong tin sinh vien. Nem ValueError neu ma SV moi bi trung."""
    try:
        _thuc_thi_ghi(
            "UPDATE sinh_vien SET ma_sv = ?, ho_ten = ?, lop = ?, diem_tb = ? WHERE id = ?",
            (ma_sv, ho_ten, lop, diem_tb, id_sv)
        )
    except sqlite3.IntegrityError:
        raise ValueError(f"Mã sinh viên '{ma_sv}' đã tồn tại.")


def xoa_sinh_vien(id_sv):
    _thuc_thi_ghi("DELETE FROM sinh_vien WHERE id = ?", (id_sv,))


def danh_dau_da_dong_hoc_phi(id_sv):
    _thuc_thi_ghi("UPDATE sinh_vien SET da_dong_hoc_phi = 1 WHERE id = ?", (id_sv,))


def thong_ke_theo_lop():
    """Tra ve [(lop, so_luong, diem_tb_trung_binh), ...] sap xep theo ten lop."""
    return _truy_van(
        "SELECT lop, COUNT(*), ROUND(AVG(diem_tb), 2) "
        "FROM sinh_vien GROUP BY lop ORDER BY lop"
    )
