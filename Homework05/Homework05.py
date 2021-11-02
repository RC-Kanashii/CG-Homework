from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init() -> None:
    """
    初始化窗口相关参数
    :return:
    """
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)  # 使用双缓存及RGB模型
    glutInitWindowSize(400, 300)  # 指定窗口尺寸
    glutInitWindowPosition(100, 100)  # 指定窗口在屏幕上的位置
    glutCreateWindow("Bouncing Ball")
    glClearColor(1.0, 1.0, 1.0, 1.0)  # 设置窗口背景颜色

    # 下两行为伴生代码
    glMatrixMode(GL_PROJECTION)  # 指定设置投影参数
    glLoadIdentity()  # 调用单位矩阵，去掉以前的投影参数设置
    gluOrtho2D(0, 200, 0, 150)  # 设置投影参数（裁剪窗口）


def dis() -> None:
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -250.0)
    glColor3f(1.0, 1.0, 0.0)
    glRectf(-250.0, -93.0, 250.0, -103.0)


def display() -> None:
    """
    绘制图形
    :return:
    """
    fElect1 = 80.0
    x = 1
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glTranslatef(0.0, 0.0 + fElect1, -250.0)
    glColor3f(1.0, 0.0, 0.0)
    glutSolidSphere(12.0, 15, 15)
    glPushMatrix()
    dis()  # 画矩形
    if fElect1 == -80.0:
        x += 1
    if fElect1 == 80.0:
        x -= 1
    if x % 2 == 0:
        fElect1 -= 10.0
    if x % 2 == 1:
        fElect1 += 10.0
    glutSwapBuffers()


def ChangeSize(w: int, h: int) -> None:
    if h == 0:
        h = 1
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    fAspect = w / h
    gluPerspective(45.0, fAspect, 1.0, 500.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def TimerFunc(value: int) -> None:
    glutPostRedisplay()
    glutTimerFunc(2, TimerFunc, 1)


if __name__ == "__main__":
    init()  # 初始化窗口
    glutDisplayFunc(display)
    glutReshapeFunc(ChangeSize)
    glutTimerFunc(2, TimerFunc, 1)
    glutMainLoop()  # 启动主GLUT事件处理循环
