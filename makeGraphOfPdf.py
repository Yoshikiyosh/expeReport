import pandas as pd
import matplotlib.pyplot as plt

# Excelファイルの読み込み
df = pd.read_excel('Zn単体_菊池_貝良塚.xlsx', sheet_name='Zn単体_菊池_貝良塚')

# データを取得（例えば、1列目をX軸、2列目から4列目をY軸として使用）
x_data = df.iloc[:, 0]  # 1列目（X軸）
y_data1 = df.iloc[:, 1]  # 2列目（Y1軸）
y_data2 = df.iloc[:, 2]  # 3列目（Y2軸）
y_data3 = df.iloc[:, 3]  # 4列目（Y3軸）

# グラフ化
plt.figure(figsize=(10, 6))
plt.plot(x_data, y_data1, marker='o', linestyle='-', label='inside a furnace')
plt.plot(x_data, y_data2, marker='x', linestyle='--', label='alloy')
plt.plot(x_data, y_data3, marker='s', linestyle='-.')
plt.xlabel('time[s]')
plt.ylabel('temperature[°C]')
plt.title('State diagram when Zn is alone')
plt.legend()  # 凡例を追加
plt.grid(True)
# PDFファイルに保存
plt.savefig("0Sn.pdf", format="pdf")
plt.show()