"""Buoi 8 - Hoat dong 1 va 2: Cua so Tkinter, Label va Frame."""
import tkinter as tk


def create_app():
    cua_so = tk.Tk()
    cua_so.title("Ung dung demo - Cua so va Frame")
    cua_so.geometry("460x300")
    cua_so.resizable(False, False)  # Doi thanh True, False de thu cho phep keo rong.

    khung_tren = tk.Frame(cua_so, bg="lightblue", height=90)
    khung_tren.pack(fill="x")
    khung_tren.pack_propagate(False)  # Giu chieu cao 90 px cho Frame.

    tk.Label(
        khung_tren,
        text="Xin chao Tkinter!",
        bg="lightblue",
        font=("Arial", 16, "bold"),
    ).pack(pady=24)

    khung_duoi = tk.Frame(cua_so, bg="lightyellow")
    khung_duoi.pack(fill="both", expand=True)

    tk.Label(
        khung_duoi,
        text="Khu vuc noi dung",
        bg="lightyellow",
        font=("Arial", 12),
    ).pack(pady=18)
    tk.Label(
        khung_duoi,
        text="Vi du gom cua so chinh va hai Frame rieng.",
        bg="lightyellow",
        font=("Arial", 10),
    ).pack(pady=4)

    return cua_so


if __name__ == "__main__":
    app = create_app()
    app.mainloop()
