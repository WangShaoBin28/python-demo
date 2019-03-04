import requests
import urllib.request
import ssl


def getimage(path, num):
    request_json = requests.get(path + str(num))
    aa = request_json.json()['results']
    for json11 in aa:
        # json11['url'].split('/')
        print(json11['url'].split('/')[len(json11['url'].split('/')) - 1].split('?')[0])
        ccc = requests.get(json11['url'], verify=False)
        if ccc.status_code == 200:
            ssl._create_default_https_context = ssl._create_unverified_context
            urllib.request.urlretrieve(json11['url'],
                                       'D:/bb/' +
                                       json11['url'].split('/')[len(json11['url'].split('/')) - 1].split('?')[0])

    print("第" + str(num) + "下载完毕！")
    num = num + 1
    if num != 62:
        getimage(path, num)


if __name__ == '__main__':
    getimage("http://gank.io/api/data/%E7%A6%8F%E5%88%A9/11/",1)
