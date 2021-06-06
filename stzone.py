import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QDialog, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QIcon, QPixmap
from PyQt5.QtCore import Qt, QPoint
import icon


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.opacityvalue = 0.3
        self.stzw = 400
        self.stzh = 500
        self.initUI()

    # def changeOpacity(self):
    #     self.opacityvalue = round(self.slider.value() / 100, 1)
    #     print(self.opacityvalue)
    #     self.setWindowOpacity(self.opacityvalue)

    def changeStzW(self):
        self.stzw = self.slider1.value()
        print(self.stzw)
        self.resize(self.stzw, self.stzh)

    def changeStzH(self):
        self.stzh = self.slider2.value()
        print(self.stzh)
        self.resize(self.stzw, self.stzh)

    def initUI(self):
        # self.slider = QSlider(Qt.Horizontal, self)
        # self.slider.setRange(10, 100)
        # self.slider.setValue(100)
        # self.slider.setSingleStep(10)

        self.slider1 = QSlider(Qt.Horizontal, self)
        self.slider1.setRange(100, 500)
        self.slider1.setValue(200)
        self.slider1.setSingleStep(2)

        self.slider2 = QSlider(Qt.Vertical, self)
        self.slider2.setRange(100, 500)
        self.slider2.setValue(200)
        self.slider2.setSingleStep(2)

        # self.slider.valueChanged.connect(self.changeOpacity)
        self.slider1.valueChanged.connect(self.changeStzW)
        self.slider2.valueChanged.connect(self.changeStzH)

        # hbox = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(self.slider)
        # hbox.addStretch(1)

        # hbox1 = QHBoxLayout()
        # # hbox1.addStretch(1)
        # hbox1.addWidget(self.slider1)
        # # hbox1.addStretch(1)

        # hbox2 = QVBoxLayout()
        # # hbox2.addStretch(1)
        # hbox2.addWidget(self.slider2)
        # # hbox2.addStretch(1)


        # vbox = QVBoxLayout()
        # # vbox.addStretch(1)
        # # vbox.addLayout(hbox)
        # vbox.addLayout(hbox2)
        # vbox.addLayout(hbox1)
        

        # self.setLayout(vbox)

        self.setWindowTitle('STZONE v1.0')
        self.setWindowIcon(QIcon(':/icon.png'))
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.move(300, 300)

        self.setWindowOpacity(self.opacityvalue)
        self.resize(self.stzw, self.stzh)
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