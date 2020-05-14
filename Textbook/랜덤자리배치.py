#학급 자리 랜덤하게 배치하기
# 몇번까지 있는가
# 결번은 몇번인가
# 자리 배정해서 출력하자
import random

max = int(input("몇 번까지 있는가? : "))
student_number = list(range(max+1))
student_number.remove(0)    #0번 제외
exclude_list = []

while(True):
    n = input("제외할 번호를 입력하세요 : ")
    if n == "":
        break
    exclude_list.append(int(n))

for n in exclude_list:
    if n in student_number:
        student_number.remove(n)

random.shuffle(student_number)
print("자리\t번호")
for i, value in enumerate(student_number):
    print("{}\t{}".format(i+1, value))
