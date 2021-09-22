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
