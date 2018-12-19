# 1. requests 로 naver.com 요청을 보내서
# 2. 응답 받은 문서를 저장하고
# 3. BeautifulSoup 로 정보를 찾기 좋게 만들고
# 4. 우리가 원하는 정보를 뽑아온다.
# 5. webbrowser 를 통해 트렌드 1위 단어를 검색한 페이지를 열어주는 코드

import webbrowser
import requests
import bs4

url = "https://www.naver.com"
search_url = "https://search.naver.com/search.naver?query="

response = requests.get(url).text
doc = bs4.BeautifulSoup(response, 'html.parser')

# result = doc.select_one('.ah_k')
result = doc.select('.ah_k')
for i in range(20):
    print(result[i].text)
    webbrowser.open(search_url + result[i].text)

# print(result.text)

# webbrowser.open(search_url + result.text)