@echo off
REM ============================================
REM ML RENTAL - Git Push Rápido
REM ============================================

echo.
echo ============================================
echo   ML RENTAL - Git Push
echo ============================================
echo.

if "%~1"=="" (
    set /p commitmsg="Ingresa el mensaje del commit: "
) else (
    set commitmsg=%*
)

echo.
echo   Mensaje: %commitmsg%
echo.

git add .
git commit -m "%commitmsg%"
git push

echo.
echo ============================================
echo   Push completado exitosamente!
echo ============================================
echo.

pause
