import turtle as t
from Rectangle import Rectangle
from Circle import Circle

def createFlagBackground(x,y):
    t.seth(0)
    base = Rectangle(_xCor=x, _yCor=y)
    base.moveTurtle()
    base.setFillColor('white')
    base.drawWithColor()
    return base

def createFlagCircle(base):
    t.seth(0)
    circle = Circle(base.getXCor() + base.getLength() /2, (base.getYCor() - base.getHeight() /2) - 50)
    circle.moveTurtle()
    circle.setFillColor('red')
    circle.setBorderColor('red')
    circle.drawWithColor()
def JapanFlag(x,y):
    base = createFlagBackground(x,y)
    createFlagCircle(base)

if __name__ == '__main__':
    JapanFlag(-200, 100)
    t.mainloop()
    t.hideturtle()


