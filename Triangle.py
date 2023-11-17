"""

"""
from Shape import Shape
import turtle as t


class Triangle(Shape):
    def __init__(self, side=50, xCor=0, yCor=0,
                 fillColor='green', borderColor='green',
                 borderThickness=1, nameOfShape='Tree'):
        super().__init__(xCor, yCor, fillColor, borderColor, borderThickness, nameOfShape)
        self.side = side

    def setSide(self, newSize):
        self.side = newSize

    def getSide(self):
        return self.side

    def draw(self):
        t.pencolor(self.borderColor)
        t.pensize(self.borderThickness)
        numSides = 3
        for eachSide in range(numSides):
            t.forward(self.side)
            t.right(120)

    def drawWithColor(self):
        t.fillcolor(self.fillColor)
        t.begin_fill()
        self.draw()
        t.end_fill()


if __name__ == '__main__':
    t.speed('fastest')
    t.title('Jermaine Williams - Triangle')

    triangleTest = Triangle(borderThickness=3, side=200)
    triangleTest.draw()

    triangleTest.updateXCor(300)
    triangleTest.moveTurtle()
   # triangleTest.drawWithColor()

    # t.hideturtle()
    t.mainloop()
