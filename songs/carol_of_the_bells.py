from time import sleep
#import RPi.GPIO as GPIO

class NewCarolSong():

    def __init__(self, win, app):
        self.win = win
        self.app = app

    def startsong(self):
        print("Carol button was clicked")
        self.win.updatelabel2("You clicked: Carol of the Bells")
        self.app.processEvents()
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(23, GPIO.OUT)
        # print("hi")

        # for i in range(5):
        #     self.win.updatelabel2("You clicked: Carol of the Bells. Iteration {}".format(i + 1))
        #     self.app.processEvents()
        #     GPIO.output(23, True)
        #     sleep(1)
        #     GPIO.output(23, False)
        #     sleep(1)

        print("done")