"""
    Project Lab 2 ECE 3332 - Fall 2020
    File: bellsgui.py
    Date created: 09/08/2020
    Author: Jason Luckow - jluckow - R11560069
    Contributors: Shawn Isbell
    Description: Main file that handles the gui and calling of songs
"""
from time import sleep
# comment out below when working on windows app
import RPi.GPIO as GPIO

import threading
import os
import math
import time
from datetime import datetime

class NewJingleSong():

    def __init__(self, win, app):
        self.win = win
        self.app = app
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(23, GPIO.OUT)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(24, GPIO.OUT)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(27, GPIO.OUT)

    def startsong(self, progress_callback):
        """
        Ideally this method is where the song would go. You would activate each gpio pin with their corresponding bell note
        and for playing two notes at the same time you would use threading
        """
        self.win.pausePlaySwitch(True) # must set the pause play buttons to be clickable

        self.win.updatelabel2(" Jingle Bells is playing")
        self.app.processEvents()

        x = threading.Thread(target=self.calc, args=(True, 22, .5, 25,))
        x.start()

        y = threading.Thread(target=self.calc, args=(True, 24, .5, 25,))
        y.start()

        #z = threading.Thread(target=calc, args=(False, 25, 1, 12,))
        #z.start()

        j = threading.Thread(target=self.calc, args=(False, 27, 1, 12,))
        j.start()

        x.join()
        y.join()
        #z.join()
        j.join()

        self.all(False)

        x = threading.Thread(target=self.motorswitch, args=(True, 22, 2,))
        x.start()

        y = threading.Thread(target=self.motorswitch, args=(True, 24, 2,))
        y.start()

        z = threading.Thread(target=self.motorswitch, args=(False, 27, 2,))
        z.start()

        x.join()
        y.join()
        z.join()

        self.all(False)

        x = threading.Thread(target=self.motorswitch, args=(False, 22, 2,))
        x.start()

        y = threading.Thread(target=self.motorswitch, args=(True, 24, 2,))
        y.start()

        z = threading.Thread(target=self.motorswitch, args=(True, 27, 2,))
        z.start()

        x.join()
        y.join()
        z.join()

        self.all(False)

        x = threading.Thread(target=self.motorswitch, args=(True, 22, 2,))
        x.start()

        y = threading.Thread(target=self.motorswitch, args=(False, 24, 2,))
        y.start()

        z = threading.Thread(target=self.motorswitch, args=(True, 27, 2,))
        z.start()

        x.join()
        y.join()
        z.join()

        self.all(False)

        self.win.updatelabel2(" Jingle button was clicked.\nClick another!")
    
    def motorswitch(self, bo, pin, t):
        """
        Controls the output to the gpio pins that control the actuators
        """
        if(self.win.getStopped() == True):
            self.win.updatelabel2("Jingle button was clicked.\nClick another!")
            return
        while self.win.getPaused() == True:
            self.all(False)
            self.win.updatelabel2("Jingle Song Paused!\nChoose A new Song or Play to Resume!")
            time.sleep(.1)
        GPIO.output(pin, bo)
        time.sleep(t)

    def calc(self, bo, pin, t, n):
        for i in range(n):
            if(self.win.getStopped() == True):
                self.win.updatelabel2("Carol button was clicked.\nClick another!")
                return
            while self.win.getPaused() == True:
                self.all(False)
                self.win.updatelabel2("Jingle Song Paused!\nChoose A new Song or Play to Resume!")
                time.sleep(.1)
            bo = not bo
            GPIO.output(pin, bo)
            time.sleep(t)

    def all(self, bo):
        """
        right now this function turns off or on 3 gpio pins depending on the
        boolean variable bo. Would encompass all outputs
        """
        GPIO.output(24, False)
        GPIO.output(27, False)
        GPIO.output(22, False)