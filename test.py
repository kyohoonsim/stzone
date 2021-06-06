import sys
from PyQt5 import QtWidgets, QtCore

app = QtWidgets.QApplication(sys.argv)

# create invisble widget
window = QtWidgets.QWidget()
window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
window.resize(800, 600)

# add visible child widget, when this widget is transparent it will also be invisible
visible_child = QtWidgets.QWidget(window)
visible_child.setStyleSheet('QWidget{background-color: white}')
visible_child.setObjectName('vc')
visible_child.resize(800, 600)
layout = QtWidgets.QGridLayout()

# add a close button
close_button = QtWidgets.QPushButton()
close_button.setText('close window')
close_button.clicked.connect(lambda: app.exit(0))
layout.addWidget(close_button)

# add a button that makes the visible child widget transparent
change_size_button = QtWidgets.QPushButton()
change_size_button.setText('change size')
change_size_button.clicked.connect(lambda: visible_child.setStyleSheet('QWidget#vc{background-color: transparent}'))
layout.addWidget(change_size_button)

visible_child.setLayout(layout)
window.show()
app.exec()