@echo off
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
    echo Dang tao moi truong ao .venv, vui long cho...
    python -m venv .venv
)
call ".venv\Scripts\activate.bat"
python -m pip install -q -r requirements.txt
python ung_dung_sinh_vien.py
