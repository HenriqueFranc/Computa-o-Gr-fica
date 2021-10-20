from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from components.covid import Covid

class Menu():
    def desenhar(self):
        covid = Covid()

        title = 'Covid Destroyer'
        start = 'Iniciar [1]'
        quit = 'Sair [ESC]'

        glColor3f(0, 0, 0)
        glRasterPos2f((250/2)+50, 50)
        for i in title:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(i))

        glPushMatrix()
        glTranslatef(-30,0, 0)
        glScalef(5, 5, 5)
        covid.bala(0)
        glPopMatrix()   

        glColor3f(0, 0, 0)
        glRasterPos2f((250/2)+90, 400)   
        for i in start:
            glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(i))

        glRasterPos2f((250/2)+90, 430)
        for i in quit:
            glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(i))

