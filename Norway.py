import turtle as t 
from Rectangle import Rectangle
from Cross import Cross
def createFlagBackground(x,y):
    t.seth(0)
    base = Rectangle(_xCor=x, _yCor=y)
    base.moveTurtle()
    base.setFillColor('red')
    base.drawWithColor()
    base.updateYCor(-base.height / 1.8)
    base.updateXCor(base.length / 4)
    base.moveTurtle()
    return base

def createFlagCross(base):
    angles = (270,90)
    cross = Cross(_xCor= base.getXCor(), _yCor=base.getYCor())
    cross.moveTurtle()
    t.penup()
    t.setposition(cross.getXCor() , cross.getYCor() - 3)
    t.pendown()
    cross.setHeight(25)
    cross.drawWithColor(angles, 2, 180, 2.5, 9, 0, 'white')
    t.penup()
    t.setposition(base.getXCor() - 6,base.getYCor() + 2.2)
    t.pendown()
    cross.setHeight(cross.height / 2 )
    cross.drawWithColor(angles, 4.5, 180, 5.5, 18.5, 0, 'navy')
def norwayFlag(x,y):
    base = createFlagBackground(x,y)
    createFlagCross(base)
    
    

if __name__== '__main__':
    t.speed('fastest')
    norwayFlag(-200, 100)
    norwayFlag(400, 100)
    t.mainloop()
    t.hideturtle()