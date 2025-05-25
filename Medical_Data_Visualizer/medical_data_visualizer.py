import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)
# 3
df['cholesterol'] = (df['cholesterol'] > 1)
df['gluc'] = (df['gluc'] > 1)
df = df.astype({'cholesterol':int, 'gluc':int})

# 4
def draw_cat_plot():
    # 5
    data = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    df_cat_melted = pd.melt(df, id_vars='cardio', value_vars=data)
    df_cat_melted['total'] = 1
    
    # 6
    df_count = df_cat_melted.groupby(['cardio', 'variable', 'value'], as_index=False).count()

    # 7
    chart = sns.catplot(x='variable', y='total', hue='value', data=df_count, col='cardio', kind='bar')

    # 8
    fig = chart.fig

    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    df_heat = df[ df['ap_lo'] <= df['ap_hi'] ]
    df_heat = df_heat[ (df['height'] >= df['height'].quantile(0.025)) & 
                       (df['height'] <= df['height'].quantile(0.975)) ]
    df_heat = df_heat[ (df['weight'] >= df['weight'].quantile(0.025)) & 
                       (df['weight'] <= df['weight'].quantile(0.975)) ]

    # 12
    corr = df_heat.corr(numeric_only=True).round(1)

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))
    colormap = sns.color_palette("icefire", as_cmap=True)

    # 14
    fig, ax = plt.subplots(figsize=(12, 9))

    # 15
    ax = sns.heatmap(corr, mask=mask, cmap=colormap, annot=True, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

    # 16
    fig.savefig('heatmap.png')
    return fig
