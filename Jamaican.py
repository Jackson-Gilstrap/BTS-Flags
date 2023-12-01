import turtle as t
from IsoscelesTriangle import IsoscelesTriangle
from Triangle import Triangle
from Rectangle import Rectangle

def JamaicanFlagBackGround():
    Flag = Rectangle()
    Flag.setFillColor('yellow')
    Flag.drawWithColor()

def JamaicanTriangle(base):
    triangle = IsoscelesTriangle(xCor=65, yCor=0)
    triangle.setSide(newSize=180)
    triangle.moveTurtle()
    triangle.drawWithColor()
    triangle.setYCor(-150)
    t.right(90)
    triangle.moveTurtle()
    triangle.drawWithColorBottom()

def JamaicanSideTriangle():
    triangle = Triangle(yCor=-125, fillColor='black')
    triangle.setSide(newSize=100)
    t.left(180)
    triangle.moveTurtle()
    triangle.drawWithColor()
    triangle.setXCor(300)
    triangle.moveTurtle()
    triangle.drawRightWithColor()


if __name__ == '__main__':
    t.speed('slow')
    JamaicanFlagBackGround()
    JamaicanTriangle(300)
    JamaicanSideTriangle()
    t.mainloop()
    t.hideturtle()

