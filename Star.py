import turtle as t

from Shape import Shape


class Star(Shape):
    def __init__(self, starSize=50, xCor=0, yCor=0,
                 fillColor='white', borderColor='black',
                 borderThickness=1, nameOfShape='Stars'):
        super().__init__(xCor, yCor, fillColor, borderColor, borderThickness, nameOfShape)
        self.starSize = starSize

    def setStarSize(self, newSize):
        self.starSize = newSize

    def getStarSize(self):
        return self.starSize


    def draw(self, rotation):
        t.pencolor(self.borderColor)
        sides = 5
        angle = 360 / sides
        t.seth(rotation)
        for i in range(sides):
            t.forward(self.starSize)
            t.right(angle)
            t.forward(self.starSize)
            t.left(angle * 2)

    


    def drawWithColor(self,rotation):
        t.fillcolor(self.fillColor)
        t.begin_fill()
        self.draw(rotation)
        t.end_fill()


if __name__ == '__main__':
    testStar = Star()
    testStar.draw(180)
    t.hideturtle()
    t.mainloop()
