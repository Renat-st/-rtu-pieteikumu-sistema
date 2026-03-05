@echo off
title RTU Pieteikumu sistēma
color 0A
echo ========================================
echo    RTU Bakalaura pieteikumu sistēma
echo ========================================
echo.

REM Миграции
echo [1/3] Migrācijas...
python manage.py migrate

REM Сервер
echo.
echo [2/3] Palaidz serveri...
echo.
echo ════════════════════════════════════════════════
echo  🌐 http://127.0.0.1:8000/ - Pieteikumi
echo  👨‍💼 http://127.0.0.1:8000/admin/ 
echo  📧 Admin: admin / admin123 (ja nav - izveido)
echo ════════════════════════════════════════════════
echo.
echo Palaid un atver browser!
pause
python manage.py runserver 0.0.0.0:8000
