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