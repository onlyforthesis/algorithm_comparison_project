# 演算法比較分析專案 - 用戶指南

## 目錄
1. [專案簡介](#專案簡介)
2. [快速開始](#快速開始)
3. [詳細功能](#詳細功能)
4. [自定義配置](#自定義配置)
5. [故障排除](#故障排除)

## 專案簡介

本專案是一個專業的演算法比較分析工具，能夠生成高品質的視覺化圖表，幫助用戶比較不同機器學習和深度學習演算法的性能表現。

### 主要功能

- **多維度比較**: 計算複雜度、算力需求、記憶體使用、準確度等
- **多種圖表類型**: 散點圖、柱狀圖、雷達圖、圓餅圖、摘要表格
- **零重疊標籤**: 使用數字標籤系統完全避免文字重疊
- **專業輸出**: 300 DPI 高品質圖表
- **模組化設計**: 易於維護和擴展

## 快速開始

### 1. 環境準備

確保您的系統已安裝 Python 3.8 或更高版本：

```bash
python --version
```

### 2. 安裝依賴

```bash
pip install -r requirements.txt
```

### 3. 運行程式

**簡化版本（推薦）:**
```bash
cd src
python simplified_main.py
```

**完整模組版本:**
```bash
cd src
python main.py
```

### 4. 查看結果

程式運行完成後，會在 `output/` 目錄生成三個圖表文件：

- `ultra_clean_algorithm_comparison.png` - 主要演算法比較圖表
- `ultra_clean_comparison_table.png` - 效能比較圖表  
- `algorithm_summary_table.png` - 演算法摘要表格

## 詳細功能

### 圖表類型說明

#### 1. 主要演算法比較圖表
- **散點圖**: 顯示計算複雜度與算力需求的關係
- **柱狀圖**: 記憶體需求比較，內嵌等級標示
- **雷達圖**: 前5個演算法的多維度比較
- **圓餅圖**: 適用場景分布統計

#### 2. 效能比較圖表
- **執行時間**: 各演算法的執行時間比較
- **準確度**: 準確度折線圖，含數值標籤
- **記憶體使用**: 散點圖顯示記憶體消耗
- **綜合效率**: 水平條形圖顯示綜合評分

#### 3. 摘要表格
- 完整的演算法資訊表格化呈現
- 包含所有重要屬性和特徵

### 演算法編號對照

| 編號 | 演算法 | 主要用途 |
|------|--------|----------|
| 1 | ARIMA | 時間序列預測 |
| 2 | 指數平滑法 | 短期預測 |
| 3 | GARCH | 波動預測 |
| 4 | SVM | 分類問題 |
| 5 | 隨機森林 | 特徵重要性分析 |
| 6 | XGBoost | 高精度預測 |
| 7 | RNN/LSTM | 序列建模 |
| 8 | CNN | 圖像特徵提取 |
| 9 | Transformer | 多模態處理 |
| 10 | 基因演算法 | 優化問題 |

## 自定義配置

### 修改演算法數據

編輯 `config/algorithm_data.py` 文件來自定義演算法數據：

```python
ALGORITHM_DATA = [
    {
        'name': '您的演算法名稱',
        'accuracy': '精度等級',
        'complexity': '複雜度等級',
        # ... 其他屬性
    }
]
```

### 調整圖表樣式

修改 `config/chart_config.py` 中的配置：

```python
# 調整圖表尺寸
FIGURE_SIZES = {
    'main_comparison': (20, 16),  # 寬度, 高度
    'performance': (18, 14),
    'summary_table': (16, 10)
}

# 調整字體大小
FONT_SIZES = {
    'title': 20,
    'subtitle': 16,
    'axis_label': 14,
    # ...
}
```

### 更改輸出路徑

在程式中指定不同的輸出目錄：

```python
generator = AlgorithmComparisonGenerator("my_output_folder")
```

## 故障排除

### 常見問題

#### 1. 中文字體顯示問題

**問題**: 圖表中的中文顯示為方框或亂碼

**解決方案**:
- 確保系統已安裝中文字體
- Windows 用戶通常不會有此問題
- Linux/Mac 用戶可能需要安裝額外的中文字體

#### 2. 模組導入錯誤

**問題**: `ModuleNotFoundError` 或導入錯誤

**解決方案**:
- 使用簡化版本: `python simplified_main.py`
- 檢查 Python 路徑設定
- 確保所有依賴已正確安裝

#### 3. 圖表不顯示

**問題**: 程式運行完成但圖表窗口不顯示

**解決方案**:
- 檢查是否在無GUI環境中運行
- 註釋掉 `plt.show()` 行，只保存圖片
- 使用 `matplotlib` 的非互動式後端

#### 4. 記憶體不足

**問題**: 生成大型圖表時記憶體不足

**解決方案**:
- 減少圖表尺寸設定
- 降低 DPI 設定（從300改為150）
- 分批生成圖表

### 獲取幫助

如果遇到其他問題：

1. 檢查錯誤訊息和堆疊追蹤
2. 確認 Python 和依賴版本
3. 查看專案的 GitHub Issues
4. 聯繫專案維護者

## 進階使用

### 批量處理

可以修改程式來批量處理多個數據集：

```python
for dataset in datasets:
    df = load_custom_data(dataset)
    generator.create_main_comparison_chart(df)
```

### 自定義分析

添加新的分析維度：

```python
def create_custom_analysis(self, df, new_metric):
    # 自定義分析邏輯
    pass
```

### 輸出格式

支持多種輸出格式：

```python
plt.savefig('chart.png', dpi=300)  # PNG
plt.savefig('chart.pdf')           # PDF  
plt.savefig('chart.svg')           # SVG
```
