import os

print(os.listdir('.'))

os.chdir(r'C:\Users\student\chatbot\day1\list')

print(os.getcwd())

name = os.listdir('.')

for i in name:
    os.rename(i, i[6:])

print(name)