from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init() -> None:
    """
    初始化窗口
    :return:
    """
    glClearColor(1.0, 1.0, 1.0, 1.0)  # 设置窗口背景色为白色
    glMatrixMode(GL_PROJECTION)  # 指定设置投影参数
    gluOrtho2D(0.0, 200.0, 0.0, 150.0)  # 设置投影参数


def render() -> None:
    """
    绘制多个图形
    :return:
    """
    glClear(GL_COLOR_BUFFER_BIT)  # 用当前背景色填充窗口

    glColor3f(1.0, 1.0, 0.4)  # 设置画笔颜色为黄色
    glRectf(0.0, 0.0, 100.0, 100.0)  # 绘制一张脸

    glColor3f(0.0, 0.0, 0.0)  # 设置画笔颜色为黑色
    glRectf(25.0, 55.0, 35.0, 65.0)  # 绘制左眼
    glRectf(65.0, 55.0, 75.0, 65.0)  # 绘制右眼
    glRectf(25.0, 20.0, 75.0, 30.0)  # 绘制嘴巴

    glFlush()  # 清空OpenGL命令缓冲区，执行OpenGL程序


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # 初始化窗口的显示模式
    glutInitWindowSize(400, 300)  # 设置窗口的尺寸
    glutInitWindowPosition(100, 120)  # 设置窗口的位置
    glutCreateWindow("Emoji")  # 创建一个名为Emoji的窗口（中文会乱码）
    glutDisplayFunc(render)  # 设置当前窗口的显示回调函数
    init()  # 完成窗口的初始化
    glutMainLoop()  # 启动主GLUT事件处理循环
