# -*- coding: utf-8 -*-
"""
簡化版主程式 - 用於錯誤診斷
"""

import sys
import traceback
from pathlib import Path

def test_imports():
    """測試模組導入"""
    print("🔍 測試模組導入...")
    
    try:
        print("測試基本模組...")
        import matplotlib
        print(f"✅ matplotlib: {matplotlib.__version__}")
        
        import numpy
        print(f"✅ numpy: {numpy.__version__}")
        
        import pandas
        print(f"✅ pandas: {pandas.__version__}")
        
    except Exception as e:
        print(f"❌ 基本模組導入失敗: {e}")
        return False
    
    try:
        print("\n測試專案模組...")
        # 添加專案根目錄到 Python 路徑
        project_root = Path(__file__).parent.parent
        sys.path.insert(0, str(project_root))
        print(f"專案根目錄: {project_root}")
        
        from src.font_manager import FontManager
        print("✅ FontManager 導入成功")
        
        from src.data_manager import DataManager
        print("✅ DataManager 導入成功")
        
        from src.chart_generator import ChartGenerator
        print("✅ ChartGenerator 導入成功")
        
        from src.utils import timer, log_operation, ProgressIndicator
        print("✅ utils 導入成功")
        
    except Exception as e:
        print(f"❌ 專案模組導入失敗: {e}")
        traceback.print_exc()
        return False
    
    return True

def test_basic_functionality():
    """測試基本功能"""
    print("\n📊 測試基本功能...")
    
    try:
        project_root = Path(__file__).parent.parent
        sys.path.insert(0, str(project_root))
        
        from src.font_manager import FontManager
        from src.data_manager import DataManager
        from src.chart_generator import ChartGenerator
        
        # 測試字體管理器
        font_manager = FontManager()
        print("✅ FontManager 初始化成功")
        
        # 測試數據管理器
        data_manager = DataManager()
        df = data_manager.create_algorithm_dataframe()
        print(f"✅ DataManager 創建數據成功: {len(df)} 行")
        
        # 測試圖表生成器
        output_dir = project_root / "output" / "test"
        chart_generator = ChartGenerator(font_manager, output_dir)
        print("✅ ChartGenerator 初始化成功")
        
        return True
        
    except Exception as e:
        print(f"❌ 基本功能測試失敗: {e}")
        traceback.print_exc()
        return False

def simple_chart_test():
    """簡單圖表測試"""
    print("\n🎨 測試簡單圖表生成...")
    
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        
        # 創建簡單測試圖表
        fig, ax = plt.subplots(figsize=(8, 6))
        
        x = np.arange(5)
        y = [1, 2, 3, 2, 1]
        
        ax.bar(x, y, color='blue', alpha=0.7)
        ax.set_title('簡單測試圖表')
        ax.set_xlabel('X軸')
        ax.set_ylabel('Y軸')
        
        # 保存圖表
        output_dir = Path(__file__).parent.parent / "output" / "test"
        output_dir.mkdir(parents=True, exist_ok=True)
        
        output_path = output_dir / "simple_test_chart.png"
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        plt.close()
        
        print(f"✅ 簡單圖表生成成功: {output_path}")
        return True
        
    except Exception as e:
        print(f"❌ 簡單圖表測試失敗: {e}")
        traceback.print_exc()
        return False

def main():
    """主函數"""
    print("="*60)
    print("🧪 演算法比較分析專案 - 錯誤診斷")
    print("="*60)
    
    # 測試步驟
    tests = [
        ("模組導入測試", test_imports),
        ("基本功能測試", test_basic_functionality),
        ("簡單圖表測試", simple_chart_test)
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ {test_name} 異常失敗: {e}")
            traceback.print_exc()
            results[test_name] = False
    
    # 顯示結果摘要
    print("\n" + "="*60)
    print("📋 診斷結果摘要")
    print("="*60)
    
    for test_name, result in results.items():
        status = "✅ 通過" if result else "❌ 失敗"
        print(f"{test_name}: {status}")
    
    if all(results.values()):
        print("\n🎉 所有測試通過！問題可能在於複雜的功能")
        print("建議: 檢查增強版圖表生成器的依賴")
    else:
        print("\n⚠️ 發現問題，請根據上述錯誤訊息進行修復")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    main()
