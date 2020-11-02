import threading
import time
import RPi.GPIO as GPIO
from NickCode.music import music

class NewJingleSong():
  def __init__(self, win, app):
      self.win = win  
      self.app = app
      self.music = music(self.win, app, "Jingle Bells ")
      self.music.setTempo(self.win.getTempoValue()) 
      self.bF = 14
      self.b = 15
      self.c = 16
      self.d = 25
      self.dS = 5
      self.e = 7
      self.f = 13
      self.fS = 0
      self.g = 8
      self.A = 12
      self.BF = 9
      self.B = 20
      self.C = 18
      self.D = 24
      self.DS = 6
      self.E = 1
      self.F = 26
      self.G = 21

  #music.updateTempo(180)

  def melody(self):
    #In case tempo changes between initialization and playing
    self.music.setTempo(self.win.getTempoValue())
    
    #m1
    self.music.qNote(self.d)
    self.music.qNote(self.B)
    self.music.qNote(self.A)
    self.music.qNote(self.g)

    # #m2
    self.music.dHalfNote(self.d)
    self.music.eNote(self.d)
    self.music.eNote(self.d)

    #m3
    self.music.qNote(self.d)
    self.music.qNote(self.B)
    self.music.qNote(self.A)
    self.music.qNote(self.g)

    #m4
    self.music.dHalfNote(self.e)
    self.music.qNote(self.e)

    #m5
    self.music.qNote(self.e)
    self.music.qNote(self.C)
    self.music.qNote(self.B)
    self.music.qNote(self.A)

    #m6
    self.music.dHalfNote(self.fS)
    self.music.qNote(self.fS)

    #m7
    self.music.qNote(self.D)
    self.music.qNote(self.D)
    self.music.qNote(self.C)
    self.music.qNote(self.A)

    #m8
    self.music.wNote(self.B)
    time.sleep(.1)

    #m9
    self.music.qNote(self.d)
    self.music.qNote(self.B)
    self.music.qNote(self.A)
    self.music.qNote(self.g)

    #m10
    self.music.dHalfNote(self.d)
    self.music.eNote(self.d)
    self.music.eNote(self.d)

    #m11
    self.music.qNote(self.d)
    self.music.qNote(self.B)
    self.music.qNote(self.A)
    self.music.qNote(self.g)

    #m12
    self.music.dHalfNote(self.e)
    self.music.qNote(self.e)

    #m13
    self.music.qNote(self.e)
    self.music.qNote(self.C)
    self.music.qNote(self.B)
    self.music.qNote(self.A)

    #m14
    self.music.qNote(self.D)
    self.music.qNote(self.D)
    self.music.qNote(self.D)
    self.music.qNote(self.D)

    #m15
    self.music.qNote(self.E)
    self.music.qNote(self.D)
    self.music.qNote(self.C)
    self.music.qNote(self.A) 

    #m16
    self.music.wNote(self.g)
    time.sleep(.1)

    #m17
    self.music.qNote(self.B)
    self.music.qNote(self.B)
    self.music.hNote(self.B)
    time.sleep(.1)

    #m18
    self.music.qNote(self.B)
    self.music.qNote(self.B)
    self.music.hNote(self.B)
    time.sleep(.1)

    #m19
    self.music.qNote(self.B)
    self.music.qNote(self.D)
    self.music.dQuarterNote(self.g)
    self.music.eNote(self.A)

    #m20
    self.music.dHalfNote(self.B)
    self.music.qNoteRest()
    time.sleep(.3)

    #m21
    self.music.qNote(self.C)
    self.music.qNote(self.C)
    self.music.dQuarterNote(self.C)
    self.music.eNote(self.C)

    #m22
    self.music.qNote(self.C)
    self.music.qNote(self.B)
    self.music.qNote(self.B)
    self.music.eNote(self.B)
    self.music.eNote(self.B)

    #m23
    self.music.qNote(self.B)
    self.music.qNote(self.A)
    self.music.qNote(self.A)
    self.music.qNote(self.B)

    #m24
    self.music.hNote(self.A)
    time.sleep(.1)
    self.music.hNote(self.D)
    time.sleep(.1)

    #m17 repeat
    self.music.qNote(self.B)
    self.music.qNote(self.B)
    self.music.hNote(self.B)
    time.sleep(.1)

    #m18 repeat
    self.music.qNote(self.B)
    self.music.qNote(self.B)
    self.music.hNote(self.B)
    time.sleep(.1)

    #m19 repeat
    self.music.qNote(self.B)
    self.music.qNote(self.D)
    self.music.dQuarterNote(self.g)
    self.music.eNote(self.A)

    #m20 repeat
    self.music.dHalfNote(self.B)
    self.music.qNoteRest()
    time.sleep(.3)

    #m21 repeat
    self.music.qNote(self.C)
    self.music.qNote(self.C)
    self.music.dQuarterNote(self.C)
    self.music.eNote(self.C)

    #m22 repeat
    self.music.qNote(self.C)
    self.music.qNote(self.B)
    self.music.qNote(self.B)
    self.music.eNote(self.B)
    self.music.eNote(self.B)

    #m23 repeat
    self.music.qNote(self.D)
    self.music.qNote(self.D)
    self.music.qNote(self.C)
    self.music.qNote(self.A)

    #m24 repeat
    self.music.hNote(self.g)
    self.music.qNote(self.G)

  def bass(self):
    #m1
    self.music.hNote(self.g)
    time.sleep(.1)
    self.music.hNote(self.d)
    time.sleep(.1)

    #m2
    self.music.hNote(self.g)
    self.music.hNote(self.d)
    time.sleep(.1)

    #m3
    self.music.hNote(self.g)
    time.sleep(.1)
    self.music.hNote(self.d)
    time.sleep(.1)

    #m4
    self.music.hNote(self.c)
    self.music.hNote(self.g)

    #m5
    self.music.hNote(self.c)
    time.sleep(.1)
    self.music.hNote(self.g)
    time.sleep(.1)

    #m6
    self.music.hNote(self.d)
    self.music.hNote(self.A)

    #m7
    self.music.hNote(self.d)
    time.sleep(.1)
    self.music.hNote(self.d)
    time.sleep(.1)

    #m8
    self.music.hNote(self.g)
    self.music.hNote(self.d)
    
    #m9
    self.music.hNote(self.g)
    time.sleep(.1)
    self.music.hNote(self.d)
    time.sleep(.1)

    #m10
    self.music.hNote(self.g)
    self.music.hNote(self.d)
    time.sleep(.1)

    #m11
    self.music.hNote(self.g)
    time.sleep(.1)
    self.music.hNote(self.d)
    time.sleep(.1)

    #m12
    self.music.hNote(self.c)
    self.music.hNote(self.g)

    #m13
    self.music.hNote(self.c)
    time.sleep(.1)
    self.music.hNote(self.g)
    time.sleep(.1)

    #m14
    self.music.hNote(self.d)
    time.sleep(.1)
    self.music.hNote(self.d)
    time.sleep(.1)

    #m15
    self.music.hNote(self.fS)
    time.sleep(.1)
    self.music.hNote(self.d)
    time.sleep(.1)

    #m16
    self.music.hNote(self.g)
    self.music.hNote(self.d)

    #m17
    self.music.qNote(self.g)
    self.music.qNote(self.g)
    self.music.qNote(self.d)
    self.music.qNote(self.g)

    #m18
    self.music.qNote(self.g)
    self.music.qNote(self.g)
    self.music.qNote(self.d)
    self.music.qNote(self.g)

    #m19
    self.music.qNote(self.g)
    self.music.qNote(self.g)
    self.music.qNote(self.d)
    self.music.qNote(self.g)

    #m20
    self.music.qNote(self.g)
    self.music.qNote(self.G)
    self.music.qNote(self.d)
    self.music.qNote(self.G)

    #m21
    self.music.qNote(self.c)
    self.music.qNote(self.C)
    self.music.qNote(self.g)
    self.music.qNote(self.C)

    #m22
    self.music.qNote(self.g)
    self.music.qNote(self.G)
    self.music.qNote(self.d)
    self.music.qNote(self.G)
    time.sleep(.1)

    #m23
    self.music.qNote(self.g)
    self.music.qNote(self.G)
    self.music.qNote(self.d)
    self.music.qNote(self.G)

    #m24
    self.music.qNote(self.d)
    self.music.qNote(self.c)
    self.music.qNote(self.b)
    self.music.qNote(self.A)

    #m17 repeat
    self.music.qNote(self.g)
    self.music.qNote(self.g)
    self.music.qNote(self.d)
    self.music.qNote(self.g)

    #m18 repeat
    self.music.qNote(self.g)
    self.music.qNote(self.g)
    self.music.qNote(self.d)
    self.music.qNote(self.g)

    #m19 repeat
    self.music.qNote(self.g)
    self.music.qNote(self.g)
    self.music.qNote(self.d)
    self.music.qNote(self.g)

    #m20 repeat
    self.music.qNote(self.g)
    self.music.qNote(self.G)
    self.music.qNote(self.d)
    self.music.qNote(self.G)

    #m21 repeat
    self.music.qNote(self.c)
    self.music.qNote(self.C)
    self.music.qNote(self.g)
    self.music.qNote(self.C)

    #m22 repeat
    self.music.qNote(self.g)
    self.music.qNote(self.G)
    self.music.qNote(self.d)
    self.music.qNote(self.G)
    time.sleep(.1)

    #m23 repeat
    self.music.qNote(self.d)
    self.music.qNote(self.d)
    self.music.qNote(self.e)
    self.music.qNote(self.fS)

    #m24 repeat
    self.music.hNote(self.G)
    self.music.qNote(self.g)

  def startsong(self, progress_callback):
    # Setting up threads and starting them
    self.win.updatelabel2("Jingle Bells is Playing!")

    #Set maximum progress bar value
    #self.win.setProgressBarMax( Time of Song * (normal song tempo / self.win.getTempoValue))
    self.win.setProgressBarMax(36*(240/self.win.getTempoValue))

    timing = 0.0
    high = threading.Thread(target=self.melody)
    high.start()

    low = threading.Thread(target=self.bass)
    low.start()

    while(True):
      if(high.isAlive & low.isAlive):
        while self.win.getPaused() == True:
          time.sleep(0.1)
        progress_callback.emit(timing)
        timing = timing + 0.1
        time.sleep(0.1)
      else:
        return

    high.join()
    low.join()