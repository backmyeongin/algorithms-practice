"""
설명: 구구단 게임
기능:
1. 입력(키보드)
2. 문제랜덤(2단~9단)
3. 3문제
4. 정답률 보이기
"""
import random

pass_count = 0

for i in range(3):
    random_value_1 = random.randint(2,9)
    random_value_2 = random.randint(1,9)

    print(f"{random_value_1} x {random_value_2} = ")
    my_input = int(input("정답을 입력하세요:"))
    if (random_value_1 * random_value_2) == my_input:
        print("정답입니다.")
        pass_count = pass_count + 1
    else:
        print("오답입니다.")


print(f"맞춘 갯수는 : {pass_count} ")


