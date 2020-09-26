"""
    Project Lab 2 ECE 3332 - Fall 2020
    File: bellsgui.py
    Date created: 09/08/2020
    Author: Jason Luckow - jluckow - R11560069
    Contributors: Shawn Isbell

    Description: Main file that handles the gui and calling of songs
"""
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

"""
    Checklist for running the application in Windows and the Raspberry Pi (in no specific order):
    Don't delete these items just uncomment them
    1. Stylesheet
    2. Font in the window function
    3. RPI imports for each of the song classes in the songs folder
    4. Anything in the songs classes that uses GPIO.method

    Note: You must make sure that the filepath for the picutres and fonts are the same as 
    they are in code.

    Note: Please remember to use good names for variables, files, classes, and functions
"""

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:
    
    error
        `tuple` (exctype, value, traceback.format_exc() )

    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)


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
        # assigned the value non unless we need to return things in between processing
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
        # only left in to show that we can return things that need to be displayed in between processing
        #     self.signals.result.emit(result)  # Return the result of the processing
        finally:
             self.signals.finished.emit()  # Done


class MyWindow(QMainWindow):
    def __init__(self, app):
        """
        Initializes all needed variables

        """
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
        self.win = self
        self.app = app

    def exitclicked(self):
        """
        Exits the application when the exit button is clicked.
        Is connected to exitbtn
        """
        sys.exit()
    
    def afterSong(self):
        """
        Is executed after every song. Is connected to a worker signal.
        """
        self.songselectbtnsswitch(True)
        self.pausePlaySwitch(False)

    def carolclicked(self):
        """
        Handles carol of the bells song playing with worker classes, signals, and threadpools.
        Think of the worker class as a thread that happens in the background while the ui continues 
        so that pause, play, and exit to work. 
        """
        self.songselectbtnsswitch(False)

        carolsong = carol.NewCarolSong(self.win, self.app)

        self.carolWorker = Worker(carolsong.startsong) # add the function to execute to the worker class
        self.carolWorker.signals.finished.connect(self.afterSong) # function that will execute after carolWorker is done
        self.threadpool.start(self.carolWorker) # starts carolWorker with the above requirements

        self.songselectbtnsswitch(True)

    def jingleclicked(self):
        """
        Handles carol of the bells song playing with worker classes, signals, and threadpools.
        Think of the worker class as a thread that happens in the background while the ui continues 
        so that pause, play, and exit to work. 
        """

        self.songselectbtnsswitch(False)

        jinglesong = jingle.NewJingleSong(self.win, self.app)
        jinglesong.startsong()

        self.songselectbtnsswitch(True)

    def littleclicked(self):
        """
        Handles carol of the bells song playing with worker classes, signals, and threadpools.
        Think of the worker class as a thread that happens in the background while the ui continues 
        so that pause, play, and exit to work. 
        """
        self.songselectbtnsswitch(False)
        
        drumsong = drum.NewDrumSong(self.win, self.app)
        drumsong.startsong()

        self.songselectbtnsswitch(True)

    def pauseClicked(self):
        """
        Handles the pause functionality for the app. Could possibly be further devloped 
        to handle pause and play. Must have songs played in a worker class so that it may run in a threadpool or else
        pause functionality will disapear since the main thread will be playing the song.
        """
        self.setPaused(True) # need to set paused to true so that way the song playing knows to pause
        self.songselectbtnsswitch(True) # set other song buttons to true in case user decides to change songs
        x = 1
        while(x == 1):
            self.win.updatelabel2("Pause Button Clicked! \nWaiting for another press!")
            if(self.ui.carolbtn):
                x = 0
                self.win.updatelabel2("Playing Carol Of Bells! ")
                # line below might not be needed since we already conntected that button to that function
                # when we initialized it.
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
        """
        Handles the play functionality for the app. Could possibly be further devloped 
        to handle pause and play. Must have songs played in a worker class so that it may run in a threadpool or else
        pause functionality will disapear since the main thread will be playing the song.
        """
        self.setPaused(False) # set paused to false so that the song currently playing knows that it is no longer paused
        self.songselectbtnsswitch(False) # since the song is playing the user should not be able to select a new song
        self.win.updatelabel2("Play button clicked!\nResuming the song.")

    def setPaused(self, logic):
        """
        Setter for the pause variable
        """
        self.isPaused = logic

    def getPaused(self):
        """
        Getter for the pause variable
        """
        return self.isPaused

    def updatelabel2(self, text):
        self.ui.label2.setText(text)
        self.ui.label2.adjustSize()

    def songselectbtnsswitch(self, logic):
        """
        Switches the song list to clickable or not
        """
        self.ui.carolbtn.setEnabled(logic)
        self.ui.jinglebtn.setEnabled(logic)
        self.ui.littlebtn.setEnabled(logic)
    
    def pausePlaySwitch(self, logic):
        """
        Switches the pause and play buttons to clickable or not
        """
        self.ui.pausebtn.setEnabled(logic)
        self.ui.playbtn.setEnabled(logic)

# use below for windows

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

    # use below for windows

    #QtGui.QFontDatabase.addApplicationFont("SantasSleighFull.ttf")

    # use below for Raspberry Pi and make sure file path mirrors the same.

    QtGui.QFontDatabase.addApplicationFont("/home/pi/Documents/Lab2Files/SantasSleighFull.ttf")
    
    app.setStyleSheet(stylesheet)   
    win = MyWindow(app)
    # win.showMaximized()
    win.showFullScreen() # For testing showMaximized is fine. For fullscreen on the 7 in display please use this line
    sys.exit(app.exec_())

window()