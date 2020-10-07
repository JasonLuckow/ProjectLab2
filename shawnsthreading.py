from threading import Thread
import RPi.GPIO as GPIO
from time import sleep

class Actuator1:
    def __init__(self):
        self.stopped = False
        self.GPON = False

    def start(self):
        t = Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        GPOUT = 23
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(22, GPIO.OUT)
        while(True):
            if(self.stopped):
                GPIO.output(22, False)
                return
            GPIO.output(22, self.GPON)
            sleep(0.5)
            self.GPON = not self.GPON
    
    def stop(self):
        self.stopped = True

class Actuator2:
    def __init__(self):
        self.stopped = False
        self.GPON = False

    def start(self):
        t = Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        GPOUT = 24
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPOUT, GPIO.OUT)
        while(True):
            if(self.stopped):
                GPIO.output(GPOUT, False)
                return
            GPIO.output(GPOUT, self.GPON)
            sleep(0.5)
            self.GPON = not self.GPON
    
    def stop(self):
        self.stopped = True

class Actuator3:
    def __init__(self):
        self.stopped = False
        self.GPON = False

    def start(self):
        t = Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        GPOUT = 25
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPOUT, GPIO.OUT)
        while(True):
            if(self.stopped):
                GPIO.output(GPOUT, False)
                return
            GPIO.output(25, self.GPON)
            sleep(0.9)
            self.GPON = not self.GPON
    
    def stop(self):
        self.stopped = True


greenLight = Actuator1()
yellowLight = Actuator2()
redLight = Actuator3()

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