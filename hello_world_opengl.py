import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtOpenGL
from OpenGL.GL import *

class MyCanvas(QtOpenGL.QGLWidget):
    def __init__(self):
        super(MyCanvas, self).__init__()
        self.setWindowTitle("MyGLDrawer")
        self.setGeometry(100, 100, 600, 400)
        self.m_w = 0
        self.m_h = 0

    def initializeGL(self):
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

    def resizeGL(self, _width, _height):
        self.m_w = _width
        self.m_h = _height
        glViewport(0, 0, self.m_w, self.m_h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, self.m_w, 0, self.m_h, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
    
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        xA = self.m_w / 3.0
        yA = self.m_h / 3.0
        xB = self.m_w * 2.0 / 3.0
        yB = self.m_h / 3.0
        xC = self.m_w / 2.0
        yC = self.m_h * 2.0 / 3.0
        glShadeModel(GL_SMOOTH)
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(xA, yA)
        glColor3f(0.0, 1.0, 0.0)
        glVertex2f(xB, yB)
        glColor3f(0.0, 0.0, 1.0)
        glVertex2f(xC, yC)
        glEnd()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    canvas = MyCanvas()
    canvas.show()
    sys.exit(app.exec_())