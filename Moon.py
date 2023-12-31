
import turtle as t

from Shape import Shape
from Arc import Arc


class CrescentMoon(Shape):
    def __init__(self, moonSize=100, xCor=0, yCor=0,
                 fillColor='white', borderColor='white',
                 borderThickness=1, nameOfShape='Crescent Moon'):
        super().__init__(xCor, yCor, fillColor, borderColor, borderThickness, nameOfShape)
        self.size = moonSize

    def setMoonSize(self, newSize):
        self.size = newSize

    def getMoonSize(self):
        return self.size

    def draw(self, rotation):
        t.pencolor(self.borderColor)
        t.pensize(self.borderThickness)
        t.seth(rotation)
        partOfTheMoon = Arc(xCor=self.xCor, yCor=self.yCor, radius=self.size, extent=200, borderColor=self.borderColor)
        t.right(180)

        partOfTheMoon.draw()
        partOfTheMoon.setRadius(-partOfTheMoon.getRadius())

        t.right(197)
        partOfTheMoon.setExtent(160)
        partOfTheMoon.draw()

    def drawWithColor(self,rotation):
        t.fillcolor(self.fillColor)
        t.begin_fill()
        self.draw(rotation)
        t.end_fill()


if __name__ == '__main__':
    t.speed('slow')
    t.title('Jermaine Williams - Crescent Moon')
    t.Screen().bgcolor('black')
    t.Screen().setup(height=1.0, width=1.0)

    myMoon = CrescentMoon(xCor=0, yCor=100, borderThickness=1, moonSize=100, borderColor='white', fillColor='white')
    myMoon.setFillColor('pink')
    myMoon.setBorderColor('pink')
    myMoon.drawWithColor(30)



    t.hideturtle()
    t.mainloop()
