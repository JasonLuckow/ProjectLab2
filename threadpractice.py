import threading
import os
import math
import time
from datetime import datetime
import RPi.GPIO as GPIO

"""
This is for the mini project. I need to clean it up.
"""

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

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

count = 0
while count < 1:

    x = threading.Thread(target=motorswitch, args=(True, 23, 2,))
    x.start()

    y = threading.Thread(target=motorswitch, args=(True, 24, 2,))
    y.start()

    z = threading.Thread(target=motorswitch, args=(False, 25, 2,))
    z.start()

    x.join()
    y.join()
    z.join()

    all(False)

    x = threading.Thread(target=motorswitch, args=(False, 23, 2,))
    x.start()

    y = threading.Thread(target=motorswitch, args=(True, 24, 2,))
    y.start()

    z = threading.Thread(target=motorswitch, args=(True, 25, 2,))
    z.start()

    x.join()
    y.join()
    z.join()

    all(False)

    x = threading.Thread(target=motorswitch, args=(True, 23, 2,))
    x.start()

    y = threading.Thread(target=motorswitch, args=(False, 24, 2,))
    y.start()

    z = threading.Thread(target=motorswitch, args=(True, 25, 2,))
    z.start()

    x.join()
    y.join()
    z.join()

    all(False)

    count += 1

i = 1
while i < 2:
    all(False)

    motorswitch(True, 23, 1)
    #motorswitch(False, 23, 1)

    #all(False)
    

    x = threading.Thread(target=motorswitch, args=(True, 23, 1,))
    x.start()

    y = threading.Thread(target=motorswitch, args=(True, 24, 1,))
    y.start()

    z = threading.Thread(target=motorswitch, args=(False, 25, 1,))
    z.start()

    x.join()
    y.join()
    z.join()

    #all(False)

    x = threading.Thread(target=motorswitch, args=(True, 23, 1,))
    x.start()

    y = threading.Thread(target=motorswitch, args=(True, 24, 1,))
    y.start()

    z = threading.Thread(target=motorswitch, args=(True, 25, 1,))
    z.start()

    x.join()
    y.join()
    z.join()

    #all(False)

    x = threading.Thread(target=motorswitch, args=(False, 23, 1,))
    x.start()

    y = threading.Thread(target=motorswitch, args=(True, 24, 1,))
    y.start()

    z = threading.Thread(target=motorswitch, args=(True, 25, 1,))
    z.start()

    x.join()
    y.join()
    z.join()

    #all(False)

    x = threading.Thread(target=motorswitch, args=(False, 23, 1,))
    x.start()

    y = threading.Thread(target=motorswitch, args=(False, 24, 1,))
    y.start()

    z = threading.Thread(target=motorswitch, args=(True, 25, 1,))
    z.start()

    x.join()
    y.join()
    z.join()

    all(False)

    i += 1

prev = 1
for i in arr:   
    if i[0] != prev:
        print("\n\n")
    print(i)    
    prev = i[0]

    