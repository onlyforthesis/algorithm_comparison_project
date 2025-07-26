# 演算法比較分析專案 - 技術文檔

## 架構設計

### 目錄結構
```
algorithm_comparison_project/
├── src/                    # 源代碼
│   ├── __init__.py        # 模組初始化
│   ├── main.py            # 完整模組版主程式
│   ├── simplified_main.py # 簡化版主程式（推薦使用）
│   ├── font_manager.py    # 字體管理模組
│   ├── data_manager.py    # 數據管理模組
│   ├── chart_generator.py # 圖表生成模組
│   └── utils.py           # 工具函數
├── config/                # 配置文件
│   ├── chart_config.py    # 圖表配置
│   └── algorithm_data.py  # 演算法數據配置
├── data/                  # 數據文件目錄
│   └── algorithms.csv     # 演算法數據（自動生成）
├── output/                # 輸出文件目錄
├── tests/                 # 測試文件
│   └── test_main.py       # 主要測試
├── docs/                  # 文檔
│   ├── user_guide.md      # 用戶指南
│   └── technical_docs.md  # 技術文檔（本文件）
├── requirements.txt       # 依賴包列表
└── README.md             # 專案說明
```

### 核心模組說明

#### 1. FontManager (字體管理器)
- **職責**: 處理中文字體設定和字體相關功能
- **主要方法**:
  - `setup_chinese_font()`: 自動檢測並設定系統中文字體
  - `get_font()`: 獲取配置好的中文字體
  - `configure_matplotlib()`: 配置 matplotlib 中文顯示

#### 2. DataManager (數據管理器)
- **職責**: 演算法數據的讀取、處理和管理
- **主要方法**:
  - `create_algorithm_dataframe()`: 建立演算法數據表
  - `load_data_from_csv()`: 從 CSV 文件載入數據
  - `save_data_to_csv()`: 保存數據到 CSV 文件
  - `generate_mock_performance_data()`: 生成模擬效能數據

#### 3. ChartGenerator (圖表生成器)
- **職責**: 生成各種類型的比較圖表
- **主要方法**:
  - `create_main_comparison_chart()`: 建立主要演算法比較圖表
  - `create_performance_comparison_chart()`: 建立效能比較圖表
  - `create_summary_table()`: 建立演算法摘要表格

#### 4. Utils (工具模組)
- **職責**: 提供通用的工具函數
- **主要功能**:
  - `timer`: 執行時間裝飾器
  - `ProgressIndicator`: 進度指示器
  - `print_algorithm_reference()`: 打印演算法對照表

### 設計原則

#### 1. 模組化設計
- 每個模組都有明確的職責分工
- 低耦合、高內聚的設計理念
- 易於維護和擴展

#### 2. 配置驅動
- 將可變的配置參數抽取到配置文件
- 支持靈活的客製化需求
- 避免硬編碼

#### 3. 錯誤處理
- 完善的異常處理機制
- 友好的錯誤提示信息
- 優雅的降級處理

## 數據結構

### 演算法數據表結構

| 欄位名稱 | 數據類型 | 說明 |
|----------|----------|------|
| 演算法 | String | 演算法名稱 |
| 預測精度 | String | 精度等級描述 |
| 計算複雜度 | String | 計算複雜度等級 |
| 算力需求 | String | 所需算力等級 |
| 記憶體需求 | String | 記憶體需求等級 |
| 可平行化 | String | 平行化能力描述 |
| 適用場景 | String | 主要應用場景 |

### 複雜度等級映射

```python
COMPLEXITY_MAPPING = {
    '極低': 1,
    '低': 2, 
    '中': 3,
    '中-高': 4,
    '高': 5,
    '極高': 6
}
```

## 圖表技術規格

### 1. 主要比較圖表
- **尺寸**: 20×16 英寸
- **DPI**: 300
- **子圖配置**: 2×2 布局
- **顏色方案**: tab10 調色盤

