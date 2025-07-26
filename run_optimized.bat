@echo off
cd /d "%~dp0"

echo =========================================
echo 圖表優化模式啟動器
echo =========================================
echo.

echo 選擇運行模式:
echo 1. 測試圖表優化功能
echo 2. 運行標準版本
echo 3. 運行增強版本
echo 4. 安裝所需依賴
echo 5. 退出
echo.

set /p choice="請選擇 (1-5): "

if "%choice%"=="1" (
    echo.
    echo 🧪 執行圖表優化測試...
    python test_chart_optimization.py
    goto end
)

if "%choice%"=="2" (
    echo.
    echo 📊 執行標準版本...
    cd src
    echo 1 | python main.py
    cd ..
    goto end
)

if "%choice%"=="3" (
    echo.
    echo ✨ 執行增強版本...
    cd src
    echo 2 | python main.py
    cd ..
    goto end
)

if "%choice%"=="4" (
    echo.
    echo 📦 安裝所需依賴...
    pip install -r requirements.txt
    echo.
    echo 依賴安裝完成！
    goto end
)

if "%choice%"=="5" (
    echo.
    echo 👋 再見！
    goto end
)

echo 無效選擇，請重新運行腳本
goto end

:end
echo.
pause
