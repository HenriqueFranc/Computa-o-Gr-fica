from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from lines import *

# Variáveis Globais para translação
Tx = 0.0
Ty = 0.0

minX, maxX = 435, 485
minY, maxY = 434, 484

# Tamanho da Janela
height, width = 500, 500

def inicializa ():
    global width, height

    glClearColor(2.0, 3.0, 1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    gluOrtho2D(0.0, width, height, 0.0)   

def quadrado ():
    global Tx, Ty

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
    for t in p: 
        t_1, t_2 = t[0], t[1]
    
    if ( 
        (((Tx+maxX) <= t_2[0] and (Tx+maxX) >= t_1[0]) or ((Tx+minX) <= t_2[0] and (Tx+minX) >= t_1[0])) 
        and 
        (((Ty+maxY) <= t_2[1] and (Ty+minY) >= t_1[1]) or ((Ty+maxY) >= t_2[1] and (Ty+minY) <= t_1[1]))
    ):
        print('Bateu no Labirinto')

    glutPostRedisplay()


# void mouse (int button, int state, int x, int y)
# {
#     if (button == GLUT_LEFT_BUTTON)
#          if (state == GLUT_DOWN) {
#                   // Troca o tamanho do retângulo, que vai do centro da 
#                   // janela até a posição onde o usuário clicou com o mouse
#                   xf = ( (2 * win * x) / view_w) - win
#                   yf = ( ( (2 * win) * (y-view_h) ) / -view_h) - win
#          }
#     glutPostRedisplay()
# }

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
    glutInitWindowPosition(500, 300)
    glutCreateWindow("Labirinto")
    glutKeyboardFunc(teclado)
    # glutMouseFunc(mouse)
    glutSpecialFunc(control)
    glutDisplayFunc(desenha)
    inicializa()
    glutMainLoop()

main()