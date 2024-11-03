import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table

# Excelファイルを読み込む
file_path = '状態図.xlsx'  # エクセルファイルのパスを指定
sheet_name = 'Sheet1'  # シート名を指定
df = pd.read_excel(file_path, sheet_name=sheet_name)

# 指定した行と列を選択
selected_data = df.loc[0:, ['ratio of Sn','solid phase line', 'liquid phase line']]  # 行と列を指定

# プロット領域を作成
fig, ax = plt.subplots(figsize=(8, 6))  # サイズを適宜変更可能
ax.axis('off')  # 軸をオフにする

# テーブルをプロット
table(ax, selected_data, loc='center', cellLoc='center', colWidths=[0.2]*len(selected_data.columns))

# PNGファイルとして保存
plt.savefig('dataOfStateGraph.png', format='png', dpi=300)

 
