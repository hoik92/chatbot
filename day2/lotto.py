# 1. 나눔로또 api를 통해 우승 번호를 가져온다.
# 2. random으로 생성된 번호와 우승 번호를 비교해서 나의 등수를 알려준다.
# - 1등 : 6개
# - 2등 : 5개 + 보너스 번호
# - 3등 : 5개
# - 4등 : 4개
# - 5등 : 3개

import random
import requests
import json

url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = requests.get(url).text
dic_res = json.loads(res)

# ## My Answer #########################################
# count = 0
# baaam = 0

# real_lotto = []
# for i in range(1,7):
#     real_lotto.append(dic_res['drwtNo{0}'.format(i)])

# while(baaam == 0):
#     lotto = sorted(random.sample(range(1,46), 6))

#     correct = 0
#     bonus = 0
#     for x in lotto:
#         for y in real_lotto:
#             if x == y:
#                 correct = correct + 1
#     for x in lotto:
#         if x == dic_res['bnusNo']:
#             bonus = bonus + 1

#     # print(lotto)
#     # print(real_lotto)
#     # print("맞은 개수 : {0}".format(correct))

#     if correct == 6:
#         # print("1등")
#         baaam = baaam + 1
#     elif correct == 5:
#         if bonus == 1:
#             # print("2등")
#             # baaam = baaam + 1
#             pass
#         else:
#             # print("3등")
#             # baaam = baaam + 1
#             pass
#     elif correct == 4:
#         # print("4등")
#         # baaam = baaam + 1
#         pass
#     elif correct == 3:
#         # print("5등")
#         # baaam = baaam + 1
#         pass
#     else:
#         # print("꽝")
#         # baaam = baaam + 1
#         pass
#     count = count + 1

# # print("꽝 개수 : {0}".format(baaam))
# print(count)
# ########################################################

lotto = json.loads(res)

winner = []

for i in range(1,7):
    winner.append(lotto[f"drwtNo{i}"])

def pickLotto():
    picked = sorted(random.sample(range(1,46), 6))
    matched = len(set(winner) & set(picked))

    if matched == 6:
        print("1등입니다.")
    elif matched == 5:
        print("3등입니다.")
    elif matched == 4:
        print("4등입니다.")
    elif matched == 3:
        print("5등입니다.")
    else:
        print("꽝입니다.")

for i in range(1000):
    pickLotto()