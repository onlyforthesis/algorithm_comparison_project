@echo off
echo ========================================
echo 演算法比較分析專案 v1.0.0
echo ========================================
echo.

echo 檢查 Python 環境...
python --version >nul 2>&1
if errorlevel 1 (
    echo 錯誤: 未找到 Python，請先安裝 Python 3.8+
    pause
    exit /b 1
)

echo 檢查依賴套件...
pip show matplotlib >nul 2>&1
if errorlevel 1 (
    echo 安裝依賴套件...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo 錯誤: 依賴套件安裝失敗
        pause
        exit /b 1
    )
)

echo 建立輸出目錄...
if not exist "output" mkdir output
if not exist "data" mkdir data

echo.
echo ========================================
echo 開始執行演算法比較分析...
echo ========================================
echo.

cd src
python simplified_main.py

echo.
echo ========================================
echo 執行完成！
echo ========================================
echo.
echo 生成的圖表文件位於 output 目錄中：
echo - ultra_clean_algorithm_comparison.png
echo - ultra_clean_comparison_table.png  
echo - algorithm_summary_table.png
echo.
pause
