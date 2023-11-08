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
        

    def drawOutsideCross(self, angles):
        for angle in angles:
            self.drawPinOfCross(2.5, angle)
        self.drawPinOfCross(9.5, 0)
    def drawInsideCross(self, angles):
        for angle in angles:
            self.drawPinOfCross(4, angle)
        self.drawPinOfCross(19.5, 0)

    def drawOutsideCrossWithColor(self, angles, color):
         t.fillcolor(color)
         t.begin_fill()
         self.drawOutsideCross(angles)
         t.end_fill()
    def drawInsideCrossWithColor(self, angles, color):
         t.fillcolor(color)
         t.begin_fill()
         self.drawInsideCross(angles)
         t.end_fill()
    
           
        

    

if __name__=='__main__':
    angles = [270,180,90]
    cross = Cross()
    tp = tp()
    cross.drawOutsideCrossWithColor(angles, 'blue')
    tp.setXCor(-cross.height / 4)
    tp.setYCor(cross.height / 4)
    tp.moveTurtle()
    cross.setHeight(cross.height / 2 )
    cross.drawInsideCrossWithColor(angles, 'red')
    t.mainloop()
    t.hideturtle()