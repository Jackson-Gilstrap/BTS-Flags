import turtle as t 
from Rectangle import Rectangle
from Star import Star

def createFlagBackground():
    base = Rectangle(_height=300, _length= 600)
    base.setFillColor('#0A3161')
    base.drawWithColor()
    base.updateYCor(-base.height / 1.8)
    base.updateXCor(base.length / 4)
    return base


def drawStarsInline(numStars):
    gap = 10
    star = Star(5,fillColor='white')
    for i in range(numStars):
        print(star.getStarSize())
        star.drawWithColor(180)
        t.penup()
        t.backward(gap* 2)
        t.pendown()

def turnLeftDownRight(stripe):
    t.right(90)
    t.backward(-stripe.height)
    t.left(90)

def createFlagStars(startX, startY):
    heightGap = -10
    rows = 4
    t.setposition(startX, startY)
    for lines in range(rows):
        drawStarsInline(6)
        t.penup()
        t.setposition(startX + 10, heightGap)
        t.pendown()
        heightGap += -10
        # print(heightGap)
        drawStarsInline(5)
        t.penup()
        t.setposition(startX, heightGap)
        t.pendown()
        heightGap += -10
        # print(heightGap)
    t.penup()
    t.setposition(startX, heightGap + 10)
    t.pendown()
    drawStarsInline(6)

def createFlagStripes(base):
    stripe = Rectangle(base.length / 2.5, _length=base.length *0.6)
    print(stripe.getXCor())
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
        stripe.drawWithColor()
        turnLeftDownRight(stripe)

def UsaFlag():
    base = createFlagBackground()
    createFlagStripes(base)
    createFlagStars(15, -5)

    




if __name__ == "__main__":
    t.speed('fastest')
    UsaFlag()
    t.mainloop()