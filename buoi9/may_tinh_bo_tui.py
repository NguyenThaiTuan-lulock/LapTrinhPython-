import tkinter as tk
from tkinter import messagebox

def click_button(item):
    global bieu_thuc
    bieu_thuc = bieu_thuc + str(item)
    bien_dau_vao.set(bieu_thuc)

def clear_button():
    global bieu_thuc
    bieu_thuc = ""
    bien_dau_vao.set("")

def tinh_toan():
    global bieu_thuc
    try:
        
        ket_qua = str(eval(bieu_thuc))
        bien_dau_vao.set(ket_qua)
        bieu_thuc = ket_qua
    except ZeroDivisionError:
        messagebox.showerror("Lỗi", "Không thể chia cho 0")
        bieu_thuc = ""
        bien_dau_vao.set("")
    except Exception as e:
        messagebox.showerror("Lỗi", "Biểu thức không hợp lệ")
        bieu_thuc = ""
        bien_dau_vao.set("")

cua_so = tk.Tk()
cua_so.title("Máy tính bỏ túi")
cua_so.geometry("320x420")
cua_so.resizable(False, False)

bieu_thuc = ""
bien_dau_vao = tk.StringVar()

# Khung hiển thị
khung_hien_thi = tk.Frame(cua_so, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
khung_hien_thi.pack(side=tk.TOP)

truong_hien_thi = tk.Entry(khung_hien_thi, font=('arial', 18, 'bold'), textvariable=bien_dau_vao, width=24, bg="#eee", bd=0, justify=tk.RIGHT)
truong_hien_thi.grid(row=0, column=0)
truong_hien_thi.pack(ipady=10)

# Khung bàn phím
khung_phim = tk.Frame(cua_so, width=312, height=272, bg="grey")
khung_phim.pack()

# Hàng 1
tk.Button(khung_phim, text="C", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=clear_button).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
tk.Button(khung_phim, text="/", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: click_button("/")).grid(row=0, column=3, padx=1, pady=1)

# Hàng 2
tk.Button(khung_phim, text="7", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click_button("7")).grid(row=1, column=0, padx=1, pady=1)
tk.Button(khung_phim, text="8", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click_button("8")).grid(row=1, column=1, padx=1, pady=1)
tk.Button(khung_phim, text="9", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click_button("9")).grid(row=1, column=2, padx=1, pady=1)
tk.Button(khung_phim, text="*", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: click_button("*")).grid(row=1, column=3, padx=1, pady=1)

# Hàng 3
tk.Button(khung_phim, text="4", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click_button("4")).grid(row=2, column=0, padx=1, pady=1)
tk.Button(khung_phim, text="5", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click_button("5")).grid(row=2, column=1, padx=1, pady=1)
tk.Button(khung_phim, text="6", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click_button("6")).grid(row=2, column=2, padx=1, pady=1)
tk.Button(khung_phim, text="-", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: click_button("-")).grid(row=2, column=3, padx=1, pady=1)

# Hàng 4
tk.Button(khung_phim, text="1", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click_button("1")).grid(row=3, column=0, padx=1, pady=1)
tk.Button(khung_phim, text="2", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click_button("2")).grid(row=3, column=1, padx=1, pady=1)
tk.Button(khung_phim, text="3", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click_button("3")).grid(row=3, column=2, padx=1, pady=1)
tk.Button(khung_phim, text="+", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: click_button("+")).grid(row=3, column=3, padx=1, pady=1)

# Hàng 5
tk.Button(khung_phim, text="0", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click_button("0")).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
tk.Button(khung_phim, text=".", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: click_button(".")).grid(row=4, column=2, padx=1, pady=1)
tk.Button(khung_phim, text="=", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=tinh_toan).grid(row=4, column=3, padx=1, pady=1)

if __name__ == "__main__":
    cua_so.mainloop()