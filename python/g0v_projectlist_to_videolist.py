import pandas as pd
import sys, requests, io

# 取得命令列參數
# 讀取 Google Spreadsheet 網址
# example url = "https://docs.google.com/spreadsheets/d/[Google Spreadsheet ID]"
url = sys.argv[1]
order = sys.argv[2]
name = sys.argv[3]

# 處裡url並加上export?format=xlsx後綴
url = url + '/export?format=xlsx'

# 使用 requests 模組，下載 Google Spreadsheet 資料
response = requests.get(url)

# 建立 Pandas DataFrame
df = pd.read_excel(io.BytesIO(response.content))

# 若下載為檔案，讀取 Excel 資料檔 (phased out)
# df = pd.read_excel(file_name)

# 確認欄位名稱
# print(df.columns)

# 刪除所有含有 NaN 的行
df = df.dropna(subset=['Unnamed: 6'])

# 合併兩個欄位，並將每一筆資料插入共同的標題

df['Unnamed: 6'] = df['Unnamed: 6'].astype(str)
df['Unnamed: 3'] = df['Unnamed: 3'].astype(str)
df['Unnamed: 6'] = 'g0v tw hackath' + order + 'n — 提案 — ' + df['Unnamed: 6'] + ' ／ ' + df['Unnamed: 3'] + ' — ' + name

# 將欄位重新排列只留下一組
df = df[['Unnamed: 6']]

# 將資料寫入新的 text 檔案
df.to_csv('output.txt', sep='\t', header=False, index=False, encoding='utf-8')
print('存入 txt 檔完成')
