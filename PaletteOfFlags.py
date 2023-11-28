from Denmark import DenmarkFlag
from Germany import germanyFlag
from Greece import GreeceFlag
from Norway import norwayFlag
from Usa import UsaFlag
import turtle as t

def drawPaletteOfFlags(gX,gY, dX,dY, nX,nY, g2X,g2Y, uX,uY):
    angles = (180, 0)
    germanyFlag(gX,gY)
    DenmarkFlag(dX,dY)
    norwayFlag(nX,nY)
    # GreeceFlag(g2X,g2Y,angles)
    # UsaFlag(uX,uY)

if __name__ == "__main__":
    screen = t.Screen()
    screen.setup(.9,.9)
    screenHeight = screen.window_height()
    screenWidth = screen.window_width()
    t.speed('fastest')
    # setPositionOfTurtle()
    drawPaletteOfFlags(-screenWidth/2, 300, 
                        -screenWidth/4, 300, 
                        screenWidth/6, 300,
                        0,0,
                        0,0)
    t.mainloop()