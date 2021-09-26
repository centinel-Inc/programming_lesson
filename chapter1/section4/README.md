# 第 4 節 スクレイピングのための環境構築



Pythonを使ってブラウザを操作するために必要な環境を構築していきます

## 1. ブラウザの準備
本講座ではPythonでChromeを操作します。

PCにインストールされていない場合は最新のChromeをインストールしてください。

https://www.google.com/intl/ja_jp/chrome/



## 2. brewのインストール
chromedriverのインストールにbrewを利用するので導入していない場合はインストールしてください

https://brew.sh/index_ja


## 3. chromedriverのインストール
chromeをpythonから操作するために必要なchromedriverをbrewを使ってインストールしてください
```
brew install chromedriver
```

## 4. seleniumのインストール
seleniumというライブラリを使ってwebdriverを制御して自動操作を行います。

```
pip3 install selenium
```

## 5. 環境構築の確認
### pythonでブラウザを起動する
```python
from selenium import webdriver
from time import sleep

# ブラウザを開く
driver = webdriver.Chrome()

# get内に指定したサイトを開く
# TODO 他のサイトも開いてみましょう
driver.get('https://centinel.jp/')

sleep(5)

# ブラウザを閉じる
driver.quit()
```

## Tips
### 起動時にエラーが出た時 その1
このようなエラーが出た場合は許可を与える必要があります。

<img src="./images/1.png">

<img src="./images/2.png">

システム環境設定 > セキュリティとプライバシー に移動すると「chromedriverは開発元を確認できないため、使用がブロックされました。」というメッセージが表示されています。

メッセージの右にある「このまま許可」をクリックしてください。



### 起動時にエラーが出た時 その2
このようなエラーが出た場合はPCにインストールされているChromeとchromedriverのバージョンが一致していません。
```
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 92
```

その場合はこのコマンドでchromedriverを最新版にしてください
```
brew upgrade chromedriver
```

