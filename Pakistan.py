import turtle as t
from Rectangle import Rectangle
from Star import Star
from Moon import CrescentMoon

def createFlagBackground(x,y):
    base= Rectangle(_xCor=x, _yCor=y)
    base.moveTurtle()
    base.setFillColor('#115740')
    base.drawWithColor()
    return base

def drawFlagStripe(base):
    stripe = Rectangle(base.getXCor(),base.getYCor(),150,70, 'white','white')
    stripe.drawWithColor()


def drawStar(base):
    star = Star(xCor=base.getXCor()/8, yCor=base.getYCor()/ 2.1)
    star.moveTurtle()
    star.setStarSize(10)
    star.setFillColor("white")
    star.setBorderColor('white')
    star.drawWithColor(-40)

def drawMoon(base):
    moon = CrescentMoon(moonSize=50, xCor=base.getXCor()/4.5, yCor=base.getYCor()/1.5)
    moon.moveTurtle()
    moon.setFillColor('white')
    moon.drawWithColor(20)

def PakistanFlag(x,y):
    base = createFlagBackground(x,y)
    drawFlagStripe(base)
    drawMoon(base)
    drawStar(base)


if __name__== '__main__':
    t.speed('normal')
    PakistanFlag(-200,100)
    t.mainloop()
    t.hideturtle()
