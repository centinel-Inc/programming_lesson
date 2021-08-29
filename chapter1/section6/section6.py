import pandas as pd
from selenium import webdriver
import time

# GoogleフォームのURL
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfoth2f2lJXwrpZSAwoW8iHeKOBnx4Ks7jesk_t65MLb_Otxw/viewform'

# パラメータを保持する辞書型の変数
# keyにurlパラメータ名、valueに入る要素名を入れる（valueはわかりやすければ適当な値でも大丈夫）
url_param_dict = {
    'usp': 'pp_url',
    'entry.1029139045': '氏名',
    'entry.387916820': 'メールアドレス',
    'entry.1239014792': '電話番号',
    'entry.1382078040': '住所',
    'entry.731826105_year': '年',
    'entry.731826105_month': '月',
    'entry.731826105_day': '日',
}

def convertDictToUrlParams(params):
    params_string = ''
    for key, value in params.items():
        params_string += '&' + key + "=" + value

    # 最初の「&」を削除している。URLパラメータの最初は「&」ではないため。
    # ここでは「スライス」という機能を使い、"1インデックス"以降の文字を取得している
    # インデックスは0始まりなので、2文字目以降を取得することになる
    return params_string[1:]

# CSVを読み込む
# 型のヒントを書くことでVS Codeにて補完が効くようになる
df: pd.DataFrame = pd.read_csv('./data.csv', dtype=str)

for index, row in df.iterrows():
    # CSVデータを入れるため、辞書型の変数をコピーして用意する
    # urlParamDictに副作用を及ぼしたくないので、値をコピーして一時的な変数を用意する
    temp_url_param_dict = url_param_dict.copy()

    # 辞書型のkeyにvalueを代入したい場合は、以下のように行います。
    temp_url_param_dict['entry.1029139045'] = row['氏名']
    temp_url_param_dict['entry.1029139045'] = row['メールアドレス']
    temp_url_param_dict['entry.387916820'] = row['電話番号']
    temp_url_param_dict['entry.1239014792'] = row['住所']
    temp_url_param_dict['entry.731826105_year'] = row['年']
    temp_url_param_dict['entry.731826105_month'] = row['月']
    temp_url_param_dict['entry.731826105_day'] = row['日']

    # URLパラメータの文字列を組み立てる
    urlParams = convertDictToUrlParams(temp_url_param_dict)

    form_url_with_params = form_url + "?" + urlParams;

    # ブラウザを操作するためのインスタンスを生成
    driver = webdriver.Chrome()

    # ブラウザでフォームを開く
    driver.get(form_url_with_params)

    # 1秒間待つ
    time.sleep(1)

    # ボタンを押して送信する
    path = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'
    driver.find_element_by_xpath(path).click()

    # 3秒間待つ
    time.sleep(3)

    # ブラウザを閉じる
    driver.close()

    # メモリを解放する
    driver.quit()