# 第 5 節 サイトから画像を収集しよう

### 完成形

```sh
git clone https://github.com/centinel-jp/programming_lesson.git
cd programming_lesson/chapter1/section5/
python3 section5-5.py
```

商品レビューサイトの画像を一括ダウンロードしてみましょう

今回のターゲット
https://centinel.jp/


## 1. ダウンロード先のサイトを開く

```
pip3 install selenium
```

### ブラウザで好きなサイトを開く
```python
from selenium import webdriver
from time import sleep

# ブラウザを開く
driver = webdriver.Chrome()

# TODO URLを変更して好きなサイトを開いてみましょう
# 画像をダウンロードしたいサイトを開く
driver.get("https://centinel.jp/")

# 表示されたのを確認するために５秒処理を止める
sleep(5)

# タブを閉じる
driver.close()

# ブラウザを閉じる
driver.quit()
```

## 2. 画像要素を取得する

### ダウンロード対象の画像要素を調査
開発者ツールから画像の要素を開いてみると画像要素のsrcに画像のURLが入っていることが確認できます。

つまりこのURLをプログラム内で取得することができれば画像がダウンロードできそうです。

<img src="./images/1.png">

### サイト内の画像要素を取得

```python
from selenium import webdriver

# ブラウザを開く
driver = webdriver.Chrome()

# 画像をダウンロードしたいサイトを開く
driver.get("https://centinel.jp/")

# 開いたサイトのimg要素(画像)を全て取得
image_elements = driver.find_elements_by_tag_name("img")
print(image_elements)

driver.close()
driver.quit()
```


## 3. 画像のURLを取得

### 画像要素のリストから画像のURLを取得する

```python
from selenium import webdriver

# ブラウザを開く
driver = webdriver.Chrome()

# 画像をダウンロードしたいサイトを開く
driver.get("https://centinel.jp/")

# 開いたサイトのimg要素(画像)を全て取得
image_elements = driver.find_elements_by_tag_name("img")

# image_elements(img要素のリスト)から一つずつ取り出して中身を確認
for image in image_elements:
    # img要素からsrc=urlを取り出す
    image_url = image.get_attribute("src")

    # 画像のURLを確認する
    print(image_url)

driver.close()
driver.quit()
```

## 4. 画像をダウンロード

### 取得したURLから画像を保存

```python
from selenium import webdriver
import requests

# ブラウザを開く
driver = webdriver.Chrome()

# 画像をダウンロードしたいサイトを開く
driver.get("https://centinel.jp/")

# 開いたサイトのimg要素(画像)を全て取得
image_elements = driver.find_elements_by_tag_name("img")

# image_elements(img要素のリスト)から一つずつ取り出して中身を確認
for image in image_elements:
    # img要素からsrc=urlを取り出す
    image_url = image.get_attribute("src")

    # 画像データをダウンロード
    responce = requests.get(image_url)

    # 書き込み先のファイルを開く
    with open("./download/test.jpeg", "wb") as file:
        # ダウンロードした画像データをtest.jpegに書き込む
        file.write(responce.content)

    # 試しに一つだけダウンロードしてforループを抜ける
    break

driver.close()
driver.quit()
```

## 5. 画像を一括ダウンロード

### カウントアップして画像に名前をつけて保存

```python
from selenium import webdriver
from time import sleep
import requests

# ブラウザを開く
driver = webdriver.Chrome()

# 画像をダウンロードしたいサイトを開く
driver.get("https://centinel.jp/")

# 開いたサイトのimg要素(画像)を全て取得
image_elements = driver.find_elements_by_tag_name("img")

# ファイル名用にカウンターを用意する
count = 1
# image_elements(img要素のリスト)から一つずつ取り出して中身を確認
# TODO enumerateを使ってカウントアップを簡潔に書き直しましょう(python enumerateで検索)
for image in image_elements:
    # TODO 商品画像のみをダウンロードするように条件分岐をしてみましょう(ヒント:image要素のalt属性の中身を元に分岐する)
    # alt属性を出力するには→ print("image要素のalt属性を出力: " + image.get_attribute("alt"))

    # img要素からsrc=urlを取り出す
    image_url = image.get_attribute("src")

    # 画像データをダウンロード
    responce = requests.get(image_url)

    # 書き込み先のファイルを開く
    # 画像ごとに名前を変えるためにカウンターの値をファイル名にする
    with open("./download/" + str(count) + ".jpeg", "wb") as file:
        # ダウンロードした画像データをtest.jpegに書き込む
        file.write(responce.content)

    # サーバーに負荷をかけないように待ち時間を入れる(スクレイピングのマナー)
    sleep(0.5)

    # カウンターに1を加算する
    count += 1

driver.close()
driver.quit()

```

# 番外編 使いやすくしよう
## 6. enumerateを使ってコードをきれいに

```python
from selenium import webdriver
from time import sleep
import requests

driver = webdriver.Chrome()
driver.get("https://centinel.jp/")

image_elements = driver.find_elements_by_tag_name("img")

# enumerateを使うとリストから要素を取り出しながらカウントアップができます
for index, image in enumerate(image_elements,1):
    image_url = image.get_attribute("src")
    responce = requests.get(image_url)

    with open("./download/" + str(index) + ".jpeg", "wb") as file:
        file.write(responce.content)

    sleep(0.5)

driver.close()
driver.quit()
```

## 7. ほしい画像だけをダウンロード

```python
from selenium import webdriver
from time import sleep
import requests

driver = webdriver.Chrome()
driver.get("https://centinel.jp/")

image_elements = driver.find_elements_by_tag_name("img")

for index, image in enumerate(image_elements,1):
    # alt属性を出力する
    print("image要素のalt属性を出力: " + image.get_attribute("alt"))

    """ 
    考え方
    1.不要な画像のalt属性にはavatorやtagという文字列が含まれている
    2.つまりalt属性に不要な文字列が含まれる画像はダウンロードせずにスキップしたい
    3.if文を使ってalt属性の中身に特定の文字列が含まれていたらスキップして次の画像のチェックを行う
    """
    if "avator" in image.get_attribute("alt") or "tag" in image.get_attribute("alt"):
        # continueを使うと後続の処理をスキップして次のループに移行します 
        print("スキップします")
        continue

    image_url = image.get_attribute("src")
    responce = requests.get(image_url)

    with open("./download/" + str(index) + ".jpeg", "wb") as file:
        file.write(responce.content)

    sleep(0.5)

driver.close()
driver.quit()
```