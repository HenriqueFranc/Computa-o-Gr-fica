from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

Tx = 0.0
Ty = 0.0

def inicializa ():
    glClearColor(2.0, 3.0, 1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    # gluOrtho2D(0.0, 10.0, 0.0, 10.0)   
    gluOrtho2D(0.0, 500, 500, 0.0)   

def quadrado ():
    global Tx
    global Ty
    
    glTranslatef(Tx, Ty, 0)

    glBegin(GL_QUADS)
    glColor3f(0,0,1)
    glVertex3f(250, 350, 0)
    glVertex3f(250, 400, 0)
    glVertex3f(300, 400, 0)
    glVertex3f(300, 350, 0) 
    glEnd()

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

def lines ():
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2i(0, 0)
    glVertex2i(500, 500)
    # glVertex2i(150, 130)
    # glVertex2i(150, 50)
    glEnd()

def desenha ():
    # Limpa a janela de visualização com a cor de fundo especificada
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    # glLoadIdentity()

    quadrado()
    # triangulo()
    # lines()
    # pontos()

    glFlush()

def teclado (key, x, y):
    print(x,y)
    print(key)
    if key == b'\x1b':
        glutDestroyWindow(glutGetWindow())

def control(key, x, y):
    global Ty
    global Tx

    # glPushMatrix()
    # glLoadIdentity()
    
    print(Tx, Ty)

    if key == GLUT_KEY_UP:
        Ty = Ty - 2
    if key == GLUT_KEY_DOWN:
        Ty = Ty + 2
    if key == GLUT_KEY_LEFT:
        Tx = Tx - 2
    if key == GLUT_KEY_RIGHT:
        Tx = Tx + 2
    if key == b'\x1b':
        glutDestroyWindow(glutGetWindow())

    # glPopMatrix() 

    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(500, 300)
    glutCreateWindow("Primeiro Programa")
    glutKeyboardFunc(teclado)
    glutSpecialFunc(control)
    glutDisplayFunc(desenha)
    inicializa()
    glutMainLoop()

main()