from time import sleep
import RPi.GPIO as GPIO

class NewCarolSong():

    def __init__(self, win):
        self.win = win

    def startsong(self):
        print("Carol button was clicked")
        self.win.updatelabel2("You clicked: Carol of the Bells")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(24, GPIO.OUT)
        print("hi")

        for i in range(5):
            self.win.app.processEvents()
            self.win.updatelabel2("You clicked: Carol of the Bells {}".format(i))
            GPIO.output(24, True)
            sleep(1)
            GPIO.output(24, False)
            sleep(1)

        print("done")