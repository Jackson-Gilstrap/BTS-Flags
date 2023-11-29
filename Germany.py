import turtle as t
from Rectangle import Rectangle

def createFlagBackground(x,y):
    base = Rectangle(_xCor= x, _yCor= y)
    base.moveTurtle()
    base.draw()
    return base

def drawFlagStripes(base):
    base.set_height(50)
    base.drawWithColor()
    base.updateYCor(-base.getHeight())
    base.moveTurtle()
    base.setFillColor('Red')
    base.drawWithColor()
    base.updateYCor(-base.getHeight())
    base.moveTurtle()
    base.setFillColor('Yellow')
    base.drawWithColor()
def germanyFlag(x,y):
    base = createFlagBackground(x,y)
    drawFlagStripes(base)
    

if __name__=='__main__':
    germanyFlag(-200,100)
    t.mainloop()
    # t.hideturtle()