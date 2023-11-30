import turtle as t
from Triangle import Triangle
from Rectangle import Rectangle

def JamaicanFlagBackGround():
    Flag = Rectangle()
    Flag.setFillColor('yellow')
    Flag.drawWithColor()

def JamaicanTriangle(base):
    triangle = Triangle(xCor=65, yCor=-0)
    triangle.setSide(newSize=180)
    triangle.moveTurtle()
    triangle.drawWithColor()


if __name__ == '__main__':
    JamaicanFlagBackGround()
    JamaicanTriangle(300)
    t.mainloop()
    t.hideturtle()

