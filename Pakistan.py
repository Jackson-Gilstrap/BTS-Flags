import turtle as t
import time
from Rectangle import Rectangle

def drawStar(x,y,color,length):
    t.goto(x,y)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.color(color)
    for turn in range(0,5):
        t.forward(length)
        t.right(144)
    t.end_fill()
    t.penup()
def drawCircle(x, y, color, radius):
    t.goto(x,y)
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def