# Q2
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i

    return result / len(args)

print(avg_numbers(3, 1))  # 1.5 출력
print(avg_numbers(4, 5, 3, 2, 1))  # 3.0 출력

# Q6
user_input = input('저장할 내용을 입력하세요 > ')
f = open('./Day03/test.txt', mode='a', encoding='utf-8')  # 내용을 추가하기 위해서 a를 사용
f.write(user_input)
f.write('\n')  # 입력한 내용을 줄단위로 구분하기 위해서 줄바꿈 추가

f.close()
