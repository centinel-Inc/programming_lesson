import pandas as pd
from selenium import webdriver
import time

# GoogleフォームのURL
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfoth2f2lJXwrpZSAwoW8iHeKOBnx4Ks7jesk_t65MLb_Otxw/viewform'

# CSVを読み込む
# 型のヒントを書くことでVS Codeにて補完が効くようになる
df: pd.DataFrame = pd.read_csv('./data.csv', dtype=str)

sleep_interval = 0.75

for index, row in df.iterrows():
    print("🚀🚀🚀 {}番目のデータの送信を開始します 🚀🚀🚀".format(index+1))
    # ブラウザを操作するためのインスタンスを生成
    driver = webdriver.Chrome()

    # ブラウザでフォームを開く
    driver.get(form_url)

    # 1秒間待つ
    # わかりやすくするため
    time.sleep(sleep_interval)

    name_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    driver.find_element_by_xpath(name_input_xpath).send_keys(row['氏名'])
    print("氏名の記入に成功しました")
    time.sleep(sleep_interval)

    mail_address_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    driver.find_element_by_xpath(mail_address_input_xpath).send_keys(row['メールアドレス'])
    print("メールアドレスの記入に成功しました")
    time.sleep(sleep_interval)

    telephone_number_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    driver.find_element_by_xpath(telephone_number_input_xpath).send_keys(row['電話番号'])
    print("電話番号の記入に成功しました")
    time.sleep(sleep_interval)

    address_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea'
    driver.find_element_by_xpath(address_input_xpath).send_keys(row['住所'])
    print("住所の記入に成功しました")
    time.sleep(sleep_interval)

    birthday_input_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'
    driver.find_element_by_xpath(birthday_input_path).send_keys(row['生年月日'])
    print("生年月日の記入に成功しました")
    time.sleep(sleep_interval)

    # ボタンを押して送信する
    path = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div' # コピーしたボタンのxpathを貼り付ける
    driver.find_element_by_xpath(path).click()
    print("送信ボタンの押下に成功しました")

    time.sleep(sleep_interval)

    # ブラウザを閉じる
    driver.close()

    # メモリを解放する
    driver.quit()

    print("🏁🏁🏁 {}番目のデータの送信が完了しました 🏁🏁🏁 \n".format(index+1))