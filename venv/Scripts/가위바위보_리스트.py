# 예제 3 > 리스트와 루프_가위바위보

# 사용자와 컴퓨터는 가위바위보 게임을 합니다
# 가위-S / 바위-R / 보 -P를 입력하면 컴퓨터는 임의의 데이터를 발생시켜서
# 게임을 진행하고, 결과를 보여줍니다.
# 먼저 결과값을 리스트에 담아보자.
# 게임을 10번 진행했을때 사용자가 몇번의 승리와 패배, 비겼는지를 출력해줄것


from random import randrange

result_list = []

for x in range(10):
    user_num = int(input('가위 0, 바위 1, 보 2\n' ))
    com_num = randrange(0,3)


    if user_num > com_num :
        com_num +=3

    gap = com_num - user_num

    result = ''

    if gap == 2:
        result_str = "U"

    elif gap == 1:
        result_str = "C"

    else :
        result_str = "D"


    result_list.append(result_str)

print (result_list)

print("당신은," , result_list.count("U"),"번 이겼습니다")
print("당신은," , result_list.count("C"),"번 졌습니다")
print("당신은," , result_list.count("D"),"번 비겼습니다")