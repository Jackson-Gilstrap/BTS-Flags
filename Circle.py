"""

   @ Author: Dr. Romas James Hada

"""
import turtle as t

from Shape import Shape


class Circle(Shape):
    def __init__(self, _xCor=0, _yCor=0, _radius=50, _fillColor='white',
                 _borderColor='black', _borderThickness=3, _nameOfShape='Circle'):
        super().__init__(_xCor, _yCor, _fillColor, _borderColor, _borderThickness, _nameOfShape)

        self.radius = _radius

    def getRadius(self):
        return self.radius

    def draw(self):
        t.pencolor(self.borderColor)
        t.pensize(self.borderThickness)

        t.pendown()
        t.circle(self.radius)
        t.penup()

    def drawWithColor(self):
        t.fillcolor(self.fillColor)
        t.begin_fill()
        self.draw()
        t.end_fill()


if __name__ == '__main__':
    # Testing
    myCircle = Circle(_nameOfShape='This is a Circle.')
    myCircle.draw()
    myCircle.setFillColor('red')
    myCircle.drawWithColor()
    print(myCircle.getName())
