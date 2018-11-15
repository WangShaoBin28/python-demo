import requests
import json
import os


def get_page(page):
    # 页面参数添加在url中，可以把此次的关键词苍井空换成其他关键词
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&' \
          'queryWord=苍井空&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=苍井空' \
          '&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=girl&pn={}&rn=30&gsm=1e' \
        .format(page)
    # 向网站发送请求
    response = requests.get(url)
    # 判断状态
    if response.status_code == 200:
        # 返回文本文件信息
        return response.text


def json_load(text):
    # 文本文件处理成字典格式
    jsondict = json.loads(text)

    urlset = set()
    # 字典里面是否包含了data这个值
    if 'data' in jsondict.keys():
        # 从jsondict中取出data这个字典里面的东西,赋值给items
        for items in jsondict.get('data'):
            # 异常处理,不包含thumbURL这个数据的时pass即可
            try:
                urlset.add(items['thumbURL'])
            except:
                pass
    return urlset


def down_pic(url):
    response = requests.get(url)
    name = url.split(',')[-1].split('&')[0]
    if response.status_code == 200:
        # 表示,如果文件名字相同,就删除当前文件,然后再创建一个一样名字的文件
        with open('./images/%s.jpg' % name, 'wb') as f:
            print('downloading...: ' + url)
            # 以二进制的方法写入到本地
            f.write(response.content)


def main():
    # 先检测是否优images文件夹，没有则创建
    if not os.path.exists(r'./images'):
        os.mkdir(r'./images')

    # p为下载页码，可以调整
    for p in range(3):
        print('it is downloading the picture of page %s' % (p + 1))
        page = p * 30
        text = get_page(page)
        urlset = json_load(text)
        for url in urlset:
            down_pic(url)


if __name__ == '__main__':
    main()
