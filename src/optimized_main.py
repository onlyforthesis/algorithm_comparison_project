# -*- coding: utf-8 -*-
"""
圖表優化主程式
展示各種增強的圖表生成功能
"""

import sys
from pathlib import Path

# 添加專案根目錄到 Python 路徑
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from font_manager import FontManager
from data_manager import DataManager
from enhanced_chart_generator import EnhancedChartGenerator
from utils import timer, log_operation, ProgressIndicator


class ChartOptimizationApp:
    """圖表優化應用程式"""
    
    def __init__(self):
        self.font_manager = FontManager()
        self.data_manager = DataManager()
        self.enhanced_generator = EnhancedChartGenerator(
            self.font_manager, 
            project_root / "output",
            theme='professional'  # 可選: 'professional', 'dark', 'cyberpunk'
        )
        self.progress = ProgressIndicator(5, "生成優化圖表")
    
    @timer
    def run_optimization(self):
        """運行圖表優化程序"""
        log_operation("🚀 開始執行圖表優化程序")
        
        try:
            # 載入數據
            self.progress.update("載入演算法數據...")
            df = self.data_manager.load_data_from_csv()
            
            # 1. 生成增強版主要比較圖表
            self.progress.update("生成增強版比較圖表...")
            self.enhanced_generator.create_enhanced_main_comparison(df)
            
            # 2. 生成交互式儀表板
            self.progress.update("生成交互式儀表板...")
            interactive_fig = self.enhanced_generator.create_interactive_dashboard(df)
            
            # 3. 生成動畫圖表
            self.progress.update("生成動畫比較圖...")
            animation = self.enhanced_generator.create_animated_comparison(df)
            
            # 4. 生成多主題版本
            self.progress.update("生成多主題圖表...")
            self._generate_multi_theme_charts(df)
            
            self.progress.finish("所有優化圖表生成完成! ✨")
            
            # 顯示優化結果摘要
            self._show_optimization_summary()
            
        except Exception as e:
            log_operation(f"程式執行錯誤: {e}", "ERROR")
            raise
    
    def _generate_multi_theme_charts(self, df):
        """生成多主題圖表"""
        themes = ['professional', 'dark', 'cyberpunk']
        
        for theme in themes:
            print(f"🎨 生成 {theme} 主題圖表...")
            theme_generator = EnhancedChartGenerator(
                self.font_manager,
                project_root / "output" / f"{theme}_theme",
                theme=theme
            )
            theme_generator.create_enhanced_main_comparison(df)
    
    def _show_optimization_summary(self):
        """顯示優化結果摘要"""
        print("\n" + "="*80)
        print("🎊 圖表優化程序執行完成！")
        print("="*80)
        
        print("\n✨ 優化特色:")
        print("   🎯 3D視覺效果 - 立體散點圖和陰影效果")
        print("   🌈 漸變色彩方案 - 現代化配色和漸變背景")
        print("   📊 多樣化圖表 - 熱力圖、氣泡圖、雷達圖等")
        print("   🎭 主題化設計 - 專業版、暗色版、賽博朋克版")
        print("   🎬 動畫效果 - 動態展示數據變化")
        print("   🌐 交互式儀表板 - HTML格式可互動圖表")
        print("   💫 裝飾元素 - 邊框、陰影、發光效果")
        
        print("\n🔧 技術改進:")
        print("   • 響應式佈局設計")
        print("   • 高解析度輸出 (300 DPI)")
        print("   • 多格式支援 (PNG, HTML, GIF)")
        print("   • 自適應顏色方案")
        print("   • 智能標籤避免重疊")
        print("   • 增強的視覺層次")
        
        print("\n📁 生成的文件:")
        output_dir = project_root / "output"
        
        files_info = [
            ("主要增強圖表", "ultra_enhanced_algorithm_comparison.png"),
            ("交互式儀表板", "interactive_dashboard.html"),
            ("動畫比較圖", "animated_comparison.gif"),
            ("專業主題圖表", "professional_theme/ultra_enhanced_algorithm_comparison.png"),
            ("暗色主題圖表", "dark_theme/ultra_enhanced_algorithm_comparison.png"),
            ("賽博朋克主題", "cyberpunk_theme/ultra_enhanced_algorithm_comparison.png")
        ]
        
        for desc, filename in files_info:
            filepath = output_dir / filename
            if filepath.exists():
                print(f"   ✅ {desc}: {filepath}")
            else:
                print(f"   📝 {desc}: {filepath} (將生成)")
        
        print("\n🎮 使用建議:")
        print("   1. 使用瀏覽器打開 interactive_dashboard.html 體驗交互功能")
        print("   2. 動畫圖表適合用於演示和報告")
        print("   3. 不同主題適合不同的展示場合")
        print("   4. 高解析度圖表適合印刷和專業展示")
        
        print("\n" + "="*80)


def main():
    """主函數"""
    print("="*80)
    print("🚀 演算法比較分析專案 - 圖表優化版 v2.0")
    print("專業的演算法比較分析工具 - 增強視覺效果")
    print("="*80)
    
    try:
        app = ChartOptimizationApp()
        app.run_optimization()
        
    except KeyboardInterrupt:
        log_operation("程式被用戶中斷", "WARNING")
    except Exception as e:
        log_operation(f"程式執行失敗: {e}", "ERROR")
        sys.exit(1)


if __name__ == "__main__":
    main()
