import threading
import os
import math
import time
from datetime import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

#x - 23
#y - 24
#z - 25

for i in range(10):

    GPIO.output(23, True)
    time.sleep(.2)
    GPIO.output(23, False)
    time.sleep(.4)

    GPIO.output(24, True)
    time.sleep(.2)
    GPIO.output(24, False)
    time.sleep(.2)

    GPIO.output(23, True)
    time.sleep(.2)
    GPIO.output(23, False)
    time.sleep(.2)

    GPIO.output(25, True)
    time.sleep(.2)
    GPIO.output(25, False)
    time.sleep(.4)