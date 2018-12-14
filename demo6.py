import requests
from requests.exceptions import RequestException
from lxml import etree


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            return response.text
            return None
    except  RequestException:
        print("You can not do it~")


def parse_one_page(html):
    movie_list = etree.HTML(html).xpath('//dl[@class="board-wrapper"]/dd')
    for movie in movie_list:
        yield {
            'index': movie.xpath('./i/text()'),
            'name': movie.xpath('.//div[@class="movie-item-info"]//a/text()')[0],
            'star': movie.xpath('.//div[@class="movie-item-info"]//p[@class="star"]/text()')[0].replace('\n', ''),
            'releasetime': movie.xpath('.//div[@class="movie-item-info"]//p[@class="releasetime"]/text()'),
        }


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    dy = parse_one_page(html)
    for i in dy:
        print(i)


if __name__ == '__main__':
    for i in range(10):
        offset = i * 10
        main(offset)
