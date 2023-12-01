from Denmark import DenmarkFlag
from Germany import germanyFlag
from Greece import GreeceFlag
from Norway import norwayFlag
from Usa import UsaFlag
from Japan import JapanFlag
from Pakistan import PakistanFlag
import turtle as t

def drawPaletteOfFlags(gX,gY, pX,pY, dX,dY, nX,nY, g2X,g2Y, uX,uY, jX,jY):
    germanyFlag(gX,gY)
    DenmarkFlag(dX,dY)
    norwayFlag(nX,nY)
    GreeceFlag(g2X,g2Y)
    UsaFlag(uX,uY)
    JapanFlag(jX,jY)
    PakistanFlag(pX,pY)

if __name__ == "__main__":
    screen = t.Screen()
    screen.setup(.9,.9)
    screenHeight = screen.window_height()
    screenWidth = screen.window_width()
    t.speed('fastest')
    drawPaletteOfFlags(-screenWidth/2.15, 300,
                       -200, 300, screenWidth/4,300,

                       -screenWidth/2.15, 100,
                        screenWidth/4,100,

                        -screenWidth/2.15, -100,
                        screenWidth/4, -100)
    t.mainloop()