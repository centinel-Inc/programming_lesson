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
