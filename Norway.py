import turtle as t 
from Rectangle import Rectangle
from Cross import Cross

def norwayFlag():
    base = Rectangle()
    base.setFillColor('red')
    base.drawWithColor()
    base.updateYCor(-base.height / 1.8)
    base.updateXCor(base.length / 4)
    angles = [270,180,90]
    cross = Cross()
    t.penup()
    t.setposition(base.getXCor() , base.getYCor())
    t.pendown()
    cross.setHeight(15)
    cross.drawOutsideCrossWithColor(angles)
    t.penup()
    t.setposition(base.getXCor(),base.getYCor() + 2.2)
    t.pendown()
    cross.setHeight(cross.height / 2 )
    cross.drawInsideCrossWithColor(angles)

if __name__== '__main__':
    norwayFlag()
    t.mainloop()
    t.hideturtle()