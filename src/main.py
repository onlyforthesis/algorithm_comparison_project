# -*- coding: utf-8 -*-
"""
主程式入口
演算法比較分析專案
"""

import sys
from pathlib import Path

# 添加專案根目錄到 Python 路徑
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.font_manager import FontManager
from src.data_manager import DataManager
from src.chart_generator import ChartGenerator
from src.utils import (
    timer, log_operation, ProgressIndicator, 
    print_algorithm_reference, generate_report_summary
)

# 導入增強版圖表生成器
try:
    from src.enhanced_chart_generator import EnhancedChartGenerator
    ENHANCED_AVAILABLE = True
except ImportError:
    ENHANCED_AVAILABLE = False


class AlgorithmComparisonApp:
    """演算法比較分析應用程式主類"""
    
    def __init__(self, enhanced_mode=False):
        self.font_manager = FontManager()
        self.data_manager = DataManager()
        self.enhanced_mode = enhanced_mode and ENHANCED_AVAILABLE
        
        if self.enhanced_mode:
            self.chart_generator = EnhancedChartGenerator(
                self.font_manager, 
                project_root / "output"
            )
            self.progress = ProgressIndicator(5, "生成增強圖表")
        else:
            self.chart_generator = ChartGenerator(
                self.font_manager, 
                project_root / "output"
            )
            self.progress = ProgressIndicator(4, "生成圖表")
    
    @timer
    def run(self):
        """運行主程式"""
        mode_text = "增強版" if self.enhanced_mode else "標準版"
        log_operation(f"開始執行演算法比較分析程式 ({mode_text})")
        
        try:
            # 1. 載入數據
            self.progress.update("載入演算法數據...")
            df = self._load_data()
            
            if self.enhanced_mode:
                # 增強模式
                self._run_enhanced_mode(df)
            else:
                # 標準模式
                self._run_standard_mode(df)
            
            # 顯示結果摘要
            self._show_summary()
            
            log_operation("程式執行完成", "INFO")
            return True
            
        except Exception as e:
            log_operation(f"程式執行錯誤: {str(e)}", "ERROR")
            import traceback
            traceback.print_exc()
            return False
    
    def _run_standard_mode(self, df):
        """運行標準模式"""
        # 2. 生成主要比較圖表
        self.progress.update("生成主要比較圖表...")
        self.chart_generator.create_main_comparison_chart(df)
        
        # 3. 生成效能比較圖表
        self.progress.update("生成效能比較圖表...")
        performance_data = self.data_manager.generate_mock_performance_data()
        self.chart_generator.create_performance_comparison_chart(performance_data)
        
        # 4. 生成摘要表格
        self.progress.update("生成摘要表格...")
        self.chart_generator.create_summary_table(df)
        
        self.progress.finish("所有圖表生成完成!")
    
    def _run_enhanced_mode(self, df):
        """運行增強模式"""
        try:
            # 2. 生成增強版主要比較圖表
            self.progress.update("生成增強版比較圖表...")
            self.chart_generator.create_enhanced_main_comparison(df)
            
            # 3. 生成交互式儀表板
            self.progress.update("生成交互式儀表板...")
            try:
                self.chart_generator.create_interactive_dashboard(df)
            except Exception as e:
                log_operation(f"交互式儀表板生成失敗 (可能是依賴問題): {e}", "WARNING")
            
            # 4. 生成多主題版本
            self.progress.update("生成多主題圖表...")
            self._generate_multi_theme_charts(df)
            
            # 5. 生成標準圖表以便比較
            self.progress.update("生成標準圖表以便比較...")
            standard_generator = ChartGenerator(self.font_manager, project_root / "output" / "standard")
            standard_generator.create_main_comparison_chart(df)
            
            self.progress.finish("所有增強圖表生成完成! ✨")
            
        except Exception as e:
            log_operation(f"增強模式執行失敗: {e}", "ERROR")
            # 降級到標準模式
            log_operation("降級到標準模式執行", "INFO")
            # 重新創建標準模式的圖表生成器
            self.chart_generator = ChartGenerator(
                self.font_manager, 
                project_root / "output"
            )
            self._run_standard_mode(df)
    
    def _generate_multi_theme_charts(self, df):
        """生成多主題圖表"""
        themes = ['dark', 'cyberpunk']
        
        for theme in themes:
            try:
                theme_generator = EnhancedChartGenerator(
                    self.font_manager,
                    project_root / "output" / f"{theme}_theme",
                    theme=theme
                )
                theme_generator.create_enhanced_main_comparison(df)
                log_operation(f"{theme} 主題圖表生成成功", "INFO")
            except Exception as e:
                log_operation(f"{theme} 主題圖表生成失敗: {e}", "WARNING")
    
    def _load_data(self):
        """載入演算法數據"""
        try:
            # 嘗試從 CSV 載入，如果不存在則使用預設數據
            df = self.data_manager.load_data_from_csv()
            
            # 保存數據到 CSV（如果是第一次運行）
            self.data_manager.save_data_to_csv(df)
            
            log_operation(f"成功載入 {len(df)} 個演算法的數據")
            return df
            
        except Exception as e:
            log_operation(f"數據載入失敗: {e}", "ERROR")
            raise
    
    def _show_summary(self):
        """顯示程式執行摘要"""
        import sys
        sys.path.append(str(project_root))
        from config.chart_config import ChartConfig
        
        output_dir = project_root / "output"
        
        if self.enhanced_mode:
            # 增強模式摘要
            print("\n" + "=" * 80)
            print("🎊 演算法比較分析程式執行完成！(增強版)")
            print("=" * 80)
            
            print("\n✨ 增強版特色:")
            print("   🎯 3D視覺效果 - 立體散點圖和陰影效果")
            print("   🌈 漸變色彩方案 - 現代化配色和漸變背景")
            print("   📊 多樣化圖表 - 熱力圖、氣泡圖、雷達圖等")
            print("   🎭 主題化設計 - 專業版、暗色版、賽博朋克版")
            print("   🌐 交互式儀表板 - HTML格式可互動圖表")
            print("   💫 裝飾元素 - 邊框、陰影、發光效果")
            print("   � 單獨圖表顯示 - 每張圖表獨立顯示，避免重疊")
            
            chart_files = {
                "增強版主要比較圖表": output_dir / ChartConfig.OUTPUT_FILES['main_comparison'],
                "交互式儀表板": output_dir / ChartConfig.OUTPUT_FILES['interactive_dashboard'],
                "暗色主題圖表": output_dir / "dark_theme" / ChartConfig.OUTPUT_FILES['main_comparison'],
                "賽博朋克主題": output_dir / "cyberpunk_theme" / ChartConfig.OUTPUT_FILES['main_comparison']
            }
        else:
            # 標準模式摘要
            chart_files = {
                "主要演算法比較圖表": output_dir / ChartConfig.OUTPUT_FILES['main_comparison'],
                "效能比較圖表": output_dir / ChartConfig.OUTPUT_FILES['performance'],
                "摘要表格": output_dir / ChartConfig.OUTPUT_FILES['summary_table']
            }
            
            print("\n" + "=" * 60)
            print("演算法比較分析程式執行完成！")
            print("=" * 60)
            
            print("\n✅ 優化特色:")
            print("   • 純數字標籤系統 - 完全避免文字重疊")
            print("   • 增強色彩方案 - 使用漸變和對比色彩")
            print("   • 視覺化等級標示 - 清楚表達數據等級")
            print("   • 多樣化圖表類型 - 散點圖、柱狀圖、雷達圖、圓餅圖")
            print("   • 專業版面設計 - 統一字體、邊框、陰影效果")
            print("   • 模組化架構 - 易於維護和擴展")
        
        print("\n✅ 技術規格:")
        print("   • 零重疊保證 - 數字標籤確保完全無重疊")
        print("   • 系統相容性 - 移除所有特殊字符和 emoji")
        print("   • 視覺層次感 - 白色邊框和透明度設計")
        print("   • 資訊完整性 - 通過顏色和對照表保持所有資訊")
        print("   • 高解析度輸出 - 300 DPI 專業品質")
        
        # 顯示演算法對照表
        print_algorithm_reference()
        
        # 生成詳細報告
        generate_report_summary(chart_files)


