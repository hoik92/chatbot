f = open('names.txt', 'a', encoding="utf-8")
f.write('\n장호익')
f.close()

## 영구적(손실 없이)으로 데이터를 저장할 때

# .txt(텍스트) 파일 연다
# 1. 읽기(Read)
# 2. 쓰기(Write)
# 3. 수정(Append)
# 파일 닫는다

# .json 파일 연다 (import json) => dictionary
# 1. 읽기(Read)
# 2. 쓰기(Write)
# 3. 수정(Append)
# 파일 닫는다

# .csv 파일 연다 (import csv) => 2d-list
# 1. 읽기(Read)
# 2. 쓰기(Write)
# 3. 수정(Append)
# 파일 닫는다

# with 키워드 활용 -> 코드를 간결하게

# DB 연다(connect) -> CRUD
# 1. 읽기(CREATE)
# 2. 쓰기(READ / RETRIEVE)
# 3. 수정(UPDATE)
# 4. 삭제(DELETE / DESTROY)
# DB 닫는다(disconnect)

# dictionary(key-value) + 강력한 메소드 추가 = object

# ORM 