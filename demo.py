# encode=utf-8
import requests
import urllib.request
import os
import sys


def getSogouImage(category, length, path):
    request = requests.get(
        'https://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=' + category + '&tag=%E5%85%A8%E9%83%A8&&start=0&len=' + str(
            length) + '&width=1920&height=1080')
    json = request.json()
    m = 0
    print("全部的json" + str(json['all_items']))
    print(len(json['all_items']))
    if not os.path.exists(path):
        os.makedirs(path)
    for j in json['all_items']:
        try:
            print('正在下载。。。' + path + str(m) + '.jpg')
            urllib.request.urlretrieve(j['pic_url'], path + str(m) + '.jpg')
            m = m + 1
        except Exception:
            print('程序出现了问题。。。' + j['pic_url'] + path + str(m) + '.jpg')



if __name__ == '__main__':
    getSogouImage('壁纸', 1079, 'D:\\壁纸\\')
