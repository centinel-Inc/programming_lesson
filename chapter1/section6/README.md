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

## 5. 読み込んだデータを全件送信してみよう
