from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def Initial():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0, 200.0, 0.0, 150.0)


def DisplayRect():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.5, 0.5, 0.0)
    glRectf(100.0, 100.0, 150.0, 50.0)
    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 300)
    glutInitWindowPosition(100, 120)
    glutCreateWindow("Rectangle")
    glutDisplayFunc(DisplayRect)
    Initial()
    glutMainLoop()
