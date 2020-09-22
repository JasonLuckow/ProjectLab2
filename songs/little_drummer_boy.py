from time import sleep
# comment out below when working on windows 
import RPi.GPIO as GPIO

class NewDrumSong():

    def __init__(self, win, app):
        self.win = win
        self.app = app
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(25, GPIO.OUT)

    def startsong(self):
        print("Little button was clicked")
        # comment out below when working on windows

        for i in range(10):
            self.win.updatelabel2(" You clicked: Little Drummer Boy.\nIteration {}".format(i + 1))
            self.app.processEvents()
            GPIO.output(25, True)
            sleep(.5)
            GPIO.output(25, False)
            sleep(.5)

        print("done")
        self.win.updatelabel2("Little button was clicked.\nClick another!")