from selenium import webdriver
from time import sleep

# ブラウザを開く
driver = webdriver.Chrome()

# 表示されたのを確認するために５秒処理を止める
sleep(5)

# ブラウザを閉じる
driver.quit()