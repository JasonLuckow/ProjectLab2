import threading
import time
import RPi.GPIO as GPIO
from NickCode.music import music
import math

class NewHousetopSong():
  def __init__(self, win, app):
    self.win = win  
    self.app = app
    self.music = music(win, app, "Up on the Housetop")
    self.music.setTempo(self.win.getTempoValue()) 
    self.bF = 14
    self.b = 24
    self.c = 16
    self.d = 25
    self.dS = 4
    self.e = 7
    self.f = 19
    self.fS = 17
    self.g = 8
    self.A = 12
    self.BF = 22
    self.B = 20
    self.C = 18
    self.D = 15
    self.DS = 13
    self.E = 1
    self.F = 6
    self.G = 21

  def melody(self):
    self.music.setTempo(self.win.getTempoValue())
    #m1
    self.music.qNote(self.g)
    self.music.eNote(self.g)
    self.music.eNote(self.A)
    self.music.qNote(self.g)
    self.music.qNote(self.e)

    #m2s
    self.music.qNote(self.c)
    self.music.qNote(self.e)
    self.music.hNote(self.g)

    #m3
    self.music.qNote(self.A)
    self.music.qNote(self.A)
    self.music.qNote(self.g)
    self.music.qNote(self.e)

    #m4
    self.music.qNote(self.d)
    self.music.qNote(self.g)
    self.music.hNote(self.g)
    time.sleep(.1)

    #m5
    self.music.qNote(self.g)
    self.music.eNote(self.g)
    self.music.eNote(self.A)
    self.music.qNote(self.g)
    self.music.eNote(self.e)
    self.music.eNote(self.d)

    #m6
    self.music.qNote(self.c)
    self.music.qNote(self.e)
    self.music.hNote(self.g)

    #m7
    self.music.qNote(self.A)
    self.music.eNote(self.A)
    self.music.eNote(self.A)
    self.music.eNote(self.g)
    self.music.eNote(self.g)
    self.music.qNote(self.e)

    #m8
    self.music.qNote(self.d)
    self.music.qNote(self.g)
    self.music.hNote(self.c)
    time.sleep(.1)

    #m9
    self.music.qNote(self.f)
    self.music.qNote(self.f)
    self.music.hNote(self.A)

    #m10
    self.music.qNote(self.g)
    self.music.eNote(self.g)
    self.music.eNote(self.g)
    self.music.hNote(self.e)

    #m11
    self.music.qNote(self.d)
    self.music.qNote(self.d)
    self.music.hNote(self.f)

    #m12
    self.music.qNote(self.e)
    self.music.eNote(self.g)
    self.music.eNote(self.g)
    self.music.qNote(self.c)
    self.music.qNote(self.e)

    #m13
    self.music.qNote(self.g)
    self.music.eNote(self.g)
    self.music.eNote(self.A)
    self.music.qNote(self.g)
    self.music.qNote(self.e)

    #m14
    self.music.qNote(self.f)
    self.music.qNote(self.g)
    self.music.qNote(self.A)
    self.music.qNoteRest()

    #m15
    self.music.qNote(self.g)
    self.music.eNote(self.g)
    self.music.eNote(self.A)
    self.music.qNote(self.g)
    self.music.eNote(self.e)
    self.music.eNote(self.e)

    #m16
    self.music.qNote(self.d)
    self.music.qNote(self.g)
    self.music.hNote(self.c)
    

  def bass(self):
    #m1
    self.music.hNote(self.c)
    time.sleep(.2)
    self.music.hNote(self.g)
    time.sleep(.1)

    #m2
    self.music.hNote(self.c)
    time.sleep(.1)
    self.music.hNote(self.e)

    #m3
    self.music.hNote(self.f)
    time.sleep(.1)
    self.music.hNote(self.e)
    time.sleep(.1)

    #m4
    self.music.qNote(self.b)
    self.music.qNote(self.A)
    self.music.qNote(self.g)
    self.music.qNote(self.b)

    #m5
    self.music.hNote(self.c)
    time.sleep(.2)
    self.music.hNote(self.g)
    time.sleep(.2)

    #m6
    self.music.hNote(self.c)
    time.sleep(.1)
    self.music.hNote(self.e)

    #m7
    self.music.hNote(self.f)
    time.sleep(.2)
    self.music.hNote(self.e)
    time.sleep(.2)

    #m8
    self.music.hNote(self.f)
    time.sleep(.1)
    self.music.qNote(self.e)
    self.music.qNote(self.c)

    #m9
    self.music.wNote(self.f)
    time.sleep(.2)

    #m10
    self.music.wNote(self.e)
    time.sleep(.3)

    #m11
    self.music.wNote(self.d)
    time.sleep(.2)

    #m12
    self.music.wNote(self.c)
    time.sleep(.4)

    #m13
    self.music.hNote(self.c)
    time.sleep(.2)
    self.music.hNote(self.bF)
    time.sleep(.1)

    #m14
    self.music.qNote(self.A)
    self.music.qNote(self.g)
    self.music.qNote(self.f)
    self.music.qNoteRest()
    
    #m15
    self.music.hNote(self.c)
    time.sleep(.2)
    self.music.hNote(self.g)
    time.sleep(.2)

    #m16
    self.music.hNote(self.b)
    time.sleep(.1)
    self.music.hNote(self.c)

  def startsong(self, progress_callback):
    # Setting up threads and starting them
    self.win.updatelabel2("Up on the Housetop is Playing!")

    #Set maximum progress bar value
    self.win.setProgressBarMax(math.floor(1013.87-142.96*math.log(self.win.getTempoValue())))

    timing = 0
    high = threading.Thread(target=self.melody)
    high.start()
    low = threading.Thread(target=self.bass)
    low.start()

    while(True):
      if(high.isAlive() or low.isAlive()):
        while self.win.getPaused() == True:
          time.sleep(0.1)
        progress_callback.emit(timing)
        timing = timing + 1
        time.sleep(0.1)
      else:
        return

    high.join()
    low.join()