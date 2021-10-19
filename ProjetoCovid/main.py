from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Componentes
from components.vacina import *
from components.covid import *
from variaveis_globais import *
from components.bala_player import*

covid = Covid()

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


def GerenciaTeclado(key, x , y):
    global atirou,moverX,moverY,Tx,Ty

    print(x,y)

    if key == b' ':
        atirou= True
        moverX = Tx
        moverY= Ty
    
    glutPostRedisplay()


# Controle do Teclado
def control(key, x, y):
    global Ty, Tx, posicaoY,posicaoX
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
    global Tx,Ty, posicaoY,posicaoX,atirou
    glClear(GL_COLOR_BUFFER_BIT)

    glPushMatrix()
    glTranslatef(Tx, Ty, 0.0)
    vacina()
    glPopMatrix()

    covid.desenhar()
    covid.bala()
    
    if (atirou == True) :
        glPushMatrix()
        glTranslatef(posicaoX,posicaoY,0)
        criarBala(moverX,moverY)
        glPopMatrix()
        glutTimerFunc(100,animaTiroInimigo,100)


    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Covid Exterminator")
    glutSpecialFunc(control)
    glutKeyboardFunc(GerenciaTeclado)
    glutDisplayFunc(desenha)
    inicializa()
    glutMainLoop()

def animaTiroInimigo(value):
    global posicaoY,y1,atirou

    posicaoY += posicaoY - 1
    
    if((y1 + posicaoY) < 0):
        atirou = False
        posicaoY = 0
        
        
       

    glutPostRedisplay()
    # glutTimerFunc(200,animaTiroInimigo,1)

main()