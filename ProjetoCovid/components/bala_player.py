
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from variaveis_globais import *

def criarBala(moverX,moverY):

    print(moverX)
    glColor3f(116/255, 185/255, 255/25)
    glBegin(GL_LINES)
    glVertex3f(312.5 + moverX, 400.0 + moverY ,0)
    glVertex3f(312.5 + moverX, 390.0 + moverY , 0)
    glEnd()
  
