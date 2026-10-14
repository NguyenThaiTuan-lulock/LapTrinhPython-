"""Buoi 8 - Hoat dong 5: Form nhap thong tin bang grid(), co nut Xoa."""
import tkinter as tk


def create_app():
    cua_so = tk.Tk()
    cua_so.title("Form nhap thong tin")
    cua_so.geometry("460x330")
    cua_so.resizable(False, False)

    tk.Label(cua_so, text="FORM NHAP THONG TIN", font=("Arial", 14, "bold")).grid(
        row=0, column=0, columnspan=2, pady=(15, 8)
    )

    tk.Label(cua_so, text="Ho ten:", font=("Arial", 10)).grid(
        row=1, column=0, padx=18, pady=9, sticky="w"
    )
    entry_ho_ten = tk.Entry(cua_so, width=30)
    entry_ho_ten.grid(row=1, column=1, padx=12, pady=9)

    tk.Label(cua_so, text="Tuoi:", font=("Arial", 10)).grid(
        row=2, column=0, padx=18, pady=9, sticky="w"
    )
    entry_tuoi = tk.Entry(cua_so, width=30)
    entry_tuoi.grid(row=2, column=1, padx=12, pady=9)

    tk.Label(cua_so, text="Email:", font=("Arial", 10)).grid(
        row=3, column=0, padx=18, pady=9, sticky="w"
    )
    entry_email = tk.Entry(cua_so, width=30)
    entry_email.grid(row=3, column=1, padx=12, pady=9)

    def xu_ly_submit():
        ho_ten = entry_ho_ten.get().strip()
        tuoi = entry_tuoi.get().strip()
        email = entry_email.get().strip()
        nhan_ket_qua.config(text=f"Da nhan: {ho_ten} - {tuoi} tuoi - {email}")

    def xoa_thong_tin():
        entry_ho_ten.delete(0, tk.END)
        entry_tuoi.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        nhan_ket_qua.config(text="Da xoa noi dung cac o nhap.")
        entry_ho_ten.focus_set()

    nut_submit = tk.Button(cua_so, text="Submit", width=12, command=xu_ly_submit)
    nut_submit.grid(row=4, column=0, padx=12, pady=13, sticky="e")
    nut_xoa = tk.Button(cua_so, text="Xoa", width=12, command=xoa_thong_tin)
    nut_xoa.grid(row=4, column=1, padx=12, pady=13, sticky="w")

    nhan_ket_qua = tk.Label(cua_so, text="", font=("Arial", 10), fg="blue", wraplength=420)
    nhan_ket_qua.grid(row=5, column=0, columnspan=2, pady=9)

    # Thuoc tinh nay chi giup kiem thu tu dong va khong hien thi them widget.
    cua_so._entry_ho_ten = entry_ho_ten
    cua_so._entry_tuoi = entry_tuoi
    cua_so._entry_email = entry_email
    cua_so._nut_submit = nut_submit
    cua_so._nut_xoa = nut_xoa
    cua_so._nhan_ket_qua = nhan_ket_qua
    return cua_so


if __name__ == "__main__":
    app = create_app()
    app.mainloop()
