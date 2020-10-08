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
qNote, qRest = BPM
hNote, hRest = BPM*2
wNote, wRest = BPM*4
eNote, eRest = BPM/2
sNote, sRest= BPM/4

def updateTempo(x):
  tempo = x # Where x is the value pulled from the GUI
  BPM = 60/tempo
  qNote, qRest = BPM
  hNote, hRest = BPM*2
  wNote, wRest = BPM*4
  eNote, eRest = BPM/2
  sNote, sRest= BPM/4

def qNote(note,noteShh):
  GPIO.output(note, True)
  GPIO.output(note, False)
  time.sleep(qRest)
  GPIO.output(noteShh, True)
  time.sleep(.25) # This line to make sure muffler actuator completely silences ringing
  GPIO.output(noteShh, False)

def hNote(note, noteShh):
  GPIO.output(note, True)
  GPIO.output(note, False)
  time.sleep(hRest)
  GPIO.output(noteShh, True)
  time.sleep(.25) # This line to make sure muffler actuator completely silences ringing
  GPIO.output(noteShh, False)

def wNote(note, noteShh):
  GPIO.output(note, True)
  GPIO.output(note, False)
  time.sleep(wRest)
  GPIO.output(noteShh, True)
  time.sleep(.25) # This line to make sure muffler actuator completely silences ringing
  GPIO.output(noteShh, False)

def eNote(note, noteShh):
  GPIO.output(note, True)
  GPIO.output(note, False)
  time.sleep(eRest)
  GPIO.output(noteShh, True)
  time.sleep(.25) # This line to make sure muffler actuator completely silences ringing
  GPIO.output(noteShh, False)

def sNote(note, noteShh):
  GPIO.output(note, True)
  GPIO.output(note, False)
  time.sleep(sRest)
  GPIO.output(noteShh, True)
  time.sleep(.25) # This line to make sure muffler actuator completely silences ringing
  GPIO.output(noteShh, False)

def qNoteRest():
  time.sleep(qNoteRest)

def hNoteRest():
  time.sleep(hNoteRest)

def wNoteRest():
  time.sleep(wNoteRest)

def eNoteRest():
  time.sleep(eNoteRest)

def sNoteRest():
  time.sleep(sNoteRest)

### END OF MUSIC CLASS 