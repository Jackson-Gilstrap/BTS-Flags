import turtle as t 
from Shape import Shape

class Cross(Shape):
    def __init__(self, _height= 50, _xCor= 0, _yCor=0, _fillColor='grey', _borderColor='black', _borderThickness=3):
      
        super().__init__(_xCor,_yCor,_fillColor, _borderColor, _borderThickness)
        self.height = _height

    def setHeight(self, newHeight):
         self.height = newHeight
        
    def getHeight(self):
         return self.height
         
    def drawPinOfCross(self, multiplier, angle):
            t.seth(angle)
            t.forward(self.height * multiplier)
            t.right(90)
            t.forward(self.height)
            t.right(90)
            t.forward(self.height * multiplier)

    def draw(self, angles,firstPinLength, firstPinAngle, sidePinLength, longPinLength, longPinAngle):
        self.drawPinOfCross(sidePinLength, angles[0])
        self.drawPinOfCross(firstPinLength, firstPinAngle)
        self.drawPinOfCross(sidePinLength, angles[1])
        self.drawPinOfCross(longPinLength, longPinAngle)

    def drawWithColor(self,angles,firstPinLength, firstPinAngle, sidePinLength, longPinLength, longPinAngle, color):
         t.fillcolor(color)
         t.begin_fill()
         self.draw(angles, firstPinLength, firstPinAngle, sidePinLength, longPinLength, longPinAngle)
         t.end_fill()
         
           
        

    

if __name__=='__main__':
    angles = (270,90)
    cross = Cross()
    cross.drawWithColor(angles, 4, 180, 2.5, 9.5, 0, 'blue')
    cross.setXCor(-cross.height / 4)
    cross.setYCor(cross.height / 4)
    cross.moveTurtle()
    cross.setHeight(cross.height / 2 )
    cross.drawWithColor(angles, 8.5, 180, 5.5, 19.5, 0, 'red')
    t.mainloop()
    t.hideturtle()