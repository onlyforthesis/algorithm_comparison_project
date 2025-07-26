# -*- coding: utf-8 -*-
"""
工具函數模組
提供通用的工具函數
"""

import time
from functools import wraps
from pathlib import Path


def timer(func):
    """執行時間裝飾器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 執行時間: {end_time - start_time:.2f} 秒")
        return result
    return wrapper


def ensure_directory(directory_path):
    """確保目錄存在"""
    path = Path(directory_path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def log_operation(message, level="INFO"):
    """記錄操作日誌"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")


def validate_dataframe(df, required_columns):
    """驗證 DataFrame 是否包含必要的欄位"""
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"DataFrame 缺少必要欄位: {missing_columns}")
    return True


def format_number(num, decimal_places=2):
    """格式化數字顯示"""
    if isinstance(num, (int, float)):
        return f"{num:.{decimal_places}f}"
    return str(num)


class ProgressIndicator:
    """進度指示器"""
    
    def __init__(self, total_steps, description="Processing"):
        self.total_steps = total_steps
        self.current_step = 0
        self.description = description
    
    def update(self, step_description=""):
        """更新進度"""
        self.current_step += 1
        percentage = (self.current_step / self.total_steps) * 100
        bar_length = 30
        filled_length = int(bar_length * self.current_step // self.total_steps)
        
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        print(f'\r{self.description}: |{bar}| {percentage:.1f}% {step_description}', 
              end='', flush=True)
        
        if self.current_step >= self.total_steps:
            print()  # 換行
    
    def finish(self, message="完成!"):
        """完成進度條"""
        self.current_step = self.total_steps
        self.update(message)


def create_algorithm_mapping():
    """創建演算法編號對照表"""
    algorithms = [
        'ARIMA', '指數平滑法', 'GARCH', 'SVM', '隨機森林',
        'XGBoost', 'RNN/LSTM', 'CNN', 'Transformer', '基因演算法'
    ]
    
    mapping = {}
    reverse_mapping = {}
    
    for i, algo in enumerate(algorithms, 1):
        mapping[str(i)] = algo
        reverse_mapping[algo] = str(i)
    
    return mapping, reverse_mapping


def print_algorithm_reference():
    """打印演算法編號對照表"""
    mapping, _ = create_algorithm_mapping()
    
    print("\n演算法編號對照表:")
    print("=" * 50)
    for num, name in mapping.items():
        print(f"{num:2s}. {name}")
    print("=" * 50)
    print("圖表中的數字標籤對應上述演算法編號")


def generate_report_summary(chart_files):
    """生成報告摘要"""
    print("\n" + "=" * 60)
    print("圖表生成完成報告")
    print("=" * 60)
    
    existing_files = []
    missing_files = []
    
    for i, (name, path) in enumerate(chart_files.items(), 1):
        if Path(path).exists():
            file_size = Path(path).stat().st_size / 1024  # KB
            existing_files.append((name, path, file_size))
        else:
            missing_files.append((name, path))
    
    # 顯示存在的文件
    for i, (name, path, file_size) in enumerate(existing_files, 1):
        print(f"{i}. {name}")
        print(f"   文件: {path}")
        print(f"   大小: {file_size:.1f} KB")
    
    # 顯示缺失的文件（如果有）
    if missing_files:
        print(f"\n⚠️ 以下 {len(missing_files)} 個文件未生成（可能是依賴問題）:")
        for name, path in missing_files:
            print(f"   • {name}: {path}")
    
    print(f"\n總共生成 {len(existing_files)} 個圖表文件")
    if existing_files:
        print("所有圖表均採用 300 DPI 高品質輸出")
    print("=" * 60)
