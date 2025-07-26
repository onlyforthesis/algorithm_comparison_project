#!/bin/bash

echo "========================================"
echo "演算法比較分析專案 v1.0.0"
echo "========================================"
echo

echo "檢查 Python 環境..."
if ! command -v python3 &> /dev/null; then
    echo "錯誤: 未找到 Python3，請先安裝 Python 3.8+"
    exit 1
fi

python3 --version

echo "檢查依賴套件..."
if ! python3 -c "import matplotlib" 2>/dev/null; then
    echo "安裝依賴套件..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "錯誤: 依賴套件安裝失敗"
        exit 1
    fi
fi

echo "建立輸出目錄..."
mkdir -p output
mkdir -p data

echo
echo "========================================"
echo "開始執行演算法比較分析..."
echo "========================================"
echo

cd src
python3 simplified_main.py

echo
echo "========================================"
echo "執行完成！"
echo "========================================"
echo
echo "生成的圖表文件位於 output 目錄中："
echo "- ultra_clean_algorithm_comparison.png"
echo "- ultra_clean_comparison_table.png"  
echo "- algorithm_summary_table.png"
echo

read -p "按任意鍵繼續..." -n1 -s
