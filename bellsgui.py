from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from test import Ui_MainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.littlebtn.clicked.connect(self.littleclicked)
        self.ui.jinglebtn.clicked.connect(self.jingleclicked)
        self.ui.carolbtn.clicked.connect(self.carolclicked)

    def carolclicked(self):
        self.ui.label2.setText("You clicked: Carol of the Bells")
        self.updatelabel2size()
        print("Carol button was clicked")

    def jingleclicked(self):
        self.ui.label2.setText("You clicked: Jingle Bells")
        self.updatelabel2size()
        print("Jingle button was clicked")

    def littleclicked(self):
        self.ui.label2.setText("You clicked: Little Drummer Boy")
        self.updatelabel2size()
        print("Little button was clicked")

    def updatelabel2size(self):
        self.ui.label2.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

window()