import os
import requests
from pprint import pprint as pp

token = os.getenv('TELEGRAM_TOKEN')
msg = input()

# ?chat_id={chat_id}&text={name}
# string 수술(interpolation)
# 1. f-string
# print(f"Hello, {name}")
# 2. format()
# print("Hello, {}".format(name))

# def sendMessage(msg):
#     token = os.getenv('TELEGRAM_TOKEN')
#     method = "getUpdates"
#     url = f"https://api.telegram.org/bot{token}/{method}"

#     res = requests.get(url)
#     doc = res.json()
#     chat_id = doc['result'][0]['message']['chat']['id']

#     method = f"sendMessage?chat_id={chat_id}&text={msg}"
#     url = f"https://api.telegram.org/bot{token}/{method}"
#     requests.get(url)

# sendMessage("WTF")

# AGENDA : 텔레그램 메시지를 보낼거임
## I. chat_id 받아오는 기능(function)
# 1. 환경변수를 불러와서
# 2. url을 만들고
# 3. getUpdates
# 4. chat_id
## II. message를 보내는 기능(function)
# 5. url 다시 만들고
# 6. 메시지를 보냄
def getID(token): # => chat_id
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    res = requests.get(url)
    doc = res.json()
    # json.loads(json) => python dictionary
    chat_id = doc['result'][0]['message']['chat']['id']
    return chat_id

def sendMessage(chat_id,token,msg): # => 텔레그램 메시지를 보냄
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)
    print(f"{msg} 을(를) {chat_id} 님에게 보냈습니다.")
    return

sendMessage(getID(token),token,msg)