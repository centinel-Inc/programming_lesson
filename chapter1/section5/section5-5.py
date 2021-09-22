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
