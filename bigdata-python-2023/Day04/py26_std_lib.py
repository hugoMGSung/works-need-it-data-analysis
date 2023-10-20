# 표준라이브러리
# import datetime as dt
from datetime import date, datetime

first_date = date(2022, 12, 25)
cur_date = date.today() # date type
print(cur_date - first_date) 

cur_dt = datetime.now() # 많이 씀
print(cur_dt)
print(cur_dt.strftime('%Y-%m-%d')) # date.today() 와 동일하지만 str

print(cur_dt.weekday()) # 0부터 월요일
print(cur_dt.isoweekday()) # 1부터 월요일

import time

for x in range(10):
    print(x)
    # time.sleep(0.1) # second C#, java, C++ time.sleep(ms)

import math

print(math.pi)

import os

# print(os.environ)
# print(os.environ['PATH'])

print(os.getcwd())
print(os.system('git --version')) # 콘솔 명령어 실행

## json 모듈(라이브러리)!!
import json

data = ''
with open('./Day04/data.json', mode='r', encoding='utf-8') as f:
    data = json.load(f) # load -> str / loads -> byteArray

print(data)



## urllib 
from urllib.request import urlopen

res = urlopen('https://www.naver.com')
print(res.status) # 200 OK
print(res.read().decode('utf-8'))  # index.html 가져옴 --> 웹 크롤링 기초

import webbrowser
webbrowser.get()
webbrowser.open('http://www.naver.com')