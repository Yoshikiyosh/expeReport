from pdf2image import convert_from_path

# Popplerのパス（Windowsのみ）
poppler_path = r'C:\Users\yoshi\Downloads\Release-24.08.0-0\poppler-24.08.0\Library\bin'

# コマンドラインから数値を入力
num = input("Enter the number for the file name (e.g., 9, 8.5, 7): ")

# PDFファイル名と出力画像名を設定
pdf_file = f'{num}Sn.pdf'
output_image = f'{num}Sn.png'

# PDFから画像に変換
images = convert_from_path(pdf_file, poppler_path=poppler_path)

# 1ページ目だけをPNGとして保存
images[0].save(output_image, 'PNG')
print(f"Converted {pdf_file} to {output_image}")

 
