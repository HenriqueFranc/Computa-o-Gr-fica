# Linhas do Labirinto

from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

posicoes = {
    'line_1': [(0, 60), (300, 60)]
}

def lines ():
    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(3)

    glBegin(GL_LINES)
    glVertex2i(0, 60)
    glVertex2i(300, 60)

    glVertex2i(300, 120)
    glVertex2i(500, 120)
    
    glVertex2i(60, 180)
    glVertex2i(440, 180)

    glVertex2i(250, 240)
    glVertex2i(250, 440)

    glVertex2i(320, 320)
    glVertex2i(500, 320)
   
    glVertex2i(400, 240)
    glVertex2i(400, 320)

    glVertex2i(0, 380)
    glVertex2i(190, 380)

    glVertex2i(60, 300)
    glVertex2i(250, 300)

    glEnd()