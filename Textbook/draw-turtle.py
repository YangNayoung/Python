import turtle
import random

## 함수 선언 부분 ##

##기능1 구현##
def screenLeftClick(x, y) :
    global r, g, b
    #global r, g, b 안써도 ok
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)

##기능2 구현##
def screenRigthClick(x, y) :
    turtle.penup()
    turtle.goto(x, y)

##기능3 구현##
def screenMidClick(x, y) :
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()


## 변수 선언 부분 ##
pSize = 10
r, g, b = 0.0, 0.0, 0.0 #검정#

## 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRigthClick, 3)

turtle.done()
