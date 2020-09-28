import threading
import os
import math
import time
from datetime import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

#x - 23
#y - 24
#z - 25

for i in range(10):

    GPIO.output(23, True)
    sleep(.5)
    GPIO.output(23, False)
    sleep(1)

    GPIO.output(24, True)
    sleep(.5)
    GPIO.output(24, False)
    sleep(.5)

    GPIO.output(23, True)
    sleep(.5)
    GPIO.output(23, False)
    sleep(.5)

    GPIO.output(25, True)
    sleep(.5)
    GPIO.output(25, False)
    sleep(1)