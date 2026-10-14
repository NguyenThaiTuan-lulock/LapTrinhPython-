"""Buoi 8 - Hoat dong 4.2: Cap nhat nhan khi bam Button."""
import tkinter as tk


def create_app():
    cua_so = tk.Tk()
    cua_so.title("Dem so lan bam nut")
    cua_so.geometry("360x220")

    trang_thai = {"so_lan": 0}

    def tang_so_lan_bam():
        trang_thai["so_lan"] += 1
        nhan_dem.config(text=f"So lan da bam: {trang_thai['so_lan']}")

    nhan_dem = tk.Label(cua_so, text="So lan da bam: 0", font=("Arial", 14))
    nhan_dem.pack(pady=28)
    nut_bam = tk.Button(cua_so, text="Bam vao day", command=tang_so_lan_bam)
    nut_bam.pack(pady=10)

    cua_so._nut_bam = nut_bam  # De kiem thu tu dong, khong anh huong giao dien.
    return cua_so


if __name__ == "__main__":
    app = create_app()
    app.mainloop()
