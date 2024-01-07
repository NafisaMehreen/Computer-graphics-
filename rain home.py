from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# New global variable to store the rain direction and background color
directionofrain = 0
is_night = True  # Initially set to night mode

raindrops = []


def draw_points(x, y):
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def draw_lines():
    glBegin(GL_LINES)

    # x-axis
    glVertex2f(100, 100)
    glVertex2f(500, 100)
    glVertex2f(100, 500)
    glVertex2f(500, 500)
    
    # ==========Y-axis==========#
    glVertex2f(100, 100)
    glVertex2f(100, 500)
    glVertex2f(500, 100)
    glVertex2f(500, 500)

    # windows x axis
    glVertex2f(150, 350)
    glVertex2f(250, 350)
    glVertex2f(150, 450)
    glVertex2f(250, 450)

    # windows y axis
    glVertex2f(150, 350)
    glVertex2f(150, 450)
    glVertex2f(250, 350)
    glVertex2f(250, 450)

    # door x axis
    glVertex2f(200, 100)
    glVertex2f(300, 100)
    glVertex2f(200, 250)
    glVertex2f(300, 250)

    # door y axis
    glVertex2f(200, 100)
    glVertex2f(200, 250)
    glVertex2f(300, 100)
    glVertex2f(300, 250)
    glEnd()


def draw_triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)
    glVertex2f(100, 500)
    glVertex2f(500, 500)
    glVertex2f(300, 600)
    glEnd()


def draw_raindrop(x, y):
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(x, y)
    glVertex2f(x, y + 20)
    glEnd()


def iterate():
    glViewport(0, 0, 600, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600, 0.0, 800, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def animate_raindrops(value):
    global directionofrain
    for i in range(len(raindrops)):
        raindrops[i][1] -= 5
        raindrops[i][0] += directionofrain * 0.01
        if raindrops[i][1] < 0:
            raindrops[i][1] = 800 + random.randint(10, 100)
            raindrops[i][0] = random.randint(0, 800)
    glutPostRedisplay()
    glutTimerFunc(10, animate_raindrops, 0)


def special_key_pressed(key, x, y):
    global directionofrain, is_night
    if key == GLUT_KEY_LEFT:
        directionofrain = -20
    elif key == GLUT_KEY_RIGHT:
        directionofrain = 20
    elif key == GLUT_KEY_DOWN:
        is_night = not is_night

        display()


def special_key_released(key, x, y):
    global directionofrain
    if key in (GLUT_KEY_LEFT, GLUT_KEY_RIGHT):
        directionofrain = 0


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 0.0)
    draw_points(250, 250)
    draw_lines()
    glColor3f(1, 0, 0)
    draw_triangle()

    for raindrop in raindrops:
        draw_raindrop(raindrop[0], raindrop[1])

    glutSwapBuffers()


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 800, 0, 600, -1, 1)
    glMatrixMode(GL_MODELVIEW)


def display():
    print(is_night)
    if is_night:
        glClearColor(0.0, 0.0, 0.0, 1.0)
    else:
        glClearColor(1.0, 1.0, 1.0, 1.0)

    glClear(GL_COLOR_BUFFER_BIT)
    for raindrop in raindrops:
        draw_raindrop(raindrop[0], raindrop[1])
    glutSwapBuffers()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 600)
glutCreateWindow(b"Combined OpenGL Practice")
glutDisplayFunc(showScreen)
glutSpecialFunc(special_key_pressed)
glutSpecialUpFunc(special_key_released)
init()

for i in range(100):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    raindrops.append([x, y])

glutTimerFunc(10, animate_raindrops, 0)
glutMainLoop()