#### 子圖詳細說明:
1. **散點圖**: 計算複雜度 vs 算力需求關係
2. **柱狀圖**: 記憶體需求比較，含等級標示
3. **雷達圖**: 前5演算法多維度比較
4. **圓餅圖**: 適用場景分布統計

### 2. 效能比較圖表
- **尺寸**: 18×14 英寸
- **顏色方案**: viridis 調色盤
- **數據來源**: 模擬效能數據

#### 子圖詳細說明:
1. **執行時間**: 柱狀圖，含等級標示 (FAST/MID/SLOW)
2. **準確度**: 折線圖，含數值標籤
3. **記憶體使用**: 散點圖
4. **綜合效率**: 水平條形圖，含等級標示

### 3. 摘要表格
- **尺寸**: 16×10 英寸
- **表格樣式**: 交替行顏色
- **標題行**: 綠色背景，白色字體

## 標籤優化技術

### 問題背景
原始版本存在的問題：
- 演算法名稱過長導致標籤重疊
- 中文字體渲染問題
- 特殊符號和 emoji 顯示異常

### 解決方案

#### 1. 純數字標籤系統
```python
def create_smart_labels(algorithm_names, max_length=2):
    """建立純數字標籤映射"""
    return [str(i+1) for i in range(len(algorithm_names))]
```

#### 2. 顏色編碼
- 使用不同顏色區分演算法
- 提供編號對照表供參考
- 保持視覺一致性

#### 3. 等級標示符號
```python
LEVEL_SYMBOLS = {
    'memory': ['LOW', 'MID', 'HIGH', 'MAX', 'SUPER', 'ULTRA'],
    'time': {'fast': 'FAST', 'medium': 'MID', 'slow': 'SLOW'},
    'efficiency': {'high': 'HIGH', 'medium': 'MID', 'low': 'LOW'}
}
```

## 性能優化

### 1. 渲染優化
- 使用適當的圖表尺寸
- 控制數據點數量
- 優化顏色和透明度設定

### 2. 記憶體管理
- 及時釋放不必要的數據
- 使用生成器處理大數據集
- 控制圖表複雜度

### 3. 批量處理
- 支持批量生成圖表
- 進度指示器提供用戶反饋
- 錯誤隔離機制

## 擴展指南

### 添加新的圖表類型

1. 在 `ChartGenerator` 類中添加新方法:
```python
def create_custom_chart(self, df, custom_params):
    """創建自定義圖表"""
    # 實現圖表邏輯
    pass
```

2. 在主程式中調用新方法:
```python
generator.create_custom_chart(df, params)
```

### 添加新的演算法

1. 修改 `config/algorithm_data.py`:
```python
ALGORITHM_DATA.append({
    'name': '新演算法',
    'accuracy': '精度等級',
    # ... 其他屬性
})
```

2. 重新運行程式即可包含新演算法

### 自定義配置

1. 修改 `config/chart_config.py` 中的配置參數
2. 添加新的配置選項
3. 在相應模組中使用新配置

## 測試策略

### 單元測試
- 測試各個模組的核心功能
- 驗證數據處理邏輯
- 確保圖表生成正常

### 集成測試
- 測試模組間的協作
- 驗證完整的工作流程
- 檢查輸出文件品質

### 性能測試
- 測試大數據集處理能力
- 記憶體使用量監控
- 執行時間基準測試

## 部署建議

### 環境要求
- Python 3.8+
- 足夠的系統記憶體（建議 4GB+）
- 支持圖形輸出的環境

### 生產環境部署
- 使用虛擬環境隔離依賴
- 配置適當的字體路徑
- 設定輸出目錄權限

### Docker 部署
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "src/simplified_main.py"]
```

## 維護指南

### 版本管理
- 使用語義化版本號
- 記錄重要變更
- 保持向後兼容性

### 代碼品質
- 遵循 PEP 8 代碼規範
- 添加適當的註釋和文檔
- 定期進行代碼審查

### 依賴管理
- 定期更新依賴包
- 檢查安全漏洞
- 測試新版本兼容性
