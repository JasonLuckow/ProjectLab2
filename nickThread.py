import threading
import time
import RPi.GPIO as GPIO
"jason testing"

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

def turnOn(pin, duration):
  GPIO.output(pin, True)
  time.sleep(duration)

def turnOff(pin, duration):
  GPIO.output(pin, False)
  time.sleep(duration)

def eigthNote(pin, duration):
  GPIO.output(pin, True)
  time.sleep(duration/2)
  GPIO.output(pin, False)
  time.sleep(duration/2)
  #GPIO.output(pin, True)
  #time.sleep(.25)
  #GPIO.output(pin, False)
  #time.sleep(.25)

def twoOn(p, p2, duration):
  threadOne = threading.Thread(target = turnOn, args = (p,duration))
  threadOne.start()
  threadTwo = threading.Thread(target = turnOn, args = (p2,duration))
  threadTwo.start()

def twoOff(p, p2, duration):
  threadOne = threading.Thread(target = turnOff, args = (p,duration))
  threadOne.start()
  threadTwo = threading.Thread(target = turnOff, args = (p2,duration))
  threadTwo.start()

GPIO.output(22, True)
time.sleep(1)

GPIO.output(24, True)
time.sleep(1)

GPIO.output(25, True)
time.sleep(1)

GPIO.output(22, False)
time.sleep(.5)

GPIO.output(24, False)
time.sleep(.5)

GPIO.output(25, False)
time.sleep(.5)

time.sleep(1)

threadOne = threading.Thread(target = turnOn, args = (22, 1))
threadOne.start()

threadTwo = threading.Thread(target = turnOff, args = (24, 1))
threadTwo.start()

threadThree = threading.Thread(target = turnOff, args = (25, 1))
threadThree.start()

threadOne.join()
threadTwo.join()
threadThree.join()
time.sleep(1)

threadOne = threading.Thread(target = turnOn, args = (22, 1))
threadOne.start()

threadTwo = threading.Thread(target = turnOn, args = (24, 1))
threadTwo.start()

threadThree = threading.Thread(target = turnOff, args = (25, 1))
threadThree.start()

threadOne.join()
threadTwo.join()
threadThree.join()
time.sleep(1)

threadOne = threading.Thread(target = turnOn, args = (22, 1))
threadOne.start()

threadTwo = threading.Thread(target = turnOn, args = (24, 1))
threadTwo.start()

threadThree = threading.Thread(target = turnOn, args = (25, 1))
threadThree.start()

threadOne.join()
threadTwo.join()
threadThree.join()
time.sleep(1)

threadOne = threading.Thread(target = eigthNote, args = (22, .5))
threadOne.start()

threadTwo = threading.Thread(target = turnOn, args = (24, .5))
threadTwo.start()

threadOne.join()
threadTwo.join()

GPIO.output(22, False)
time.sleep(.5)

GPIO.output(24, False)
time.sleep(.5)

GPIO.output(25, False)
time.sleep(.5)

time.sleep(2)

threadOne = threading.Thread(target = twoOn, args = (22, 24, 1))
threadOne.start()

threadTwo = threading.Thread(target = eigthNote, args = (25, 1))
threadTwo.start()

threadOne.join()
threadTwo.join()
time.sleep(1)

GPIO.output(22, False)
time.sleep(.5)

GPIO.output(24, False)
time.sleep(.5)

GPIO.output(25, False)
time.sleep(.5)