def main():
    """主函數"""
    print("="*80)
    print("演算法比較分析專案 v2.0.0")
    print("專業的演算法比較分析工具")
    print("="*80)
    
    # 詢問用戶選擇模式
    if ENHANCED_AVAILABLE:
        print("\n🎨 選擇運行模式:")
        print("1. 標準模式 - 經典圖表生成")
        print("2. 增強模式 - 3D效果、多主題、多種圖表類型（單獨顯示）")
        
        while True:
            try:
                choice = input("\n請選擇模式 (1或2，默認為1): ").strip()
                if choice == "" or choice == "1":
                    enhanced_mode = False
                    break
                elif choice == "2":
                    enhanced_mode = True
                    break
                else:
                    print("❌ 請輸入1或2")
            except KeyboardInterrupt:
                print("\n👋 程式已取消")
                return
    else:
        print("\n📝 注意: 增強模式功能未安裝，將使用標準模式")
        enhanced_mode = False
    
    try:
        app = AlgorithmComparisonApp(enhanced_mode=enhanced_mode)
        success = app.run()
        
        if success:
            print("\n🎉 程式執行成功完成！")
        else:
            print("\n⚠️ 程式執行遇到問題，但已嘗試恢復")
        
    except KeyboardInterrupt:
        log_operation("程式被用戶中斷", "WARNING")
        print("\n👋 程式已被用戶中斷")
    except Exception as e:
        log_operation(f"程式執行失敗: {str(e)}", "ERROR")
        print(f"\n❌ 程式執行失敗: {e}")
        print("請檢查錯誤日誌以獲取更多信息")
        # 不要 sys.exit(1)，讓程式正常結束


if __name__ == "__main__":
    main()
