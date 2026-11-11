BUOI 12 - DO AN TONG HOP: QUAN LY TU SACH CA NHAN

1. CAU TRUC THU MUC
   Buoi12_QuanLyTuSach/
       csdl_sach.py
       ung_dung_tu_sach.py
       requirements.txt
       README.txt
       tu_sach.db  (tu dong tao khi chay lan dau)

2. TAO MOI TRUONG AO (WINDOWS POWERSHELL)
   Mo terminal tai thu muc nay, chay:
       py -3.14 -m venv .venv
       .\.venv\Scripts\Activate.ps1
       python -m pip install --upgrade pip
       python -m pip install -r requirements.txt

   Neu PowerShell chan kich hoat moi truong:
       Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   Sau do chay lai:
       .\.venv\Scripts\Activate.ps1

3. CHAY UNG DUNG
       python ung_dung_tu_sach.py

4. DONG GOI EXE (TUY CHON)
       python -m PyInstaller --onefile --windowed ung_dung_tu_sach.py
   File EXE nam trong thu muc dist. Tep tu_sach.db se duoc tao ben canh file EXE
   khi ung dung duoc chay.

5. CAC CHUC NANG
   - Them sach moi (ten sach, tac gia, the loai).
   - Hien thi toan bo sach.
   - Danh dau sach da doc.
   - Xoa sach.
   - Thong ke so sach theo the loai bang bieu do cot.

Luu y: csdl_sach.py va ung_dung_tu_sach.py phai nam cung thu muc.
Tep tu_sach.db chua du lieu cua ban; khong xoa tep nay neu muon giu lai du lieu.
