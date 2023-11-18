import turtle as t 
from Rectangle import Rectangle
from Cross import Cross   

def DenmarkFlag():
    base = Rectangle()
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

if __name__== '__main__':
    DenmarkFlag()
    t.mainloop()
    t.hideturtle()