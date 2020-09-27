from threading import Thread
import RPi.GPIO as GPIO
from time import sleep

class Actuator1:
    def __init__(outPin, timing, self):
        self.stopped = False
        self.GPON = False
        self.output = outPin
        self.timing = timing

    def start(self):
        t = Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.output, GPIO.OUT)
        while(True):
            if(self.stopped):
                GPIO.output(self.output, False)
                return
            GPIO.output(self.output, self.GPON)
            sleep(self.timing)
            self.GPON = not self.GPON
    
    def stop(self):
        self.stopped = True

greenLight = Actuator1(23, 0.5)
yellowLight = Actuator1(24, 0.5)
redLight = Actuator1(25, 0.7)

def main():
    greenLight.start()
    yellowLight.start()
    redLight.start()
    stopTimer = 20
    while(stopTimer > 0):
        stopTimer = stopTimer - 1
        sleep(1)
    greenLight.stop()
    yellowLight.stop()
    redLight.stop()
    exit()

if __name__ == "__main__":
    main()