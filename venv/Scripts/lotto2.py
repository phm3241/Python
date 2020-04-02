# 예제 4-2 > 리스트와 루프 _로또게임(2)
# del로 리스트 요소 하나씩 삭제하기


balls = [ x for x in range(1,46)]

print(balls)

# 반복문으로 6번째까지 x에 담는다
for x in range(6):

    # balls 리스트의 첫번째 숫자를 출력한다.
    print(balls[0])

    # del a[x]는 x번째 요솟값을 삭제, del 함수는 파이썬이 자체적으로 가지고 있는 삭제 함수
    # balls 리스트의 첫번째 숫자를 삭제하고, balls 리스트를 출력한다.
    del balls[0]
    print(balls)

# 이렇게 6까지 리스트 첫번째 숫자 출력, 삭제하고 전체리스트 출력을 반복한다.

