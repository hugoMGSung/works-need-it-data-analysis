# 
hong = { '국어' : 80, '영어': 75, '수학': 55}
print(hong.values())

sum = 0
for item in hong.values():
    sum += item

print(f'홍길동의 평균점수는 {sum / 3} 입니다')

number = 13
result = 13 % 2 == 0
print(f'{number} 은 짝수? {result}')

pin = '881020-1068234'
yyyymmdd = pin.split('-')[0]
num = pin.split('-')[1]
print(yyyymmdd)
print(num)

a = [1,3,5,4,2]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

a = [1,1,1,2,2,3,3,3,4,4,5]
print(set(a))

