import threading
import time
import RPi.GPIO as GPIO
import self.music
import math

class NewHousetopSong():
  def __init__(self, win, app):
    self.win = win  
    self.app = app
    self.music = music(self.win, app, "Jingle Bells ")
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

  def melody():
    self.music.setTempo(self.win.getTempoValue())
    #m1
    self.music.qNote(g)
    self.music.eNote(g)
    self.music.eNote(A)
    self.music.qNote(g)
    self.music.qNote(e)

    #m2s
    self.music.qNote(c)
    self.music.qNote(e)
    self.music.hNote(g)

    #m3
    self.music.qNote(A)
    self.music.qNote(A)
    self.music.qNote(g)
    self.music.qNote(e)

    #m4
    self.music.qNote(d)
    self.music.qNote(g)
    self.music.hNote(g)
    time.sleep(.1)

    #m5
    self.music.qNote(g)
    self.music.eNote(g)
    self.music.eNote(A)
    self.music.qNote(g)
    self.music.eNote(e)
    self.music.eNote(d)

    #m6
    self.music.qNote(c)
    self.music.qNote(e)
    self.music.hNote(g)

    #m7
    self.music.qNote(A)
    self.music.eNote(A)
    self.music.eNote(A)
    self.music.eNote(g)
    self.music.eNote(g)
    self.music.qNote(e)

    #m8
    self.music.qNote(d)
    self.music.qNote(g)
    self.music.hNote(c)
    time.sleep(.1)

    #m9
    self.music.qNote(f)
    self.music.qNote(f)
    self.music.hNote(A)

    #m10
    self.music.qNote(g)
    self.music.eNote(g)
    self.music.eNote(g)
    self.music.hNote(e)

    #m11
    self.music.qNote(d)
    self.music.qNote(d)
    self.music.hNote(f)

    #m12
    self.music.qNote(e)
    self.music.eNote(g)
    self.music.eNote(g)
    self.music.qNote(c)
    self.music.qNote(e)

    #m13
    self.music.qNote(g)
    self.music.eNote(g)
    self.music.eNote(A)
    self.music.qNote(g)
    self.music.qNote(e)

    #m14
    self.music.qNote(f)
    self.music.qNote(g)
    self.music.qNote(A)
    self.music.qNoteRest()

    #m15
    self.music.qNote(g)
    self.music.eNote(g)
    self.music.eNote(A)
    self.music.qNote(g)
    self.music.eNote(e)
    self.music.eNote(e)

    #m16
    self.music.qNote(d)
    self.music.qNote(g)
    self.music.hNote(c)
    

  def bass():
    #m1
    self.music.hNote(c)
    time.sleep(.2)
    self.music.hNote(g)
    time.sleep(.1)

    #m2
    self.music.hNote(c)
    time.sleep(.1)
    self.music.hNote(e)

    #m3
    self.music.hNote(f)
    time.sleep(.1)
    self.music.hNote(e)
    time.sleep(.1)

    #m4
    self.music.qNote(b)
    self.music.qNote(A)
    self.music.qNote(g)
    self.music.qNote(b)

    #m5
    self.music.hNote(c)
    time.sleep(.2)
    self.music.hNote(g)
    time.sleep(.2)

    #m6
    self.music.hNote(c)
    time.sleep(.1)
    self.music.hNote(e)

    #m7
    self.music.hNote(f)
    time.sleep(.2)
    self.music.hNote(e)
    time.sleep(.2)

    #m8
    self.music.hNote(f)
    time.sleep(.1)
    self.music.qNote(e)
    self.music.qNote(c)

    #m9
    self.music.wNote(f)
    time.sleep(.2)

    #m10
    self.music.wNote(e)
    time.sleep(.3)

    #m11
    self.music.wNote(d)
    time.sleep(.2)

    #m12
    self.music.wNote(c)
    time.sleep(.4)

    #m13
    self.music.hNote(c)
    time.sleep(.2)
    self.music.hNote(bF)
    time.sleep(.1)

    #m14
    self.music.qNote(A)
    self.music.qNote(g)
    self.music.qNote(f)
    self.music.qNoteRest()
    
    #m15
    self.music.hNote(c)
    time.sleep(.2)
    self.music.hNote(g)
    time.sleep(.2)

    #m16
    self.music.hNote(b)
    time.sleep(.1)
    self.music.hNote(c)

 def startsong(self, progress_callback):
    # Setting up threads and starting them
    self.win.updatelabel2("Up on the Housetop is Playing!")

    #Set maximum progress bar value
    self.win.setProgressBarMax(math.floor(1995.084-283.78*math.log(self.win.getTempoValue())))

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