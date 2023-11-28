import turtle as t 
from Rectangle import Rectangle
from Cross import Cross  

def createFlagBackground(x,y):
    base = Rectangle(_xCor=x, _yCor=y)
    base.moveTurtle()
    base.setFillColor('#001489')
    base.drawWithColor()
    base.updateYCor(-base.height / 1.8)
    base.updateXCor(base.length / 4)
    return base
def createFlagCross(base, angles):
    cross = Cross()
    cross.setHeight(10)
    t.penup()
    t.forward(base.length / 9.5)
    t.right(90)
    t.forward(base.length /7.4)
    t.pendown()
    cross.drawOutsideCrossWithColor(angles,3,90,3,3,270, 'white')
    t.penup()
    t.right(180)
    t.setposition(base.length / 4.21, 0)
    t.left(90)
    t.pendown()

def turnLeftDownRight(stripe):
    t.left(90)
    t.forward(-stripe.height)
    t.right(90)
def createFlagStripes(base):
    stripe = Rectangle(_xCor= base.getXCor() - 2.5,_yCor=base.getYCor()+ 82.2, _length=base.length *0.76)
    stripe.moveTurtle()
    for i in range(5):
        stripe.setFillColor('#001489')
        stripe.set_height(base.height / 10)
        stripe.drawWithColor()
        turnLeftDownRight(stripe)
        stripe.setFillColor('white')
        i += 1
        if i == 3:
            stripe.set_Length(base.length)
            t.penup()
            t.backward(base.length /4.21)
            t.pendown()
        stripe.drawWithColor()
        turnLeftDownRight(stripe)

def GreeceFlag(x,y,angles):
    base = createFlagBackground(x,y)
    createFlagCross(base, angles)
    createFlagStripes(base)
    

    


if __name__ == '__main__':
    angles = (180, 0)
    t.speed('fast')
    GreeceFlag(angles)
    t.mainloop()