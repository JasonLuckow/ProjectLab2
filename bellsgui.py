from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from test import Ui_MainWindow

from songs import jingle_bells as jingle
from songs import little_drummer_boy as drum
from songs import carol_of_the_bells as carol

class MyWindow(QMainWindow):
    def __init__(self, app):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.littlebtn.clicked.connect(self.littleclicked)
        self.ui.jinglebtn.clicked.connect(self.jingleclicked)
        self.ui.carolbtn.clicked.connect(self.carolclicked)
        self.win = self
        self.app = app

    def carolclicked(self):
        carolsong = carol.NewCarolSong(self.win, self.app)
        carolsong.startsong()

    def jingleclicked(self):
        jinglesong = jingle.NewJingleSong(self.win, self.app)
        jinglesong.startsong()

    def littleclicked(self):
        drumsong = drum.NewDrumSong(self.win, self.app)
        drumsong.startsong()

    def updatelabel2(self, text):
        self.ui.label2.setText(text)
        self.ui.label2.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow(app)
    win.showMaximized()
    sys.exit(app.exec_())

window()