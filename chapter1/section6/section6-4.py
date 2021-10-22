import pandas as pd

# CSVを読み込む
# 型のヒントを書くことでVS Codeにて補完が効くようになる
df: pd.DataFrame = pd.read_csv('./data.csv', dtype=str)

for index, row in df.iterrows():
    # 一行プリント
    print(row.to_string())

    # 「氏名」カラムのみ取得
    print('氏名: {}'.format(row['氏名']))

    # 「メールアドレス」カラムのみ取得
    print('メールアドレス: {}'.format(row['メールアドレス']))

    # 以下同様
    print('電話番号: {}'.format(row['電話番号']))
    print('住所: {}'.format(row['住所']))
    print('生年月日: {}'.format(row['生年月日']))
