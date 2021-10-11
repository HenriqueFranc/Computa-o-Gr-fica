from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
# Componentes
from components.vacina import *
from variaveis_globais import *

# Impedir de avançar além das paredes
def colisoes_das_paredes():
    global Tx, Ty
    global height, width 

	# Muda a direção quando chega na bord6a esquerda ou direita
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

# Controle do Teclado
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
     
    glutPostRedisplay()


def inicializa ():
    global width, height

    glClearColor(2.0, 3.0, 1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    gluOrtho2D(0.0, width, height, 0.0)  

def desenha ():
    glClear(GL_COLOR_BUFFER_BIT)
    vacina()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Covid Exterminator")
    glutSpecialFunc(control)
    glutDisplayFunc(desenha)
    inicializa()
    glutMainLoop()


main()