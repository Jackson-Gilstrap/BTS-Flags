import turtle as t 
from Rectangle import Rectangle
from Cross import Cross   

def createFlagBackGround(x,y):
    t.seth(0)
    base = Rectangle(_xCor=x, _yCor=y)
    base.moveTurtle()
    base.setFillColor('red')
    base.drawWithColor()
    base.updateYCor(-base.height / 1.8)
    base.updateXCor(base.length / 4)
    return base

def createFlagCross(base):
    angles = [270,90]
    cross = Cross()
    t.penup()
    t.setposition(base.getXCor() , base.getYCor() - 3)
    t.pendown()
    cross.setHeight(25)
    cross.drawWithColor(angles, 2, 180, 2.5, 9, 0, 'white')

def DenmarkFlag(x,y):
    base = createFlagBackGround(x,y)
    createFlagCross(base)
   
if __name__== '__main__':
    DenmarkFlag(-200, 100)
    t.mainloop()
    t.hideturtle()