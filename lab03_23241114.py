from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window_width, window_height = 600, 600
num_of_circles = [] 
init_rad = 50  
growth_res = .01
paused = False

def draw_circle(x_cent, y_cent, rad):
    x, y = 0, rad
    d = 1 - rad

    glBegin(GL_POINTS)
    while x <= y:
        
        glVertex2f(x + x_cent, y + y_cent)
        glVertex2f(-x + x_cent, y + y_cent)
        glVertex2f(x + x_cent, -y + y_cent)
        glVertex2f(-x + x_cent, -y +y_cent)
        glVertex2f(y + x_cent, x + y_cent)
        glVertex2f(-y + x_cent, x + y_cent)
        glVertex2f(y + x_cent, -x + y_cent)
        glVertex2f(-y + x_cent, -x + y_cent)

        if d < 0:  
            d += 2*x + 3
        else:    
            d += 2*(x - y) + 5
            y -= 1

        x += 1

    glEnd()
    glFlush()

def draw():
    global paused,growth_res
    if not paused:
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 1.0, 1.0) 

        to_remove = []
        for i in range(len(num_of_circles)):
            cent_x, cent_y, rad = num_of_circles[i]
            rad += growth_res
            num_of_circles[i] = (cent_x, cent_y, rad)  
            draw_circle(cent_x, cent_y, rad)  

            #Boundary checking
            x_min, x_max = rad, window_width - rad
            y_min, y_max = rad, window_height - rad

            if not (x_min < cent_x < x_max and y_min < cent_y < y_max):
                to_remove.append(i) 

        for ind in (to_remove):
            del num_of_circles[ind]

        glutSwapBuffers()
        glutPostRedisplay()  

def keyboard(key, x, y):
    global paused,growth_res
    if key == b' ':
        paused = not paused 
    elif key == GLUT_KEY_LEFT: 
        growth_res += 0.01  
    elif key == GLUT_KEY_RIGHT:  
        growth_res -= 0.01  
        growth_res = max(growth_res, 0.01)  

def special_keys(key, x, y):
    if key == GLUT_KEY_LEFT:
        keyboard(key, x, y)
    elif key == GLUT_KEY_RIGHT:
        keyboard(key, x, y)


def mouse_click(button, state, x, y):
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        
        cent_x = x
        cent_y = window_height - y 
        num_of_circles.append((cent_x, cent_y, init_rad))  
        glutPostRedisplay() 

# def main():
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(window_width, window_height)
glutCreateWindow(b"Circle")

glClearColor(0.0, 0.0, 0.0, 1.0)
gluOrtho2D(0.0, window_width, 0.0, window_height)

glutDisplayFunc(draw)
glutMouseFunc(mouse_click) 
glutKeyboardFunc(keyboard)
glutSpecialFunc(special_keys)
glutIdleFunc(draw)  
glutMainLoop()

