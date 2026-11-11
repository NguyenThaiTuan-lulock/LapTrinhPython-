"""Module thao tac voi co so du lieu SQLite cho ung dung quan ly tu sach."""

from pathlib import Path
import sqlite3
import sys


# Khi chay file .py: luu CSDL cung thu muc voi ma nguon.
# Khi dong goi bang PyInstaller: luu CSDL cung thu muc voi file .exe.
if getattr(sys, "frozen", False):
    THU_MUC_DU_LIEU = Path(sys.executable).resolve().parent
else:
    THU_MUC_DU_LIEU = Path(__file__).resolve().parent

TEN_FILE_CSDL = THU_MUC_DU_LIEU / "tu_sach.db"


def ket_noi_csdl():
    """Mo ket noi toi tep SQLite."""
    return sqlite3.connect(TEN_FILE_CSDL)


def tao_bang_neu_chua_co():
    """Tao bang sach trong lan chay dau tien."""
    ket_noi = ket_noi_csdl()
    try:
        con_tro = ket_noi.cursor()
        con_tro.execute(
            """
            CREATE TABLE IF NOT EXISTS sach (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ten_sach TEXT NOT NULL,
                tac_gia TEXT NOT NULL,
                the_loai TEXT NOT NULL,
                da_doc INTEGER NOT NULL DEFAULT 0 CHECK (da_doc IN (0, 1))
            )
            """
        )
        ket_noi.commit()
    finally:
        ket_noi.close()


def them_sach(ten_sach, tac_gia, the_loai):
    """Them mot cuon sach moi; sach moi mac dinh chua doc."""
    ten_sach = ten_sach.strip()
    tac_gia = tac_gia.strip()
    the_loai = the_loai.strip()

    if not ten_sach or not tac_gia or not the_loai:
        raise ValueError("Ten sach, tac gia va the loai khong duoc de trong.")

    ket_noi = ket_noi_csdl()
    try:
        con_tro = ket_noi.cursor()
        con_tro.execute(
            """
            INSERT INTO sach (ten_sach, tac_gia, the_loai, da_doc)
            VALUES (?, ?, ?, 0)
            """,
            (ten_sach, tac_gia, the_loai),
        )
        ket_noi.commit()
    finally:
        ket_noi.close()


def lay_toan_bo_sach():
    """Lay danh sach sach, sap xep theo ma sach tang dan."""
    ket_noi = ket_noi_csdl()
    try:
        con_tro = ket_noi.cursor()
        con_tro.execute(
            """
            SELECT id, ten_sach, tac_gia, the_loai, da_doc
            FROM sach
            ORDER BY id
            """
        )
        return con_tro.fetchall()
    finally:
        ket_noi.close()


def xoa_sach(id_sach):
    """Xoa sach theo ma sach."""
    ket_noi = ket_noi_csdl()
    try:
        con_tro = ket_noi.cursor()
        con_tro.execute("DELETE FROM sach WHERE id = ?", (id_sach,))
        ket_noi.commit()
        return con_tro.rowcount > 0
    finally:
        ket_noi.close()


def danh_dau_da_doc(id_sach):
    """Chuyen trang thai sach sang da doc."""
    ket_noi = ket_noi_csdl()
    try:
        con_tro = ket_noi.cursor()
        con_tro.execute(
            "UPDATE sach SET da_doc = 1 WHERE id = ?",
            (id_sach,),
        )
        ket_noi.commit()
        return con_tro.rowcount > 0
    finally:
        ket_noi.close()


def thong_ke_theo_the_loai():
    """Dem so sach trong tung the loai."""
    ket_noi = ket_noi_csdl()
    try:
        con_tro = ket_noi.cursor()
        con_tro.execute(
            """
            SELECT the_loai, COUNT(*)
            FROM sach
            GROUP BY the_loai
            ORDER BY the_loai
            """
        )
        return con_tro.fetchall()
    finally:
        ket_noi.close()
