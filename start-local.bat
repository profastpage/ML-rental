@echo off
REM ============================================
REM ML RENTAL - Servidor Local
REM ============================================

echo.
echo ============================================
echo   ML RENTAL - Servidor Local
echo ============================================
echo.
echo   Abriendo: http://localhost:8080
echo   Presiona CTRL+C para detener
echo.
echo ============================================
echo.

start http://localhost:8080

npx http-server -p 8080 -c-1 --cors

pause
