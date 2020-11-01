import threading
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(0, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(1, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)


# Have these values modified by GUI 
#Min is 120, Max is 420 Carol
#Min
tempo = 240
BPM = 60/tempo
qNoteL = BPM
hNoteL = BPM * 2
wNoteL = BPM * 4
eNoteL = BPM / 2
sNoteL = BPM / 4

s = .1

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
  time.sleep(s)
  GPIO.output(note, False)
  time.sleep(qNoteL)

def dQuarterNote(note):
  GPIO.output(note, True)
  time.sleep(s)
  GPIO.output(note, False)
  time.sleep(qNoteL+eNoteL)

def hNote(note):
  GPIO.output(note, True)
  time.sleep(s)
  GPIO.output(note, False)
  time.sleep(hNoteL)

def dHalfNote(note):
  GPIO.output(note, True)
  time.sleep(s)
  GPIO.output(note, False)
  time.sleep(qNoteL+hNoteL)

def wNote(note):
  GPIO.output(note, True)
  time.sleep(s)
  GPIO.output(note, False)
  time.sleep(wNoteL)

def eNote(note):
  GPIO.output(note, True)
  time.sleep(s)
  GPIO.output(note, False)
  time.sleep(eNoteL)

def sNote(note):
  GPIO.output(note, True)
  time.sleep(s)
  GPIO.output(note, False)
  time.sleep(sNoteL)

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