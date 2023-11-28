import turtle as t
from Rectangle import Rectangle
def germanyFlag(x,y):
    myShape = Rectangle(_xCor= x, _yCor= y)
    myShape.moveTurtle()
    myShape.draw()
    print(myShape.height)
    myShape.set_height(50)
    myShape.drawWithColor()
    myShape.updateYCor(-myShape.getHeight())
    myShape.moveTurtle()
    myShape.setFillColor('Red')
    myShape.drawWithColor()
    myShape.updateYCor(-myShape.getHeight())
    myShape.moveTurtle()
    myShape.setFillColor('Yellow')
    myShape.drawWithColor()

if __name__=='__main__':
    germanyFlag(-200,100)
    t.mainloop()
    # t.hideturtle()