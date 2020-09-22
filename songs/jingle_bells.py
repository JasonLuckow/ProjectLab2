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
        
        for i in range(2):
            self.win.updatelabel2(" You clicked: Jingle Bells.\nIteration {}".format(i + 1))
            self.app.processEvents()
            GPIO.output(24, True)
            sleep(.5)
            GPIO.output(24, False)
            sleep(.5)

        print("done")
        self.win.updatelabel2(" Jingle button was clicked.\nClick another!")