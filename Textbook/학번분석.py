#학번 -> 학년 학과 반 번호
# 학번 입력
# 학년 학과 반 번호 출력
majors = [["뉴미디어소프트웨어", "뉴미디어웹솔루션", "뉴미디어디자인"],
["뉴미디어소프트웨어", "뉴미디어웹솔루션", "뉴미디어디자인"],
["인터랙티브미디어과", "뉴미디어디자인과", "뉴미디어솔루션과"]]
student_number = input("학번을 입력하세요 : ")
grade = student_number[0]
classroom = student_number[1]
number = student_number[2:]
number = str(int(number))
major = majors[int(grade)-1][(int(classroom)-1)//2]
print("{}학년 {}과 {}반 {}번입니다.".format(grade, major, classroom, number))

# 학년 반을 한꺼번에 11, 12 / 13, 14 / 15, 16 // 21, 22 / 23, 24 / 25, 26 // 31, 32 / 33, 34 / 35, 36
# 학년 짜르고 반 짜르고
#  1, 2 / 3
#    1, 2 / 3, 4 / 5, 6
