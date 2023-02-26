import turtle
import random

t1 = turtle.Turtle()
t2 = turtle.Turtle()
s = turtle.Screen()


def turtle_set_up():
    t1.hideturtle()
    t2.hideturtle()
    s.tracer(1, 0)
    s.onclick(get_mouse_click)   # define the 'click' event callback


def draw():
    for i in range(2):
        t1.fd(400)
        t1.lt(90)
        t1.fd(400)
        t1.lt(90)


def drawbox():
    global box                   # store box coordinates as global variable
    X = random.randint(0, 350)   # so that they are available for testing
    Y = random.randint(0, 350)   # in the mouse click callback
    box = (X, Y, X+50, Y+50)
    t2.clear()                   # clear previous box before drawing new one
    t2.penup()
    t2.goto(X, Y)
    t2.pendown()
    for i in range(2):
        t2.fd(50)
        t2.lt(90)
        t2.fd(50)
        t2.lt(90)
    s.ontimer(drawbox, 3000)     # define timer event callback


def get_mouse_click(x, y):
    if box[0] <= x <= box[2] and box[1] <= y <= box[3]:
        print('You clicked!')


def starter():
    turtle_set_up()
    draw()
    drawbox()


starter()
