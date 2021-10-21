from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Componentes
from variaveis_globais import *
from components.vacina import *
from components.covid import *
from components.menu import *
from components.bala_player import*

covid = Covid()
menu = Menu()

def colisoes_das_paredes():
    global Tx, Ty , maxX, minX, maxY,minY, colisãoDireita, colisãoEsquerda, colisãoCima,colisãoBaixo, height, width 

    if ((Tx+maxX) > width):
        
        colisãoDireita = True
        if (Ty+maxY) > height :
            colisãoBaixo = True
        elif (Ty+minY) < 0 :
            colisãoCima = True
    elif ( (Tx+minX) < 0 ):
        
        colisãoEsquerda = True
        if (Ty+maxY) > height :
            colisãoBaixo = True
        elif (Ty+minY) < 0 :
            colisãoCima = True
    elif( (Ty+maxY) > height ):
        
        colisãoBaixo = True
    elif ((Ty+minY) < 0) :
        
         colisãoCima = True
    else:
        colisãoEsquerda = False
        colisãoDireita = False
        colisãoCima = False
        colisãoBaixo = False
        
    glutPostRedisplay()

def colisoes_covid():
    global maxXcovid, minXcovid,covidTx,colisãoCovidDireita,colisãoCovidEsquerda

    if ((covidTx + maxXcovid) > width):
        colisãoCovidDireita = True
        colisãoCovidEsquerda = False

    elif ( (covidTx + minXcovid) < 0 ):
        colisãoCovidEsquerda = True
        colisãoCovidDireita = False

def controle_teclas_alfanumericas(key, x , y):
    global atirou,moverX,moverY,Tx,Ty, menuAtivado
    
    print(x, y)

    if key == b' ':
        atirou= True
        moverX = Tx
        moverY = Ty
    elif key == b'1':
        menuAtivado = not menuAtivado
    elif key == b'\x1b':
        glutDestroyWindow(glutGetWindow())
    
    glutPostRedisplay()

def controle_teclas_especiais(key, x, y):
    global Ty, Tx, posicaoY,posicaoX,colisão
    step = 15
  
    colisoes_das_paredes()
    
    if key == GLUT_KEY_UP:
        if colisãoCima == False:
            Ty -= step
    elif key == GLUT_KEY_DOWN:
        if colisãoBaixo == False:
            Ty += step
    elif key == GLUT_KEY_LEFT:
        if colisãoEsquerda == False:
            Tx -= step
    elif key == GLUT_KEY_RIGHT:
        if colisãoDireita == False:
            Tx += step 

    glutPostRedisplay()

def controle_mouse(button, state, x, y):
    global menuAtivado
    
    if button == GLUT_LEFT_BUTTON:
        if (state == GLUT_DOWN):
            if (x > 200 and  x < 300) and (y > 328 and y < 368):
                menuAtivado = not menuAtivado
            if (x > 200 and  x < 300) and (y > 410 and y < 450):
                glutDestroyWindow(glutGetWindow())

    glutPostRedisplay()

def anima_tiro_player(value):
    global posicaoY,y1,atirou

    posicaoY += posicaoY - 1

    if(((390.0 + moverY) + posicaoY) < 0):
        atirou = False
        posicaoY = 0
        
    glutPostRedisplay()

def anima_tiro_inimigo(value):
    global posicaoYinimigo,posicaoXinimigo
    
    posicaoYinimigo += posicaoYinimigo + 1

    if((150 + posicaoYinimigo) > height):
        posicaoYinimigo = 0
        
    glutPostRedisplay()
    glutTimerFunc(500, anima_tiro_inimigo,10)

def anima_covid(value):
    global covidTx,colisãoCovidEsquerda,colisãoCovidDireita

    num = 10

    colisoes_covid()

    if (colisãoCovidEsquerda == True):
        num = 10
        

    elif (colisãoCovidDireita == True):
        num = -10
        
    
    covidTx = covidTx + num
    glutPostRedisplay()
    glutTimerFunc(100, anima_covid,100)
    
def inicializa ():
    global width, height

    glClearColor(2.0, 3.0, 1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    gluOrtho2D(0.0, width, height, 0.0)
     
def desenha ():
    global Tx,Ty, posicaoY,posicaoX,atirou
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    if menuAtivado:
        menu.desenhar()
    else:
        glPushMatrix()
        glTranslatef(Tx, Ty, 0.0)
        vacina()
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef(covidTx, 0.0, 0.0)
        covid.desenhar()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(posicaoXinimigo,posicaoYinimigo,0)
        covid.bala(covidTx)
        glPopMatrix()

        covid.barra_de_vida()
  
    if (atirou == True) :
        glPushMatrix()
        glTranslatef(posicaoX,posicaoY,0)
        criarBala(moverX,moverY)
        glPopMatrix()
        glutTimerFunc(100, anima_tiro_player,100)


    glutSwapBuffers()

def main():
    global width, height
    
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow("Covid Exterminator")
    glutSpecialFunc(controle_teclas_especiais)
    glutKeyboardFunc(controle_teclas_alfanumericas)
    glutMouseFunc(controle_mouse)
    glutDisplayFunc(desenha) 
    inicializa()
    glutTimerFunc(500, anima_tiro_inimigo,10)
    glutTimerFunc(100, anima_covid,100)
    glutMainLoop()

main()