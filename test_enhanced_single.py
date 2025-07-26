# -*- coding: utf-8 -*-
"""
測試增強版圖表生成器的單圖表功能
"""

import pandas as pd
from pathlib import Path
import sys
sys.path.append('src')
sys.path.append('.')

from src.enhanced_chart_generator import EnhancedChartGenerator
from src.font_manager import FontManager
from config.algorithm_data import ALGORITHM_DATA

def test_single_chart_generation():
    """測試單個圖表生成功能"""
    print("🧪 開始測試增強版單圖表生成...")
    
    # 初始化
    font_manager = FontManager()
    output_dir = Path("output") / "test_enhanced"
    
    generator = EnhancedChartGenerator(
        font_manager=font_manager,
        output_dir=output_dir,
        theme='professional'
    )
    
    # 創建測試數據 - 使用正確的列名映射
    raw_df = pd.DataFrame(ALGORITHM_DATA)
    
    # 創建符合預期格式的數據框
    df = pd.DataFrame({
        '演算法名稱': raw_df['name'],
        '計算複雜度': raw_df['complexity'],
        '算力需求': raw_df['compute_power'],
        '記憶體需求': raw_df['memory'],
        '適用場景': raw_df['scenario']
    })
    
    # 測試生成單個散點圖
    print("\n📊 測試生成單個散點圖...")
    generator.create_single_chart(df, 'scatter')
    
    # 測試生成單個柱狀圖
    print("\n📊 測試生成單個柱狀圖...")
    generator.create_single_chart(df, 'bar')
    
    # 測試錯誤的圖表類型
    print("\n📊 測試錯誤的圖表類型...")
    generator.create_single_chart(df, 'invalid_type')
    
    print("\n✅ 測試完成！")

if __name__ == "__main__":
    test_single_chart_generation()
