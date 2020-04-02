
# 데이터가 많은 변수는 리모컨
movie_list = [
    ('A', 3, 32),
    ('M', 12, 3)

]

#이중루프

for data in movie_list:
    for m in data:
        print(m,end='')                #end=''를 붙이면 옆으로 결과같이 이어서 나옴.
    print()                            #출력할것이 없어서 줄바꿈이 됨