# 로또 (함수로)

import random

#6자리 뽑는 함수 먼저 만들기
def makeNums():
    # 일단 1부터 45까지 볼 리스트 만들기
    balls = [i for i in range(1,46)]
    random.shuffle(balls)
    return balls[0:6]


#화면에서 입력만 받는 함수 만들기 (또는 입력출력함수를 같이 만들어도됨)
def input_display():
    money = int(input("금액을 입력하세요"))
    if money % 1000 != 0:
        print("try again")
        input_display()   #재귀, 함수안에서 다시 함수반복하는 것
    else:
        return money / 1000

#화면에서 출력만 하는 함수 만들기
def main():
    count = input_display()
    for x in range(int(count)):
        nums = makeNums()
        print(sorted(nums))
    print("-------------------------")

if __name__ == "__main__":
    main()
