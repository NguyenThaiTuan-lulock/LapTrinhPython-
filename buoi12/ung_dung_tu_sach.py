
"""Giao dien Tkinter cho ung dung Quan ly Tu sach ca nhan."""

import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import csdl_sach as db


DANH_SACH_THE_LOAI = [
    "Ky nang song",
    "Tieu thuyet",
    "Lich su",
    "Khoa hoc",
    "Kinh te",
    "Khac",
]


class UngDungTuSach(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly Tu sach ca nhan")
        self.geometry("760x570")
        self.minsize(700, 520)

        self.danh_sach_hien_tai = []

        db.tao_bang_neu_chua_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach_sach()

    def khoi_tao_giao_dien(self):
        tieu_de = tk.Label(
            self,
            text="QUAN LY TU SACH CA NHAN",
            font=("Arial", 17, "bold"),
        )
        tieu_de.pack(pady=(12, 8))

        khung_nhap = ttk.LabelFrame(self, text="Thong tin sach", padding=10)
        khung_nhap.pack(padx=12, pady=5, fill="x")
        khung_nhap.columnconfigure(1, weight=1)

        ttk.Label(khung_nhap, text="Ten sach:").grid(
            row=0, column=0, sticky="w", padx=5, pady=6
        )
        self.o_nhap_ten_sach = ttk.Entry(khung_nhap, width=45)
        self.o_nhap_ten_sach.grid(
            row=0, column=1, sticky="ew", padx=5, pady=6
        )

        ttk.Label(khung_nhap, text="Tac gia:").grid(
            row=1, column=0, sticky="w", padx=5, pady=6
        )
        self.o_nhap_tac_gia = ttk.Entry(khung_nhap, width=45)
        self.o_nhap_tac_gia.grid(
            row=1, column=1, sticky="ew", padx=5, pady=6
        )

        ttk.Label(khung_nhap, text="The loai:").grid(
            row=2, column=0, sticky="w", padx=5, pady=6
        )
        self.chon_the_loai = ttk.Combobox(
            khung_nhap,
            values=DANH_SACH_THE_LOAI,
            state="readonly",
            width=42,
        )
        self.chon_the_loai.current(0)
        self.chon_the_loai.grid(
            row=2, column=1, sticky="w", padx=5, pady=6
        )

        ttk.Button(
            khung_nhap,
            text="Them sach",
            command=self.xu_ly_them_sach,
        ).grid(row=3, column=0, columnspan=2, pady=(8, 2))

        khung_danh_sach = ttk.LabelFrame(
            self,
            text="Danh sach sach (chon mot dong de thao tac)",
            padding=8
        )
        khung_danh_sach.pack(
            padx=12, pady=8, fill="both", expand=True
        )

        self.listbox_sach = tk.Listbox(
            khung_danh_sach,
            width=95,
            height=14,
            font=("Consolas", 10),
            activestyle="dotbox",
        )
        self.listbox_sach.pack(side="left", fill="both", expand=True)

        thanh_cuon = ttk.Scrollbar(
            khung_danh_sach,
            orient="vertical",
            command=self.listbox_sach.yview,
        )
        thanh_cuon.pack(side="right", fill="y")
        self.listbox_sach.configure(yscrollcommand=thanh_cuon.set)

        khung_nut_thao_tac = ttk.Frame(self)
        khung_nut_thao_tac.pack(pady=(0, 12))

        ttk.Button(
            khung_nut_thao_tac,
            text="Danh dau da doc",
            command=self.xu_ly_danh_dau_da_doc,
        ).grid(row=0, column=0, padx=6)

        ttk.Button(
            khung_nut_thao_tac,
            text="Xoa sach",
            command=self.xu_ly_xoa_sach,
        ).grid(row=0, column=1, padx=6)

        ttk.Button(
            khung_nut_thao_tac,
            text="Thong ke theo the loai",
            command=self.xu_ly_thong_ke,
        ).grid(row=0, column=2, padx=6)

    def tai_lai_danh_sach_sach(self):
        """Doc lai CSDL va cap nhat Listbox."""
        self.listbox_sach.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo_sach()

        for sach in self.danh_sach_hien_tai:
            id_sach, ten_sach, tac_gia, the_loai, da_doc = sach
            trang_thai = "Da doc" if da_doc == 1 else "Chua doc"
            dong_hien_thi = (
                f"Ma: {id_sach:<4} | {trang_thai:<8} | "
                f"{ten_sach} - {tac_gia} ({the_loai})"
            )
            self.listbox_sach.insert(tk.END, dong_hien_thi)

    def xu_ly_them_sach(self):
        ten_sach = self.o_nhap_ten_sach.get().strip()
        tac_gia = self.o_nhap_tac_gia.get().strip()
        the_loai = self.chon_the_loai.get().strip()

        if not ten_sach or not tac_gia or not the_loai:
            messagebox.showerror(
                "Thieu thong tin",
                "Vui long nhap ten sach, tac gia va chon the loai.",
            )
            return

        try:
            db.them_sach(ten_sach, tac_gia, the_loai)
            self.o_nhap_ten_sach.delete(0, tk.END)
            self.o_nhap_tac_gia.delete(0, tk.END)
            self.chon_the_loai.current(0)
            self.tai_lai_danh_sach_sach()
            messagebox.showinfo(
                "Thanh cong", f"Da them sach: {ten_sach}"
            )
        except (ValueError, sqlite3.Error) as loi:
            messagebox.showerror("Loi", str(loi))

    def lay_id_sach_dang_chon(self):
        """Tra ve ID sach tu dong Listbox dang duoc chon."""
        lua_chon = self.listbox_sach.curselection()
        if not lua_chon:
            messagebox.showwarning(
                "Chua chon sach",
                "Vui long chon mot cuon sach trong danh sach.",
            )
            return None

        vi_tri = lua_chon[0]
        return self.danh_sach_hien_tai[vi_tri][0]

    def xu_ly_xoa_sach(self):
        id_sach = self.lay_id_sach_dang_chon()
        if id_sach is None:
            return

        dong_sach = self.danh_sach_hien_tai[
            self.listbox_sach.curselection()[0]
        ]
        ten_sach = dong_sach[1]

        xac_nhan = messagebox.askyesno(
            "Xac nhan xoa",
            f"Ban co chac muon xoa sach '{ten_sach}' khong?"
        )
        if not xac_nhan:
            return

        try:
            db.xoa_sach(id_sach)
            self.tai_lai_danh_sach_sach()
            messagebox.showinfo("Thanh cong", f"Da xoa sach: {ten_sach}")
        except sqlite3.Error as loi:
            messagebox.showerror("Loi co so du lieu", str(loi))

    def xu_ly_danh_dau_da_doc(self):
        lua_chon = self.listbox_sach.curselection()
        id_sach = self.lay_id_sach_dang_chon()
        if id_sach is None:
            return

        sach = self.danh_sach_hien_tai[lua_chon[0]]
        if sach[4] == 1:
            messagebox.showinfo(
                "Thong bao",
                f"'{sach[1]}' da duoc danh dau la da doc."
            )
            return

        try:
            db.danh_dau_da_doc(id_sach)
            self.tai_lai_danh_sach_sach()
            messagebox.showinfo(
                "Thanh cong",
                f"Da danh dau '{sach[1]}' la da doc."
            )
        except sqlite3.Error as loi:
            messagebox.showerror("Loi co so du lieu", str(loi))

    def xu_ly_thong_ke(self):
        du_lieu_thong_ke = db.thong_ke_theo_the_loai()
        if not du_lieu_thong_ke:
            messagebox.showinfo(
                "Chua co du lieu",
                "Chua co sach de thong ke."
            )
            return

        cac_the_loai = [dong[0] for dong in du_lieu_thong_ke]
        so_luong = [dong[1] for dong in du_lieu_thong_ke]

        fig, truc = plt.subplots(figsize=(8, 4.5))
        truc.bar(cac_the_loai, so_luong)
        truc.set_title("So luong sach theo the loai")
        truc.set_xlabel("The loai")
        truc.set_ylabel("So luong sach")
        truc.set_ylim(bottom=0)
        truc.tick_params(axis="x", rotation=15)

        for vi_tri, gia_tri in enumerate(so_luong):
            truc.text(vi_tri, gia_tri, str(gia_tri), ha="center", va="bottom")

        fig.tight_layout()
        plt.show()


if __name__ == "__main__":
    ung_dung = UngDungTuSach()
    ung_dung.mainloop()
