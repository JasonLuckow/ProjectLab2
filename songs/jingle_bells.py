from time import sleep
# comment out below when working on windows 
import RPi.GPIO as GPIO

class NewJingleSong():

    def __init__(self, win, app):
        self.win = win
        self.app = app

    def startsong(self):
        print("Jingle button was clicked")
        self.win.updatelabel2("You clicked: Jingle Bells")
        self.app.processEvents()
        # comment out below when working on windows 
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(24, GPIO.OUT)
        print("hi")

        for i in range(5):
            self.win.updatelabel2("You clicked: Jingle Bells. Iteration {}".format(i + 1))
            self.app.processEvents()
            GPIO.output(24, True)
            sleep(1)
            GPIO.output(24, False)
            sleep(1)

        print("done")