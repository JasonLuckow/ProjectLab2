from time import sleep
# comment out below when working on windows 
import RPi.GPIO as GPIO

class NewCarolSong():

    def __init__(self, win, app):
        self.win = win
        self.app = app
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(23, GPIO.OUT)

    def startsong(self):
        print("Carol button was clicked")
        # comment out below when working on windows

        for i in range(2):
            self.win.updatelabel2(" You forgot to click: Carol of the Bells.\nIteration {}".format(i + 1))
            self.app.processEvents()
            GPIO.output(23, True)
            sleep(.5)
            GPIO.output(23, False)
            sleep(.5)

        print("done")
        self.win.updatelabel2("Carol button was clicked.\nClick another!")