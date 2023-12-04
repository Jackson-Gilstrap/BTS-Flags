import turtle as t
from IsoscelesTriangle import IsoscelesTriangle
from Triangle import Triangle
from Rectangle import Rectangle

def JamaicanFlagBackGround(x,y):
    t.seth(0)
    base = Rectangle(_xCor=x, _yCor=y)
    base.moveTurtle()
    base.setFillColor('yellow')
    base.drawWithColor()
    return base

def JamaicanTriangle(base):
    triangle = IsoscelesTriangle(xCor=base.getXCor()/1.4, yCor=base.getYCor())
    triangle.setSide(newSize=180)
    triangle.moveTurtle()
    triangle.drawWithColor()
    triangle.setYCor(base.getYCor()*2.5)
    t.right(90)
    triangle.moveTurtle()
    triangle.drawWithColorBottom()

def JamaicanSideTriangle(base):
    triangle = Triangle(xCor=base.getXCor(), yCor=base.getYCor() *2.25, fillColor='black')
    triangle.setSide(newSize=100)
    t.left(180)
    triangle.moveTurtle()
    triangle.drawWithColor()
    triangle.setXCor(base.getXCor() + base.getLength())
    triangle.moveTurtle()
    triangle.drawRightWithColor()

def JamaicaFlag(x,y):
    base = JamaicanFlagBackGround(x,y)
    JamaicanTriangle(base)
    JamaicanSideTriangle(base)
    
if __name__ == '__main__':
    t.speed('fastest')
    JamaicaFlag(-200, -100)
    t.mainloop()
    t.hideturtle()

