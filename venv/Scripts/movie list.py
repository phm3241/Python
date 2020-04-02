# 예제 6-1 > 영화 타입 출력하기(거리계산)

#영화 타입, 키스신숫자, 액션신숫자
import math

movie_sample =[
        (0,10,'A'),
        (1,9,'A'),
        (2,5,'A'),
        (4,8,'A'),
        (6,6,'A'),
        (7,3,'M'),
        (9,1,'M'),
        (10,5,'M')
]

def calcDistance(point1, point2):
    result = math.sqrt(math.pow(point1[0] - point2[0],2) +
                      math.pow(point1[1] - point2[1],2))
    return result


count_kiss = int(input("키스씬의 숫자를 입력하세요"))
count_action = int(input("액션씬의 숫자를 입력하세요"))


target = (count_kiss, count_action)

movie_sample.sort(key= lambda x: calcDistance(x,target))

result =[movie_sample[0][2]
        ,movie_sample[1][2]
        ,movie_sample[2][2]
]


M_count = 0
A_count = 0

for x in result :
    if x =='A':
        A_count += 1
    elif x == 'M':
        M_count += 1

if A_count > M_count:
    print ("A")
else:
    print ('M')



