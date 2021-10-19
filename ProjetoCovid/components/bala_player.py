
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from variaveis_globais import *

def inicializaBala_player():
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    moverX = 0
    moverY = 0
    posicaoX = 0
    posicaoY = 0
    x1 = 312.5
    y1 = 390
    x2 = 312.5
    y2 = 400
    x3 = 314.5
    y3 = 400
    x4 = 314.5
    y4 = 390

def criarBala(moverX,moverY):

    print(moverX)
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex3f(312.5 + moverX, 400.0 + moverY ,0)
    glVertex3f(312.5 + moverX, 390.0 + moverY , 0)
    glEnd()
  


def setMoverX(novoMoverX):
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX
    moverX += novoMoverX; 


def getMoverX():
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    return moverX;  



def setMoverY(novoMoverY):
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    moverY += novoMoverY; 


def getMoverY():
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX    
    
    return moverY


def setPosicaoX(novaPosicaoX):
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    posicaoX = novaPosicaoX; 


def getPosicaoX():
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    return posicaoX


def setPosicaoY(novaPosicaoY):
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    posicaoY = novaPosicaoY; 


def getPosicaoY():
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    return posicaoY




def setX1(novoX1):
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    x1 = novoX1


def getX1():
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    return x1


def setY1(novoY1):
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    y1 = novoY1


def getY1():
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    return y1



def setX2(novoX2):
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    x2 = novoX2


def getX2():
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    return x2


def setY2( novoY2):
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    y2 = novoY2


def getY2():
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    return y2



def setX3( novoX3):
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    x3 = novoX3


def getX3():
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    return x3


def setY3(novoY3):
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    y3 = novoY3


def getY3():
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    return y3



def setX4(novoX4):
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    x4 = novoX4


def getX4():
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    return x4


def setY4(novoY4):
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    y4 = novoY4


def getY4():
    global x1,x2,x3,x4,y1,y2,y3,y4,moverX,moverY,posicaoY,posicaoX

    return y4

