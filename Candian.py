import turtle as t
from Rectangle import Rectangle

def BackgroundOfFlag(x, y):
    Back = Rectangle(_xCor=x, _yCor=y, _fillColor='white')
    Back.setFillColor('red')
    Back.moveTurtle()
    Back.drawWithColor()
    Back.updateXCor(100)
    Back.moveTurtle()
    Back.setFillColor('White')
    Back.set_height(150)
    Back.set_Length(100)
    Back.drawWithColor()
    Back.setYCor(-75)
    Back.moveTurtle()

def drawRedLeaf():
    t.color("red")
    t.begin_fill()

    # Draw the leaf outline
    for _ in range(2):
        t.forward(100)
        t.right(45)
        t.forward(100)
        t.right(135)

    t.end_fill()


if __name__ == "__main__":
    t.speed('slow')
    BackgroundOfFlag(-300, 0)
    drawRedLeaf()
    t.mainloop()


