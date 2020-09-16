from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from test import Ui_MainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.littlebtn.clicked.connect(self.littleclicked)
        self.ui.jinglebtn.clicked.connect(self.jingleclicked)
        self.ui.carolbtn.clicked.connect(self.carolclicked)

    def carolclicked(self):
        print("Carol button was clicked")

    def jingleclicked(self):
        print("Jingle button was clicked")

    def littleclicked(self):
        print("Little button was clicked")


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

window()