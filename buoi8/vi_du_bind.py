"""Buoi 8 - Hoat dong 4.3: Bat su kien ban phim va chuot bang bind()."""
import tkinter as tk


def create_app():
    cua_so = tk.Tk()
    cua_so.title("Vi du bind()")
    cua_so.geometry("440x250")

    def khi_go_phim(event):
        ky_tu = event.char if event.char else event.keysym
        nhan_thong_bao.config(text=f"Ban vua nhan phim: {ky_tu}")

    def khi_click_chuot(event):
        nhan_thong_bao.config(text=f"Ban vua click tai toa do: ({event.x}, {event.y})")

    nhan_thong_bao = tk.Label(
        cua_so, text="Hay go phim hoac click chuot", font=("Arial", 12)
    )
    nhan_thong_bao.pack(pady=35)
    huong_dan = tk.Label(cua_so, text="Click vao cua so, sau do go phim de thu.")
    huong_dan.pack(pady=5)

    cua_so.bind("<Key>", khi_go_phim)
    cua_so.bind("<Button-1>", khi_click_chuot)
    cua_so._nhan_thong_bao = nhan_thong_bao
    return cua_so


if __name__ == "__main__":
    app = create_app()
    app.mainloop()
