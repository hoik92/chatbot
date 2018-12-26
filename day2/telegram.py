import requests
from time import sleep
from bs4 import BeautifulSoup as bs

# url = f"https://api.telegram.org/bot{key}/"

# key = "<token>" # 환경 변수를 이용

# user_id = "<id>" # 환경 변수를 이용



search_url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=nba+%EC%9D%BC%EC%A0%95&oquery=nba&tqi=UtAYQlpVuFRsstR%2Biulssssstbl-389057"
res = requests.get(search_url).text
doc = bs(res, 'html.parser')

result_time = doc.select('.bg_none')
result_time_txt = []
result_lteam = doc.select('.l_team span')
result_lteam_txt = []
result_rteam = doc.select('.r_team span')
result_rteam_txt = []
result_score = doc.select('.score')
result_score_txt = []

for i in result_time:
    result_time_txt.append(i.text)

for i in result_lteam:
    result_lteam_txt.append(i.select_one('a')["title"])

for i in result_rteam:
    result_rteam_txt.append(i.select_one('a')["title"])

for i in result_score:
    result_score_txt.append(i.text)

for i in range(len(result_lteam_txt)):
    msg = result_time_txt[i] + " " + result_lteam_txt[i] + " " + result_score_txt[i] + " " + result_rteam_txt[i]
    url = f"https://api.telegram.org/bot<token>/sendMessage?chat_id=<id>&text={msg}"
    requests.get(url)
