# Ứng dụng Quản lý Sinh viên (Tkinter + SQLite + Matplotlib)

Đồ án tổng hợp cuối khóa – Buổi 12. Ứng dụng desktop quản lý danh sách sinh viên có giao diện đồ họa,
lưu dữ liệu bằng SQLite và thống kê bằng biểu đồ cột.

## Chức năng

| # | Chức năng | Hàm trong `csdl_sinh_vien.py` | Thành phần giao diện |
|---|-----------|-------------------------------|----------------------|
| 1 | Thêm sinh viên (mã SV, họ tên, lớp, điểm TB) | `them_sinh_vien` | Ô nhập + Combobox + nút **Thêm sinh viên** |
| 2 | Hiển thị toàn bộ danh sách | `lay_toan_bo_sinh_vien` | Bảng `Treeview` + thanh cuộn |
| 3 | Đánh dấu **đã đóng học phí** | `danh_dau_da_dong_hoc_phi` | Nút **Đánh dấu đã đóng học phí** (dòng tô xanh) |
| 4 | Xóa sinh viên (có hỏi xác nhận) | `xoa_sinh_vien` | Nút **Xóa sinh viên** |
| 5 | Thống kê theo lớp bằng biểu đồ cột | `thong_ke_theo_lop` | Nút **Thống kê theo lớp** (2 biểu đồ: số lượng + điểm TB) |
| 6 | *Mở rộng:* Sửa thông tin sinh viên | `cap_nhat_sinh_vien` | Click vào dòng → form tự điền → **Cập nhật** |
| 7 | *Mở rộng:* Tìm kiếm theo mã SV / họ tên / lớp | `tim_kiem_sinh_vien` | Ô tìm kiếm + **Tìm** / **Hiện tất cả** |

**Xử lý lỗi nhập liệu:** để trống mã/họ tên, điểm không phải số, điểm ngoài khoảng 0–10, trùng mã sinh viên,
chưa chọn dòng khi xóa/sửa/đánh dấu, thống kê khi chưa có dữ liệu.

## Cấu trúc thư mục

```
QuanLySinhVien/
├── csdl_sinh_vien.py          # Module dữ liệu SQLite (không biết gì về giao diện)
├── ung_dung_sinh_vien.py      # Giao diện Tkinter, gọi lại các hàm của csdl_sinh_vien.py
├── sinh_vien.db               # CSDL SQLite có sẵn 14 sinh viên mẫu
├── test_csdl.py               # Kiểm thử module dữ liệu độc lập
├── test_giao_dien.py          # Kiểm thử giao diện (mô phỏng thao tác người dùng)
├── ung_dung_sinh_vien.spec    # Cấu hình PyInstaller
├── requirements.txt           # Thư viện cần cài
├── chay_ung_dung.bat          # Chạy nhanh trên Windows (tự tạo .venv)
├── build_exe.bat              # Đóng gói ra file .exe trên Windows
├── .gitignore
└── README.md
```

Các thư mục `.venv/`, `build/`, `dist/`, `__pycache__/` được **sinh ra tự động** khi chạy/đóng gói nên không nằm sẵn trong gói.

## Thiết kế bảng `sinh_vien`

| Cột | Kiểu | Ghi chú |
|-----|------|---------|
| `id` | INTEGER PRIMARY KEY AUTOINCREMENT | Tự tăng |
| `ma_sv` | TEXT NOT NULL **UNIQUE** | Mã sinh viên, không được trùng |
| `ho_ten` | TEXT NOT NULL | Bắt buộc |
| `lop` | TEXT NOT NULL | Chọn từ Combobox |
| `diem_tb` | REAL NOT NULL DEFAULT 0 | Điểm trung bình 0–10 |
| `da_dong_hoc_phi` | INTEGER NOT NULL DEFAULT 0 | 0 = chưa đóng, 1 = đã đóng |

## Cách chạy

Yêu cầu: **Python 3.9+** (tải tại python.org, nhớ tick *Add Python to PATH*). `tkinter` và `sqlite3` có sẵn.

**Cách 1 – Nhanh nhất (Windows):** nhấp đúp `chay_ung_dung.bat`.

**Cách 2 – Dùng terminal / VS Code:**

```bash
python -m venv .venv
.venv\Scripts\activate          # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python ung_dung_sinh_vien.py
```

## Kiểm thử

```bash
python test_csdl.py          # kiểm thử module dữ liệu
python test_giao_dien.py     # kiểm thử giao diện (cửa sổ mở/đóng nhanh trong lúc test)
```

Cả hai script dùng file DB tạm riêng, **không** làm thay đổi `sinh_vien.db`.

## Đóng gói thành file .exe (Hoạt động 6)

Nhấp đúp `build_exe.bat`, hoặc chạy thủ công:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed ung_dung_sinh_vien.py
```

Kết quả: `dist/ung_dung_sinh_vien.exe`. File `sinh_vien.db` được tạo/đọc **cạnh file `.exe`**
(`build_exe.bat` tự sao chép DB mẫu vào `dist/`). File `.exe` chỉ chạy trên hệ điều hành đã build ra nó
(build trên Windows → chạy trên Windows).

## Công nghệ

Python · Tkinter / ttk · SQLite (`sqlite3`) · Matplotlib (nhúng vào Tkinter bằng `FigureCanvasTkAgg`) · PyInstaller
