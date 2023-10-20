# 주석
# https://github.com/hugoMGSung/basic-python-2023.git
from faker import Faker
import pandas as pd
import os

print(os.getcwd())

dummy = Faker('ko-KR')
# print(dummy.name())
# print(dummy.address())
# print(dummy.company())
dummy_data = [[dummy.name(), dummy.postcode(), dummy.address(), 
               dummy.phone_number(), dummy.email()] for i in range(1)]
df = pd.DataFrame(data=dummy_data, columns=['이름', '우편번호', '주소', '전화번호', '이메일'])
# print(dummy_data)
df.to_csv('./Day04/dummy_members3.csv', index=True, encoding='utf-8')
print('CSV 생성완료!')


data = pd.read_csv('./Day04/dummy_members3.csv')
print(data)