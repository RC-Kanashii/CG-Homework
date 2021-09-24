from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init() -> None:
    """
    初始化窗口相关参数
    :return:
    """
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # 使用双缓存及RGB模型
    glutInitWindowSize(400, 300)  # 指定窗口尺寸
    glutInitWindowPosition(100, 100)  # 指定窗口在屏幕上的位置
    glutCreateWindow("Circle using Bresenham algorithm")
    glClearColor(1.0, 1.0, 1.0, 1.0)  # 设置窗口背景颜色

    # 下两行为伴生代码
    glMatrixMode(GL_PROJECTION)  # 指定设置投影参数
    glLoadIdentity()  # 调用单位矩阵，去掉以前的投影参数设置
    gluOrtho2D(0, 200, 0, 150)  # 设置投影参数（裁剪窗口）


def circlePoint(x: int, y: int, color: list) -> None:
    """
    绘制像素点
    :param x: 横坐标
    :param y: 纵坐标
    :param color: 颜色[r, g, b]
    :return:
    """
    r, g, b = color
    glColor3f(r, g, b)  # 设置颜色
    glPointSize(2.0)  # 设置像素点大小

    glBegin(GL_POINTS)
    dist = 100  # 圆距离窗口左上角偏移量
    glVertex2i(x + dist, y + dist)
    glVertex2i(y + dist, x + dist)
    glVertex2i(-y + dist, x + dist)
    glVertex2i(-x + dist, y + dist)
    glVertex2i(-x + dist, -y + dist)
    glVertex2i(-y + dist, -x + dist)
    glVertex2i(y + dist, -x + dist)
    glVertex2i(x + dist, -y + dist)
    glEnd()

    glFlush()


def midBresenhamCircle(r: int, color: list) -> None:
    """
    运用中点Bresenham算法绘制圆
    :param r: 半径
    :param color: 颜色[r, g, b]
    :return:
    """
    x = 0
    y = r
    d = 1 - r
    while x <= y:
        circlePoint(x, y, color)
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1


def display() -> None:
    """
    绘制图形
    :return:
    """
    glClear(GL_COLOR_BUFFER_BIT)  # 用当前背景色填充窗口
    midBresenhamCircle(8, [0.0, 0.5, 0.5])
    glFlush()  # 清空OpenGL命令缓冲区，执行OpenGL程序


if __name__ == "__main__":
    init()  # 初始化窗口
    glutDisplayFunc(display)
    glutMainLoop()  # 启动主GLUT事件处理循环
