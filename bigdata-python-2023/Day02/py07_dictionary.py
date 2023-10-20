# 딕셔너리 
iron_man = { 'name' : 'Tony Stark', 
             'address' : 'New york',
             'armer' : 'Repluser Arm' } # json과도 일치

print(iron_man)

# 아래 두개 결과 동일
print(iron_man.get('name'))
print(iron_man['name'])

# Key 중복불가
d1 =  { 1 : 'a', 1: 'b'}
print(d1)

# Value 중복허용
d2 = { 1 : 'test', 2 : 'test' }
print(d2)

# 딕셔너리 함수들
print(iron_man.keys())

for item in iron_man.keys():
    print(item)

print(iron_man.values())
print(iron_man.items()) # values(), items() 는 많이 사용안함
print(iron_man)



    