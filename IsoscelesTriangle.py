from Shape import Shape
import turtle as t


class IsoscelesTriangle(Shape):
    def __init__(self, side=50, xCor=0, yCor=0,
                 fillColor='green', borderColor='black',
                 borderThickness=1, nameOfShape='Isosceles Triangle'):
        super().__init__(xCor, yCor, fillColor, borderColor, borderThickness, nameOfShape)
        self.side = side

    def setSide(self, newSize):
        self.side = newSize

    def getSide(self):
        return self.side

    def draw(self):
        t.pencolor(self.borderColor)
        t.pensize(self.borderThickness)
        numSides = 2
        t.forward(self.side)
        t.right(150)
        for side in range(numSides):
            t.forward(self.side * 0.58)
            t.right(60)

    def drawBottomTriangle(self):
        t.pencolor(self.borderColor)
        t.pensize(self.borderThickness)
        numSides = 2
        t.forward(self.side)
        t.left(150)
        for side in range(numSides):
            t.forward(self.side * 0.58)
            t.left(60)

    def drawWithColor(self):
        t.fillcolor(self.fillColor)
        t.begin_fill()
        self.draw()
        t.end_fill()

    def drawWithColorBottom(self):
        t.fillcolor(self.fillColor)
        t.begin_fill()
        self.drawBottomTriangle()
        t.end_fill()


    # def drawWithColorBottom(self):
    #     t.fillcolor(self.fillColor)
    #     t.begin_fill()
    #     self.drawBottomTriangle()
    #     t.end_fill()



if __name__ == '__main__':
    t.speed('slow')
    triangleTest = IsoscelesTriangle(borderThickness=3, side=200)
    triangleTest.draw()

    triangleTest.updateXCor(300)
    triangleTest.moveTurtle()
    triangleTest.drawWithColor()

    # t.hideturtle()
    t.mainloop()