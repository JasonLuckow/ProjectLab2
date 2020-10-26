import threading
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

# Have these values modified by GUI 
tempo = 120
BPM = 60/tempo
qNoteL = BPM
hNoteL = BPM*2
wNoteL = BPM*4
eNoteL = BPM/2
sNoteL = BPM/4

def updateTempo(x):
  tempo = x # Where x is the value pulled from the GUI
  BPM = 60/tempo
  qNoteL = BPM
  hNoteL = BPM*2
  wNoteL = BPM*4
  eNoteL = BPM/2
  sNoteL = BPM/4

def qNote(note):
  GPIO.output(note, True)
  time.sleep(qNoteL)
  GPIO.output(note, False)

def dQuarterNote(note):
  GPIO.output(note, True)
  time.sleep(qNoteL+eNoteL)
  GPIO.output(note, False)

def hNote(note):
  GPIO.output(note, True)
  time.sleep(hNoteL)
  GPIO.output(note, False)

def dHalfNote(note):
  GPIO.output(note, True)
  time.sleep(qNoteL+hNoteL)
  GPIO.output(note, False)

def wNote(note):
  GPIO.output(note, True)
  time.sleep(wNoteL)
  GPIO.output(note, False)

def eNote(note):
  GPIO.output(note, True)
  time.sleep(eNoteL)
  GPIO.output(note, False)

def sNote(note):
  GPIO.output(note, True)
  time.sleep(sNoteL)
  GPIO.output(note, False)

def qNoteRest():
  time.sleep(qNoteL)

def hNoteRest():
  time.sleep(hNoteL)

def wNoteRest():
  time.sleep(wNoteL)

def eNoteRest():
  time.sleep(eNoteL)

def sNoteRest():
  time.sleep(sNoteL)

### END OF MUSIC CLASS 