from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from lines import *

# Variáveis Globais para translação
Tx = 0.0
Ty = 0.0

def inicializa ():
    glClearColor(2.0, 3.0, 1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    gluOrtho2D(0.0, 500, 500, 0.0)   

def quadrado ():
    global Tx
    global Ty

    glPushMatrix()
    glTranslatef(Tx, Ty, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0,0,1)  
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
    glClear(GL_COLOR_BUFFER_BIT)

    quadrado()
    # triangulo()
    lines()
    # pontos()
    glFlush()

# Tecla ESC fecha a janela
def teclado (key, x, y):
    print(x,y)
    print(key)
    if key == b'\x1b':
        glutDestroyWindow(glutGetWindow())

def control(key, x, y):
    global Ty
    global Tx
    step = 10
  
    print(Tx, Ty)
    
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
  
    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(500, 300)
    glutCreateWindow("Labirinto")
    glutKeyboardFunc(teclado)
    glutSpecialFunc(control)
    glutDisplayFunc(desenha)
    inicializa()
    glutMainLoop()

main()