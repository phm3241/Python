# 예제 2 > 리스트 기준값으로 정렬하기

#리스트 만들고
nums = [10,20,30,90,88,50,60,70,80]

#변수 선언하고
score = 67


# 기준을 주고 정렬하는 메서드.sort로 정렬.
# abs는 절대값으로 만들어 주는 것.
nums.sort(key= lambda num: abs(score - num))

print(nums)
