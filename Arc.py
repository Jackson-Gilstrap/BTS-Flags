
import turtle as t
from Shape import Shape


class Arc(Shape):
    def __init__(self, xCor=0, yCor=0, radius=50, extent=45, fillColor='white',
                 borderColor='black', borderThickness=3, nameOfShape='Arc'):
        super().__init__(xCor, yCor, fillColor, borderColor, borderThickness, nameOfShape)

        self.extent = extent
        self.radius = radius

    def setRadius(self, radius):
        self.radius = radius

    def setExtent(self, extent):
        self.extent = extent

    def getRadius(self):
        return self.radius

    def getExtent(self):
        return self.extent

    def draw(self):
        t.pencolor(self.borderColor)
        t.pensize(self.borderThickness)

        t.pendown()
        t.circle(self.radius, self.extent)
        t.penup()

    def drawWithColor(self):
        t.fillcolor(self.fillColor)
        t.begin_fill()
        self.draw()
        t.end_fill()


if __name__ == '__main__':
    # Testing
    myArc = Arc()
    myArc.draw()
    myArc.setFillColor('red')
    myArc.drawWithColor()
    myArc.setName('This is my new Arc!')
    print(myArc.getName())
