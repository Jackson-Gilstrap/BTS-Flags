import turtle as t
from Rectangle import Rectangle

def drawingJapanBackground():
    Background = Rectangle()
    Background.setFillColor('white')
    Background.drawWithColor()

def draw_circle(color,radius):
    t.begin_fill()
    t.fillcolor(color)
    t.penup()
    t.goto(150, -120)
    t.circle(radius)
    t.end_fill()

if __name__ == '__main__':
    drawingJapanBackground()
    draw_circle("black", 50)
    draw_circle("red", 50)
    t.mainloop()
    t.hideturtle()


