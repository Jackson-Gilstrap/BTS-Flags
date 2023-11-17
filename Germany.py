import turtle as t
from Rectangle import Rectangle
def germanyFlag():
    myShape = Rectangle()
    myShape.draw()
    print(myShape.height)
    myShape.set_height(50)
    myShape.drawWithColor()
    myShape.updateYCor(-50)
    myShape.moveTurtle()
    myShape.setFillColor('Red')
    myShape.drawWithColor()
    myShape.updateYCor(-50)
    myShape.moveTurtle()
    myShape.setFillColor('Yellow')
    myShape.drawWithColor()

if __name__=='__main__':
    germanyFlag()
    t.mainloop()
    t.hideturtle()