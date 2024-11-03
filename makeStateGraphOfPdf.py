
import pandas as pd
import matplotlib.pyplot as plt

# Excelファイルの読み込み
df = pd.read_excel('状態図.xlsx', sheet_name='Sheet1')

# データを取得（例えば、1列目をX軸、2列目から4列目をY軸として使用）
x_data = df.iloc[1:, 0]  # 1列目（X軸）
y_data1 = df.iloc[1:, 1]  # 2列目（Y1軸）
y_data2 = df.iloc[1:, 2]  # 3列目（Y2軸）
#y_data3 = df.iloc[:, 3]  # 4列目（Y3軸）

# グラフ化
plt.figure(figsize=(10, 6))
plt.plot(x_data, y_data1, marker='o', linestyle='-', label='solid phase line')
plt.plot(x_data, y_data2, marker='x', linestyle='--', label='liquid phase line')
#plt.plot(x_data, y_data3, marker='s', linestyle='-.')
plt.xlabel('Sn ratio (against Zn)')
plt.ylabel('Temperature in furnace[°C]')
plt.title('State diagram with Solid phase line and liquid phase line')
plt.legend()  # 凡例を追加
plt.grid(True)
# PDFファイルに保存
plt.savefig("stateGraph.pdf", format="pdf")
plt.show()
'''
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np

# Excelファイルの読み込み
df = pd.read_excel('状態図.xlsx', sheet_name='Sheet1')

# データを取得（例えば、1列目をX軸、2列目から4列目をY軸として使用）
x_data = df.iloc[1:, 0].values  # 1列目（X軸）
y_data1 = df.iloc[1:, 1].values  # 2列目（Y1軸）
y_data2 = df.iloc[1:, 2].values  # 3列目（Y2軸）

# NaNや無限大の値を除外（y_data1用）
mask1 = ~np.isnan(x_data) & ~np.isnan(y_data1) & ~np.isinf(x_data) & ~np.isinf(y_data1)
x_data_clean1 = x_data[mask1]
y_data1_clean = y_data1[mask1]

# NaNや無限大の値を除外（y_data2用）
mask2 = ~np.isnan(x_data) & ~np.isnan(y_data2) & ~np.isinf(x_data) & ~np.isinf(y_data2)
x_data_clean2 = x_data[mask2]
y_data2_clean = y_data2[mask2]

# 補間のために細かいX軸の値を生成（y_data1とy_data2でX軸の範囲を統一）
x_smooth = np.linspace(min(x_data_clean1.min(), x_data_clean2.min()), max(x_data_clean1.max(), x_data_clean2.max()), 300)

# 補間を行って滑らかな曲線を作成
spl1 = make_interp_spline(x_data_clean1, y_data1_clean, k=3)  # k=3は3次スプライン補間
y_smooth1 = spl1(x_smooth)
spl2 = make_interp_spline(x_data_clean2, y_data2_clean, k=3)
y_smooth2 = spl2(x_smooth)

# グラフ化
plt.figure(figsize=(10, 6))
plt.plot(x_smooth, y_smooth1, label='inside a furnace', linestyle='-', color='blue')
plt.plot(x_smooth, y_smooth2, label='alloy', linestyle='--', color='orange')
plt.xlabel('time[s]')
plt.ylabel('temperature[°C]')
plt.title('State diagram when Zn is alone')
plt.legend()  # 凡例を追加
plt.grid(True)

# PDFファイルに保存
# plt.savefig("stateGraph.pdf", format="pdf")
plt.show()
'''
