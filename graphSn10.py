import pandas as pd
import matplotlib.pyplot as plt

# Excelファイルの読み込み
df = pd.read_excel('Sn単体_2024_09_26.xlsx', sheet_name='Sn単体_2024_09_26')

# データを取得（例えば、1列目をX軸、2列目から4列目をY軸として使用）
x_data = df.iloc[:, 0]  # 1列目（X軸）
y_data1 = df.iloc[:, 1]  # 2列目（Y1軸）
y_data2 = df.iloc[:, 2]  # 3列目（Y2軸）
y_data3 = df.iloc[:, 3]  # 4列目（Y3軸）

# グラフ化
plt.figure(figsize=(10, 6))
plt.plot(x_data, y_data1, marker='o', linestyle='-', label='Y1')
plt.plot(x_data, y_data2, marker='x', linestyle='--', label='Y2')
plt.plot(x_data, y_data3, marker='s', linestyle='-.', label='Y3')
plt.xlabel('time[s]')
plt.ylabel('temperature[°C]')
plt.title('Graph with Multiple Y Values for Single X Value')
plt.legend()  # 凡例を追加
plt.grid(True)
# PDFファイルに保存
plt.savefig("graph_output.pdf", format="pdf")
plt.show()