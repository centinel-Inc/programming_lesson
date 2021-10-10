# 第 6 節 抽選フォームへの入力を自動化しよう

## 完成形

```sh
git clone https://github.com/centinel-jp/programming_lesson.git
cd programming_lesson/chapter1/section6/
python3 section6.py
```

## 目的

主に2つあります。

1. 2~4節で学んだ知識をもとに実際に目に見える形の成果物を作り、この動画を見て学んでいる皆さんのモチベーションを上げること
2. 成果物を増やすことで、それが新たなプログラムを作るための足掛かりにでき、さらにスキルを伸ばすことができるという良い流れを作る

## 学び方

複数回動画を見て学んでいただくのがおすすめです。

1回目は深く考えずコピペしながら進んでいき、実際にプログラムを動かしながら楽しさや驚きを感じて欲しいです。
2回目以降は各所でやっていることの意味を考えながら、自分で改造したりして理解を深めることでより自分の知識にすることができます。

今回お見せしている資料は概要欄に貼っておりますので、ぜひご利用ください。

# 実装

## 1. フォームを準備する

抽選に Google フォームが使われていたとして話を進めます

1. フォームファイルを作成

<img src="./images/5.jpg">

2. フォームに項目を追加

<img src="./images/6.jpg">

3. 完成

<img src="./images/7.jpg">

## 2. 何を実現したいか考える

https://docs.google.com/forms/d/e/1FAIpQLSfoth2f2lJXwrpZSAwoW8iHeKOBnx4Ks7jesk_t65MLb_Otxw/viewform

1. フォームページを開く

<img src="./images/2.jpg">

2. 情報を入力する

<img src="./images/3.jpg">

3. 送信ボタンを押す

<img src="./images/4.jpg">

## 3. 実現方法を調査する

<img src="./images/1.jpg">

一番上の記事が良さそう

https://qiita.com/kota-yata/items/9d4124ec7a7dd4e3d4f0

### わかったこと

1. Selenium とかいうものを使ってフォームを送信するらしい
2. Google Form は URL にパラメータを指定することで、初期値を持った状態でフォームを開くことができるらしい
   - `usp=pp_url` を URL パラメータに付与
   - `entry.番号=回答内容` を URL パラメータに付与

## 4. パラメータ付きのフォームをブラウザで開いてみる

1. フォーム中身を Chrome の開発者ツールを使って覗き、 `entry.番号` の規則性を調べる

```
開発者ツールの開き方

Mac -> CMD + Opt + i
Windows -> Ctrl + Shift + i
```

2. 結果

<img src="./images/8.jpg">

3. まとめた

```
entry.1029139045 -> 氏名
entry.387916820 -> メールアドレス
entry.1239014792 -> 電話番号
entry.1382078040 -> 住所
entry.731826105_year -> 生年月日の年
entry.731826105_month -> 生年月日の月
entry.731826105_day -> 生年月日の日
```

4. 3 を URL に反映してフォームを開いて

フォームの URL とパラメータの間に`?`を入れ、それからは`&`でパラメータを区切っていく

まずは試しに氏名だけ

https://docs.google.com/forms/d/e/1FAIpQLSfoth2f2lJXwrpZSAwoW8iHeKOBnx4Ks7jesk_t65MLb_Otxw/viewform?usp=pp_url&entry.1029139045=URLアクセステスト名

<img src="./images/9.jpg">

では全部入り

https://docs.google.com/forms/d/e/1FAIpQLSfoth2f2lJXwrpZSAwoW8iHeKOBnx4Ks7jesk_t65MLb_Otxw/viewform?usp=pp_url&entry.1029139045=URLアクセステスト名&entry.387916820=test@gmail.com&entry.1239014792=0000-0000-0000&entry.1382078040=TEST prefecture&entry.731826105_year=1996&entry.731826105_month=7&entry.731826105_day=17

## 5. 4 でできた URL をプログラムから開く

```
pip3 install selenium
pip3 install pandas
```

```python
from selenium import webdriver
import time

# フォームのURLを変数で保持する
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfoth2f2lJXwrpZSAwoW8iHeKOBnx4Ks7jesk_t65MLb_Otxw/viewform?usp=pp_url&entry.1029139045=URLアクセステスト名&entry.387916820=test@gmail.com&entry.1239014792=0000-0000-0000&entry.1382078040=TEST prefecture&entry.731826105_year=1996&entry.731826105_month=7&entry.731826105_day=17';

# ブラウザを操作するためのインスタンスを生成
driver = webdriver.Chrome()

# ブラウザでフォームを開く
driver.get(form_url)

# 3秒間待つ
# わかりやすくするため
time.sleep(3)

# 本プログラムで起動したブラウザのタブを閉じる
driver.close()

# 全てのタブを閉じてブラウザを終了させる
driver.quit()
```

## 6. 送信ボタンをプログラムから押す

### Selenium でボタンを押させるためには、ボタンの特徴を教えてあげる必要がある

