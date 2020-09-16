from time import sleep
#import RPi.GPIO as GPIO

class NewDrumSong():

    def __init__(self, win, app):
        self.win = win
        self.app = app

    def startsong(self):
        print("Little button was clicked")
        self.win.updatelabel2("You clicked: Little Drummer Boy")
        self.app.processEvents()
        # comment out below when working on windows
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(25, GPIO.OUT)
        print("hi")

        for i in range(5):
            self.win.updatelabel2("You clicked: Little Drummer Boy. Iteration {}".format(i + 1))
            self.app.processEvents()
            GPIO.output(25, True)
            sleep(1)
            GPIO.output(25, False)
            sleep(1)

        print("done")