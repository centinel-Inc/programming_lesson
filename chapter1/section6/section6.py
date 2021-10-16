from selenium import webdriver
import time

# フォームのURLを変数で保持する
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfoth2f2lJXwrpZSAwoW8iHeKOBnx4Ks7jesk_t65MLb_Otxw/viewform'

# ブラウザを操作するためのインスタンスを生成
driver = webdriver.Chrome()

# ブラウザでフォームを開く
driver.get(form_url)

# 1秒間待つ
# わかりやすくするため
time.sleep(1)

name_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
driver.find_element_by_xpath(name_input_xpath).send_keys('テスト 太郎')
print("氏名の記入に成功しました")
time.sleep(1)

mail_address_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
driver.find_element_by_xpath(mail_address_input_xpath).send_keys('test@gmail.com')
print("メールアドレスの記入に成功しました")
time.sleep(1)

telephone_number_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
driver.find_element_by_xpath(telephone_number_input_xpath).send_keys('000-0000-0000')
print("電話番号の記入に成功しました")
time.sleep(1)

address_input_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea'
driver.find_element_by_xpath(address_input_xpath).send_keys('東京都テスト市テスト町0-0-00')
print("住所の記入に成功しました")
time.sleep(1)

birthday_input_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input'
driver.find_element_by_xpath(birthday_input_path).send_keys('19960717')
print("生年月日の記入に成功しました")

# ボタンを押して送信する
path = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div' # コピーしたボタンのxpathを貼り付ける
driver.find_element_by_xpath(path).click()
print("送信ボタンの押下に成功しました")

# 3秒間待つ
time.sleep(3)

# ブラウザを閉じる
driver.close()

# メモリを解放する
driver.quit()