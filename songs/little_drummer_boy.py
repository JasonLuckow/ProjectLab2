"""
    Project Lab 2 ECE 3332 - Fall 2020
    File: bellsgui.py
    Date created: 09/08/2020
    Author: Jason Luckow - jluckow - R11560069
    Contributors: Shawn Isbell

    Description: Main file that handles the gui and calling of songs
"""
from time import sleep
# comment out below when working on windows 
import RPi.GPIO as GPIO

class NewDrummerSong():

    def __init__(self, win, app):
        self.win = win
        self.app = app
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(24, GPIO.OUT)

    def startsong(self, progress_callback):
        print("Little button was clicked")
        # comment out below when working on windows
        self.win.pausePlaySwitch(True)

        self.win.updatelabel2(" Little Drummer Boy is Playing")
        self.app.processEvents()

        self.all(False)

        GPIO.output(24, True)
        sleep(.5)
        GPIO.output(24, False)
        sleep(.5)
        GPIO.output(24, True)
        sleep(.5)
        GPIO.output(24, False)
        sleep(.5)
        GPIO.output(24, True)
        sleep(.5)
        GPIO.output(24, False)
        sleep(.5)

        self.win.updatelabel2("Little button was clicked.\nClick another!")

    def all(self, bo):
        """
        right now this function turns off or on 3 gpio pins depending on the
        boolean variable bo
        """

        GPIO.output(24, False)
        GPIO.output(27, False)
        GPIO.output(22, False)