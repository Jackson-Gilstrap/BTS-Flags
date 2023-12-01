import turtle as t
from IsoscelesTriangle import IsoscelesTriangle
from Triangle import Triangle
from Rectangle import Rectangle

def JamaicanFlagBackGround():
    Flag = Rectangle()
    Flag.setFillColor('yellow')
    Flag.drawWithColor()

def JamaicanTriangle():
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

def JamaicaFlag():
    JamaicanFlagBackGround()
    JamaicanTriangle()
    JamaicanSideTriangle()
    
if __name__ == '__main__':
    t.speed('slow')
    JamaicaFlag()
    t.mainloop()
    t.hideturtle()

