"""Buoi 8 - Hoat dong 4.1: Doi mau cua so qua tham so command."""
import tkinter as tk


DANH_SACH_MAU = ["white", "lightblue", "lightgreen", "lightyellow", "lightpink"]


def create_app():
    cua_so = tk.Tk()
    cua_so.title("Doi mau nen")
    cua_so.geometry("360x220")
    cua_so.configure(bg=DANH_SACH_MAU[0])

    trang_thai = {"vi_tri": 0}

    def doi_mau_nen():
        trang_thai["vi_tri"] = (trang_thai["vi_tri"] + 1) % len(DANH_SACH_MAU)
        mau = DANH_SACH_MAU[trang_thai["vi_tri"]]
        cua_so.configure(bg=mau)
        nhan_mau.config(text=f"Mau hien tai: {mau}", bg=mau)
        nhan_huong_dan.config(bg=mau)

    nhan_huong_dan = tk.Label(
        cua_so, text="Nhan nut de doi mau nen", font=("Arial", 12), bg=DANH_SACH_MAU[0]
    )
    nhan_huong_dan.pack(pady=(35, 12))
    nhan_mau = tk.Label(cua_so, text="Mau hien tai: white", font=("Arial", 10), bg="white")
    nhan_mau.pack(pady=5)
    nut_doi_mau = tk.Button(cua_so, text="Doi mau nen", command=doi_mau_nen)
    nut_doi_mau.pack(pady=15)

    cua_so._nut_doi_mau = nut_doi_mau  # De kiem thu tu dong, khong anh huong giao dien.
    return cua_so


if __name__ == "__main__":
    app = create_app()
    app.mainloop()
