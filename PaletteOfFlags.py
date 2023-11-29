from Denmark import DenmarkFlag
from Germany import germanyFlag
from Greece import GreeceFlag
from Norway import norwayFlag
from Usa import UsaFlag
import turtle as t

def drawPaletteOfFlags(gX,gY, dX,dY, nX,nY, g2X,g2Y, uX,uY):
    
    germanyFlag(gX,gY)
    DenmarkFlag(dX,dY)
    # t.penup()
    # t.setposition(nX,nY)
    # t.pendown()
    norwayFlag(nX,nY)
    GreeceFlag(g2X,g2Y)
    UsaFlag(uX,uY)

if __name__ == "__main__":
    screen = t.Screen()
    screen.setup(.9,.9)
    screenHeight = screen.window_height()
    screenWidth = screen.window_width()
    t.speed('fastest')
    # setPositionOfTurtle()
    drawPaletteOfFlags(-screenWidth/2.15, 300, 
                        screenWidth/4, 300, 
                       -screenWidth/2.15, 100,
                        screenWidth/4,100,
                        -screenWidth/2.15, -100)
    t.mainloop()