- class
- id
- [xpath](https://www.octoparse.jp/blog/xpath-introduction/) 👈 今回これを利用する

### 開発者ツールから xpath をコピー

<img src="./images/10.jpg">

### 実際にプログラムから押す

```python
from selenium import webdriver
import time

# フォームのURLを変数で保持する
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfoth2f2lJXwrpZSAwoW8iHeKOBnx4Ks7jesk_t65MLb_Otxw/viewform?usp=pp_url&entry.1029139045=URLアクセステスト名&entry.387916820=test@gmail.com&entry.1239014792=0000-0000-0000&entry.1382078040=TEST prefecture&entry.731826105_year=1996&entry.731826105_month=7&entry.731826105_day=17';

# ブラウザを操作するためのインスタンスを生成
driver = webdriver.Chrome()

# ブラウザでフォームを開く
driver.get(form_url)

# 1秒間待つ
# わかりやすくするため
time.sleep(1)

# ボタンを押して送信する
path = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div' # コピーしたボタンのxpathを貼り付ける
driver.find_element_by_xpath(path).click()

# 3秒間待つ
time.sleep(3)

# 本プログラムで起動したブラウザのタブを閉じる
driver.close()

# 全てのタブを閉じてブラウザを終了させる
driver.quit()
```

# 番外編 使いやすくしよう

## 7. ファイルからデータを読み込む

以下のようなデータを CSV 形式で用意します
|氏名|メールアドレス|電話番号|住所|年|月|日|
|:----|:----|:----|:----|:----|:----|:----|
|テストタロウ 0|test0@gmail.com|0800000000|東京都|1990|1|10|
|テストタロウ 1|test1@gmail.com|08011111111|神奈川県|1991|1|11|

### CSV を読み込む

```python
import pandas as pd

# CSVを読み込む
df = pd.read_csv('./data.csv', dtype=str)

# コンソールにプリントして確認してみる
print(df)
```

### 読み取った CSV を一列ごとに取り出して値を表示してみる

```python
import pandas as pd

# CSVを読み込む
# 型のヒントを書くことで補完が効くようになる
df: pd.DataFrame = pd.read_csv('./data.csv', dtype=str)

# 一列ごとに処理できる
for index, row in df.iterrows():
    # どのような値が入っているか確認してみる
    # print(index)

    # 上の確認ができたら、下のコメントを外してこちらも確認してみる
    # print(row)

    # 値にアクセスしてみる
    # 以下のようにキー名を指定するとデータを取得できる
    print(row['氏名'])
    print(row['電話番号'])

    # ダブルクオーテーションでも取得できる
    # シングル・ダブルどちらでも良いのだが、どちらか一方に一貫した方が変な意図を感じさせず読みやすいと思う
    print(row["氏名"])
    print(row["電話番号"])
```

## 8. 読み取った CSV を URL パラメータの文字列に変換する準備を行う

読み取ったデータを辞書型の変数に格納し、その変数を URL パラメータに変換したい。
そのため辞書型の変数を URL パラメータへ変換する関数を実装する。

```python
# パラメータを保持する辞書型の変数
# keyにurlパラメータ名、valueに入る要素名を入れる（valueはわかりやすければ適当な値でも大丈夫）
url_param_dict = {
    'usp': 'pp_url',
    'entry.1029139045': '氏名',
    'entry.387916820': 'メールアドレス',
    'entry.1239014792': '電話番号',
    'entry.1382078040': '住所',
    'entry.731826105_year': '年',
    'entry.731826105_month': '月',
    'entry.731826105_day': '日',
}

def convertDictToUrlParams(params):
    params_string = ''
    for key, value in params.items():
        params_string += '&' + key + "=" + value

    # 最初の「&」を削除している。URLパラメータの最初は「&」ではないため。
    # ここでは「スライス」という機能を使い、"1インデックス"以降の文字を取得している
    # インデックスは0始まりなので、2文字目以降を取得することになる
    return params_string[1:]

# 期待している値
expect = 'usp=pp_url&entry.1029139045=氏名&entry.387916820=メールアドレス&entry.1239014792=電話番号&entry.1382078040=住所&entry.731826105_year=年&entry.731826105_month=月&entry.731826105_day=日'
actual = convertDictToUrlParams(url_param_dict)

# 期待する値になっているかテストを行う
if expect == actual:
    print('🎉期待する値です🎉')
else:
    print'🥲期待する文字列ではありません🥲')
```

## 9. 読み取った CSV を URL パラメータの文字列に変換する

```python
import pandas as pd

# パラメータを保持する辞書型の変数
# keyにurlパラメータ名、valueに入る要素名を入れる（valueはわかりやすければ適当な値でも大丈夫）
url_param_dict = {
    'usp': 'pp_url',
    'entry.1029139045': '氏名',
    'entry.387916820': 'メールアドレス',
    'entry.1239014792': '電話番号',
    'entry.1382078040': '住所',
    'entry.731826105_year': '年',
    'entry.731826105_month': '月',
    'entry.731826105_day': '日',
}

def convertDictToUrlParams(params):
    params_string = ''
    for key, value in params.items():
        params_string += '&' + key + "=" + value

    # 最初の「&」を削除している。URLパラメータの最初は「&」ではないため。
    # ここでは「スライス」という機能を使い、"1インデックス"以降の文字を取得している
    # インデックスは0始まりなので、2文字目以降を取得することになる
    return params_string[1:]

# CSVを読み込む
# 型のヒントを書くことでVS Codeにて補完が効くようになる
df: pd.DataFrame = pd.read_csv('./data.csv', dtype=str)

for index, row in df.iterrows():
    # CSVデータを入れるため、辞書型の変数をコピーして用意する
    # url_param_dictに副作用を及ぼしたくないので、値をコピーして一時的な変数を用意する
    temp_url_param_dict = url_param_dict.copy()

    # 辞書型のkeyにvalueを代入したい場合は、以下のように行います。
    temp_url_param_dict['entry.1029139045'] = row['氏名']

    # 変数の中身をこまめにprintして確認すると、状況を把握しやすく効率よく開発できるのでおすすめです
    # 以下のように文字列に変数を埋め込んで、printすることができます
    # 他の言語でも方法は違いますが、可能ですので調べてみてください
    print('url_param_dictの氏名は「{}」で、temp_url_param_dictの氏名は「{}」です。'.format(url_param_dict['entry.1029139045'], temp_url_param_dict['entry.1029139045']))

    temp_url_param_dict['entry.1029139045'] = row['メールアドレス']
    temp_url_param_dict['entry.387916820'] = row['電話番号']
    temp_url_param_dict['entry.1239014792'] = row['住所']
    temp_url_param_dict['entry.731826105_year'] = row['年']
    temp_url_param_dict['entry.731826105_month'] = row['月']
    temp_url_param_dict['entry.731826105_day'] = row['日']

    # URLパラメータの文字列を組み立てる
    url_params = convertDictToUrlParams(temp_url_param_dict)
    print("urlParams: {}".format(url_params))
```

## 10. 今まで作ってきたものを組み合わせて、CSV データをフォームへ投稿する機能を完成させる

```python
import pandas as pd
from selenium import webdriver
import time

# GoogleフォームのURL
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfoth2f2lJXwrpZSAwoW8iHeKOBnx4Ks7jesk_t65MLb_Otxw/viewform'

# パラメータを保持する辞書型の変数
# keyにurlパラメータ名、valueに入る要素名を入れる（valueはわかりやすければ適当な値でも大丈夫）
url_param_dict = {
    'usp': 'pp_url',
    'entry.1029139045': '氏名',
    'entry.387916820': 'メールアドレス',
    'entry.1239014792': '電話番号',
    'entry.1382078040': '住所',
    'entry.731826105_year': '年',
    'entry.731826105_month': '月',
    'entry.731826105_day': '日',
}

def convertDictToUrlParams(params):
    params_string = ''
    for key, value in params.items():
        params_string += '&' + key + "=" + value

    # 最初の「&」を削除している。URLパラメータの最初は「&」ではないため。
    # ここでは「スライス」という機能を使い、"1インデックス"以降の文字を取得している
    # インデックスは0始まりなので、2文字目以降を取得することになる
    return params_string[1:]

# CSVを読み込む
# 型のヒントを書くことでVS Codeにて補完が効くようになる
df: pd.DataFrame = pd.read_csv('./data.csv', dtype=str)

for index, row in df.iterrows():
    # CSVデータを入れるため、辞書型の変数をコピーして用意する
    # urlParamDictに副作用を及ぼしたくないので、値をコピーして一時的な変数を用意する
    temp_url_param_dict = url_param_dict.copy()

    # 辞書型のkeyにvalueを代入したい場合は、以下のように行います。
    temp_url_param_dict['entry.1029139045'] = row['氏名']
    temp_url_param_dict['entry.1029139045'] = row['メールアドレス']
    temp_url_param_dict['entry.387916820'] = row['電話番号']
    temp_url_param_dict['entry.1239014792'] = row['住所']
    temp_url_param_dict['entry.731826105_year'] = row['年']
    temp_url_param_dict['entry.731826105_month'] = row['月']
    temp_url_param_dict['entry.731826105_day'] = row['日']

    # URLパラメータの文字列を組み立てる
    urlParams = convertDictToUrlParams(temp_url_param_dict)

    form_url_with_params = form_url + "?" + urlParams;

    # ブラウザを操作するためのインスタンスを生成
    driver = webdriver.Chrome()

    # ブラウザでフォームを開く
    driver.get(form_url_with_params)

    # 1秒間待つ
    time.sleep(1)

    # ボタンを押して送信する
    path = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'
    driver.find_element_by_xpath(path).click()

    # 3秒間待つ
    time.sleep(3)

    # 本プログラムで起動したブラウザのタブを閉じる
    driver.close()

    # 全てのタブを閉じてブラウザを終了させる
    driver.quit()
```
