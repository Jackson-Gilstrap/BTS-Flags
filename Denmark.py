import turtle as t 
from Rectangle import Rectangle
from Cross import Cross   

def DenmarkFlag(x,y):
    base = Rectangle(_xCor=x, _yCor=y)
    base.moveTurtle()
    base.setFillColor('red')
    base.drawWithColor()
    base.updateYCor(-base.height / 1.8)
    base.updateXCor(base.length / 4)
    angles = [270,90]
    cross = Cross()
    print(cross.height)
    print(cross.x_Cor, cross.y_Cor)
    t.penup()
    t.setposition(base.getXCor() , base.getYCor() - 3)
    t.pendown()
    cross.setHeight(25)
    cross.drawOutsideCrossWithColor(angles, 2, 180, 2.5, 9, 0, 'white')

if __name__== '__main__':
    DenmarkFlag(-200, 100)
    t.mainloop()
    # t.hideturtle()