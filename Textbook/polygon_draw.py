import turtle
t = turtle.Turtle()
t.shape("turtle")

s = input("그리려는 도형을 입력하시오(사각형 또는 원) : ")
if s == "사각형" :
    w = int(input("가로: "))
    h = int(input("세로: "))

    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)

elif s == "원" :
    r = int(input("원의 반지름 : "))
    t.circle(r)
else:
    print("잘못입력했어요")
