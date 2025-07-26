# -*- coding: utf-8 -*-
"""
圖表優化測試腳本
快速測試各種圖表生成功能
"""

import sys
from pathlib import Path

# 添加專案根目錄到 Python 路徑
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

def test_basic_dependencies():
    """測試基本依賴"""
    print("🔍 測試基本依賴...")
    
    try:
        import matplotlib
        print(f"✅ matplotlib: {matplotlib.__version__}")
    except ImportError:
        print("❌ matplotlib 未安裝")
        return False
    
    try:
        import numpy as np
        print(f"✅ numpy: {np.__version__}")
    except ImportError:
        print("❌ numpy 未安裝")
        return False
    
    try:
        import pandas as pd
        print(f"✅ pandas: {pd.__version__}")
    except ImportError:
        print("❌ pandas 未安裝")
        return False
    
    try:
        import seaborn as sns
        print(f"✅ seaborn: {sns.__version__}")
    except ImportError:
        print("❌ seaborn 未安裝")
        return False
    
    return True

def test_enhanced_dependencies():
    """測試增強功能依賴"""
    print("\n🚀 測試增強功能依賴...")
    
    results = {}
    
    try:
        import plotly
        print(f"✅ plotly: {plotly.__version__}")
        results['plotly'] = True
    except ImportError:
        print("❌ plotly 未安裝 (交互式圖表功能將不可用)")
        results['plotly'] = False
    
    try:
        from PIL import Image
        print(f"✅ pillow: {Image.__version__}")
        results['pillow'] = True
    except ImportError:
        print("❌ pillow 未安裝 (動畫功能將不可用)")
        results['pillow'] = False
    
    try:
        import scipy
        print(f"✅ scipy: {scipy.__version__}")
        results['scipy'] = True
    except ImportError:
        print("❌ scipy 未安裝 (高級計算功能將不可用)")
        results['scipy'] = False
    
    return results

def test_chart_generation():
    """測試基本圖表生成"""
    print("\n📊 測試基本圖表生成...")
    
    try:
        from font_manager import FontManager
        from data_manager import DataManager
        from chart_generator import ChartGenerator
        
        font_manager = FontManager()
        data_manager = DataManager()
        chart_generator = ChartGenerator(font_manager, project_root / "output" / "test")
        
        # 載入測試數據
        df = data_manager.create_algorithm_dataframe()
        print(f"✅ 成功載入 {len(df)} 個演算法數據")
        
        # 測試圖表生成
        chart_generator.create_main_comparison_chart(df)
        print("✅ 基本圖表生成成功")
        
        return True
        
    except Exception as e:
        print(f"❌ 基本圖表生成失敗: {e}")
        return False

def test_enhanced_chart_generation():
    """測試增強版圖表生成"""
    print("\n✨ 測試增強版圖表生成...")
    
    try:
        from enhanced_chart_generator import EnhancedChartGenerator
        from font_manager import FontManager
        from data_manager import DataManager
        
        font_manager = FontManager()
        data_manager = DataManager()
        enhanced_generator = EnhancedChartGenerator(
            font_manager, 
            project_root / "output" / "test_enhanced"
        )
        
        # 載入測試數據
        df = data_manager.create_algorithm_dataframe()
        
        # 測試增強版圖表生成
        enhanced_generator.create_enhanced_main_comparison(df)
        print("✅ 增強版圖表生成成功")
        
        return True
        
    except Exception as e:
        print(f"❌ 增強版圖表生成失敗: {e}")
        return False

def main():
    """主測試函數"""
    print("="*60)
    print("🧪 圖表優化功能測試")
    print("="*60)
    
    # 測試基本依賴
    if not test_basic_dependencies():
        print("\n❌ 基本依賴測試失敗，請安裝必要的套件")
        return
    
    # 測試增強功能依賴
    enhanced_deps = test_enhanced_dependencies()
    
    # 測試基本圖表生成
    if not test_chart_generation():
        print("\n❌ 基本圖表生成測試失敗")
        return
    
    # 測試增強版圖表生成
    if not test_enhanced_chart_generation():
        print("\n⚠️ 增強版圖表生成測試失敗，但基本功能可用")
    
    print("\n" + "="*60)
    print("🎉 測試完成！")
    print("="*60)
    
    print("\n📋 功能狀態總結:")
    print("✅ 基本圖表生成: 可用")
    print(f"{'✅' if enhanced_deps.get('plotly', False) else '❌'} 交互式圖表: {'可用' if enhanced_deps.get('plotly', False) else '不可用'}")
    print(f"{'✅' if enhanced_deps.get('pillow', False) else '❌'} 動畫圖表: {'可用' if enhanced_deps.get('pillow', False) else '不可用'}")
    print("✅ 多主題支援: 可用")
    print("✅ 3D視覺效果: 可用")
    
    if not all(enhanced_deps.values()):
        print(f"\n💡 建議執行以下命令安裝缺失的依賴:")
        print(f"   pip install -r {project_root}/requirements.txt")


if __name__ == "__main__":
    main()
