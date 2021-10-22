# 第 6 節 抽選フォームへの入力を自動化しよう

## 目的

主に 2 つあります。

1. 2~4 節で学んだ知識をもとに実際に目に見える形の成果物を作り、この動画を見て学んでいる皆さんのモチベーションを上げること
2. 成果物を増やすことで、それが新たなプログラムを作るための足掛かりにでき、さらにスキルを伸ばすことができるという良い流れを作る

## 学び方

複数回動画を見て学んでいただくのがおすすめです。

1 回目は深く考えずコピペしながら進んでいき、実際にプログラムを動かしながら楽しさや驚きを感じて欲しいです。
2 回目以降は各所でやっていることの意味を考えながら、自分で改造したりして理解を深めることでより自分の知識にすることができます。

今回お見せしている資料は概要欄に貼っておりますので、ぜひご利用ください。

### 完成形

```sh
git clone https://github.com/centinel-jp/programming_lesson.git
cd programming_lesson/chapter1/section6/
python3 section6.py
```

### 今回のターゲット

Google Form を使用します。

フォームを作成するのが面倒な方は、以下にフォームを用意してありますのでそれを利用していただければと思います。
[リンク](https://docs.google.com/forms/d/e/1FAIpQLSfoth2f2lJXwrpZSAwoW8iHeKOBnx4Ks7jesk_t65MLb_Otxw/viewform)

# 実装前の準備

## 1. 何を実現したいか考える

1. フォームページを開く

https://docs.google.com/forms/d/e/1FAIpQLSfoth2f2lJXwrpZSAwoW8iHeKOBnx4Ks7jesk_t65MLb_Otxw/viewform

<img src="./images/2.jpg">

2. 情報を入力する

<img src="./images/3.jpg">

3. 送信ボタンを押す

<img src="./images/4.jpg">

この三つの作業をプログラムに行わせたい。

## 2. 今回使用するライブラリをインストール

```
pip3 install selenium
pip3 install pandas
```

# 実装開始

## 1. フォームの URL をプログラムで開く

### 目標

**プログラムからページを開く**

```python
from selenium import webdriver
import time

# フォームのURLを変数で保持する
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfoth2f2lJXwrpZSAwoW8iHeKOBnx4Ks7jesk_t65MLb_Otxw/viewform'

# ブラウザを操作するためのインスタンスを生成
driver = webdriver.Chrome()

# ブラウザでフォームを開く
driver.get(form_url)

# 1秒間待つ
# ページを開いたことをわかりやすくするため
time.sleep(1)

# ブラウザを閉じる
driver.close()

# メモリを解放する
driver.quit()
```

## 2. 情報を入力する

### 目標

フォームを特定し文字を入力する

#### フォームを特定する方法

特徴をもとに特定する

- class
- id
- [xpath](https://www.octoparse.jp/blog/xpath-introduction/) 👈 今回これを利用する

1. 開発者ツールを開く

   ```
    Mac -> CMD + Opt + i
    Windows -> Ctrl + Shift + i
   ```

2.フォームの xpath を抜き取る

<img src="./images/10.jpg">

#### 文字を入力する方法

以下のコードで実現可能

```python
driver.find_element_by_xpath(xpathの文字列).send_keys('入力したい内容')
```

```python
from selenium import webdriver
import time

form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfoth2f2lJXwrpZSAwoW8iHeKOBnx4Ks7jesk_t65MLb_Otxw/viewform'

driver = webdriver.Chrome()

driver.get(form_url)

time.sleep(1)

name_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
driver.find_element_by_xpath(name_input_xpath).send_keys('テスト 太郎')
print("氏名の記入に成功しました")
time.sleep(1)

mail_address_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
driver.find_element_by_xpath(mail_address_input_xpath).send_keys('test@gmail.com')
print("メールアドレスの記入に成功しました")
time.sleep(1)

telephone_number_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
driver.find_element_by_xpath(telephone_number_input_xpath).send_keys('000-0000-0000')
print("電話番号の記入に成功しました")
time.sleep(1)

address_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea'
driver.find_element_by_xpath(address_input_xpath).send_keys('東京都テスト市テスト町0-0-00')
print("住所の記入に成功しました")
time.sleep(1)

birthday_input_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'
driver.find_element_by_xpath(birthday_input_path).send_keys('19960717')
print("生年月日の記入に成功しました")
time.sleep(1)

driver.close()

driver.quit()

```

## 3. 送信ボタンを押す

### 目標

ボタンを特定し押下する

#### ボタンを特定する方法

フォームと同様にボタンの xpath を取得して利用する。

#### ボタンを押下する方法

```python
driver.find_element_by_xpath(xpathの文字列).click()
```

```python
from selenium import webdriver
import time

form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfoth2f2lJXwrpZSAwoW8iHeKOBnx4Ks7jesk_t65MLb_Otxw/viewform'

driver = webdriver.Chrome()

driver.get(form_url)

time.sleep(1)

name_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
driver.find_element_by_xpath(name_input_xpath).send_keys('テスト 太郎')
print("氏名の記入に成功しました")
time.sleep(1)

mail_address_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
driver.find_element_by_xpath(mail_address_input_xpath).send_keys('test@gmail.com')
print("メールアドレスの記入に成功しました")
time.sleep(1)

telephone_number_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
driver.find_element_by_xpath(telephone_number_input_xpath).send_keys('000-0000-0000')
print("電話番号の記入に成功しました")
time.sleep(1)

address_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea'
driver.find_element_by_xpath(address_input_xpath).send_keys('東京都テスト市テスト町0-0-00')
print("住所の記入に成功しました")
time.sleep(1)

birthday_input_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'
driver.find_element_by_xpath(birthday_input_path).send_keys('19960717')
print("生年月日の記入に成功しました")
time.sleep(1)

# ボタンを押して送信する
path = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div' # コピーしたボタンのxpathを貼り付ける
driver.find_element_by_xpath(path).click()
print("送信ボタンの押下に成功しました")

driver.close()

driver.quit()

```

# 番外編 使いやすくしよう

## 4. CSV で送信したいデータを用意して、プログラムから読み込む

### 目標

CSV データを作成し、それを Python で読み込んでプリントする

#### CSV データの作成

スクリプトと同じ階層のフォルダに`data.csv`という名前のファイルを作成し、以下のデータを書き込んで保存

```csv
氏名,メールアドレス,電話番号,住所,生年月日
テストタロウ0,test0@gmail.com,0800000000,東京都,19900110
テストタロウ1,test1@gmail.com,08011111111,神奈川県,19910111
```

#### CSV データを読み込む

以下のように pandas というライブラリで読み込む。

```python
import pandas as pd

# CSVを読み込む
# 型のヒントを書くことでVS Codeにて補完が効くようになる
df: pd.DataFrame = pd.read_csv('./data.csv', dtype=str)
```

```python
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
```

## 5. 読み込んだデータを全件送信してみよう

### 目標

3 と 4 を組み合わせて、CSV データの内容を全て送信する

```python
import pandas as pd
from selenium import webdriver
import time

# GoogleフォームのURL
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfoth2f2lJXwrpZSAwoW8iHeKOBnx4Ks7jesk_t65MLb_Otxw/viewform'

# CSVを読み込む
# 型のヒントを書くことでVS Codeにて補完が効くようになる
df: pd.DataFrame = pd.read_csv('./data.csv', dtype=str)

# 毎度スリープ時間を直接指定してると、変更するときに面倒なので変数で保持する
sleep_interval = 0.75

for index, row in df.iterrows():
    print("🚀🚀🚀 {}番目のデータの送信を開始します 🚀🚀🚀".format(index+1))
    # ブラウザを操作するためのインスタンスを生成
    driver = webdriver.Chrome()

    # ブラウザでフォームを開く
    driver.get(form_url)

    # 1秒間待つ
    # わかりやすくするため
    time.sleep(sleep_interval)

    name_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    # send_keysの引数に、CSVから取得したデータを入れる
    driver.find_element_by_xpath(name_input_xpath).send_keys(row['氏名'])
    print("氏名の記入に成功しました")
    time.sleep(sleep_interval)

    mail_address_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    driver.find_element_by_xpath(mail_address_input_xpath).send_keys(row['メールアドレス'])
    print("メールアドレスの記入に成功しました")
    time.sleep(sleep_interval)

    telephone_number_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    driver.find_element_by_xpath(telephone_number_input_xpath).send_keys(row['電話番号'])
    print("電話番号の記入に成功しました")
    time.sleep(sleep_interval)

    address_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea'
    driver.find_element_by_xpath(address_input_xpath).send_keys(row['住所'])
    print("住所の記入に成功しました")
    time.sleep(sleep_interval)

    birthday_input_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'
    driver.find_element_by_xpath(birthday_input_path).send_keys(row['生年月日'])
    print("生年月日の記入に成功しました")
    time.sleep(sleep_interval)

    # ボタンを押して送信する
    path = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div' # コピーしたボタンのxpathを貼り付ける
    driver.find_element_by_xpath(path).click()
    print("送信ボタンの押下に成功しました")

    time.sleep(sleep_interval)

    # ブラウザを閉じる
    driver.close()

    # メモリを解放する
    driver.quit()

    print("🏁🏁🏁 {}番目のデータの送信が完了しました 🏁🏁🏁 \n".format(index+1))
```
