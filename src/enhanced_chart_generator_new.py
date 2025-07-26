# -*- coding: utf-8 -*-
"""
增強版圖表生成模組
提供現代化、單獨顯示的圖表生成功能（無動畫）
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd
from pathlib import Path
import warnings
import seaborn as sns

# 嘗試導入可選依賴
try:
    import plotly.graph_objects as go
    import plotly.express as px
    from plotly.subplots import make_subplots
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

warnings.filterwarnings('ignore')

# 動態導入配置模組
import sys
sys.path.append(str(Path(__file__).parent.parent))
from config.chart_config import ChartConfig


class EnhancedChartGenerator:
    """增強版圖表生成器"""
    
    def __init__(self, font_manager, output_dir=None, theme='professional'):
        self.font_manager = font_manager
        self.zh_font = font_manager.get_font()
        self.output_dir = output_dir or Path(__file__).parent.parent / "output"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.theme = theme
        self.setup_style()
    
    def setup_style(self):
        """設置全局樣式"""
        plt.style.use('seaborn-v0_8' if hasattr(plt.style, 'seaborn-v0_8') else 'default')
        
        # 設置中文字體
        plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'DejaVu Sans']
        plt.rcParams['axes.unicode_minus'] = False
        
        # 設置主題樣式
        theme_style = ChartConfig.get_theme_style(self.theme)
        plt.rcParams['figure.facecolor'] = theme_style['background']
        plt.rcParams['axes.facecolor'] = theme_style['background']
        plt.rcParams['text.color'] = theme_style['text_color']
        plt.rcParams['axes.labelcolor'] = theme_style['text_color']
        plt.rcParams['xtick.color'] = theme_style['text_color']
        plt.rcParams['ytick.color'] = theme_style['text_color']
    
    def create_enhanced_main_comparison(self, df):
        """建立增強版演算法比較圖表 - 分別生成多個獨立圖表"""
        print("\n🎨 開始生成增強版圖表系列...")
        
        # 建立顏色映射和數據
        colors = ChartConfig.get_color_scheme('cyberpunk')
        gradient_colors = ChartConfig.get_gradient_colors('gradient_blue', len(df))
        complexity_map = {'極低': 1, '低': 2, '中': 3, '中-高': 4, '高': 5, '極高': 6}
        
        # 準備數據
        x = [complexity_map.get(x.split('(')[0], 3) for x in df['計算複雜度']]
        y = [complexity_map.get(x.split('(')[0], 3) for x in df['算力需求']]
        labels = [str(i+1) for i in range(len(df))]
        
        # 1. 生成3D風格散點圖
        self._create_single_3d_scatter(df, x, y, colors, complexity_map)
        
        # 2. 生成增強柱狀圖
        self._create_single_enhanced_bar(df, gradient_colors, labels, complexity_map)
        
        # 3. 生成熱力圖
        self._create_single_heatmap(df, complexity_map)
        
        # 4. 生成雷達圖
        self._create_single_radar(df, colors, labels, complexity_map)
        
        # 5. 生成圓餅圖
        self._create_single_pie(df)
        
        # 6. 生成氣泡圖  
        self._create_single_bubble(df, complexity_map)
        
        print("✨ 所有增強版圖表已生成完成！")
    
    def _create_single_3d_scatter(self, df, x, y, colors, complexity_map):
        """創建獨立的3D風格散點圖"""
        fig, ax = plt.subplots(figsize=(12, 9))
        
        # 模擬3D效果的散點圖
        z_values = np.random.rand(len(x)) * 100  # 模擬第三維度
        
        # 創建氣泡大小變化
        sizes = [300 + z*5 for z in z_values]
        
        scatter = ax.scatter(x, y, c=colors[:len(x)], s=sizes, 
                           alpha=ChartConfig.CHART_STYLE['alpha'], 
                           edgecolors='white', 
                           linewidth=3)
        
        # 添加陰影效果
        shadow_scatter = ax.scatter([xi-0.1 for xi in x], [yi-0.1 for yi in y], 
                                  c='gray', s=[s*0.8 for s in sizes], 
                                  alpha=0.3, zorder=0)
        
        ChartConfig.apply_modern_style(ax, '計算複雜度 vs 算力需求 (3D風格)', self.theme)
        ax.set_xlabel('計算複雜度', fontproperties=self.zh_font, fontsize=14)
        ax.set_ylabel('算力需求', fontproperties=self.zh_font, fontsize=14)
        ax.set_xlim(0.5, 6.5)
        ax.set_ylim(0.5, 6.5)
        
        # 添加數值標籤
        for i, (xi, yi) in enumerate(zip(x, y)):
            ax.annotate(str(i+1), (xi, yi), ha='center', va='center',
                       fontweight='bold', fontsize=12, color='white')
        
        # 添加演算法對照表
        self._add_algorithm_legend(ax, df)
        
        # 保存並顯示
        output_path = self.output_dir / "enhanced_scatter_3d.png"
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"✨ 3D風格散點圖已儲存: {output_path}")
        plt.show()
        plt.close()
    
    def _create_single_enhanced_bar(self, df, colors, labels, complexity_map):
        """創建獨立的增強柱狀圖"""
        fig, ax = plt.subplots(figsize=(14, 8))
        
        memory_values = [complexity_map.get(x, 3) for x in df['記憶體需求']]
        
        # 創建漸變柱狀圖
        bars = ax.bar(range(len(df)), memory_values, 
                     color=colors[:len(df)], 
                     alpha=ChartConfig.CHART_STYLE['alpha'], 
                     edgecolor='white', 
                     linewidth=2)
        
        # 添加紋理效果
        for i, bar in enumerate(bars):
            height = bar.get_height()
            # 添加頂部發光效果
            glow_height = height * 0.1
            ax.add_patch(patches.Rectangle(
                (bar.get_x(), height-glow_height), 
                bar.get_width(), glow_height,
                facecolor='white', alpha=0.3, zorder=10
            ))
            
            # 添加數值標籤
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.1, 
                   f'{height:.1f}', ha='center', va='bottom',
                   fontweight='bold', fontsize=11)
        
        ChartConfig.apply_modern_style(ax, '記憶體需求比較 (增強版)', self.theme)
        ax.set_xlabel('演算法編號', fontproperties=self.zh_font, fontsize=14)
        ax.set_ylabel('記憶體需求等級', fontproperties=self.zh_font, fontsize=14)
        ax.set_xticks(range(len(df)))
        ax.set_xticklabels(labels)
        
        # 添加演算法對照表
        self._add_algorithm_legend(ax, df)
        
        # 保存並顯示
        output_path = self.output_dir / "enhanced_bar_memory.png"
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"✨ 增強版記憶體需求圖已儲存: {output_path}")
        plt.show()
        plt.close()
    
    def _create_single_heatmap(self, df, complexity_map):
        """創建獨立的熱力圖"""
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # 準備熱力圖數據
        features = ['計算複雜度', '算力需求', '記憶體需求']
        data = []
        
        for feature in features:
            if feature == '記憶體需求':
                row = [complexity_map.get(val, 3) for val in df[feature]]
            else:
                row = [complexity_map.get(val.split('(')[0], 3) for val in df[feature]]
            data.append(row)
        
        data = np.array(data)
        
        # 創建熱力圖
        im = ax.imshow(data, cmap='RdYlBu_r', aspect='auto', alpha=0.8)
        
        # 設置標籤
        ax.set_xticks(range(len(df)))
        ax.set_xticklabels([str(i+1) for i in range(len(df))])
        ax.set_yticks(range(len(features)))
        ax.set_yticklabels(features, fontproperties=self.zh_font)
        
        # 添加數值標籤
        for i in range(len(features)):
            for j in range(len(df)):
                text = ax.text(j, i, f'{data[i, j]:.0f}',
                             ha="center", va="center", color="white", fontweight='bold')
        
        ChartConfig.apply_modern_style(ax, '演算法特性熱力圖', self.theme)
        
        # 添加顏色條
        cbar = plt.colorbar(im, ax=ax, shrink=0.8)
        cbar.set_label('複雜度等級', fontproperties=self.zh_font)
        
        # 添加演算法對照表
        self._add_algorithm_legend_below(fig, df)
        
        # 保存並顯示
        output_path = self.output_dir / "enhanced_heatmap.png"
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"✨ 熱力圖已儲存: {output_path}")
        plt.show()
        plt.close()
    
    def _create_single_radar(self, df, colors, labels, complexity_map):
        """創建獨立的雷達圖"""
        fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))
        
        categories = ['計算複雜度', '算力需求', '記憶體需求']
        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
        angles += angles[:1]
        
        # 繪製前5個演算法
        for i in range(min(5, len(df))):
            values = [
                complexity_map.get(df.iloc[i]['計算複雜度'].split('(')[0], 3),
                complexity_map.get(df.iloc[i]['算力需求'].split('(')[0], 3),
                complexity_map.get(df.iloc[i]['記憶體需求'], 3)
            ]
            values += values[:1]
            
            # 創建漸變效果
            line = ax.plot(angles, values, 'o-', linewidth=3, label=f'演算法{i+1}', 
                         color=colors[i], markersize=8)
            ax.fill(angles, values, alpha=0.25, color=colors[i])
            
            # 添加發光效果
            ax.plot(angles, values, 'o-', linewidth=6, alpha=0.3, color=colors[i])
        
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories, fontproperties=self.zh_font)
        ax.set_ylim(0, 6)
        ax.set_title('多維度演算法比較 (雷達圖)', fontproperties=self.zh_font, 
                    fontsize=16, fontweight='bold', pad=30)
        ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
        ax.grid(True, alpha=0.3)
        
        # 保存並顯示
        output_path = self.output_dir / "enhanced_radar.png"
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"✨ 雷達圖已儲存: {output_path}")
        plt.show()
        plt.close()
    
    def _create_single_pie(self, df):
        """創建獨立的圓餅圖"""
        fig, ax = plt.subplots(figsize=(10, 8))
        
        scenario_counts = {}
        for scenario in df['適用場景']:
            if '預測' in scenario:
                key = '預測類'
            elif '分類' in scenario or '特徵' in scenario:
                key = '分類類'
            elif '建模' in scenario or '圖像' in scenario or '多模態' in scenario:
                key = '深度學習類'
            else:
                key = '其他類'
            scenario_counts[key] = scenario_counts.get(key, 0) + 1
        
        colors = ChartConfig.get_color_scheme('neon')
        explode = [0.05] * len(scenario_counts)
        
        # 創建3D效果的圓餅圖
        wedges, texts, autotexts = ax.pie(
            scenario_counts.values(), 
            labels=scenario_counts.keys(),
            autopct='%1.1f%%', 
            startangle=90,
            colors=colors[:len(scenario_counts)],
            explode=explode,
            shadow=True,
            textprops={'fontsize': 12, 'fontweight': 'bold'}
        )
        
        # 添加邊框效果
        for wedge in wedges:
            wedge.set_linewidth(3)
            wedge.set_edgecolor('white')
        
        for text in texts:
            text.set_fontproperties(self.zh_font)
        
        ax.set_title('適用場景分布', fontproperties=self.zh_font, 
                    fontsize=16, fontweight='bold')
        
        # 保存並顯示
        output_path = self.output_dir / "enhanced_pie_scenarios.png"
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"✨ 適用場景圓餅圖已儲存: {output_path}")
        plt.show()
        plt.close()
    
    def _create_single_bubble(self, df, complexity_map):
        """創建獨立的氣泡圖"""
        fig, ax = plt.subplots(figsize=(12, 9))
        
        # 準備數據
        x_vals = [complexity_map.get(x.split('(')[0], 3) for x in df['計算複雜度']]
        y_vals = [complexity_map.get(x.split('(')[0], 3) for x in df['算力需求']]
        sizes = [complexity_map.get(x, 3) * 100 for x in df['記憶體需求']]
        
        colors = ChartConfig.get_color_scheme('viridis')
        
        # 創建氣泡圖
        scatter = ax.scatter(x_vals, y_vals, s=sizes, c=colors[:len(df)], 
                           alpha=0.7, edgecolors='white', linewidth=2)
        
        # 添加標籤
        for i, (x, y) in enumerate(zip(x_vals, y_vals)):
            ax.annotate(str(i+1), (x, y), ha='center', va='center',
                       fontweight='bold', color='white', fontsize=12)
        
        ChartConfig.apply_modern_style(ax, '綜合特性氣泡圖', self.theme)
        ax.set_xlabel('計算複雜度', fontproperties=self.zh_font, fontsize=14)
        ax.set_ylabel('算力需求', fontproperties=self.zh_font, fontsize=14)
        
        # 添加氣泡大小說明
        legend_elements = [
            plt.scatter([], [], s=100, c='gray', alpha=0.7, edgecolors='white', linewidth=2, label='記憶體需求: 低'),
            plt.scatter([], [], s=300, c='gray', alpha=0.7, edgecolors='white', linewidth=2, label='記憶體需求: 中'),
            plt.scatter([], [], s=500, c='gray', alpha=0.7, edgecolors='white', linewidth=2, label='記憶體需求: 高')
        ]
        ax.legend(handles=legend_elements, loc='upper left')
        
        # 添加演算法對照表
        self._add_algorithm_legend(ax, df)
        
        # 保存並顯示
        output_path = self.output_dir / "enhanced_bubble.png"
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"✨ 氣泡圖已儲存: {output_path}")
        plt.show()
        plt.close()
    
    def _add_algorithm_legend(self, ax, df):
        """添加演算法對照表"""
        legend_text = "演算法編號對照:\n"
        for i, row in df.iterrows():
            legend_text += f"{i+1}. {row['演算法名稱']}\n"
        
        ax.text(1.02, 1, legend_text, transform=ax.transAxes, 
               fontproperties=self.zh_font, fontsize=9, 
               verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3", 
               facecolor='lightgray', alpha=0.8))
    
    def _add_algorithm_legend_below(self, fig, df):
        """在圖表下方添加演算法對照表"""
        legend_text = "演算法編號對照: "
        for i, row in df.iterrows():
            if i > 0 and i % 3 == 0:
                legend_text += "\n"
            legend_text += f"{i+1}.{row['演算法名稱']}  "
        
        fig.text(0.5, 0.02, legend_text, ha='center', va='bottom',
                fontproperties=self.zh_font, fontsize=10, 
                bbox=dict(boxstyle="round,pad=0.5", facecolor='lightgray', alpha=0.8))
    
    def create_interactive_dashboard(self, df):
        """創建交互式儀表板（不含動畫）"""
        if not PLOTLY_AVAILABLE:
            print("⚠️ Plotly未安裝，跳過交互式儀表板生成")
            return None
            
        try:
            # 創建互動式Plotly圖表
            fig = make_subplots(
                rows=2, cols=2,
                subplot_titles=('計算複雜度 vs 算力需求', '記憶體需求比較', 
                              '演算法特性雷達圖', '適用場景分布'),
                specs=[[{"type": "scatter"}, {"type": "bar"}],
                       [{"type": "scatterpolar"}, {"type": "pie"}]]
            )
            
            complexity_map = {'極低': 1, '低': 2, '中': 3, '中-高': 4, '高': 5, '極高': 6}
            
            # 1. 散點圖
            x = [complexity_map.get(x.split('(')[0], 3) for x in df['計算複雜度']]
            y = [complexity_map.get(x.split('(')[0], 3) for x in df['算力需求']]
            
            fig.add_trace(
                go.Scatter(x=x, y=y, mode='markers+text',
                          text=[str(i+1) for i in range(len(df))],
                          textposition="middle center",
                          marker=dict(size=15, color=np.arange(len(df)), 
                                    colorscale='Viridis', showscale=True),
                          name='演算法'),
                row=1, col=1
            )
            
            # 2. 柱狀圖
            memory_values = [complexity_map.get(x, 3) for x in df['記憶體需求']]
            fig.add_trace(
                go.Bar(x=[str(i+1) for i in range(len(df))], y=memory_values,
                      name='記憶體需求', marker_color='lightblue'),
                row=1, col=2
            )
            
            # 3. 雷達圖
            categories = ['計算複雜度', '算力需求', '記憶體需求']
            for i in range(min(3, len(df))):
                values = [
                    complexity_map.get(df.iloc[i]['計算複雜度'].split('(')[0], 3),
                    complexity_map.get(df.iloc[i]['算力需求'].split('(')[0], 3),
                    complexity_map.get(df.iloc[i]['記憶體需求'], 3)
                ]
                
                fig.add_trace(
                    go.Scatterpolar(r=values, theta=categories,
                                  fill='toself', name=f'演算法{i+1}'),
                    row=2, col=1
                )
            
            # 4. 圓餅圖
            scenario_counts = {}
            for scenario in df['適用場景']:
                if '預測' in scenario:
                    key = '預測類'
                elif '分類' in scenario or '特徵' in scenario:
                    key = '分類類'
                elif '建模' in scenario or '圖像' in scenario or '多模態' in scenario:
                    key = '深度學習類'
                else:
                    key = '其他類'
                scenario_counts[key] = scenario_counts.get(key, 0) + 1
            
            fig.add_trace(
                go.Pie(labels=list(scenario_counts.keys()), 
                      values=list(scenario_counts.values())),
                row=2, col=2
            )
            
            # 更新佈局
            fig.update_layout(
                title_text="演算法比較交互式儀表板",
                title_x=0.5,
                height=800,
                showlegend=True
            )
            
            # 保存為HTML文件
            output_path = self.output_dir / ChartConfig.OUTPUT_FILES['interactive_dashboard']
            fig.write_html(str(output_path))
            print(f"🌐 交互式儀表板已儲存: {output_path}")
            
            return fig
            
        except Exception as e:
            print(f"⚠️ 交互式儀表板生成失敗: {e}")
            return None
