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

class NewCarolSong():

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

        for i in range(2):
            # self.win.updatelabel2(" You clicked: Carol of the Bells.\nIteration {}".format(i + 1))
            # self.app.processEvents()
            # GPIO.output(23, True)
            # sleep(.5)
            # GPIO.output(23, False)
            # sleep(.5)

            count = 0
            while count < 1:
                if(self.win.getStopped() == True):
                    self.win.updatelabel2("Carol button was clicked.\nClick another!")
                    self.all(False)
                    return
                self.win.updatelabel2(" PASS {}".format(i))
                self.app.processEvents()
                #First movement: all three actuators move in and out 5 times
                first_solenoid = threading.Thread(target=self.calc, args=(True, 22, 0.5, 5))
                first_solenoid.start()
                second_solenoid = threading.Thread(target=self.calc, args=(True, 24, 0.5, 5))
                second_solenoid.start()
                third_solenoid = threading.Thread(target=self.calc, args=(True, 27, 0.5, 5))
                third_solenoid.start()
                first_solenoid.join()
                second_solenoid.join()
                third_solenoid.join()
                self.all(False)
                #Second movement: the actuators all move at different speeds, but will sometimes move at the same time when the timing matches
                first_solenoid = threading.Thread(target=self.calc, args=(True, 22, 1, 5))
                first_solenoid.start()
                second_solenoid = threading.Thread(target=self.calc, args=(True, 24, 0.75, 7))
                second_solenoid.start()
                third_solenoid = threading.Thread(target=self.calc, args=(True, 27, 0.5, 10))
                third_solenoid.start()
                first_solenoid.join()
                second_solenoid.join()
                third_solenoid.join()
                self.all(False)
                #Third movement: the third actuator will move in and out while the other two are in a resting position
                first_solenoid = threading.Thread(target=self.calc, args=(True, 22, 1, 1))
                first_solenoid.start()
                second_solenoid = threading.Thread(target=self.calc, args=(True, 24, 1, 1))
                second_solenoid.start()
                third_solenoid = threading.Thread(target=self.calc, args=(False, 27, 1, 1))
                third_solenoid.start()
                first_solenoid.join()
                second_solenoid.join()
                third_solenoid.join()
                self.all(False)
                #Fourth movement: the second actuator will move in and out while the other two are in a resting position
                first_solenoid = threading.Thread(target=self.calc, args=(True, 22, 1, 1))
                first_solenoid.start()
                second_solenoid = threading.Thread(target=self.calc, args=(False, 24, 1, 1))
                second_solenoid.start()
                third_solenoid = threading.Thread(target=self.calc, args=(True, 27, 1, 1))
                third_solenoid.start()
                first_solenoid.join()
                second_solenoid.join()
                third_solenoid.join()
                self.all(False)
                #Fifth movement: the first actuator will move in and out while the other two are in a resting position
                first_solenoid = threading.Thread(target=self.calc, args=(False, 22, 1, 1))
                first_solenoid.start()
                second_solenoid = threading.Thread(target=self.calc, args=(True, 24, 1, 1))
                second_solenoid.start()
                third_solenoid = threading.Thread(target=self.calc, args=(True, 27, 1, 1))
                third_solenoid.start()
                first_solenoid.join()
                second_solenoid.join()
                third_solenoid.join()
                self.all(False)
                #Sixth movement: the actuators all move at different speeds, but will sometimes move at the same time when the timing matches. 
                #Similar to the second movement, but is at a faster speed
                first_solenoid = threading.Thread(target=self.calc, args=(True, 22, 0.25, 25))
                first_solenoid.start()
                second_solenoid = threading.Thread(target=self.calc, args=(True, 24, 0.75, 25))
                second_solenoid.start()
                third_solenoid = threading.Thread(target=self.calc, args=(True, 27, 0.5, 25))
                third_solenoid.start()
                first_solenoid.join()
                second_solenoid.join()
                third_solenoid.join()
                self.all(False)

                count += 1
            if(self.win.getStopped() == True):
                self.all(False)
                self.win.updatelabel2("Carol button was clicked.\nClick another!")
                return
        self.win.updatelabel2("Carol button was clicked.\nClick another!")
    
    def motorswitch(self, bo, pin, t):
        """
        Controls the output to the gpio pins that control the actuators
        """
        self.app.processEvents()
        if(self.win.getStopped() == True):
            self.win.updatelabel2("Carol button was clicked.\nClick another!")
            return
        while self.win.getPaused() == True:
            self.app.processEvents() # Not really too sure if this line is needed. NEEDS TESTING
            self.win.updatelabel2("Carol Song Paused!\nChoose A new Song or Play to Resume!")
            time.sleep(.1)
        GPIO.output(pin, bo)
        time.sleep(t)

    def calc(self, bo, pin, t, n):
        for i in range(n):
            self.app.processEvents()
            if(self.win.getStopped() == True):
                self.win.updatelabel2("Carol button was clicked.\nClick another!")
                return
            while self.win.getPaused() == True:
                self.app.processEvents() # Not really too sure if this line is needed. NEEDS TESTING
                self.win.updatelabel2("Carol Song Paused!\nChoose A new Song or Play to Resume!")
                time.sleep(.1)
            bo = not bo
            GPIO.output(pin, bo)
            time.sleep(t)

    def all(self, bo):
        """
        right now this function turns off or on 3 gpio pins depending on the
        boolean variable bo
        """

        x = threading.Thread(target=self.motorswitch, args=(bo, 22, .5,))
        x.start()

        y = threading.Thread(target=self.motorswitch, args=(bo, 24, .5,))
        y.start()

        z = threading.Thread(target=self.motorswitch, args=(bo, 27, .5,))
        z.start()

        x.join()
        y.join()
        z.join()