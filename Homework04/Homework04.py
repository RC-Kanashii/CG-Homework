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
    glutCreateWindow("Ellipse using Bresenham algorithm")
    glClearColor(1.0, 1.0, 1.0, 1.0)  # 设置窗口背景颜色

    # 下两行为伴生代码
    glMatrixMode(GL_PROJECTION)  # 指定设置投影参数
    glLoadIdentity()  # 调用单位矩阵，去掉以前的投影参数设置
    gluOrtho2D(0, 200, 0, 150)  # 设置投影参数（裁剪窗口）


def putPixel(x: int, y: int, color: list) -> None:
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
    # glVertex2i(y + dist, x + dist)
    # glVertex2i(-y + dist, x + dist)
    # glVertex2i(-x + dist, y + dist)
    # glVertex2i(-x + dist, -y + dist)
    # glVertex2i(-y + dist, -x + dist)
    # glVertex2i(y + dist, -x + dist)
    # glVertex2i(x + dist, -y + dist)
    glEnd()

    glFlush()


def midBresenhamEllipse(a: int, b: int, color: list) -> None:
    """
    运用中点Bresenham算法绘制椭圆
    :param a: 长半轴
    :param b: 短半轴
    :param color: 颜色[r, g, b]
    :return:
    """

    def putPixels(x: int, y: int, color: list) -> None:
        """
        绘制一系列关于椭圆中点对称的点
        :param x: 横坐标
        :param y: 纵坐标
        :param color: 颜色[r, g, b]
        :return:
        """
        putPixel(x, y, color)
        putPixel(-x, -y, color)
        putPixel(-x, y, color)
        putPixel(x, -y, color)

    x = 0
    y = b
    d1 = b ** 2 + a ** 2 * (-b + 0.25)
    putPixels(x, y, color)
    while b ** 2 * (x + 1) < a ** 2 * (y - 0.5):
        if d1 < 0:
            d1 += b ** 2 * (2 * x + 3)
            x += 1
        else:
            d1 += b ** 2 * (2 * x + 3) + a ** 2 * (-2 * y + 2)
            x += 1
            y -= 1
        putPixels(x, y, color)
    d2 = b ** 2 * (x + 0.5) ** 2 + a ** 2 * (y - 1) ** 2 - a ** 2 * b ** 2
    while y > 0:
        if d2 <= 0:
            d2 += b ** 2 * (2 * x + 2) + a ** 2 * (-2 * y + 3)
            x += 1
            y -= 1
        else:
            d2 += a ** 2 * (-2 * y + 3)
            y -= 1
        putPixels(x, y, color)


def display() -> None:
    """
    绘制图形
    :return:
    """
    glClear(GL_COLOR_BUFFER_BIT)  # 用当前背景色填充窗口
    midBresenhamEllipse(8, 6, [0.0, 0.5, 0.5])
    glFlush()  # 清空OpenGL命令缓冲区，执行OpenGL程序


if __name__ == "__main__":
    init()  # 初始化窗口
    glutDisplayFunc(display)
    glutMainLoop()  # 启动主GLUT事件处理循环
