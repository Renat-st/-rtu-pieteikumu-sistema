@echo off
title RTU Pieteikumu sistema
color 0A
echo ========================================
echo    RTU Bakalaura pieteikumu sistema
echo ========================================
echo.

echo [1/3] Migracijas...
python manage.py migrate

echo.
echo [2/3] Palaidz serveri...
echo.
echo ════════════════════════════════════════════════
echo  http://127.0.0.1:8000/ - Pieteikumi
echo  http://127.0.0.1:8000/admin/ 
echo  Admin: admin / 12345678 
echo ════════════════════════════════════════════════
echo.
echo Palaid un atver browser!
pause
python manage.py runserver 0.0.0.0:8000
