
import random

#start <= x <= end 정수 랜덤
i = random.randint(1,2)
print(i)

#start <= x < end, step 정수 랜덤
i = random.randrange(1, 100+1, 2)
print(i)

#0 <= x < end 정수 랜덤
i = random.randrange(100+1)
print(i)

#리스트, 튜플, 집합에서 샘플링
numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = random.sample(numlist, 3)
print(s)

fruites = ("귤", "사과", "배", "포도", "딸기")
s = random.sample(fruites, 3)
print(s)

sites = {"google", "daum", "apple", "naver"}
s = random.sample(sites, 3)
print(s)
