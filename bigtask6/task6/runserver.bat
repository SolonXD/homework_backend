@echo off
cd /d "C:\Users\Artyom Ugreninov\PycharmProjects\backend"
call venv\Python\Scripts\activate.bat
python backend/bigtask6/task6/manage.py runserver
pause