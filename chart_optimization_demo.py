# -*- coding: utf-8 -*-
"""
圖表優化演示腳本
展示不使用複雜依賴的基本圖表優化功能
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path

# 設置中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def create_sample_data():
    """創建示例數據"""
    return pd.DataFrame({
        '演算法': [
            'ARIMA', '指數平滑法', 'GARCH', 'SVM', '隨機森林',
            'XGBoost', 'RNN/LSTM', 'CNN', 'Transformer', '基因演算法'
        ],
        '預測精度': [3, 2, 3, 4, 5, 5, 5, 4, 5, 4],
        '計算複雜度': [2, 1, 3, 3, 5, 5, 6, 5, 6, 5],
        '算力需求': [2, 1, 3, 4, 5, 6, 6, 6, 6, 4],
        '記憶體需求': [2, 1, 2, 3, 4, 5, 6, 5, 6, 3]
    })

def create_enhanced_scatter_plot(df, output_dir):
    """創建增強版散點圖"""
    fig, ax = plt.subplots(figsize=(12, 8))
    
    x = df['計算複雜度']
    y = df['算力需求']
    sizes = df['記憶體需求'] * 100
    colors = plt.cm.viridis(np.linspace(0, 1, len(df)))
    
    # 創建散點圖
    scatter = ax.scatter(x, y, s=sizes, c=colors, alpha=0.7, 
                        edgecolors='white', linewidth=2)
    
    # 添加陰影效果
    shadow_scatter = ax.scatter([xi-0.1 for xi in x], [yi-0.1 for yi in y], 
                               s=[s*0.8 for s in sizes], c='gray', alpha=0.3, zorder=0)
    
    # 添加標籤
    for i, (xi, yi) in enumerate(zip(x, y)):
        ax.annotate(str(i+1), (xi, yi), ha='center', va='center',
                   fontweight='bold', fontsize=12, color='white')
    
    # 美化設置
    ax.set_xlabel('計算複雜度', fontsize=14, fontweight='bold')
    ax.set_ylabel('算力需求', fontsize=14, fontweight='bold')
    ax.set_title('🎯 演算法複雜度比較 (增強版)', fontsize=16, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_facecolor('#f8f9fa')
    
    # 設置軸範圍
    ax.set_xlim(0.5, 6.5)
    ax.set_ylim(0.5, 6.5)
    
    plt.tight_layout()
    output_path = output_dir / "enhanced_scatter_demo.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()
    print(f"✅ 增強版散點圖已保存: {output_path}")

def create_gradient_bar_chart(df, output_dir):
    """創建漸變柱狀圖"""
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # 準備數據
    memory_values = df['記憶體需求']
    labels = [str(i+1) for i in range(len(df))]
    
    # 創建漸變顏色
    colors = plt.cm.plasma(np.linspace(0, 1, len(df)))
    
    # 創建柱狀圖
    bars = ax.bar(range(len(df)), memory_values, color=colors, 
                 alpha=0.8, edgecolor='white', linewidth=2)
    
    # 添加發光效果
    for i, bar in enumerate(bars):
        height = bar.get_height()
        # 添加頂部高光
        glow_height = height * 0.1
        glow_rect = plt.Rectangle((bar.get_x(), height-glow_height), 
                                 bar.get_width(), glow_height,
                                 facecolor='white', alpha=0.4, zorder=10)
        ax.add_patch(glow_rect)
        
        # 添加數值標籤
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1, 
               f'{height}', ha='center', va='bottom',
               fontweight='bold', fontsize=11)
    
    # 美化設置
    ax.set_xlabel('演算法編號', fontsize=14, fontweight='bold')
    ax.set_ylabel('記憶體需求等級', fontsize=14, fontweight='bold')
    ax.set_title('💾 記憶體需求比較 (漸變效果)', fontsize=16, fontweight='bold', pad=20)
    ax.set_xticks(range(len(df)))
    ax.set_xticklabels(labels)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_facecolor('#f8f9fa')
    
    plt.tight_layout()
    output_path = output_dir / "gradient_bar_demo.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()
    print(f"✅ 漸變柱狀圖已保存: {output_path}")

def create_modern_radar_chart(df, output_dir):
    """創建現代化雷達圖"""
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='polar')
    
    # 準備數據
    categories = ['計算複雜度', '算力需求', '記憶體需求', '預測精度']
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
    
    # 繪製前5個演算法
    for i in range(min(5, len(df))):
        values = [
            df.iloc[i]['計算複雜度'],
            df.iloc[i]['算力需求'],
            df.iloc[i]['記憶體需求'],
            df.iloc[i]['預測精度']
        ]
        values += values[:1]
        
        # 繪製線條和填充
        ax.plot(angles, values, 'o-', linewidth=3, label=f'演算法{i+1}', 
               color=colors[i], markersize=8)
        ax.fill(angles, values, alpha=0.25, color=colors[i])
        
        # 添加發光效果
        ax.plot(angles, values, 'o-', linewidth=6, alpha=0.2, color=colors[i])
    
    # 設置標籤和樣式
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=12, fontweight='bold')
    ax.set_ylim(0, 6)
    ax.set_title('⭐ 多維度演算法比較雷達圖', fontsize=16, fontweight='bold', pad=30)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0), fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_facecolor('#f8f9fa')
    
    plt.tight_layout()
    output_path = output_dir / "modern_radar_demo.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()
    print(f"✅ 現代化雷達圖已保存: {output_path}")

def create_comparison_dashboard(df, output_dir):
    """創建比較儀表板"""
    fig = plt.figure(figsize=(20, 12))
    fig.suptitle('🚀 演算法比較分析儀表板 - 演示版', fontsize=20, fontweight='bold', y=0.95)
    
    # 子圖1: 散點圖
    ax1 = plt.subplot(2, 3, 1)
    x = df['計算複雜度']
    y = df['算力需求']
    colors = plt.cm.Set3(np.linspace(0, 1, len(df)))
    scatter = ax1.scatter(x, y, c=colors, s=200, alpha=0.7, edgecolors='white', linewidth=2)
    for i, (xi, yi) in enumerate(zip(x, y)):
        ax1.annotate(str(i+1), (xi, yi), ha='center', va='center', fontweight='bold')
    ax1.set_title('計算複雜度 vs 算力需求', fontweight='bold')
    ax1.set_xlabel('計算複雜度')
    ax1.set_ylabel('算力需求')
    ax1.grid(True, alpha=0.3)
    
    # 子圖2: 柱狀圖
    ax2 = plt.subplot(2, 3, 2)
    bars = ax2.bar(range(len(df)), df['記憶體需求'], color=colors, alpha=0.7, edgecolor='white')
    ax2.set_title('記憶體需求比較', fontweight='bold')
    ax2.set_xlabel('演算法編號')
    ax2.set_ylabel('記憶體需求')
    ax2.set_xticks(range(len(df)))
    ax2.set_xticklabels([str(i+1) for i in range(len(df))])
    ax2.grid(axis='y', alpha=0.3)
    
    # 子圖3: 線圖
    ax3 = plt.subplot(2, 3, 3)
    ax3.plot(range(len(df)), df['預測精度'], marker='o', linewidth=3, markersize=8, color='red')
    ax3.fill_between(range(len(df)), df['預測精度'], alpha=0.3, color='red')
    ax3.set_title('預測精度變化', fontweight='bold')
    ax3.set_xlabel('演算法編號')
    ax3.set_ylabel('預測精度')
    ax3.grid(True, alpha=0.3)
    
    # 子圖4-6: 個別分析
    metrics = ['計算複雜度', '算力需求', '記憶體需求']
    for i, metric in enumerate(metrics):
        ax = plt.subplot(2, 3, 4+i)
        bars = ax.barh(range(len(df)), df[metric], color=colors, alpha=0.7)
        ax.set_title(f'{metric}分布', fontweight='bold')
        ax.set_xlabel(metric)
        ax.set_ylabel('演算法')
        ax.set_yticks(range(len(df)))
        ax.set_yticklabels([str(i+1) for i in range(len(df))])
        ax.grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    output_path = output_dir / "comparison_dashboard_demo.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()
    print(f"✅ 比較儀表板已保存: {output_path}")

def main():
    """主函數"""
    print("="*60)
    print("🎨 圖表優化演示程式")
    print("="*60)
    
    # 創建輸出目錄
    output_dir = Path("demo_output")
    output_dir.mkdir(exist_ok=True)
    
    # 創建示例數據
    df = create_sample_data()
    print(f"📊 已載入 {len(df)} 個演算法的數據")
    
    print("\n🎯 正在生成增強版圖表...")
    
    try:
        # 1. 增強版散點圖
        create_enhanced_scatter_plot(df, output_dir)
        
        # 2. 漸變柱狀圖
        create_gradient_bar_chart(df, output_dir)
        
        # 3. 現代化雷達圖
        create_modern_radar_chart(df, output_dir)
        
        # 4. 比較儀表板
        create_comparison_dashboard(df, output_dir)
        
        print("\n" + "="*60)
        print("🎉 圖表優化演示完成！")
        print("="*60)
        print(f"📁 所有圖表已保存到: {output_dir.absolute()}")
        print("\n✨ 演示特色:")
        print("   • 3D陰影效果")
        print("   • 漸變色彩方案")
        print("   • 發光和高光效果")
        print("   • 現代化雷達圖")
        print("   • 多子圖儀表板")
        print("   • 高解析度輸出 (300 DPI)")
        
    except Exception as e:
        print(f"❌ 圖表生成失敗: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
