from time import sleep
# comment out below when working on windows 
import RPi.GPIO as GPIO

class NewCarolSong():

    def __init__(self, win, app):
        self.win = win
        self.app = app
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(23, GPIO.OUT)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(23, GPIO.OUT)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(24, GPIO.OUT)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(25, GPIO.OUT)

    def startsong(self):
        print("Carol button was clicked")
        # comment out below when working on windows

        for i in range(2):
            self.win.updatelabel2(" You clicked: Carol of the Bells.\nIteration {}".format(i + 1))
            self.app.processEvents()
            # GPIO.output(23, True)
            # sleep(.5)
            # GPIO.output(23, False)
            # sleep(.5)

            x = threading.Thread(target=calc, args=(True, 23, .5, 25,))
            x.start()

            y = threading.Thread(target=calc, args=(True, 24, .5, 25,))
            y.start()

            z = threading.Thread(target=calc, args=(False, 25, 1, 12,))
            z.start()

            x.join()
            y.join()
            z.join()

            all(False)

        print("done")
        self.win.updatelabel2("Carol button was clicked.\nClick another!")

    

    def motorswitch(bo, pin, t):
        GPIO.output(pin, bo)
        time.sleep(t)

    arr = []

    def timenow():
        return (datetime.now().strftime("%H:%M:%S"))

    def calc(bo, pin, t, n):
        for i in range(n):
            bo = not bo
            GPIO.output(pin, bo)
            time.sleep(t)



    def stepsame(count, type, bo, t):
        print("working {}".format(count))
        arr.append([count, type, bo, timenow()])
        time.sleep(t)

    def all(bo):
        x = threading.Thread(target=motorswitch, args=(bo, 23, .5,))
        x.start()

        y = threading.Thread(target=motorswitch, args=(bo, 24, .5,))
        y.start()

        z = threading.Thread(target=motorswitch, args=(bo, 25, .5,))
        z.start()

        x.join()
        y.join()
        z.join()
