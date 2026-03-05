@echo off
echo [1] Python versija:
python --version
echo.

echo [2] Django check:
python manage.py check
echo.

echo [3] Migracijas:
python manage.py migrate
echo.

echo [4] Serveris palaidis:
python manage.py runserver 0.0.0.0:8000
pause
