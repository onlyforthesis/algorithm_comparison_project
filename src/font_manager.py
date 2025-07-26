# -*- coding: utf-8 -*-
"""
字體管理模組
負責處理中文字體設定和字體相關功能
"""

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt


class FontManager:
    """字體管理器"""
    
    def __init__(self):
        self.zh_font = self._setup_chinese_font()
        self._configure_matplotlib()
    
    def _setup_chinese_font(self):
        """設定中文字型"""
        try:
            # 嘗試使用系統中文字型
            font_paths = [
                'C:\\Windows\\Fonts\\kaiu.ttf',        # 標楷體
                'C:\\Windows\\Fonts\\msyhl.ttf',       # 微軟雅黑
                'C:\\Windows\\Fonts\\msjh.ttc',        # 微軟正黑體
                'C:/Windows/Fonts/simsun.ttc',         # 新細明體
                'C:/Windows/Fonts/mingliu.ttc'         # 細明體
            ]
            
            for font_path in font_paths:
                try:
                    zh_font = fm.FontProperties(fname=font_path)
                    return zh_font
                except:
                    continue
                    
            # 使用預設字型
            return fm.FontProperties()
        except:
            return fm.FontProperties()
    
    def _configure_matplotlib(self):
        """配置 matplotlib 中文顯示"""
        plt.rcParams['font.sans-serif'] = [
            'Microsoft JhengHei', 'SimHei', 'Arial Unicode MS'
        ]
        plt.rcParams['axes.unicode_minus'] = False
    
    def get_font(self):
        """獲取中文字體"""
        return self.zh_font
    
    @staticmethod
    def create_font_with_size(size=12, weight='normal'):
        """創建指定大小和重量的字體屬性"""
        return {'fontsize': size, 'fontweight': weight}
