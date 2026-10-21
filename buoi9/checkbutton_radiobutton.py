import tkinter as tk

# HOẠT ĐỘNG 1: CHECKBUTTON 
def hien_thi_cua_so_checkbutton():
    cua_so_cb = tk.Toplevel()
    cua_so_cb.title("Vi du Checkbutton")
    cua_so_cb.geometry("300x220")
    tk.Label(cua_so_cb, text="Chon so thich cua ban:", font=("Arial", 12)).pack(pady=10)
    
    bien_doc_sach = tk.BooleanVar()
    bien_the_thao = tk.BooleanVar()
    bien_am_nhac = tk.BooleanVar()
    
    tk.Checkbutton(cua_so_cb, text="Doc sach", variable=bien_doc_sach).pack(anchor="w", padx=30)
    tk.Checkbutton(cua_so_cb, text="The thao", variable=bien_the_thao).pack(anchor="w", padx=30)
    tk.Checkbutton(cua_so_cb, text="Am nhac", variable=bien_am_nhac).pack(anchor="w", padx=30)
    
    def xem_lua_chon():
        print("Doc sach:", bien_doc_sach.get())
        print("The thao:", bien_the_thao.get())
        print("Am nhac:", bien_am_nhac.get())
        
    tk.Button(cua_so_cb, text="Xem lua chon (in ra console)", command=xem_lua_chon).pack(pady=15)

# HOẠT ĐỘNG 2: RADIOBUTTON 
def hien_thi_cua_so_radiobutton():
    cua_so_rb = tk.Toplevel()
    cua_so_rb.title("Vi du Radiobutton")
    cua_so_rb.geometry("300x200")
    bien_loai_tai_khoan = tk.StringVar(value="ca_nhan")
    
    tk.Label(cua_so_rb, text="Chon loai tai khoan:", font=("Arial", 12)).pack(pady=10)
    tk.Radiobutton(cua_so_rb, text="Ca nhan", variable=bien_loai_tai_khoan, value="ca_nhan").pack(anchor="w", padx=30)
    tk.Radiobutton(cua_so_rb, text="Doanh nghiep", variable=bien_loai_tai_khoan, value="doanh_nghiep").pack(anchor="w", padx=30)
    
    def xem_loai_tai_khoan():
        nhan_ket_qua.config(text=f"Ban da chon: {bien_loai_tai_khoan.get()}")
        
    tk.Button(cua_so_rb, text="Xac nhan", command=xem_loai_tai_khoan).pack(pady=10)
    nhan_ket_qua = tk.Label(cua_so_rb, text="")
    nhan_ket_qua.pack()

cua_so_chinh = tk.Tk()
cua_so_chinh.title("Bai tap HĐ 1 & 2")
cua_so_chinh.geometry("300x150")
tk.Button(cua_so_chinh, text="Mở bài Checkbutton", command=hien_thi_cua_so_checkbutton).pack(pady=15)
tk.Button(cua_so_chinh, text="Mở bài Radiobutton", command=hien_thi_cua_so_radiobutton).pack(pady=15)

cua_so_chinh.mainloop()