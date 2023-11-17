import turtle as t 
from Rectangle import Rectangle
from Cross import Cross

def norwayFlag():
    base = Rectangle()
    base.set_height(200)
    base.set_Length(400)
    base.setFillColor('red')
    base.drawWithColor()
    base.updateYCor(-base.height / 1.8)
    base.updateXCor(base.length / 4)
    angles = [270,180,90]
    cross = Cross()
    # cross.setHeight(200)
    print(cross.height)
    t.penup()
    t.setposition(base.getXCor() , base.getYCor())
    t.pendown()
    cross.setHeight(200)
    cross.drawOutsideCrossWithColor(angles,'white')
    t.penup()
    t.setposition(base.getXCor(),base.getYCor() + 2.2)
    t.pendown()
    cross.setHeight(cross.height / 2 )
    cross.drawInsideCrossWithColor(angles, 'navy')

if __name__== '__main__':
    norwayFlag()
    t.mainloop()
    t.hideturtle()