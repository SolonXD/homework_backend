@echo off
cd /d "C:\Users\Artyom Ugreninov\PycharmProjects\backend"
call venv\Python\Scripts\activate.bat
python task1/manage.py runserver 192.168.1.81:8000
pause