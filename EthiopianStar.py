import turtle as t

from Shape import Shape


class EthiopianStar(Shape):
    def __init__(self, starSize=50, xCor=0, yCor=0,
                 fillColor='red', borderColor='yellow',
                 borderThickness=10, nameOfShape='Stars'):
        super().__init__(xCor, yCor, fillColor, borderColor, borderThickness, nameOfShape)
        self.starSize = starSize

    def setStarSize(self, newSize):
        self.starSize = newSize

    def getStarSize(self):
        return self.starSize

    def drawSawTooth(self):
        pass

    def draw(self):
        t.pencolor(self.borderColor)
        sides = 5
        angle = 144
        for i in range(sides):
            t.forward(self.starSize)
            t.right(angle)
            t.forward(self.starSize)


    def drawWithColor(self):
        t.fillcolor(self.fillColor)
        t.begin_fill()
        self.draw()
        t.end_fill()


if __name__ == '__main__':
    testStar = EthiopianStar()
    testStar.draw()
    testStar.drawWithColor()


    t.hideturtle()
    t.mainloop()
