## 두 사람이 주사위를 던져서 더 큰 수가 나오면 이기는 게임 ##
## A가 이기거나 B가 이기거나 비기는 결과 ##

import random

## 변수 선언 ##
A = random.randrange(1,7)
B = random.randrange(1,7)

print("A의 주사위 숫자는 %d입니다."%A)
print("B의 주사위 숫자는 %d입니다."%B)

if A>B:
    print("A가 이겼습니다.")
elif A<B:
    print("B가 이겼습니다.")
else:
    print("비겼습니다.")
