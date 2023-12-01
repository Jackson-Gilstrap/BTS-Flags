import turtle as t
from EthiopianStar import EthiopianStar
from Rectangle import Rectangle

def BackGround():
    Back = Rectangle(_fillColor="#3D9140")
    Back.drawWithColor()
    Back.set_height(50)
    Back.setFillColor("yellow")
    Back.setYCor(-50)
    Back.moveTurtle()
    Back.drawWithColor()
    Back.updateYCor(-50)
    Back.moveTurtle()
    Back.setFillColor("red")
    Back.drawWithColor()

def draw_circle(color, radius):
    t.begin_fill()
    t.fillcolor(color)
    t.penup()
    t.goto(150, -130)
    t.circle(radius)
    t.end_fill()

def Drawstar():
    Estar = EthiopianStar(starSize=50, xCor=150, yCor=-50)
    Estar.setBorderColor('yellow')
    Estar.moveTurtle()
    Estar.draw()



def YellowDashes(x, y):
    t.penup()
    t.right(90)
    t.update()








if __name__== '__main__':
    t.speed('normal')
    BackGround()
    draw_circle("navy", 60)
    Drawstar()
    Draw
    t.mainloop()
    t.hideturtle()

