"""Buoi 8 - Hoat dong 3.3: Dat vi tri widget bang place()."""
import tkinter as tk


def create_app():
    cua_so = tk.Tk()
    cua_so.title("Bo cuc bang place()")
    cua_so.geometry("360x260")

    tk.Label(cua_so, text="Ho ten:", font=("Arial", 11)).place(x=25, y=25)
    tk.Label(cua_so, text="Tuoi:", font=("Arial", 11)).place(x=25, y=70)
    tk.Label(cua_so, text="Email:", font=("Arial", 11)).place(x=25, y=115)
    tk.Button(cua_so, text="Dong y", width=10).place(x=35, y=180)
    tk.Button(cua_so, text="Huy", width=10).place(x=190, y=180)

    return cua_so


if __name__ == "__main__":
    app = create_app()
    app.mainloop()
