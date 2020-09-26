from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys, traceback
from test import Ui_MainWindow
import PyQt5

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from songs import jingle_bells as jingle
from songs import little_drummer_boy as drum
from songs import carol_of_the_bells as carol

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data
    
    error
        `tuple` (exctype, value, traceback.format_exc() )
    
    result
        `object` data returned from processing, anything

    progress
        `int` indicating % progress 

    '''
    # finished = pyqtSignal()
    error = pyqtSignal(tuple)
    # result = pyqtSignal(object)
    #progress = pyqtSignal()


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and 
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()    

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = None      

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        
        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        # else:
        #     self.signals.result.emit(result)  # Return the result of the processing
        # finally:
        #     self.signals.finished.emit()  # Done


class MyWindow(QMainWindow):
    def __init__(self, app):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.carolbtn.clicked.connect(self.carolclicked)
        self.ui.jinglebtn.clicked.connect(self.jingleclicked)
        self.ui.littlebtn.clicked.connect(self.littleclicked)
        self.ui.pausebtn.clicked.connect(self.pauseClicked)
        self.ui.playbtn.clicked.connect(self.playClicked)
        self.ui.exitbtn.clicked.connect(self.exitclicked)
        self.isPaused = False
        self.threadpool = QThreadPool()
        self.carolWorker = None
        self.win = self
        self.app = app

    def exitclicked(self):
        sys.exit()

    def carolclicked(self):
        self.songselectbtnsswitch(False)

        carolsong = carol.NewCarolSong(self.win, self.app)

        self.carolWorker = Worker(carolsong.startsong) # Any other args, kwargs are passed to the run function
        # worker.signals.result.connect(self.print_output)
        # worker.signals.finished.connect(self.thread_complete)
        #worker.signals.progress.connect(self.carolnotify)

        self.threadpool.start(self.carolWorker) 

        #carolsong.startsong()
        print("here after threadpool")
        self.songselectbtnsswitch(True)

    def getCarolWorker(self):
        return self.carolWorker

    def getThreadPool(self):
        return self.threadpool

    def jingleclicked(self):
        print("here1")
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
        self.setPaused(True)
        self.songselectbtnsswitch(True)
        x = 1
        while(x == 1):
            self.win.updatelabel2("Pause Button Clicked! \nWaiting for another press!")
            if(self.ui.carolbtn):
                x = 0
                self.win.updatelabel2("Playing Carol Of Bells! ")
                # line below shouldnt be needed since we already conntected that button to that function.
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

    def playClicked(self):
        self.setPaused(False)
        self.songselectbtnsswitch(False)
        self.win.updatelabel2("Play button clicked!\nResuming the song.")
        

    def setPaused(self, logic):
        self.isPaused = logic

    def getPaused(self):
        return self.isPaused

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

    #QtGui.QFontDatabase.addApplicationFont("SantasSleighFull.ttf")

    # use below for Raspberry Pi and make sure file path mirrors the same.
    QtGui.QFontDatabase.addApplicationFont("/home/pi/Documents/Lab2Files/SantasSleighFull.ttf")
    
    app.setStyleSheet(stylesheet)   
    win = MyWindow(app)
    # win.showMaximized()
    win.showFullScreen()
    sys.exit(app.exec_())

window()