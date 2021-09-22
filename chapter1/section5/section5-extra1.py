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
