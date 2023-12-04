import turtle as t 
from Rectangle import Rectangle
from Star import Star

def createFlagBackground(x,y):
    t.seth(0)
    base = Rectangle(_xCor= x, _yCor= y)
    base.moveTurtle()
    base.setFillColor('#0A3161')
    base.drawWithColor()
    base.updateYCor(-base.height / 1.8)
    base.updateXCor(base.length / 4)
    return base


def drawStarsInline(numStars, base):
    gap = 10
    star = Star(5, xCor = base.getXCor() - 60, yCor= base.getYCor() + 78,fillColor='white')
    for i in range(numStars):
        star.drawWithColor(180)
        t.penup()
        t.backward(gap* 2)
        t.pendown()

def turnLeftDownRight(stripe):
    t.right(90)
    t.backward(-stripe.height)
    t.left(90)

def createFlagStars(startX, startY,base):
    heightGap = -20
    rows = 4
    t.penup()
    t.setposition(startX, startY)
    t.pendown()
    for sixStarLines in range(rows):
        drawStarsInline(6,base)
        t.penup()
        t.setposition(startX, startY + heightGap)
        heightGap += -20
    heightGap = -10
    t.penup()
    t.setposition(startX + 10, startY + heightGap)
    t.pendown()
    for fiveStarLines in range(rows):
        drawStarsInline(5,base)
        t.penup()
        t.setposition(startX + 10, startY + heightGap -20) 
        t.pendown()
        heightGap += -20
    t.penup()
    t.setposition(startX, startY + (heightGap + 13))
    t.pendown()
    drawStarsInline(6,base)
  
def createFlagStripes(base):
    stripe = Rectangle(_xCor=base.getXCor() + 45, _yCor=base.getYCor() + 83, _length=base.getLength() *0.6)
    stripe.moveTurtle()
    t.penup()
    t.setposition(stripe.getXCor(),stripe.getYCor())
    t.pendown()
    for i in range(8):
        stripe.setFillColor('#B31942')
        stripe.set_height(base.height / 15)
        stripe.drawWithColor()
        turnLeftDownRight(stripe)
        stripe.setFillColor('white')
        i += 1
        if i == 5:
            stripe.set_Length(base.length)
            t.penup()
            t.backward(base.length /2.5)
            t.pendown()
        stripe.drawWithColor()
        turnLeftDownRight(stripe)

def UsaFlag(x,y):
    base = createFlagBackground(x,y)
    createFlagStripes(base)
    createFlagStars(base.getXCor() -60, base.getYCor() + 78,base)

    




if __name__ == "__main__":
    t.speed('fastest')
    UsaFlag(-200,100)
    t.mainloop()