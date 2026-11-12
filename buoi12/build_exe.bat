@echo off
cd /d "%~dp0"
echo === Dong goi ung dung Quan ly Sinh vien bang PyInstaller ===
if not exist ".venv\Scripts\python.exe" (
    echo [1/3] Tao moi truong ao .venv
    python -m venv .venv
)
call ".venv\Scripts\activate.bat"
echo [2/3] Cai thu vien tu requirements.txt
python -m pip install -r requirements.txt
echo [3/3] Chay PyInstaller
pyinstaller --noconfirm ung_dung_sinh_vien.spec
if exist sinh_vien.db copy /Y sinh_vien.db dist\sinh_vien.db >nul
echo.
echo Xong! File thuc thi nam o: dist\ung_dung_sinh_vien.exe
pause
