# 예제 4-3 > 리스트와 루프 _로또게임(3)_중복 안되게 6볼 뽑기

import random


# range(1, 46)은 숫자 1부터 45까지(1 이상 16 미만)의 숫자를 데이터로 갖는 객체
# x 변수에 리스트의 숫자가 1부터 45까지 하나씩 차례로 대입

balls = [x for x in range(1,46)]

# shuffle() 순서형 자료(sequence)를 뒤죽박죽으로 섞어놓는 함수
random.shuffle(balls)

# 리스트의 슬라이싱 [0:2] 범위설정하면 첫번째자리부터 세번째 미만까지 출력됨
print(balls[0:6])


