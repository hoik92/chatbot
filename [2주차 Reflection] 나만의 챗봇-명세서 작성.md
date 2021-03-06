# SSAFY Start Camp 챗봇 퀘스트

서울_1_장호익, https://github.com/hoik92



## I. 스펙(Specification)

(1) 메아리 기능

* 사용자가 Telegram을 통해 챗봇에게 전송한 데이터를 분석한다.
* 데이터가 텍스트일 경우, 해당 문자를 그대로 돌려보낸다.

(2) Clova Face Recognition

* 사용자가 Telegram을 통해 챗봇에게 전송한 데이터를 분석한다.
* 데이터가 이미지일 경우, 해당 이미지와 가장 비슷한 얼굴의 유명인 이름을 돌려보낸다.



## II. 회고(Retrospective)

(1) 환경변수

* 외부에 노출되지 않아야 하는 Telegram Token이나 Clova ID, Secret을 컴퓨터 환경변수에 저장하여 불러와 사용하도록 하는 부분이 어려웠다.

(2) json 해석

* Telegram이 발신할 상대의 ID를 찾아내기 위해 request를 통해 json 형태의 문서를 받아서 이를 해석하는 부분이 어려웠다.



## III. 보완 계획(Feedback)

(1) 이미지 인식

* 사용자가 이미지 파일을 전송할 때 이미지의 형태로 보낼 때는 제대로 작동하지만, document 형식으로 보내면 이를 텍스트로 인식하여 아무 내용도(메아리 조차도) 피드백을 하지 않는다.
* document 형식으로 이미지를 전송해도 이를 처리하여 얼굴 인식 프로세싱을 할 수 있도록 만드는 것이 필요해보인다.

(2) 키워드 인식

* 텍스트를 분석하여 메아리 기능이 아닌 특정 키워드에 반응하는 기능
* ''로또''를 입력하여 보내면 1~45 범위 내의 숫자 6개를 랜덤으로 알려주는 기능 등을 구현했으나 적용하지 못함.