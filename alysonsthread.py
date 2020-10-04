#Connects to Raspberry Pi
import threading
import os
import math
import time
from datetime import datetime
import RPi.GPIO as GPIO

#Sets up the pins on the Raspberry Pi as output pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

#Sets up the motors switching
def motorswitch(bo, pin, t):
    GPIO.output(pin, bo)
    time.sleep(t)
arr = []

#Gets the current time
def timenow():
    return (datetime.now().strftime("%H:%M:%S"))

#Creates the order that the information must be placed in order for the movements to work. (bo = direction of movement for actuator, 
# pin = the output pin is this command controlling, t = speed that the actuator moves, n = how many times this movement will be preformed)
def calc(bo, pin, t, n):
    for i in range(n):
        bo = not bo
        GPIO.output(pin, bo)
        time.sleep(t)

#Made for the display in the command line
def stepsame(count, type, bo, t):
    print("working {}".format(count))
    arr.append([count, type, bo, timenow()])
    time.sleep(t)

#Sets up the threading required to move multiple actuators at once
def all(bo):
    first_solenoid = threading.Thread(target=motorswitch, args=(bo, 22, .5,))
    first_solenoid.start()

    second_solenoid = threading.Thread(target=motorswitch, args=(bo, 24, .5,))
    second_solenoid.start()

    third_solenoid = threading.Thread(target=motorswitch, args=(bo, 25, .5,))
    third_solenoid.start()

    first_solenoid.join()
    second_solenoid.join()
    third_solenoid.join()
    
count = 0
#This while loops controls the movement of the actuators
while count < 1:
    #First movement: all three actuators move in and out 5 times
    first_solenoid = threading.Thread(target=calc, args=(True, 22, 0.5, 5))
    first_solenoid.start()
    second_solenoid = threading.Thread(target=calc, args=(True, 24, 0.5, 5))
    second_solenoid.start()
    third_solenoid = threading.Thread(target=calc, args=(True, 25, 0.5, 5))
    third_solenoid.start()
    first_solenoid.join()
    second_solenoid.join()
    third_solenoid.join()
    all(False)
    #Second movement: the actuators all move at different speeds, but will sometimes move at the same time when the timing matches
    first_solenoid = threading.Thread(target=calc, args=(True, 22, 1, 5))
    first_solenoid.start()
    second_solenoid = threading.Thread(target=calc, args=(True, 24, 0.75, 7))
    second_solenoid.start()
    third_solenoid = threading.Thread(target=calc, args=(True, 25, 0.5, 10))
    third_solenoid.start()
    first_solenoid.join()
    second_solenoid.join()
    third_solenoid.join()
    all(False)
    #Third movement: the third actuator will move in and out while the other two are in a resting position
    first_solenoid = threading.Thread(target=calc, args=(True, 22, 1, 1))
    first_solenoid.start()
    second_solenoid = threading.Thread(target=calc, args=(True, 24, 1, 1))
    second_solenoid.start()
    third_solenoid = threading.Thread(target=calc, args=(False, 25, 1, 1))
    third_solenoid.start()
    first_solenoid.join()
    second_solenoid.join()
    third_solenoid.join()
    all(False)
    #Fourth movement: the second actuator will move in and out while the other two are in a resting position
    first_solenoid = threading.Thread(target=calc, args=(True, 22, 1, 1))
    first_solenoid.start()
    second_solenoid = threading.Thread(target=calc, args=(False, 24, 1, 1))
    second_solenoid.start()
    third_solenoid = threading.Thread(target=calc, args=(True, 25, 1, 1))
    third_solenoid.start()
    first_solenoid.join()
    second_solenoid.join()
    third_solenoid.join()
    all(False)
    #Fifth movement: the first actuator will move in and out while the other two are in a resting position
    first_solenoid = threading.Thread(target=calc, args=(False, 22, 1, 1))
    first_solenoid.start()
    second_solenoid = threading.Thread(target=calc, args=(True, 24, 1, 1))
    second_solenoid.start()
    third_solenoid = threading.Thread(target=calc, args=(True, 25, 1, 1))
    third_solenoid.start()
    first_solenoid.join()
    second_solenoid.join()
    third_solenoid.join()
    all(False)
    #Sixth movement: the actuators all move at different speeds, but will sometimes move at the same time when the timing matches. 
    #Similar to the second movement, but is at a faster speed
    first_solenoid = threading.Thread(target=calc, args=(True, 22, 0.25, 25))
    first_solenoid.start()
    second_solenoid = threading.Thread(target=calc, args=(True, 24, 0.75, 25))
    second_solenoid.start()
    third_solenoid = threading.Thread(target=calc, args=(True, 25, 0.5, 25))
    third_solenoid.start()
    first_solenoid.join()
    second_solenoid.join()
    third_solenoid.join()
    all(False)
    count += 1