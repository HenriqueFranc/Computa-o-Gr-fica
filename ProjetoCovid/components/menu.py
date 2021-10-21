from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from components.covid import Covid

def desenhar_rect_oco(x, y, w, h):
    glBegin(GL_LINE_LOOP)
    glVertex3f(x, y, 0)
    glVertex3f(x, y + h, 0)
    glVertex3f(x + w, y + h, 0)
    glVertex3f(x + w, y, 0)
    glEnd()

def desenhar_texto(x , y, font, text ):
    glRasterPos2f(x, y)
    for i in text:
        glutBitmapCharacter(font, ord(i))
        
class Menu():
    def desenhar(self):

        title = 'Covid Destroyer'
        start = 'Iniciar'
        quit = 'Sair'

        glColor3f(0, 0, 0)
        glRasterPos2f((250/2)+50, 50)
        for i in title:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(i))
 
        desenhar_rect_oco((250/2)+75, 328, 100, 40)
        glColor3f(0, 0, 0)
        glRasterPos2f((250/2)+90, 350)   
        for i in start:
            glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(i))

        desenhar_rect_oco((250/2)+75, 410, 100, 40)
        glRasterPos2f((250/2)+95, 435)
        for i in quit:
            glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(i))

    def fim_de_jogo(self):
        glColor3f(235/255, 47/255, 6/255)

        desenhar_rect_oco(100, 100, 300, 250)
        desenhar_texto((250/2)+70, 250, GLUT_BITMAP_TIMES_ROMAN_24, 'Game Over')
        desenhar_rect_oco((250/2)+75, 410, 100, 40)
        desenhar_texto((250/2)+105, 435, GLUT_BITMAP_9_BY_15, 'Sair')

