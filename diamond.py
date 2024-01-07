from OpenGL.GL import *
from OpenGL.GLUT import *
import random

# Global variables
windowWidth = 800
windowHeight = 600
catcherX = windowWidth // 2
catcherWidth = 100
diamondX = random.randint(20, windowWidth - 20)
diamondY = windowHeight
diamondSpeed = 2.0
gameOver = False
score = 0
paused = False


def drawCatcherBowl():
    catcherTopX = catcherX
    catcherTopY = 30
    catcherBottomY = 0
    catcherSize = 100 / 2

    glColor3f(3.0, 4.0, 0.5)
    glBegin(GL_LINES)

    glVertex2f(catcherTopX - catcherSize, catcherTopY)
    glVertex2f(catcherTopX + catcherSize, catcherTopY)
    glVertex2f(catcherTopX + catcherSize, catcherTopY)
    glVertex2f(catcherTopX + catcherSize, catcherBottomY)
    glVertex2f(catcherTopX - catcherSize, catcherTopY)
    glVertex2f(catcherTopX - catcherSize, catcherBottomY)

    glEnd()


def drawDiamond():
    random_color = (random.uniform(0.9, 2.0), random.uniform(0.3, 3.0), random.uniform(0.8, 4.0))
    glColor3f(*random_color)

    diamondXCenter = diamondX
    diamondYCenter = diamondY
    diamondSize = 10

    glBegin(GL_LINES)

    glVertex2f(diamondXCenter, diamondYCenter + diamondSize)  
    glVertex2f(diamondXCenter + diamondSize, diamondYCenter)  
    glVertex2f(diamondXCenter + diamondSize, diamondYCenter)  
    glVertex2f(diamondXCenter, diamondYCenter - diamondSize)  
    glVertex2f(diamondXCenter, diamondYCenter - diamondSize)  
    glVertex2f(diamondXCenter - diamondSize, diamondYCenter)  
    glVertex2f(diamondXCenter - diamondSize, diamondYCenter)  
    glVertex2f(diamondXCenter, diamondYCenter + diamondSize)

    glEnd()

def drawLine(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    xp = 1 if x0 < x1 else -1
    yp = 1 if y0 < y1 else -1

    x, y = x0, y0
    difference = dx - dy

    while True:
        glVertex2f(x, y)

        if x == x1 and y == y1:
            break

        err = 2 * difference
        if err > -dy:
            error -= dy
            x += xp
        if err < dx:
            error += dx
            y += yp



def handleSpecialKeypress(key, x, y):
    global catcherX
    if not gameOver and not paused:
        if key == GLUT_KEY_LEFT:
            catcherX = max(catcherWidth / 2, catcherX - 10)
        elif key == GLUT_KEY_RIGHT:
            catcherX = min(windowWidth - catcherWidth / 2, catcherX + 10)
        glutPostRedisplay()


def updateGameLogic():
    global diamondY, diamondSpeed, gameOver, score, diamondX
    if not gameOver and not paused:
        diamondY -= diamondSpeed
        if diamondY < -20:
            if catcherX - catcherWidth / 2 > diamondX + 20 or catcherX + catcherWidth / 2 < diamondX - 20:
                print("Game Over! Your Score:", score)
                gameOver = True
            else:
                diamondY = windowHeight
                diamondX = random.randint(20, windowWidth - 20)
                diamondSpeed += 0.1
                score += 1
                print("Score:", score)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    drawCatcherBowl()
    drawDiamond()

    # Handle game over state
    if gameOver:
        glColor3f(1.0, 0.0, 0.0)
        glRasterPos2f(windowWidth // 2 - 50, windowHeight // 2)
        glutBitmapString(GLUT_BITMAP_HELVETICA_18, b"Game Over. Your Score: " + str(score).encode('utf-8'))

        # Draw a game over message
        glColor3f(1.0, 1.0, 1.0)  # Reset color to white
        glRasterPos2f(10, windowHeight - 20)
        glutBitmapString(GLUT_BITMAP_HELVETICA_12, b"Score: " + str(score).encode('utf-8'))

    if paused:
        glColor3f(1.0, 1.0, 1.0)  

    glFlush()
    glutSwapBuffers()

# Function to update the window size
def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    global windowWidth, windowHeight
    windowWidth = width
    windowHeight = height

# Function to update the scene
def update(value):
    updateGameLogic()
    glutPostRedisplay()
    glutTimerFunc(10, update, 0)


glutInit()
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
glutInitWindowSize(windowWidth, windowHeight)
glutCreateWindow(b"Catch the Diamonds")
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutSpecialFunc(handleSpecialKeypress)
glutTimerFunc(10, update, 0)
glutMainLoop()