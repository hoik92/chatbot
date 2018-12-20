# CSV(Comma Separated Value : 콤마로 구분된 값(들))

# .csv 파일 연다 (import csv)
# 1. 읽기(Read)
# 2. 쓰기(Write)
# 3. 수정(Append)
# 파일 닫는다

# csv 쓰기
import csv
# f = open('sspy1.csv', 'w', encoding='utf-8')
# sspy1 = csv.writer(f)
# sspy1.writerow(["john","john@hphk.kr","01012345678","sspy1","CS"])
# f.close()

# csv 읽기
f = open('sspy1.csv', 'r', encoding='utf-8')
sspy1 = csv.reader(f)
for i in sspy1:
    # for k in i:
    print(i)
f.close()

# csv 수정(추가)
# f = open('sspy1.csv', 'a', encoding='utf-8')
# sspy1 = csv.writer(f)
# sspy1.writerow(["hoik","hoik@hphk.kr","01098765432","sspy1","EE"])
# f.close()