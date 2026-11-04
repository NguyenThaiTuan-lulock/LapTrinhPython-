# BUỔI 10 – THỰC HÀNH PYQT5

Bộ bài làm này được triển khai theo các hoạt động trong file PDF Buổi 10 – Thiết kế giao diện với PyQt & Qt Designer.

## 1. Danh sách file

| File | Nội dung |
|---|---|
| `cua_so_dau_tien_pyqt.py` | Bài 1.1: cửa sổ PyQt đầu tiên, `QWidget`, `QLabel`, `QVBoxLayout` |
| `vi_du_grid_layout.py` | Bài 1.2: minh họa `QGridLayout` và `QHBoxLayout` |
| `form_widget_co_ban.py` | Hoạt động 2: `QLabel`, `QLineEdit`, `QComboBox`, `QPushButton` |
| `vi_du_signal_slot.py` | Hoạt động 3: signal-slot; một nút kết nối với hai slot |
| `form_dang_nhap.ui` | Giao diện đăng nhập tạo theo định dạng Qt Designer `.ui` |
| `cua_so_dang_nhap.py` | Hoạt động 5: nạp giao diện `.ui` bằng `uic.loadUi()` |
| `todo_app_pyqt.py` | Hoạt động 6: thêm, xóa và đánh dấu hoàn thành công việc |
| `requirements.txt` | Thư viện cần cài đặt |

## 2. Cài đặt trên Windows

Mở CMD hoặc Terminal tại thư mục chứa các file. Nếu máy đã cài Python, chạy:

```bash
python -m pip install -r requirements.txt
```

Nếu máy dùng lệnh `py` thay cho `python`, chạy:

```bash
py -m pip install -r requirements.txt
```

## 3. Cách chạy từng bài

Chạy một file mỗi lần, ví dụ:

```bash
python cua_so_dau_tien_pyqt.py
python vi_du_grid_layout.py
python form_widget_co_ban.py
python vi_du_signal_slot.py
python cua_so_dang_nhap.py
python todo_app_pyqt.py
```

Có thể thay `python` bằng `py` nếu đó là lệnh Python đang hoạt động trên máy. Với bài đăng nhập, hãy để `form_dang_nhap.ui` cùng thư mục với `cua_so_dang_nhap.py`. File Python đã tự tìm file `.ui` trong chính thư mục này.

## 4. Nếu muốn mở/chỉnh sửa giao diện bằng Qt Designer

Mở Qt Designer, chọn **Open**, sau đó chọn `form_dang_nhap.ui`. Các `objectName` quan trọng phải được giữ đúng để chương trình Python tìm thấy widget:

- Ô tài khoản: `o_nhap_tai_khoan`
- Ô mật khẩu: `o_nhap_mat_khau`
- Nút đăng nhập: `nut_dang_nhap`

Ô mật khẩu đã được đặt `echoMode = Password` để che ký tự. Sau khi lưu thay đổi, chạy lại `cua_so_dang_nhap.py`.

## 5. Trả lời các câu hỏi lý thuyết trong đề

### Bài 1.1 – `app.exec_()` và `mainloop()` của Tkinter

Hai lệnh đều khởi động vòng lặp sự kiện của ứng dụng giao diện. Vòng lặp này nhận và xử lý các thao tác như nhấn nút, nhập văn bản, vẽ lại cửa sổ; ứng dụng tiếp tục hoạt động cho đến khi đóng cửa sổ hoặc thoát chương trình. Tkinter dùng `root.mainloop()`, còn PyQt5 thường dùng `app.exec_()`.

Khác biệt trong cấu trúc: Tkinter thường tạo cửa sổ gốc bằng `tk.Tk()`, còn PyQt5 tạo đối tượng `QApplication` quản lý ứng dụng rồi tạo cửa sổ bằng `QWidget` hoặc lớp con của nó. `QApplication` phải được tạo trước khi hiển thị widget.

### Hoạt động 3 – Signal và slot

- **Signal (tín hiệu):** thông báo một sự kiện vừa xảy ra. Ví dụ `clicked` được phát khi người dùng bấm nút.
- **Slot (hàm xử lý):** hàm được gọi để phản ứng với tín hiệu. Ví dụ `hien_thi_noi_dung()` đọc nội dung `QLineEdit` rồi cập nhật `QLabel`.
- Câu lệnh `nut_hien_thi.clicked.connect(self.hien_thi_noi_dung)` kết nối signal với slot.
- Một signal có thể nối nhiều slot. Trong `vi_du_signal_slot.py`, nút vừa cập nhật nhãn kết quả vừa in thông báo ra cửa sổ console.

Trong Tkinter, ví dụ phổ biến là `Button(command=ten_ham)`. Cách đó gắn hàm xử lý vào tùy chọn `command` của nút; PyQt dùng cơ chế signal-slot tổng quát hơn, có thể kết nối tín hiệu với nhiều hàm hoặc đối tượng xử lý.

### Hoạt động 4 – Nên chọn Tkinter hay PyQt cho ứng dụng bàn giao khách hàng?

Nếu ưu tiên giao diện giàu tính năng, nhiều widget, khả năng tùy biến và hỗ trợ thiết kế giao diện kéo-thả, **PyQt** thường là lựa chọn phù hợp. Qt Designer giúp tạo form trực quan, còn hệ thống widget và layout hỗ trợ bố cục phức tạp.

Tkinter lại nhẹ, thường có sẵn cùng Python, dễ học và hợp với công cụ nhỏ hoặc bài tập cơ bản. Việc chọn thư viện còn phụ thuộc yêu cầu giao diện, thời gian phát triển, môi trường triển khai và giấy phép sử dụng. Với ứng dụng cần giao diện chuyên nghiệp theo đề bài này, có thể chọn PyQt.

### Hoạt động 5 – Qt Designer

Qt Designer tạo giao diện và lưu cấu trúc widget, layout, thuộc tính vào file `.ui`. Trong chương trình này, `uic.loadUi(path, self)` nạp giao diện vào đối tượng cửa sổ. Sau khi nạp, Python truy cập widget qua `objectName`, ví dụ `self.nut_dang_nhap`, rồi kết nối `clicked` với `self.xu_ly_dang_nhap`.

Bản đăng nhập trong bài thực hành chỉ kiểm tra hai ô không được để trống rồi hiển thị thông báo thành công. Đây là minh họa giao diện, chưa kiểm chứng tài khoản/mật khẩu trong cơ sở dữ liệu.

### Hoạt động 6 – To-do list

Ứng dụng sử dụng `QLineEdit` để nhập công việc, `QListWidget` để hiển thị, và `QMessageBox` để báo lỗi. Nút **Thêm** thêm một công việc mới với trạng thái chưa hoàn thành; **Đánh dấu hoàn thành** đổi trạng thái của dòng đang chọn; **Xóa công việc** xóa dòng đang chọn. Nếu chưa nhập nội dung hoặc chưa chọn dòng, chương trình hiện hộp thoại báo lỗi.

## 6. Lưu ý khi nộp bài

Theo phần “Sản phẩm cuối buổi” trong tài liệu, cần chuẩn bị các file code, chụp ảnh màn hình từng chương trình chạy thành công, trả lời câu hỏi, thêm đường dẫn GitHub nếu có, rồi tập hợp vào PDF để nộp. ZIP này cung cấp mã nguồn và phần trả lời; ảnh chụp thực thi và link GitHub cần được bổ sung từ máy/tài khoản của bạn sau khi chạy.
