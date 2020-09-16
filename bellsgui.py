from PyQt5 import QtWidgets, QtCore
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
        self.ui.carolbtn.clicked.connect(self.carolclicked)
        self.ui.jinglebtn.clicked.connect(self.jingleclicked)
        self.ui.littlebtn.clicked.connect(self.littleclicked)
        self.win = self
        self.app = app

    def carolclicked(self):
        self.songselectbtnsswitch(False)

        carolsong = carol.NewCarolSong(self.win, self.app)
        carolsong.startsong()

        self.songselectbtnsswitch(True)

    def jingleclicked(self):
        self.songselectbtnsswitch(False)

        jinglesong = jingle.NewJingleSong(self.win, self.app)
        jinglesong.startsong()

        self.songselectbtnsswitch(True)

    def littleclicked(self):
        self.songselectbtnsswitch(False)
        
        drumsong = drum.NewDrumSong(self.win, self.app)
        drumsong.startsong()

        self.songselectbtnsswitch(True)

    def updatelabel2(self, text):
        self.ui.label2.setText(text)
        self.ui.label2.adjustSize()

    def songselectbtnsswitch(self, logic):
        self.ui.carolbtn.setEnabled(logic)
        self.ui.jinglebtn.setEnabled(logic)
        self.ui.littlebtn.setEnabled(logic)

stylesheet = """
    QMainWindow {
        background-image: url("pics/christmasbackground.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
        background-size: 150px;
        width: 100px;
        height: 100px;
        border: 1px solid black;
    }
"""

# #use below for Raspberry Pi and make sure file path mirrors the same.
# stylesheet = """
#     QMainWindow {
#         background-image: url("/home/pi/Pictures/christmasbackground.jpg"); 
#         background-repeat: no-repeat; 
#         background-position: center;
#         border: 1px solid black;
#     }
# """

def window():
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)   
    win = MyWindow(app)
    win.showMaximized()
    sys.exit(app.exec_())

window()