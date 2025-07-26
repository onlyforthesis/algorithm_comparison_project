@echo off
:: 設置 Python 路徑
set PYTHON_PATH="C:\Users\USER\AppData\Local\Programs\Python\Python310\python.exe"

cd /d "%~dp0"

echo =========================================
echo 演算法比較分析專案啟動器 v2.0
echo =========================================
echo.

echo 選擇運行模式:
echo 1. 診斷測試
echo 2. 運行標準版本
echo 3. 運行增強版本 (如果可用)
echo 4. 簡化演示版本
echo 5. 安裝所需依賴
echo 6. 退出
echo.

set /p choice="請選擇 (1-6): "

if "%choice%"=="1" (
    echo.
    echo 🧪 執行診斷測試...
    %PYTHON_PATH% diagnostic_test.py
    goto end
)

if "%choice%"=="2" (
    echo.
    echo 📊 執行標準版本...
    cd src
    echo 1 | %PYTHON_PATH% main.py
    cd ..
    goto end
)

if "%choice%"=="3" (
    echo.
    echo ✨ 執行增強版本...
    cd src
    echo 2 | %PYTHON_PATH% main.py
    cd ..
    goto end
)

if "%choice%"=="4" (
    echo.
    echo 🎨 執行簡化演示版本...
    %PYTHON_PATH% chart_optimization_demo.py
    goto end
)

if "%choice%"=="5" (
    echo.
    echo 📦 安裝所需依賴...
    %PYTHON_PATH% -m pip install -r requirements.txt
    echo.
    echo 依賴安裝完成！
    goto end
)

if "%choice%"=="6" (
    echo.
    echo 👋 再見！
    goto end
)

echo 無效選擇，請重新運行腳本
goto end

:end
echo.
pause
