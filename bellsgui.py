"""
    Project Lab 2 ECE 3332 - Fall 2020
    File: bellsgui.py
    Date created: 09/08/2020
    Author: Jason Luckow - jluckow - R11560069
    Contributors: Shawn Isbell - 
    Description: Main file that handles the gui and calling of songs

    adding this for master
"""
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys, traceback
from test import Ui_MainWindow
import PyQt5
import time

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from NickCode import JingleBells as jingle
from NickCode import Housetop as drummer
from NickCode import Carol as carol
from NickCode import music

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
    """
        Defines the signals available from a running worker thread.
        Supported signals are:
        
        error
            `tuple` (exctype, value, traceback.format_exc() )
    """
    progress_callback = pyqtSignal(int)
    finished = pyqtSignal()
    error = pyqtSignal(tuple)


class Worker(QRunnable):
    """
        Worker thread
        Inherits from QRunnable to handler worker thread setup, signals and wrap-up.
        :param callback: The function callback to run on this worker thread. Supplied args and 
                        kwargs will be passed through to the runner.
        :type callback: function
        :param args: Arguments to pass to the callback function
        :param kwargs: Keywords to pass to the callback function
    """

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()    

        # Add the callback to our kwargs
        # assigned the value non unless we need to return things in between processing
        self.kwargs['progress_callback'] = self.signals.progress_callback      

    @pyqtSlot()
    def run(self):
        """
            Initialise the runner function with passed args, kwargs.
        """
        
        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
        # only left in to show that we can return things that need to be displayed in between processing
            self.signals.progress_callback.emit(result)  # Return the result of the processing
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
        self.ui.exitbtn.clicked.connect(self.exitclicked)
        self.ui.tempoSlider.valueChanged[int].connect(self.updateTempo)

        self.setSongPlaying(False)#Initialize Song Stopper
        self.isPaused = False
        self.progress = 0
        self.currentTempo = 290
        
        self.threadpool = QThreadPool()
        self.win = self
        self.app = app

        self.ui.progressBar.setVisible(False)

    def exitclicked(self):
        """
            Exits the application when the exit button is clicked.
            Is connected to exitbtn
        """
        # We need to have a class containing functions that all songs use so that we can call 
        # the all function here. For now this will do.
        forPausing = music.music(self.win, self.app, "no song")
        forPausing.all(False)
        sys.exit()
    
    def afterSong(self):
        """
            Is executed after every song. Is connected to a worker signal.
            Right now it is not used because it causes bugs in switching songs.
        """
        #self.songselectbtnsswitch(True)
        #self.pausePlaySwitch(False)
        
    def carolclicked(self):
        """
            Handles carol of the bells song playing with worker classes, signals, and threadpools.
            Think of the worker class as a thread that happens in the background while the ui continues 
            so that pause, play, and exit to work. 
        """
        #Turn All Songs Off
        self.setPaused(False) #Turn Paused Off
        self.setSongPlaying(False) #Turn Song Off
        self.threadpool.waitForDone() #Wait for songs to return
        self.setSongPlaying(True) #Turn Song On
        self.ui.progressBar.setVisible(True)

        carolsong = carol.NewCarolSong(self.win, self.app)
        self.carolWorker = Worker(carolsong.startsong) # add the function to execute to the worker class
        self.carolWorker.signals.finished.connect(self.afterSong) # function that will execute after carolWorker is done
        self.carolWorker.signals.progress_callback.connect(self.updateProgressBar) # function that will execute when carolWorker sends a signal
        self.threadpool.start(self.carolWorker) # starts carolWorker with the above requirements
        #self.songselectbtnsswitch(True)

    def jingleclicked(self):
        """
            Handles jingle bells song playing with worker classes, signals, and threadpools.
            Think of the worker class as a thread that happens in the background while the ui continues 
            so that pause, play, and exit to work. 
        """
        #Turn All Songs Off
        #Setup For next Song
        self.setPaused(False) #Turn Paused Off
        self.setSongPlaying(False) #Turn Song Off
        self.threadpool.waitForDone() #Wait for songs to return
        self.setSongPlaying(True) #Turn Song On
        self.ui.progressBar.setVisible(True)

        jinglesong = jingle.NewJingleSong(self.win, self.app)
        self.jingleWorker = Worker(jinglesong.startsong) # add the function to execute to the worker class
        self.jingleWorker.signals.finished.connect(self.afterSong) # function that will execute after carolWorker is done
        self.jingleWorker.signals.progress_callback.connect(self.updateProgressBar) # function that will execute when carolWorker sends a signal
        self.threadpool.start(self.jingleWorker) # starts carolWorker with the above requirements


    def littleclicked(self):
        """
            Handles little drummer boy song playing with worker classes, signals, and threadpools.
            Think of the worker class as a thread that happens in the background while the ui continues 
            so that pause, play, and exit to work. 
        """
        #Setup For next Song
        self.setPaused(False) #Turn Paused Off
        self.setSongPlaying(False) #Turn Song Off
        self.threadpool.waitForDone() #Wait for songs to return
        self.setSongPlaying(True) #Turn Song On
        self.ui.progressBar.setVisible(True)

        drummersong = drummer.NewHousetopSong(self.win, self.app)
        self.drummerWorker = Worker(drummersong.startsong) # add the function to execute to the worker class
        self.drummerWorker.signals.finished.connect(self.afterSong) # function that will execute after carolWorker is done
        self.drummerWorker.signals.progress_callback.connect(self.updateProgressBar) # function that will execute when carolWorker sends a signal
        self.threadpool.start(self.drummerWorker) # starts carolWorker with the above requirements

    def pauseClicked(self):
        """
            Handles the pause functionality for the app. Could possibly be further devloped 
            to handle pause and play. Must have songs played in a worker class so that it may run in a threadpool or else
            pause functionality will disapear since the main thread will be playing the song.
        """
        self.updatelabel2('paused')
        print("\n\npause clicked\n\n")
        if self.getPaused() is True:
            self.setPaused(False) # set paused to false so that the song currently playing knows that it is no longer paused
            self.win.updatelabel2("Play button clicked!\nResuming the song.")
        else:
            self.setPaused(True) # need to set paused to true so that way the song playing knows to pause

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

    def getStopped(self):
        """
            Getter for the stop variable
        """
        return self.stopSong

    def setSongPlaying(self, logic):
        """
            Setter for the stop variable
        """
        self.stopSong = not logic

    def setProgressBarMax(self,value):
        """
            Sets Max value for progress bar
        """
        self.ui.progressBar.setMaximum(value)

    def updateTempo(self, valueChanged):
        """
            Updates the global tempo variable and Tempo label
        """
        self.currentTempo = valueChanged
        self.ui.tempoSlider.setValue(self.currentTempo)
        self.updateTempoLabel(str(valueChanged))

    def getTempoValue(self):
        return self.currentTempo

    def updateProgressBar(self, progress_callback):
        """
            Updates progress bar with progress_callback as current value
        """
        self.ui.progressBar.setValue(progress_callback)

    def updateTempoLabel(self, text):
        self.ui.tempoLabel.setText("Tempo : "+text)
        # self.ui.tempoLabel.adjustSize()

    def updatelabel2(self, text):
        self.ui.label2.setText(text)
        self.ui.label2.adjustSize()
    
    def pausePlaySwitch(self, logic):
        """
            Switches the pause and play buttons to clickable or not
        """
        self.ui.pausebtn.setEnabled(logic)

# use below for windows

# stylesheet = """
#     QMainWindow {
#         background-image: url("pics/christmasbackground.jpg"); 
#         background-repeat: no-repeat; 
#         background-position: center;

#         border: 1px solid black;
#     }

# """

# use below for Shawns Raspberry Pi and make sure file path mirrors the same.

# stylesheet = """
#     QMainWindow {
#         background-image: url("/home/pi/Desktop/PLab02/PLabTest/pics/christmasbackground.jpg"); 
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

    # use below for Shawns Raspberry Pi and make sure file path mirrors the same.

    #QtGui.QFontDatabase.addApplicationFont("/home/pi/Desktop/PLab02/PLabTest/SantasSleighFull.ttf")

    # use below for Raspberry Pi and make sure file path mirrors the same.
    
    QtGui.QFontDatabase.addApplicationFont("/home/pi/Documents/Lab2Files/SantasSleighFull.ttf")
    
    app.setStyleSheet(stylesheet)   
    win = MyWindow(app)
    # win.showMaximized()
    win.showFullScreen() # For testing showMaximized is fine. For fullscreen on the 7 in display please use this line
    sys.exit(app.exec_())

window()