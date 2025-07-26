# -*- coding: utf-8 -*-
"""
圖表配置模組 (增強版本)
定義所有圖表的樣式和配置參數，支援現代化視覺效果
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import seaborn as sns


class ChartConfig:
    """增強版圖表配置類"""
    
    # 現代化顏色方案
    COLORS = {
        'primary': plt.cm.tab10(np.linspace(0, 1, 10)),
        'viridis': plt.cm.viridis(np.linspace(0, 1, 10)),
        'set3': plt.cm.Set3(np.linspace(0, 1, 8)),
        'gradient_blue': LinearSegmentedColormap.from_list('gradient_blue', 
                        ['#E3F2FD', '#1976D2', '#0D47A1']),
        'gradient_green': LinearSegmentedColormap.from_list('gradient_green', 
                         ['#E8F5E8', '#4CAF50', '#2E7D32']),
        'cyberpunk': ['#FF073A', '#39FF14', '#00FFFF', '#FF4500', '#8A2BE2', 
                     '#FFD700', '#FF1493', '#00FF7F', '#DC143C', '#1E90FF'],
        'modern_dark': ['#1F2937', '#374151', '#6B7280', '#9CA3AF', '#D1D5DB'],
        'neon': ['#FF0080', '#00FF80', '#8000FF', '#FF8000', '#0080FF']
    }
    
    # 適應性圖表尺寸
    FIGURE_SIZES = {
        'main_comparison': (24, 18),
        'performance': (20, 16),
        'summary_table': (18, 12),
        'single_chart': (12, 8),
        'wide_chart': (16, 6)
    }
    
    # 層次化字體大小
    FONT_SIZES = {
        'title': 24,
        'subtitle': 18,
        'axis_label': 16,
        'tick_label': 14,
        'legend': 13,
        'annotation': 12,
        'table': 11,
        'watermark': 8
    }
    
    # 增強圖表樣式
    CHART_STYLE = {
        'dpi': 300,
        'bbox_inches': 'tight',
        'alpha': 0.85,
        'linewidth': 2.5,
        'markersize': 10,
        'grid_alpha': 0.25,
        'edge_color': 'white',
        'shadow_color': '#888888',
        'shadow_alpha': 0.3,
        'border_radius': 0.1,
        'gradient_alpha': 0.7
    }
    
    # 3D效果配置
    EFFECT_3D = {
        'elevation': 20,
        'azimuth': 45,
        'depth_shade': True,
        'light_source': (1, 1, 1)
    }
    
    # 動畫配置
    ANIMATION = {
        'duration': 1500,  # 毫秒
        'easing': 'ease-in-out',
        'delay': 200,
        'frames': 60
    }
    
    # 增強等級標示符號和樣式
    LEVEL_SYMBOLS = {
        'memory': {
            'symbols': ['🟢', '🟡', '🟠', '🔴', '🟣', '⚫'],
            'labels': ['極低', '低', '中', '高', '極高', '超高'],
            'colors': ['#4CAF50', '#FFEB3B', '#FF9800', '#F44336', '#9C27B0', '#424242']
        },
        'time': {
            'fast': {'symbol': '⚡', 'color': '#4CAF50', 'label': '快速'},
            'medium': {'symbol': '⏱️', 'color': '#FF9800', 'label': '中等'}, 
            'slow': {'symbol': '🐌', 'color': '#F44336', 'label': '緩慢'}
        },
        'efficiency': {
            'high': {'symbol': '🚀', 'color': '#4CAF50', 'label': '高效'},
            'medium': {'symbol': '⚖️', 'color': '#FF9800', 'label': '中等'},
            'low': {'symbol': '⚠️', 'color': '#F44336', 'label': '低效'}
        },
        'accuracy': {
            'excellent': {'symbol': '🎯', 'color': '#4CAF50', 'label': '優秀'},
            'good': {'symbol': '✅', 'color': '#8BC34A', 'label': '良好'},
            'average': {'symbol': '🔄', 'color': '#FF9800', 'label': '普通'},
            'poor': {'symbol': '❌', 'color': '#F44336', 'label': '較差'}
        }
    }
    
    # 向後相容性：保留舊版本的簡單符號格式
    LEVEL_SYMBOLS_LEGACY = {
        'memory': ['LOW', 'MID', 'HIGH', 'MAX', 'SUPER', 'ULTRA'],
        'time': {
            'fast': 'FAST',
            'medium': 'MID', 
            'slow': 'SLOW'
        },
        'efficiency': {
            'high': 'HIGH',
            'medium': 'MID',
            'low': 'LOW'
        }
    }
    
    # 複雜度標籤和顏色映射
    COMPLEXITY_LABELS = ['', '極低', '低', '中', '中-高', '高', '極高']
    COMPLEXITY_COLORS = {
        '極低': '#E8F5E8', '低': '#C8E6C9', '中': '#FFEB3B',
        '中-高': '#FF9800', '高': '#FF5722', '極高': '#D32F2F'
    }
    
    # 主題樣式配置
    THEMES = {
        'professional': {
            'background': '#FFFFFF',
            'text_color': '#2C3E50',
            'grid_color': '#ECF0F1',
            'accent_color': '#3498DB'
        },
        'dark': {
            'background': '#2C3E50',
            'text_color': '#ECF0F1',
            'grid_color': '#34495E',
            'accent_color': '#E74C3C'
        },
        'cyberpunk': {
            'background': '#0D1117',
            'text_color': '#FF073A',
            'grid_color': '#39FF14',
            'accent_color': '#00FFFF'
        }
    }
    
    # 輸出文件名配置
    OUTPUT_FILES = {
        'main_comparison': 'ultra_enhanced_algorithm_comparison.png',
        'performance': 'advanced_performance_analysis.png',
        'summary_table': 'professional_algorithm_summary.png',
        'animated_chart': 'animated_comparison.gif',
        'interactive_dashboard': 'interactive_dashboard.html'
    }
    
    # 圖表佈局配置
    LAYOUTS = {
        'grid_2x2': {'rows': 2, 'cols': 2, 'spacing': 0.3},
        'grid_2x3': {'rows': 2, 'cols': 3, 'spacing': 0.25},
        'single': {'rows': 1, 'cols': 1, 'spacing': 0},
        'horizontal': {'rows': 1, 'cols': 3, 'spacing': 0.2}
    }
    
    @classmethod
    def get_color_scheme(cls, scheme='primary'):
        """獲取指定的顏色方案"""
        return cls.COLORS.get(scheme, cls.COLORS['primary'])
    
    @classmethod
    def get_gradient_colors(cls, scheme='gradient_blue', n_colors=10):
        """獲取漸變顏色"""
        if scheme in cls.COLORS and hasattr(cls.COLORS[scheme], 'colors'):
            return [cls.COLORS[scheme](i/n_colors) for i in range(n_colors)]
        return cls.get_color_scheme('primary')
    
    @classmethod
    def get_figure_size(cls, chart_type='main_comparison'):
        """獲取指定圖表類型的尺寸"""
        return cls.FIGURE_SIZES.get(chart_type, (12, 8))
    
    @classmethod
    def get_font_size(cls, element='title'):
        """獲取指定元素的字體大小"""
        return cls.FONT_SIZES.get(element, 12)
    
    @classmethod
    def get_theme_style(cls, theme='professional'):
        """獲取主題樣式"""
        return cls.THEMES.get(theme, cls.THEMES['professional'])
    
    @classmethod
    def apply_modern_style(cls, ax, title="", theme='professional'):
        """應用現代化樣式到軸"""
        theme_style = cls.get_theme_style(theme)
        
        # 設置背景色
        ax.set_facecolor(theme_style['background'])
        
        # 設置標題
        if title:
            ax.set_title(title, color=theme_style['text_color'], 
                        fontsize=cls.get_font_size('subtitle'), 
                        fontweight='bold', pad=20)
        
        # 設置網格
        ax.grid(True, alpha=cls.CHART_STYLE['grid_alpha'], 
               color=theme_style['grid_color'], linestyle='--')
        
        # 設置軸顏色
        ax.tick_params(colors=theme_style['text_color'])
        ax.xaxis.label.set_color(theme_style['text_color'])
        ax.yaxis.label.set_color(theme_style['text_color'])
        
        return ax
    
    @classmethod
    def add_shadow_effect(cls, ax, elements):
        """為圖表元素添加陰影效果"""
        for element in elements:
            if hasattr(element, 'set_path_effects'):
                from matplotlib.patheffects import withStroke
                element.set_path_effects([
                    withStroke(linewidth=3, foreground=cls.CHART_STYLE['shadow_color'])
                ])
        return ax
    
    @classmethod
    def create_gradient_background(cls, ax, colors=['#FFFFFF', '#F5F5F5']):
        """創建漸變背景"""
        gradient = np.linspace(0, 1, 256).reshape(256, -1)
        gradient = np.vstack((gradient, gradient))
        
        ax.imshow(gradient, extent=ax.get_xlim() + ax.get_ylim(), 
                 aspect='auto', cmap=LinearSegmentedColormap.from_list('bg', colors),
                 alpha=0.3, zorder=0)
        return ax
