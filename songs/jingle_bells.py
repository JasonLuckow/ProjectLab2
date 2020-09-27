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

class NewJingleSong():

    def __init__(self, win, app):
        self.win = win
        self.app = app
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(24, GPIO.OUT)

    def startsong(self):
        print("Jingle button was clicked")
        # comment out below when working on windows 
        self.win.pausePlaySwitch(True)
        
        for i in range(2):
            self.win.updatelabel2(" You clicked: Jingle Bells.\nIteration {}".format(i + 1))
            self.app.processEvents()
            GPIO.output(24, True)
            sleep(.5)
            GPIO.output(24, False)
            sleep(.5)

        print("done")
        self.win.updatelabel2(" Jingle button was clicked.\nClick another!")