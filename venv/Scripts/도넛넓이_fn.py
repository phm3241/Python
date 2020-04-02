# 예제 1 > 도넛넓이구하기 (함수지향패러다임)

# 일단 메인기능부터 만들기, 함수만들기
# pi값 써야해서 math모듈 불러오기

import math

# 메인기능(넓이구하기)부터 함수로 만들기
# pow는 제곱
def getCircleArea(radius):
    return math.pow(radius,2)*math.pi


# 반지름으로 도넛넓이 만드는 함수 만들기
def getDonutArea(r1,r2):

    area1 = getCircleArea(r1)
    area2 = getCircleArea(r2)

    return abs(area1 - area2)

# 기본으로 돌아가고 있는 ...
if __name__ == "__main__":

	result = getDonutArea(5,10)

print(result)

# 참고사이트
# 파이썬 if __name__ == "__main__" 의미
# https://madplay.github.io/post/python-main-function
