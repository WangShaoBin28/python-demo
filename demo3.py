import requests
from bs4 import BeautifulSoup
import os
import urllib.request
import random


def getwin400Image(path):
    request_html = requests.get('http://www.win4000.com/wallpaper_big_98816_4.html')

    soup = BeautifulSoup(request_html.text, "html.parser")
    page = soup.find('div', class_='keBody').find_all('a')

    for a in page:
        href = a['href']
        urllib.request.urlretrieve(href, 'D:/bb/' + str(random.randint(1, 100)) + '.jpg')


if __name__ == '__main__':
    getwin400Image('D:/bb/')
