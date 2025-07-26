# -*- coding: utf-8 -*-
"""
演算法數據配置
定義演算法的基本數據和屬性
"""

# 演算法基本資料
ALGORITHM_DATA = [
    {
        'name': 'ARIMA',
        'accuracy': '中',
        'complexity': '低',
        'compute_power': '低',
        'memory': '低',
        'parallelizable': '限制',
        'scenario': '趨勢預測'
    },
    {
        'name': '指數平滑法',
        'accuracy': '低-中',
        'complexity': '極低',
        'compute_power': '極低',
        'memory': '極低',
        'parallelizable': '限制',
        'scenario': '短期預測'
    },
    {
        'name': 'GARCH',
        'accuracy': '中(波動)',
        'complexity': '中',
        'compute_power': '中',
        'memory': '低',
        'parallelizable': '限制',
        'scenario': '波動預測'
    },
    {
        'name': 'SVM',
        'accuracy': '中-高',
        'complexity': '中',
        'compute_power': '中-高',
        'memory': '中',
        'parallelizable': '部分',
        'scenario': '分類問題'
    },
    {
        'name': '隨機森林',
        'accuracy': '高',
        'complexity': '高',
        'compute_power': '高',
        'memory': '中-高',
        'parallelizable': '高',
        'scenario': '特徵重要'
    },
    {
        'name': 'XGBoost',
        'accuracy': '高',
        'complexity': '高',
        'compute_power': '極高',
        'memory': '高',
        'parallelizable': '高',
        'scenario': '高精度'
    },
    {
        'name': 'RNN/LSTM',
        'accuracy': '高',
        'complexity': '極高',
        'compute_power': '極高',
        'memory': '極高',
        'parallelizable': '極高(GPU)',
        'scenario': '序列建模'
    },
    {
        'name': 'CNN',
        'accuracy': '中-高',
        'complexity': '高',
        'compute_power': '極高',
        'memory': '高',
        'parallelizable': '極高(GPU)',
        'scenario': '圖像特徵'
    },
    {
        'name': 'Transformer',
        'accuracy': '高',
        'complexity': '極高',
        'compute_power': '極高',
        'memory': '極高',
        'parallelizable': '極高(GPU)',
        'scenario': '多模態'
    },
    {
        'name': '基因演算法',
        'accuracy': '中-高',
        'complexity': '高',
        'compute_power': '中-高',
        'memory': '中',
        'parallelizable': '高',
        'scenario': '優化問題'
    }
]

# 複雜度映射
COMPLEXITY_MAPPING = {
    '極低': 1, '低': 2, '中': 3, 
    '中-高': 4, '高': 5, '極高': 6
}

# 等級標示符號
LEVEL_SYMBOLS = {
    'memory': ['LOW', 'MID', 'HIGH', 'MAX', 'SUPER', 'ULTRA'],
    'time': {'fast': 'FAST', 'medium': 'MID', 'slow': 'SLOW'},
    'efficiency': {'high': 'HIGH', 'medium': 'MID', 'low': 'LOW'}
}

# 複雜度標籤
COMPLEXITY_LABELS = ['', '極低', '低', '中', '中-高', '高', '極高']
