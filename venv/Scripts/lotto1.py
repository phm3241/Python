# 예제 4-1 > 리스트와 루프 _로또게임(1) ***추가 이해 필요!

from random import randrange

nums = []

def checkDuplicate(num_list, target):

    result = False

    for x in num_list:
        if x == target:
            result = True
            break

    return result

#루프를 nums 가 6개가 되는 동안
while len(nums) < 6:
    #1부터 45 사이의 숫자를 뽑는다
    num = randrange(1,46)
    #뽑힌 숫자가 있는지 확인

    if checkDuplicate(nums,num) == True:
        continue

    # nums라는 리스트에 num값을 추가한다.
    nums.append(num)

print(nums)

