# 예 1 > 리스트 담기

# 불규칙적인 데이터, 비연속적인 데이터 리스트로 잡아야함. (몇개 생길지 모르는 핫딜처럼)
# 연속적인 데이터도 잘 만들어냄
# 파이썬의 리스트 크기는 가변적. 자바의 배열은 크기가 고정.


#빈 리스트 만들기
my_list = []

# .append(x)는 리스트의 맨 마지막에 x를 추가하는 함수
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)


#read (읽어오기) _리스트 안에 두번째 값 읽어오기
print(my_list[1])


#update (수정)
my_list[1] = 100
print(my_list)

#remove(x)는 리스트에서 첫 번째로 나오는 x(값)을 삭제하는 함수
#삭제되고나서 떙겨져 온다.

my_list.remove(10)
print(my_list)

