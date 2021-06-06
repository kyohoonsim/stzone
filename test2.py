import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QDialog, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QIcon, QPixmap
from PyQt5.QtCore import Qt, QPoint
import icon


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        blueButton = QPushButton('')
        blueButton.setStyleSheet("background-color: yellow;")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(blueButton)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        
        self.move(300, 300)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setStyleSheet('QWidget{border: 1px solid black}')
        self.setWindowOpacity(0.3)
        self.resize(200, 220)
        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    STZone = MyApp()
    sys.exit(app.exec_())