import requests
from bs4 import BeautifulSoup
import urllib.request

num = 0


def dow(index):
    request = requests.get('https://www.i4.cn/wper_1_4_0_' + str(index) + '.html')
    soup = BeautifulSoup(request.text, "html.parser")
    page = soup.find_all('img', attrs={'class': 'wper_img'})
    for aa in page:
        href = aa['data-big']
        urllib.request.urlretrieve(href, 'D:/壁纸11/' + aa['alt'] + '.' + aa['data-big'].split('.')[3])
        print('完成---' + aa['alt'] + '.' + aa['data-big'].split('.')[3])
        global num
        num = num + 1
    print('第一页已下载完成！当前下载第' + str(num) + '张')
    if index != 2072:
        dow(index + 1)
        print('开始下载第' + str(index) + '页')


if __name__ == '__main__':
    dow(1)
