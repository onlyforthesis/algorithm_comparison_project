# -*- coding: utf-8 -*-
"""
數據管理模組
負責演算法數據的讀取、處理和管理
"""

import pandas as pd
import numpy as np
from pathlib import Path


class DataManager:
    """數據管理器"""
    
    def __init__(self, data_path=None):
        self.data_path = data_path or Path(__file__).parent.parent / "data"
        self.complexity_map = {
            '極低': 1, '低': 2, '中': 3, 
            '中-高': 4, '高': 5, '極高': 6
        }
    
    def create_algorithm_dataframe(self):
        """建立演算法比較資料表"""
        return pd.DataFrame({
            '演算法': [
                'ARIMA', '指數平滑法', 'GARCH', 'SVM', '隨機森林',
                'XGBoost', 'RNN/LSTM', 'CNN', 'Transformer', '基因演算法'
            ],
            '預測精度': [
                '中', '低-中', '中(波動)', '中-高', '高',
                '高', '高', '中-高', '高', '中-高'
            ],
            '計算複雜度': [
                '低', '極低', '中', '中', '高',
                '高', '極高', '高', '極高', '高'
            ],
            '算力需求': [
                '低', '極低', '中', '中-高', '高',
                '極高', '極高', '極高', '極高', '中-高'
            ],
            '記憶體需求': [
                '低', '極低', '低', '中', '中-高',
                '高', '極高', '高', '極高', '中'
            ],
            '可平行化': [
                '限制', '限制', '限制', '部分', '高',
                '高', '極高(GPU)', '極高(GPU)', '極高(GPU)', '高'
            ],
            '適用場景': [
                '趨勢預測', '短期預測', '波動預測', '分類問題', '特徵重要',
                '高精度', '序列建模', '圖像特徵', '多模態', '優化問題'
            ]
        })
    
    def load_data_from_csv(self, filename="algorithms.csv"):
        """從 CSV 文件載入數據"""
        try:
            csv_path = self.data_path / filename
            if csv_path.exists():
                return pd.read_csv(csv_path)
            else:
                print(f"CSV 文件不存在，使用預設數據: {csv_path}")
                return self.create_algorithm_dataframe()
        except Exception as e:
            print(f"載入 CSV 數據時發生錯誤: {e}")
            return self.create_algorithm_dataframe()
    
    def save_data_to_csv(self, df, filename="algorithms.csv"):
        """將數據保存到 CSV 文件"""
        try:
            csv_path = self.data_path / filename
            csv_path.parent.mkdir(parents=True, exist_ok=True)
            df.to_csv(csv_path, index=False, encoding='utf-8-sig')
            print(f"數據已保存到: {csv_path}")
        except Exception as e:
            print(f"保存 CSV 數據時發生錯誤: {e}")
    
    def create_smart_labels(self, algorithm_names, max_length=2):
        """建立純數字標籤映射"""
        return [str(i+1) for i in range(len(algorithm_names))]
    
    def get_complexity_value(self, complexity_str):
        """將複雜度字符串轉換為數值"""
        clean_str = complexity_str.split('(')[0]
        return self.complexity_map.get(clean_str, 3)
    
    def generate_mock_performance_data(self, num_algorithms=10):
        """生成模擬效能數據"""
        np.random.seed(42)  # 確保可重現
        
        return {
            'algorithms': [str(i+1) for i in range(num_algorithms)],
            'execution_time': np.random.randint(10, 600, num_algorithms).tolist(),
            'accuracy': np.random.randint(65, 99, num_algorithms).tolist(),
            'memory_usage': np.random.randint(50, 1200, num_algorithms).tolist()
        }
    
    def calculate_efficiency_score(self, execution_time, memory_usage, accuracy):
        """計算綜合效率評分"""
        return [100 - (t/10 + m/20 - a/2) 
                for t, m, a in zip(execution_time, memory_usage, accuracy)]
