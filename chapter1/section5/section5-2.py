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