# http://sc.chinaz.com/jiaoben/index.html
# http://sc.chinaz.com/jiaoben/index_2.html
import requests
from bs4 import BeautifulSoup

response = requests.get('http://sc.chinaz.com/jiaoben/index_2.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, "html.parser")

page = soup.find('div', attrs={'class': 'framework_require'}).find_all('a', attrs={'target': '_blank'})
print(soup)
print(page)
