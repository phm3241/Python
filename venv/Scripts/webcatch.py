import requests
from bs4 import BeautifulSoup


def getData():

    url = 'https://bbs.ruliweb.com/market/board/1020'

    print("getData......")

    req = requests.get(url)

    html = req.text

    print(html)

    return []



