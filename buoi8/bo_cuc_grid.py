"""Buoi 8 - Hoat dong 3.2: Sap xep widget bang grid()."""
import tkinter as tk


def create_app():
    cua_so = tk.Tk()
    cua_so.title("Bo cuc bang grid()")
    cua_so.geometry("360x260")

    tk.Label(cua_so, text="Ho ten:", font=("Arial", 11)).grid(
        row=0, column=0, padx=18, pady=10, sticky="w"
    )
    tk.Label(cua_so, text="Tuoi:", font=("Arial", 11)).grid(
        row=1, column=0, padx=18, pady=10, sticky="w"
    )
    tk.Label(cua_so, text="Email:", font=("Arial", 11)).grid(
        row=2, column=0, padx=18, pady=10, sticky="w"
    )
    tk.Button(cua_so, text="Dong y", width=10).grid(
        row=3, column=0, padx=18, pady=15
    )
    tk.Button(cua_so, text="Huy", width=10).grid(
        row=3, column=1, padx=18, pady=15
    )

    return cua_so


if __name__ == "__main__":
    app = create_app()
    app.mainloop()
