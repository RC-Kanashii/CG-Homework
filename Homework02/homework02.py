from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Point:
    """
    点类
    """

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x  # 实例变量
        self.y = y


iPointNum = 0  # 已确定点的数目
points = [Point(), Point()]  # 点集，存储直线的两个端点
winWidth = 400  # 窗口的宽度
winHeight = 300  # 窗口的高度


def init() -> None:
    glClearColor(1.0, 1.0, 1.0, 1.0)  # 设置窗口背景颜色


def changeSize(w: int, h: int) -> None:
    """
    改变窗口大小
    :param w: 调整后窗口的宽度
    :param h: 调整后窗口的高度
    :return:
    """
    # 保存当前窗口的大小
    global winWidth, winHeight
    winWidth = w
    winHeight = h

    glViewport(0, 0, w, h)  # 指定窗口显示区域

    # 下两行为伴生代码
    glMatrixMode(GL_PROJECTION)  # 指定设置投影参数
    glLoadIdentity()  # 调用单位矩阵，去掉以前的投影参数设置
    gluOrtho2D(0, winWidth, 0, winHeight)  # 设置投影参数（裁剪窗口）


def display() -> None:
    """
    显示直线
    :return:
    """
    glClear(GL_COLOR_BUFFER_BIT)  # 用当前背景色填充窗口
    glColor3f(1.0, 0.0, 0.0)  # 指定当前的绘图颜色

    if iPointNum >= 1:
        # 绘制直线段的代码要写在glBegin, glEnd之间
        glBegin(GL_LINES)  # 绘制直线段
        glVertex2i(points[0].x, points[0].y)  # 起点
        glVertex2i(points[1].x, points[1].y)  # 终点
        glEnd()

    glutSwapBuffers()  # 交换缓冲区


def mousePlot(button: GLint, action: GLint, xMouse: GLint, yMouse: GLint) -> None:
    """
    监听鼠标按键
    :param button: 被按下的键
    :param action: 按下/抬起
    :param xMouse: 光标横坐标
    :param yMouse: 光标纵坐标
    :return:
    """
    if button == GLUT_LEFT_BUTTON and action == GLUT_DOWN:  # 鼠标左键被按下
        global iPointNum
        if iPointNum == 0 or iPointNum == 2:  # 要么没有顶点，要么两个顶点都有，这时候需要重新绘制直线
            # 确定直线段的第一个端点
            iPointNum = 1
            points[0].x = xMouse
            points[0].y = winHeight - yMouse
        else:
            # 确定直线的第二个端点
            iPointNum = 2
            points[1].x = xMouse
            points[1].y = winHeight - yMouse
            glutPostRedisplay()  # 指定窗口重新绘制

    if button == GLUT_RIGHT_BUTTON and action == GLUT_DOWN:  # 鼠标右键被按下
        iPointNum = 0
        glutPostRedisplay()  # 清空界面


def passiveMouseMove(xMouse: GLint, yMouse: GLint) -> None:
    """
    监听鼠标移动
    :param xMouse: 光标横坐标
    :param yMouse: 光标纵坐标
    :return:
    """
    if iPointNum == 1:
        # 将当前鼠标位置指定为直线的未固定端点
        points[1].x = xMouse
        points[1].y = winHeight - yMouse
        glutPostRedisplay()


def pressKey(key: str, x: int, y: int) -> None:
    """
    监听键盘操作
    :param key: 按下哪个按键
    :param x:
    :param y:
    :return:
    """
    if key == b'p':  # 注意：必须要加二进制前缀
        global iPointNum
        if iPointNum == 0 or iPointNum == 2:  # 要么没有顶点，要么两个顶点都有，这时候需要重新绘制直线
            # 确定直线的第一个端点
            iPointNum = 1
            points[0].x = x
            points[0].y = winHeight - y
        else:
            # 确定直线的第二个端点
            iPointNum = 2
            points[1].x = x
            points[1].y = winHeight - y
            glutPostRedisplay()  # 指定窗口重新绘制


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # 使用双缓存及RGB模型
    glutInitWindowSize(400, 300)  # 指定窗口尺寸
    glutInitWindowPosition(100, 100)  # 指定窗口在屏幕上的位置
    glutCreateWindow("Rubber-band drawing")
    glutDisplayFunc(display)
    glutReshapeFunc(changeSize)  # 指定窗口再整形回调函数
    glutMouseFunc(mousePlot)  # 指定鼠标响应函数
    glutPassiveMotionFunc(passiveMouseMove)  # 指定鼠标移动响应函数
    glutKeyboardFunc(pressKey)  # 指定键盘回调函数
    init()
    glutMainLoop()  # 启动主GLUT事件处理循环
