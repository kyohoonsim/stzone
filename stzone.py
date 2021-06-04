import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt, QPoint

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):
        self.setWindowTitle('STZONE v1.0')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.move(300, 300)
        self.setStyleSheet("background-color: yellow;")
        self.setWindowOpacity(0.3)
        self.resize(400, 400)
        self.show()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_rect(qp)
        qp.end()

    def draw_rect(self, qp):
        qp.setBrush(QColor(0, 0, 0))
        qp.setPen(QPen(QColor(255, 0, 0), 3))
        qp.drawRect(int(self.width()/3), int(self.height()/3), int(self.width()/3), int(self.height()/3))

        qp.setPen(QPen(Qt.red, 2))
        qp.drawLine(int(self.width()/3), int(4*self.height()/9), int(2 * self.width()/3), int(4*self.height()/9))

        qp.setPen(QPen(Qt.red, 2))
        qp.drawLine(int(self.width()/3), int(5*self.height()/9), int(2 * self.width()/3), int(5*self.height()/9))

        qp.setPen(QPen(Qt.red, 2))
        qp.drawLine(int(4*self.width()/9), int(self.height()/3), int(4 * self.width()/9), int(2*self.height()/3))

        qp.setPen(QPen(Qt.red, 2))
        qp.drawLine(int(5*self.width()/9), int(self.height()/3), int(5 * self.width()/9), int(2*self.height()/3))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    STZone = MyApp()
    sys.exit(app.exec_())