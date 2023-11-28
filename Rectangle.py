import turtle as t
from Shape import Shape

class Rectangle(Shape):
    def __init__(self, _xCor=0, _yCor=0, _height=150, _length=300, _fillColor='black', _borderColor='blue', _borderThickness=3):
        super().__init__(_xCor, _yCor, _fillColor, _borderColor, _borderThickness)
        self.height = _height
        self.length = _length
    
    def set_height(self, newHeight):
        self.height = newHeight

    def set_Length(self, newLength):
        self.length = newLength

    def getHeight(self):
        return self.height

    def getLength(self):
        return self.length    
    def draw(self):
        for i in range(2):
            t.forward(self.length)
            t.right(90)
            t.forward(self.height)
            t.right(90)

    def drawWithColor(self):
        t.fillcolor(self.fillColor)
        t.begin_fill()
        self.draw()
        t.end_fill()

    

if __name__ == '__main__':
    t.speed('fast')
    testRectangle = Rectangle()
    testRectangle.drawWithColor()
    t.hideturtle()
    t.mainloop()


    