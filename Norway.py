import turtle as t 
from Rectangle import Rectangle
from Cross import Cross

def norwayFlag(x,y):
    base = Rectangle(_xCor=x, _yCor=y)
    base.moveTurtle()
    base.setFillColor('red')
    base.drawWithColor()
    base.updateYCor(-base.height / 1.8)
    base.updateXCor(base.length / 4)
    angles = [270,90]
    cross = Cross()
    print(cross.height)
    t.penup()
    t.setposition(base.getXCor() , base.getYCor() - 3)
    t.pendown()
    cross.setHeight(25)
    cross.drawOutsideCrossWithColor(angles, 2, 180, 2.5, 9, 0, 'white')
    t.penup()
    t.setposition(base.getXCor() - 6,base.getYCor() + 2.2)
    t.pendown()
    cross.setHeight(cross.height / 2 )
    cross.drawInsideCrossWithColor(angles, 4.5, 180, 5.5, 18.5, 0, 'navy')

if __name__== '__main__':
    norwayFlag(-200, 100)
    t.mainloop()
    t.hideturtle()