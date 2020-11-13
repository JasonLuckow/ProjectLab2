import threading
import time
import RPi.GPIO as GPIO


class music():
  def __init__(self, win, app, song):
    self.win = win
    self.app = app
    self.song = song
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

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22, GPIO.OUT)

    # Have these values modified by GUI 
    #Min is 120, Max is 420
    self.tempo = 290
    self.BPM = 60/self.tempo
    self.qNoteL = self.BPM
    self.hNoteL = self.BPM * 2
    self.wNoteL = self.BPM * 4
    self.eNoteL = self.BPM / 2
    self.sNoteL = self.BPM / 4

    self.s = .1 # Sleep variable for in between motor on/off

  def setTempo(self, tempo):
    self.tempo = tempo
    self.win.updateTempo(self.tempo)
    self.BPM = 60/self.tempo
    self.qNoteL = self.BPM
    self.hNoteL = self.BPM * 2
    self.wNoteL = self.BPM * 4
    self.eNoteL = self.BPM / 2
    self.sNoteL = self.BPM / 4

  def qNote(self, note):
    if(self.win.getStopped() == True):
        # self.win.updatelabel2("Carol button was clicked.\nClick another!")
        return
    GPIO.output(note, True)
    time.sleep(self.s)
    GPIO.output(note, False)
    i = 0
    for i in range(2):
      while self.win.getPaused() == True:
        self.all(False)
        self.win.updatelabel2(self.song + "is Paused!\nChoose A new Song or Play to Resume!")
        time.sleep(.1)
      time.sleep(self.eNoteL)
      # i = i+1

  def dQuarterNote(self, note):
    if(self.win.getStopped() == True):
        # self.win.updatelabel2("Carol button was clicked.\nClick another!")
        return
    GPIO.output(note, True)
    time.sleep(self.s)
    GPIO.output(note, False)
    i = 0
    for i in range(3):
      while self.win.getPaused() == True:
        self.all(False)
        self.win.updatelabel2(self.song + "is Paused!\nChoose A new Song or Play to Resume!")
        time.sleep(.1)
      time.sleep(self.eNoteL)
      # i = i+1

  def hNote(self, note):
    if(self.win.getStopped() == True):
        # self.win.updatelabel2("Carol button was clicked.\nClick another!")
        return
    GPIO.output(note, True)
    time.sleep(self.s)
    GPIO.output(note, False)
    i = 0
    for i in range(4):
      while self.win.getPaused() == True:
        self.all(False)
        self.win.updatelabel2(self.song + "is Paused!\nChoose A new Song or Play to Resume!")
        time.sleep(.1)
      time.sleep(self.eNoteL)
      # i = i+1

  def dHalfNote(self, note):
    if(self.win.getStopped() == True):
        # self.win.updatelabel2("Carol button was clicked.\nClick another!")
        return
    GPIO.output(note, True)
    time.sleep(self.s)
    GPIO.output(note, False)
    i = 0
    for i in range(6):
      while self.win.getPaused() == True:
        self.all(False)
        self.win.updatelabel2(self.song + "is Paused!\nChoose A new Song or Play to Resume!")
        time.sleep(.1)
      time.sleep(self.eNoteL)
      # i = i+1

  def wNote(self, note):
    if(self.win.getStopped() == True):
        # self.win.updatelabel2("Carol button was clicked.\nClick another!")
        return
    GPIO.output(note, True)
    time.sleep(self.s)
    GPIO.output(note, False)
    i = 0
    for i in range(8):
      while self.win.getPaused() == True:
        self.all(False)
        self.win.updatelabel2(self.song + "is Paused!\nChoose A new Song or Play to Resume!")
        time.sleep(.1)
      time.sleep(self.eNoteL)
      # i = i+1

  def eNote(self, note):
    if(self.win.getStopped() == True):
        # self.win.updatelabel2("Carol button was clicked.\nClick another!")
        return
    GPIO.output(note, True)
    time.sleep(self.s)
    GPIO.output(note, False)
    while self.win.getPaused() == True:
        self.all(False)
        self.win.updatelabel2(self.song + "is Paused!\nChoose A new Song or Play to Resume!")
        time.sleep(.1)
    time.sleep(self.eNoteL)


  def sNote(self, note):
    if(self.win.getStopped() == True):
        # self.win.updatelabel2("Carol button was clicked.\nClick another!")
        return
    GPIO.output(note, True)
    time.sleep(self.s)
    GPIO.output(note, False)
    while self.win.getPaused() == True:
        self.all(False)
        self.win.updatelabel2(self.song + "is Paused!\nChoose A new Song or Play to Resume!")
        time.sleep(.1)
    time.sleep(self.sNoteL)

  def qNoteRest(self):
    i = 0
    for i in range(2):
      while self.win.getPaused() == True:
        self.all(False)
        self.win.updatelabel2(self.song + "is Paused!\nChoose A new Song or Play to Resume!")
        time.sleep(.1)
      time.sleep(self.eNoteL)

  def hNoteRest(self):
    i = 0
    for i in range(4):
      while self.win.getPaused() == True:
        self.all(False)
        self.win.updatelabel2(self.song + "is Paused!\nChoose A new Song or Play to Resume!")
        time.sleep(.1)
      time.sleep(self.eNoteL)

  def wNoteRest(self):
    i = 0
    for i in range(8):
      while self.win.getPaused() == True:
        self.all(False)
        self.win.updatelabel2(self.song + "is Paused!\nChoose A new Song or Play to Resume!")
        time.sleep(.1)
      time.sleep(self.eNoteL)

  def eNoteRest(self):
    time.sleep(self.eNoteL)

  def sNoteRest(self):
    time.sleep(self.sNoteL)


  def all(self, switch):
    
    GPIO.output(0, switch)
    
    GPIO.output(1, switch)
    
    GPIO.output(5, switch)
    
    GPIO.output(6, switch)
    
    GPIO.output(7, switch)
    
    GPIO.output(8, switch)
    
    GPIO.output(9, switch)
    
    GPIO.output(11, switch)
    
    GPIO.output(12, switch)
    
    GPIO.output(13, switch)
    
    GPIO.output(14, switch)
    
    GPIO.output(15, switch)
    
    GPIO.output(16, switch)
    
    GPIO.output(18, switch)
    
    GPIO.output(19, switch)
    
    GPIO.output(20, switch)
    
    GPIO.output(21, switch)
    
    GPIO.output(24, switch)
    
    GPIO.output(25, switch)
    
    GPIO.setup(26, switch)
    ### END OF MUSIC CLASS 