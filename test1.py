import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CustomWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_NoSystemBackground, True)
        # self.setAttribute(Qt.WA_TranslucentBackground, True)

        # Create the button
        pushButton = QPushButton('')
        pushButton.setGeometry(QRect(240, 190, 90, 31))
        pushButton.setText("Finished")
        pushButton.clicked.connect(app.quit)

        # Center the button
        qr = pushButton.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        pushButton.move(qr.topLeft())

        # Run the application
        self.showFullScreen()

    def paintEvent(self, event=None):
        painter = QPainter(self)
        painter.setOpacity(0.2)
        painter.setBrush(Qt.white)
        painter.setPen(QPen(Qt.white))   
        painter.drawRect(self.rect())





if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Create the main window
    window = CustomWindow() 
    sys.exit(app.exec_())