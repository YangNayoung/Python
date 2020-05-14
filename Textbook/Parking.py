# 주차 시간을 분으로 입력받아서 주차 요금을 계산해서 출력하는 프로그램을 작성하시오.
# 주차요금은 최초 30분은 2000원, 10분당 1000원씩 계산
# 하루 최대 25000원
# 주차 시간은 24시간을 넘을 수 없다
# +0을 입력할 때까지 무한 반복
# +시:분 형식, 분 형식 둘다 가능하도록...
import sys

while(True):
    minutes = input("주차한 시간을 입력하세요 : ")
    if minutes == "0":
        sys.exit()
    if minutes.find(":") == -1:
        minutes = int(minutes)
    else:
        # 시:분 형식도 지원하자
        hm = minutes.split(":")
        hours = int(hm[0])
        minutes = int(hm[1])
        minutes += hours*60

    # 24시간을 넘을 수 없음
    if minutes > 24*60:
        print("24시간 이상 넘게 주차할 수 없습니다.")
    else:
        # 기본 2000원
        result = 2000
        # 10분당 1000원
        m = (minutes-30)//10
        result += m*1000
        # 짜투리 시간있으면 1000원
        if (minutes-30) % 10 != 0:
            result += 1000
        # 25000원 초과하면 25000원
        if result > 25000:
            print("25000원을 넘을 수 없습니다.")
            result = 25000

        print("주차요금은 {}원입니다.".format(result))
