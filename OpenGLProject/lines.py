# Linhas do Labirinto

from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

p = [
    [(0, 60), (400, 60)],
    [(300, 120), (500, 120)],
    [(60, 120), (240, 120)],
    [(60, 180), (440, 180)],
    [(250, 240), (250, 440)],
    [(320, 320), (500, 320)],
    [(400, 240), (400, 320)],
    [(0, 380), (190, 380)],
    [(60, 300), (250, 300)],
]

def lines ():
    # glColor3f(0.0, 0.0, 0.0)
    glLineWidth(3)
    for t in p: 
        t_1, t_2 = t[0], t[1]    
        glBegin(GL_LINES)
        glVertex2i(t_1[0], t_1[1])
        glVertex2i(t_2[0], t_2[1])
        glEnd()