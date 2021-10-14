from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from variaveis_globais import *

def vacina():
    glLineWidth(2)
   
    glBegin(GL_LINES)
    glColor3f(0.0,0.0,0.0)
    glVertex3f(312.5, 400,0)
    glVertex3f(312.5, 390,0)
    glEnd()
    
   
    glBegin(GL_QUADS)
    # glColor3f(0.25,0.50,0.55)
    glColor3f(116/255, 185/255, 255/255)
    glVertex3f(300, 400, 0)
    glVertex3f(300, 440, 0)
    glVertex3f(325, 440, 0)
    glVertex3f(325, 400, 0)
    glEnd()
    
   
    glBegin(GL_QUADS)
    glColor3f(0.8,0.8,0.8)
    glVertex3f(300, 440, 0)
    glVertex3f(300, 450, 0)
    glVertex3f(325, 450, 0)
    glVertex3f(325, 440, 0)
    glEnd()
    
   
    glBegin(GL_LINES)
    glColor3f(0.0,0.0,0.0)
    glVertex2i(290, 450)
    glVertex2i(335, 450)
    glEnd()
    
    