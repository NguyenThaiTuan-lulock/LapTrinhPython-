import tkinter as tk
from tkinter import messagebox

danh_sach = [
    {"MaSach": "S001", "TenSach": "Lap trinh Python co ban", "Gia": 95000, "SoLuong": 40},
    {"MaSach": "S002", "TenSach": "Cau truc du lieu va giai thuat", "Gia": 120000, "SoLuong": 6},
    {"MaSach": "S003", "TenSach": "Nhap mon tri tue nhan tao", "Gia": 150000, "SoLuong": 25}
]

def hien_thi(ds):
    listbox.delete(0, tk.END)
    for s in ds:
        dong = f"{s['MaSach']} - {s['TenSach']} - {int(s['Gia'])}d - SL: {s['SoLuong']}"
        listbox.insert(tk.END, dong)

def them_sach():
    ma = entry_ma.get().strip()
    ten = entry_ten.get().strip()
    gia_str = entry_gia.get().strip()
    sl_str = entry_sl.get().strip()

    # Kiểm tra rỗng
    if ma == "" or ten == "":
        messagebox.showerror("Loi", "Ma sach va Ten sach khong duoc de trong!")
        return

    # KIỂM TRA MÃ SÁCH TRÙNG LẶP
    for s in danh_sach:
        if s["MaSach"] == ma:
            messagebox.showerror("Loi", f"Ma sach '{ma}' da ton tai! Vui long nhap ma khac.")
            return

    # Kiểm tra giá trị số
    try:
        gia = float(gia_str)
        soluong = int(sl_str)
        if gia < 0 or soluong < 0:
            messagebox.showerror("Loi", "Gia va So luong phai lon hon hoac bang 0!")
            return
    except ValueError:
        messagebox.showerror("Loi", "Gia hoac So luong khong phai la so hop le!")
        return

    # Thêm sách mới vào danh sách
    sach_moi = {
        "MaSach": ma,
        "TenSach": ten,
        "Gia": gia,
        "SoLuong": soluong
    }
    danh_sach.append(sach_moi)
    hien_thi(danh_sach)

    # Xóa trắng form sau khi thêm thành công
    entry_ma.delete(0, tk.END)
    entry_ten.delete(0, tk.END)
    entry_gia.delete(0, tk.END)
    entry_sl.delete(0, tk.END)

def tim_kiem():
    tu_khoa = entry_tim.get().strip().lower()
    ket_qua = []
    for s in danh_sach:
        if tu_khoa in s["TenSach"].lower():
            ket_qua.append(s)
    hien_thi(ket_qua)


root = tk.Tk()
root.title("Quan ly sach thu vien")
root.geometry("500x400")

tk.Label(root, text="Ma sach:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_ma = tk.Entry(root, width=30)
entry_ma.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Ten sach:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_ten = tk.Entry(root, width=30)
entry_ten.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Gia:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_gia = tk.Entry(root, width=30)
entry_gia.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="So luong:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_sl = tk.Entry(root, width=30)
entry_sl.grid(row=3, column=1, padx=5, pady=5)

btn_them = tk.Button(root, text="Them sach", command=them_sach)
btn_them.grid(row=4, column=1, padx=5, pady=5, sticky="w")

tk.Label(root, text="Tim kiem:").grid(row=5, column=0, padx=5, pady=5, sticky="w")
entry_tim = tk.Entry(root, width=30)
entry_tim.grid(row=5, column=1, padx=5, pady=5)

btn_tim = tk.Button(root, text="Tim kiem", command=tim_kiem)
btn_tim.grid(row=5, column=2, padx=5, pady=5)

listbox = tk.Listbox(root, width=65, height=10)
listbox.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

hien_thi(danh_sach)

root.mainloop()