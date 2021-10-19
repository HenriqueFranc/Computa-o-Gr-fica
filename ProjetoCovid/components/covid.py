from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from variaveis_globais import *
import math

def desenhar_circulo(x, y, radius):
    triangleAmount = 800
    twicePi = 2.0 * math.pi

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range (0, triangleAmount): 
        glVertex2f(x + (radius * math.cos(i *  twicePi / triangleAmount)), y + (radius * math.sin(i * twicePi / triangleAmount)))
    glEnd()

def desenhar_rect(x, y, type):
    if type == 1:
        glBegin(GL_QUADS)
        glVertex3f(x, y, 0)
        glVertex3f(x, y + 40, 0)
        glVertex3f(x + 20, y + 40, 0)
        glVertex3f(x + 20, y, 0)
        glEnd()  
    else:
        glBegin(GL_QUADS)
        glVertex3f(x, y, 0)
        glVertex3f(x, y + 20, 0)
        glVertex3f(x + 40, y + 20, 0)
        glVertex3f(x + 40, y, 0)
        glEnd()  

class Covid():
    def desenhar(self):
        glPushMatrix()
        glTranslatef(0, 50, 0)  

        glColor3f(235/255, 47/255, 6/255)
        
        # Círculo Maior
        desenhar_circulo(250, 100, 70)

        # 250, 170
        desenhar_rect(240, 160, 1)
        desenhar_circulo(250, 200, 20)

        # 320, 100
        desenhar_rect(310, 90, 2)
        desenhar_circulo(350, 100, 20)

        # 320, 100
        desenhar_rect(310, 90, 2)
        desenhar_circulo(350, 100, 20)

        # 150, 100
        desenhar_rect(150, 90, 2)
        desenhar_circulo(150, 100, 20)

        # 250, 30
        desenhar_rect(240, 0, 1)
        desenhar_circulo(250, 0, 20)
        glPopMatrix()

        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glTranslatef(200, 180, 0)
        glRotatef(40, 0, 0, 1)
        glTranslatef(-250, -250, 0)
        desenhar_rect(250, 250, 1)
        glPopMatrix()
        desenhar_circulo(175, 220, 20)
 
        glPushMatrix()
        glTranslatef(310, 70, 0)
        glRotatef(40, 0, 0, 1)
        glTranslatef(-250, -250, 0)
        desenhar_rect(250, 250, 1)
        glPopMatrix()
        desenhar_circulo(319, 80, 20)
 
        glPushMatrix()
        glTranslatef(215, 105, 0)
        glRotatef(130, 0, 0, 1)
        glTranslatef(-250, -250, 0)
        desenhar_rect(250, 250, 1)
        glPopMatrix()
        desenhar_circulo(170, 80, 20)
         
        glPushMatrix()
        glTranslatef(330, 205, 0)
        glRotatef(130, 0, 0, 1)
        glTranslatef(-250, -250, 0)
        desenhar_rect(250, 250, 1)
        glPopMatrix()
        desenhar_circulo(334, 220, 20)
        
        glColor3f(1, 1, 1)
        desenhar_circulo(220, 130, 20)
        desenhar_circulo(273, 186, 10)

    def bala(self): 
        glPushMatrix()
        glTranslatef(10, 10, 0)
        glScalef(0.2,0.2,0.2)
        self.desenhar()
        glPopMatrix()



