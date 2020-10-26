import threading
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

# Have these values modified by GUI 
tempo = 120
BPM = 60/tempo
qNote = BPM
hNote = BPM*2
wNote = BPM*4
eNote = BPM/2
sNote= BPM/4

def updateTempo(x):
  tempo = x # Where x is the value pulled from the GUI
  BPM = 60/tempo
  qNote = BPM
  hNote = BPM*2
  wNote = BPM*4
  eNote = BPM/2
  sNote= BPM/4

def qNote(note):
  GPIO.output(note, True)
  GPIO.output(note, False)
  time.sleep(qNote)

def dQuarterNote(note):
  GPIO.output(note, True)
  GPIO.output(note, False)
  time.sleep(qNote+eNoteRest)

def hNote(note):
  GPIO.output(note, True)
  GPIO.output(note, False)
  time.sleep(hNote)

def dHalfNote(note):
  GPIO.output(note, True)
  GPIO.output(note, False)
  time.sleep(qNote+hNote)

def wNote(note):
  GPIO.output(note, True)
  GPIO.output(note, False)
  time.sleep(wNote)

def eNote(note):
  GPIO.output(note, True)
  GPIO.output(note, False)
  time.sleep(eNote)

def sNote(note):
  GPIO.output(note, True)
  GPIO.output(note, False)
  time.sleep(sNote)

def qNoteRest():
  time.sleep(qNote)

def hNoteRest():
  time.sleep(hNote)

def wNoteRest():
  time.sleep(wNote)

def eNoteRest():
  time.sleep(eNote)

def sNoteRest():
  time.sleep(sNote)

### END OF MUSIC CLASS 