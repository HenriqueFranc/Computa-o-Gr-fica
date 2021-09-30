from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from lines import *
import random

# Variáveis Globais para translação
Tx = 0.0
Ty = 0.0
vidas = 3
change = 0
cor_1, cor_2 , cor_3 = 0,0,0 
minX, maxX = 435, 485
minY, maxY = 434, 484

# Tamanho da Janela
height, width = 500, 500

def inicializa ():
    global width, height

    glClearColor(2.0, 3.0, 1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    gluOrtho2D(0.0, width, height, 0.0)   

def vidas_desenho ():
    global vidas
    for x in range(0,vidas):
        glPushMatrix()
        if x == 0:
            glTranslatef(20, 0.0, 0.0)
        if x == 1:
            glTranslatef(40, 0.0, 0.0)
        if x == 2:
            glTranslatef(60, 0.0, 0.0)
        glBegin(GL_QUADS)
        #glColor3f(0,0,1)  
        glVertex3f(0, 0, 0)
        glVertex3f(0, 10, 0)
        glVertex3f(10, 10, 0)
        glVertex3f(10, 0, 0)
        glEnd()
        glPopMatrix()

def quadrado ():
    global Tx, Ty

    glPushMatrix()
    glTranslatef(Tx, Ty, 0.0)
    glBegin(GL_QUADS)
    #glColor3f(0,0,1)  
    glVertex3f(435, 434, 0)
    glVertex3f(435, 484, 0)
    glVertex3f(485, 484, 0)
    glVertex3f(485, 434, 0)
    glEnd()
    glPopMatrix()

def triangulo ():
    # Define a cor de desenho: vermelho
    glColor3f(1.0, 0.0, 0.0)
    
    # Desenha um triângulo no centro da janela
    glBegin(GL_TRIANGLES)
    glVertex3f(100, 100, 0)
    glVertex3f(120, 100, 0)
    glVertex3f(140, 100, 0)
    
    glEnd()

def pontos ():
    # glColor3f(1.0, 0.0, 0.0)
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2i(200, 200)
    glVertex2i(4, 2)
    glEnd() 

def desenha ():
    global change
    glClear(GL_COLOR_BUFFER_BIT)
    

    if change == 0:
        glColor3f(0,0,1) 
        quadrado()
        glColor3f(10,5,0) 
        lines()
        glColor3f(0,0,1) 
        vidas_desenho()
    if change == 1:
         glColor3f(1,0,1) 
         quadrado()
         glColor3f(0,5,0) 
         lines()
         glColor3f(1,0,1) 
         vidas_desenho()
    if change == 2:
         glColor3f(0,0,0) 
         quadrado()
         glColor3f(1,0,0) 
         lines()
         glColor3f(0,0,0) 
         vidas_desenho()
    
    
    glFlush()

# Tecla ESC fecha a janela
def teclado (key, x, y):
    if key == b'\x1b':
        glutDestroyWindow(glutGetWindow())

def colisoes_das_paredes():
    global Tx, Ty
    global height, width 

	# Muda a direção quando chega na borda esquerda ou direita
    # print('Tx+maxX', Tx+maxX)
    # print('Tx+minX', Tx+minX)

    if ( (Tx+maxX) > width or (Tx+minX) < 0 ):
        print('Bateu na Parede')

    # print('Ty+maxY', Ty+maxY)
    # print('Ty+minY', Ty+minY)
    # print()
	# Muda a direção quando chega na borda superior ou inferior
    if( (Ty+maxY) > height or (Ty+minY) < 0 ):
        print('Bateu na Parede')
 
	# Redesenha a casinha em outra posição
    glutPostRedisplay()


def colisoes_no_labirinto():
    global Tx, Ty , vidas
    for t in p: 
        t_1, t_2 = t[0], t[1]

        # print('Tx+maxX', Tx+maxX)
        # print('Tx+minX', Tx+minX)
        # print('Ty+maxY', Ty+maxY)
        # print('Ty+minY', Ty+minY)
        # print('-------------')

        collisionX = (Tx+maxX >= t_1[0] and t_2[0] >= Tx+minX)

        collisionY = (Ty+maxY >= t_1[1] and t_2[1] >= Ty+minY)


        if collisionX and collisionY: 
            Tx = 0
            Ty = 0
            vidas= vidas - 1
            if vidas == 0:
                 glutDestroyWindow(glutGetWindow())
            desenha()
            
    

    glutPostRedisplay()

    
def mouse (button, state, x , y):
    global change
    print('chamei mouse')
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN):
                if(change == 2):
                    change = 0
                else:
                    change = change + 1              

    glutPostRedisplay()
 

def control(key, x, y):
    global Ty, Tx
    step = 10
  
    # print(Tx, Ty)
    
    if key == GLUT_KEY_UP:
        Ty -= step
    elif key == GLUT_KEY_DOWN:
        Ty += step
    elif key == GLUT_KEY_LEFT:
        Tx -= step
    elif key == GLUT_KEY_RIGHT:
        Tx += step
    elif key == b'\x1b':
        glutDestroyWindow(glutGetWindow())
    
    colisoes_das_paredes()
    colisoes_no_labirinto()
    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    #glutInitWindowPosition(500, 300)
    glutCreateWindow("Labirinto")
    glutKeyboardFunc(teclado)
    glutMouseFunc(mouse)
    glutSpecialFunc(control)
    glutDisplayFunc(desenha)
    inicializa()
    glutMainLoop()

main()