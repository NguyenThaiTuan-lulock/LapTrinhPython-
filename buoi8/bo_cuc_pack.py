"""Buoi 8 - Hoat dong 3.1: Sap xep widget bang pack()."""
import tkinter as tk


def create_app():
    cua_so = tk.Tk()
    cua_so.title("Bo cuc bang pack()")
    cua_so.geometry("360x260")

    tk.Label(cua_so, text="Ho ten:", font=("Arial", 11)).pack(pady=5)
    tk.Label(cua_so, text="Tuoi:", font=("Arial", 11)).pack(pady=5)
    tk.Label(cua_so, text="Email:", font=("Arial", 11)).pack(pady=5)

    khung_nut = tk.Frame(cua_so)
    khung_nut.pack(fill="x", pady=15)
    tk.Button(khung_nut, text="Dong y", width=10).pack(side="left", padx=35)
    tk.Button(khung_nut, text="Huy", width=10).pack(side="right", padx=35)

    return cua_so


if __name__ == "__main__":
    app = create_app()
    app.mainloop()
