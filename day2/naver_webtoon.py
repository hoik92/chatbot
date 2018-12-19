# naver webtoon 화요일 웹툰 긁어오기

import bs4
import requests

a = requests.get("https://m.comic.naver.com/webtoon/weekday.nhn?week=tue").text

doc = bs4.BeautifulSoup(a, 'html.parser')

result = doc.select('.toon_name')
img = doc.select('.im_br')

names = []
imgs = []
for i in result:
    names.append(i.text)
    print(i.text)
for i in img:
    imgs.append(i.select_one('img')["src"])
    print(i.select_one('img')["src"])

# f = open('./a.txt', 'a+')
# for name in names:
#     f.write(name + '\n')

print(len(names))
print(len(imgs))