import turtle as t
from Rectangle import Rectangle
def germanyFlag():
    myShape = Rectangle()
    myShape.draw()
    myShape.set_height(34)
    myShape.drawWithColor()
    myShape.updateYCor(-34)
    myShape.moveTurtle()
    myShape.setFillColor('Red')
    myShape.drawWithColor()
    myShape.updateYCor(-33)
    myShape.moveTurtle()
    myShape.setFillColor('Yellow')
    myShape.drawWithColor()

if __name__=='__main__':
    germanyFlag()
    t.mainloop()
    t.hideturtle()