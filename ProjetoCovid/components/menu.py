from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from components.covid import Covid

def desenhar_rect_oco(x,y):
    glBegin(GL_LINE_LOOP)
    glVertex3f(x, y, 0)
    glVertex3f(x, y + 40, 0)
    glVertex3f(x + 100, y + 40, 0)
    glVertex3f(x + 100, y, 0)
    glEnd()

class Menu():
    def desenhar(self):
        # covid = Covid()

        title = 'Covid Destroyer'
        start = 'Iniciar'
        quit = 'Sair'

        glColor3f(0, 0, 0)
        glRasterPos2f((250/2)+50, 50)
        for i in title:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(i))

        # glPushMatrix()
        # glTranslatef(-30,0, 0)
        # glScalef(5, 5, 5)
        # covid.bala(0)
        # glPopMatrix()   

        desenhar_rect_oco((250/2)+75, 328)
        glColor3f(0, 0, 0)
        glRasterPos2f((250/2)+90, 350)   
        for i in start:
            glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(i))

        desenhar_rect_oco((250/2)+75, 410)
        glRasterPos2f((250/2)+95, 435)
        for i in quit:
            glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(i))