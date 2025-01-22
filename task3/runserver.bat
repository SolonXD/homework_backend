@echo off
cd /d "C:\Users\Artyom Ugreninov\PycharmProjects\backend"
call venv\Python\Scripts\activate.bat
python backend/task3/manage.py runserver
pause