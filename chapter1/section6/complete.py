from selenium import webdriver
import time
import pandas as pd

url = 'https://docs.google.com/forms/d/e//viewform'

paramDict = {
    'usp': 'pp_url',
    'entry.1213226508': '氏名',
    'entry.92659105': 'email',
    'entry.590874451': 'TEL',
    'entry.32877361': '住所',
    'entry.1383903086_year': '年',
    'entry.1383903086_month': '月',
    'entry.1383903086_day': '日',
}


def convertDictToUrlParams(params):
    """[summary]

    Args:
        params (Dict): 入力したい値を辞書型で表現した値

    Returns:
        string: paramsをURLパラメータに変換した値
    """
    paramsString = ''
    for index, (key, value) in enumerate(params.items()):
        if index != 0:
            paramsString += '&'
        paramsString += key + "=" + value

    return paramsString


# パスからボタンを探し出して、クリックする
def click(xpath):
    driver.find_element_by_xpath(xpath).click()


# 全てのパラメータをStringで読み取る
df = pd.read_csv('data.csv', dtype=str)

for index, row in df.iterrows():
    getParamsDict = paramDict.copy()
    getParamsDict['entry.1213226508'] = row['氏名']
    getParamsDict['entry.92659105'] = row['email']
    getParamsDict['entry.590874451'] = row['TEL']
    getParamsDict['entry.32877361'] = row['住所']
    getParamsDict['entry.1383903086_year'] = row['年']
    getParamsDict['entry.1383903086_month'] = row['月']
    getParamsDict['entry.1383903086_day'] = row['日']
    getParams = convertDictToUrlParams(getParamsDict)
    getUrl = url + '?' + getParams
    driver = webdriver.Chrome()
    driver.implicitly_wait(1)

    # 作成したパラメータでフォームにアクセスする
    driver.get(getUrl)
    time.sleep(1)

    # divかつroleがbuttonの要素が送信用ボタン
    submitButton = '//div[@role = "button"]'
    click(submitButton)

    time.sleep(1)
    driver.close
    driver.quit

    # 完了後5秒待つ
    time.sleep(5)

