# Bithumb에서 코인 이름과 가격 가져오기

import bs4
import requests

a = requests.get("https://www.bithumb.com/").text
doc = bs4.BeautifulSoup(a, 'html.parser')

result = doc.select('.coin_list tr td p a strong')
result2 = doc.select('.sort_real')

for i in range(len(result)):
    print(result[i].text + result2[i].text)