from selenium import webdriver
from time import sleep

# ブラウザを開く
driver = webdriver.Chrome()

# 画像をダウンロードしたいサイトを開く
driver.get("https://centinel.jp/")

# 表示されたのを確認するために５秒処理を止める
sleep(5)

# タブを閉じる
driver.close()

# ブラウザを閉じる
driver.quit()