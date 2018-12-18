import os

print(os.listdir('.'))

os.chdir(r'C:\Users\student\chatbot\day1\list')
print(os.getcwd())

# print(os.listdir('.'))

# os.rename('hello.txt', 'what_the.txt')

name_list = os.listdir('.')

for i in name_list:
    os.rename(i, "ssafy_" + i)

# for i in name_list:
#     os.rename(i, i[6:])