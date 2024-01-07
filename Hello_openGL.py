from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(10) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def draw_lines():
    glBegin(GL_LINES)

    #x-axis
    glVertex2f(100, 100)
    glVertex2f(500, 100)

    glVertex2f(100, 500)
    glVertex2f(500, 500)
    #==========Y-axis==========#
    glVertex2f(100, 100)
    glVertex2f(100, 500)

    glVertex2f(500, 100)
    glVertex2f(500, 500)

    #windows x axis
    glVertex2f(150,350)
    glVertex2f(250,350)
    glVertex2f(150,450)
    glVertex2f(250,450)

    #windows y axis
    glVertex2f(150,350)
    glVertex2f(150,450)
    glVertex2f(250,350)
    glVertex2f(250,450)
    

    #door x axis 
    glVertex2f(200,100)
    glVertex2f(300,100)
    glVertex2f(200,250)
    glVertex2f(300,250)

    #door y axis
    glVertex2f(200,100)
    glVertex2f(200,250)
    glVertex2f(300,100)
    glVertex2f(300,250)
    glEnd()

def draw_points(x,y):
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def draw_triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(1,0,0)
    glVertex2f(100,500)
    glVertex2f(500,500)
    glVertex2f(300,750)
    glEnd()

def iterate():
    glViewport(0, 0, 600, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600, 0.0, 800, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    draw_points(250, 250)
    draw_lines()
    glColor3f(1,0,0)
    draw_triangle()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()