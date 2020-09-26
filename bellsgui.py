from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from test import Ui_MainWindow
import PyQt5

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
        self.ui.pauseplaybtn.clicked.connect(self.pauseClicked)
        self.ui.exitbtn.clicked.connect(self.exitclicked)
        self.win = self
        self.app = app

    def exitclicked(self):
        sys.exit()

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

    def pauseClicked(self):
        self.songselectbtnsswitch(True)
        x = 1
        while(x == 1):
            self.win.updatelabel2("Pause Button Clicked! \nWaiting for another press!")
            if(self.ui.carolbtn):
                x = 0
                self.win.updatelabel2("Playing Carol Of Bells! ")
                self.ui.carolbtn.clicked.connect(self.carolclicked)
            if(self.ui.jinglebtn):
                x = 0
                self.win.updatelabel2("Playing Jingle Bells!")
                self.ui.jinglebtn.clicked.connect(self.jingleclicked)
            if(self.ui.littlebtn):
                x = 0
                self.win.updatelabel2("Playing Little Drummer Boy!")
                self.ui.littlebtn.clicked.connect(self.littleclicked)
            if(self.ui.exitbtn):
                x = 0
                self.win.updatelabel2("Exiting Program!")
                self.ui.exitbtn.clicked.connect(self.exitclicked)
            if(self.ui.exitbtn):
                x = 0
                self.songselectbtnsswitch(False)

    def updatelabel2(self, text):
        self.ui.label2.setText(text)
        self.ui.label2.adjustSize()

    def songselectbtnsswitch(self, logic):
        self.ui.carolbtn.setEnabled(logic)
        self.ui.jinglebtn.setEnabled(logic)
        self.ui.littlebtn.setEnabled(logic)

# stylesheet = """
#     QMainWindow {
#         background-image: url("pics/christmasbackground.jpg"); 
#         background-repeat: no-repeat; 
#         background-position: center;

#         border: 1px solid black;
#     }

# """

# use below for Raspberry Pi and make sure file path mirrors the same.

stylesheet = """
    QMainWindow {
        background-image: url("/home/pi/Documents/Lab2Files/christmasbackground.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
        border: 1px solid black;
    }
"""

def window():
    app = QApplication(sys.argv)

    QtGui.QFontDatabase.addApplicationFont("SantasSleighFull.ttf")

    # use below for Raspberry Pi and make sure file path mirrors the same.
    QtGui.QFontDatabase.addApplicationFont("/home/pi/Documents/HopperAppStyles/SantasSleighFull.ttf")
    
    app.setStyleSheet(stylesheet)   
    win = MyWindow(app)
    # win.showMaximized()
    win.showFullScreen()
    sys.exit(app.exec_())

window()