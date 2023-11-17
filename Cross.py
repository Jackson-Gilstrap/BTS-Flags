import turtle as t 
from TurtleProperties import TurtleProperties as tp
# might violate dry principle try and draw one cross then make a new cross class to draw the second smaller cross
class Cross():
    def __init__(self, _height= 50, _xCor= 0, _yCor=0, _fillColor='grey'):
      
        self.height = _height
        self.x_Cor = _xCor
        self.y_Cor = _yCor
        self.fillColor = _fillColor
        self.borderColor = _fillColor

    def setHeight(self, newHeight):
         self.height = newHeight
    def setFillColor(self, newFillColor):
         self.fillColor = newFillColor
    

    def drawPinOfCross(self, multiplier, angle):
            t.seth(angle)
            t.forward(self.height * multiplier)
            t.right(90)
            t.forward(self.height)
            t.right(90)
            t.forward(self.height * multiplier)
        

    def drawOutsideCross(self, angles,firstPinLength, firstPinAngle, sidePinLength, longPinLength, longPinAngle):
        self.drawPinOfCross(sidePinLength, angles[0])
        self.drawPinOfCross(firstPinLength, firstPinAngle)
        self.drawPinOfCross(sidePinLength, angles[1])
        self.drawPinOfCross(longPinLength, longPinAngle)
    def drawInsideCross(self, angles,firstPinLength, firstPinAngle, sidePinLength, longPinLength, longPinAngle):
        self.drawPinOfCross(sidePinLength, angles[0])
        self.drawPinOfCross(firstPinLength, firstPinAngle)
        self.drawPinOfCross(sidePinLength, angles[1])
        self.drawPinOfCross(longPinLength, longPinAngle)

    def drawOutsideCrossWithColor(self, angles,firstPinLength, firstPinAngle, sidePinLength, longPinLength, longPinAngle, color):
         t.fillcolor(color)
         t.begin_fill()
         self.drawOutsideCross(angles, firstPinLength, firstPinAngle, sidePinLength, longPinLength, longPinAngle)
         t.end_fill()
    def drawInsideCrossWithColor(self, angles,firstPinLength, firstPinAngle, sidePinLength, longPinLength, longPinAngle, color):
         t.fillcolor(color)
         t.begin_fill()
         self.drawInsideCross(angles,firstPinLength, firstPinAngle, sidePinLength, longPinLength, longPinAngle)
         t.end_fill()
    
           
        

    

if __name__=='__main__':
    angles = (270,90)
    cross = Cross()
    tp = tp()
    cross.drawOutsideCrossWithColor(angles, 4, 180, 2.5, 9.5, 0, 'blue')
    tp.setXCor(-cross.height / 4)
    tp.setYCor(cross.height / 4)
    tp.moveTurtle()
    cross.setHeight(cross.height / 2 )
    cross.drawInsideCrossWithColor(angles, 8.5, 180, 5.5, 19.5, 0, 'red')
    t.mainloop()
    t.hideturtle()