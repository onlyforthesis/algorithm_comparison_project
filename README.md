# 演算法比較分析專案 v2.0

## 專案簡介

本專案是一個完整的演算法比較分析工具，能夠生成專業的視覺化圖表，比較不同機器學習和深度學習演算法的性能表現。v2.0版本新增了大量圖表優化功能，包括3D效果、動畫、交互式圖表等現代化視覺效果。

## 🎨 新版本特色 (v2.0)

### 標準模式特色
- ✅ **零重疊標籤系統** - 使用數字標籤完全避免文字重疊
- ✅ **多維度比較分析** - 包含計算複雜度、算力需求、記憶體使用、準確度等
- ✅ **多樣化圖表類型** - 散點圖、柱狀圖、雷達圖、圓餅圖、表格
- ✅ **高品質輸出** - 300 DPI 專業品質圖表
- ✅ **系統相容性** - 移除所有特殊字符和 emoji
- ✅ **模組化設計** - 易於維護和擴展

### 🚀 增強模式新特色
- ✨ **3D視覺效果** - 立體散點圖、陰影效果、發光邊框
- 🌈 **現代化配色** - 漸變背景、霓虹色系、賽博朋克風格
- 🎭 **多主題支援** - 專業版、暗色版、賽博朋克主題
- 📊 **豐富圖表類型** - 熱力圖、氣泡圖、時間線圖、3D圓餅圖
- 🎬 **動畫效果** - GIF動畫圖表，動態數據展示
- 🌐 **交互式儀表板** - HTML格式，可縮放、篩選的互動圖表
- 💫 **視覺增強** - 紋理效果、邊框裝飾、漸變填充

## 專案結構

```
algorithm_comparison_project/
├── src/                           # 源代碼
│   ├── __init__.py
│   ├── main.py                   # 主程式入口 (支援雙模式)
│   ├── optimized_main.py         # 圖表優化專用主程式
│   ├── enhanced_chart_generator.py # 增強版圖表生成器
│   ├── data_manager.py           # 數據管理模組
│   ├── chart_generator.py        # 標準圖表生成模組
│   ├── font_manager.py           # 字體管理模組
│   └── utils.py                  # 工具函數
├── config/                       # 配置文件
│   ├── chart_config.py           # 增強版圖表配置
│   └── algorithm_data.py         # 演算法數據配置
├── data/                         # 數據文件
│   └── algorithms.csv            # 演算法數據
├── output/                       # 輸出文件
│   ├── standard/                 # 標準模式輸出
│   ├── professional_theme/       # 專業主題
│   ├── dark_theme/              # 暗色主題
│   └── cyberpunk_theme/         # 賽博朋克主題
├── tests/                        # 測試文件
├── docs/                         # 文檔
├── requirements.txt              # 依賴包
├── test_chart_optimization.py   # 功能測試腳本
├── run_optimized.bat            # 圖表優化啟動器
└── README.md                    # 專案說明
```

## 🚀 快速開始

### 方法一: 使用批次腳本 (推薦)

```bash
# Windows用戶
run_optimized.bat

# 選擇功能:
# 1. 測試圖表優化功能
# 2. 運行標準版本  
# 3. 運行增強版本
# 4. 安裝所需依賴
```

### 方法二: 手動安裝與運行

#### 1. 安裝依賴

```bash
pip install -r requirements.txt
```

#### 2. 測試功能 (可選)

```bash
python test_chart_optimization.py
```

#### 3. 運行程式

**標準模式:**
```bash
python src/main.py
# 選擇 1 (標準模式)
```

**增強模式:**
```bash
python src/main.py  
# 選擇 2 (增強模式)
```

**純增強模式:**
```bash
python src/optimized_main.py
```
```

### 3. 自定義配置

修改 `config/` 目錄下的配置文件來自定義圖表樣式和數據。

## 輸出文件

程式運行後會在 `output/` 目錄生成以下文件：

- `ultra_clean_algorithm_comparison.png` - 主要演算法比較圖表
- `ultra_clean_comparison_table.png` - 效能比較圖表
- `algorithm_summary_table.png` - 演算法摘要表格

## 演算法編號對照

1. ARIMA - 時間序列預測
2. 指數平滑法 - 短期預測
3. GARCH - 波動預測
4. SVM - 支持向量機
5. 隨機森林 - 集成學習
6. XGBoost - 梯度提升
7. RNN/LSTM - 循環神經網絡
8. CNN - 卷積神經網絡
9. Transformer - 注意力機制
10. 基因演算法 - 進化計算

## 技術規格

- Python 3.8+
- matplotlib 3.8+
- numpy 1.24+
- pandas 2.0+

## 授權

MIT License

## 作者

演算法比較分析專案團隊
