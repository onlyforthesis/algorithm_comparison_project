# -*- coding: utf-8 -*-
"""
演算法比較專案測試模組
"""

import unittest
import sys
from pathlib import Path

# 添加專案路徑
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))

try:
    from simplified_main import AlgorithmComparisonGenerator, create_algorithm_dataframe
except ImportError:
    print("無法導入主模組，請檢查專案結構")


class TestAlgorithmComparison(unittest.TestCase):
    """演算法比較功能測試"""
    
    def setUp(self):
        """測試前置設定"""
        self.test_output_dir = Path("test_output")
        self.test_output_dir.mkdir(exist_ok=True)
        self.generator = AlgorithmComparisonGenerator(self.test_output_dir)
        self.df = create_algorithm_dataframe()
    
    def test_dataframe_creation(self):
        """測試數據框建立"""
        self.assertIsNotNone(self.df)
        self.assertEqual(len(self.df), 10)
        self.assertIn('演算法', self.df.columns)
        self.assertIn('預測精度', self.df.columns)
    
    def test_chart_generation(self):
        """測試圖表生成"""
        try:
            # 測試主要比較圖表
            chart_path = self.generator.create_main_comparison_chart(self.df)
            self.assertTrue(chart_path.exists())
            
            # 測試效能比較圖表
            perf_chart_path = self.generator.create_performance_comparison_chart()
            self.assertTrue(perf_chart_path.exists())
            
            # 測試摘要表格
            table_path = self.generator.create_summary_table(self.df)
            self.assertTrue(table_path.exists())
            
        except Exception as e:
            self.fail(f"圖表生成失敗: {e}")
    
    def test_complexity_mapping(self):
        """測試複雜度映射"""
        complexity_map = self.generator.complexity_map
        self.assertEqual(complexity_map['極低'], 1)
        self.assertEqual(complexity_map['極高'], 6)
    
    def tearDown(self):
        """測試清理"""
        # 清理測試文件
        import shutil
        if self.test_output_dir.exists():
            shutil.rmtree(self.test_output_dir)


if __name__ == '__main__':
    print("開始執行演算法比較專案測試...")
    unittest.main(verbosity=2)
