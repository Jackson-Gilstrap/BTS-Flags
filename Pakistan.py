import turtle as t
from Rectangle import Rectangle
from Star import Star
from Moon import CrescentMoon

def BackgroundForFlag():
    Back = Rectangle(_fillColor='#3D9140')
    Back.drawWithColor()
    Back.setXCor(100)
    t.right(90)
    Back.set_Length(150)
    Back.set_height(100)
    Back.setFillColor("white")
    Back.moveTurtle()
    Back.drawWithColor()



def drawStar():
    Pstar = Star(starSize=10)
    Pstar.setFillColor("white")
    Pstar.setXCor(250)
    Pstar.setYCor(-40)
    Pstar.moveTurtle()
    Pstar.drawWithColor(angle=20)

def drawMoon():
    moon = CrescentMoon(moonSize=50, xCor=150, yCor=-50,)
    moon.moveTurtle()
    moon.draw()



if __name__== '__main__':
    t.speed('normal')
    BackgroundForFlag()
    drawStar()
    drawMoon()
    t.mainloop()
    t.hideturtle()
