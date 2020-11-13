import threading
import time
import RPi.GPIO as GPIO
from NickCode.music import music
import math

class NewCarolSong():
  def __init__(self, win, app):
    self.win = win
    self.app = app
    self.music = music(win, app, "Carol of the Bells ")
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
    #In case tempo changes between initialization and playing
    self.music.setTempo(self.win.getTempoValue())
    
    #m1
    self.music.qNote(self.BF)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    self.music.qNote(self.g)

    #m2
    self.music.qNote(self.BF)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    self.music.qNote(self.g)

    #m3
    self.music.qNote(self.BF)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    self.music.qNote(self.g)

    #m4
    self.music.qNote(self.BF)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    self.music.qNote(self.g)


    #m5
    self.music.qNote(self.BF)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    self.music.qNote(self.g)

    #m6
    self.music.qNote(self.BF)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    self.music.qNote(self.g)

    #m7
    self.music.qNote(self.BF)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    self.music.qNote(self.g)

    #m8
    self.music.qNote(self.BF)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    self.music.qNote(self.g)

    #m9
    self.music.qNote(self.BF)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    self.music.qNote(self.g)

    #m10
    self.music.qNote(self.BF)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    self.music.qNote(self.g)

    #m11
    self.music.qNote(self.BF)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    self.music.qNote(self.g)

    #m12
    self.music.qNote(self.BF)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    self.music.qNote(self.g)

    #m13
    self.music.qNote(self.D)
    self.music.eNote(self.C)
    self.music.eNote(self.D)
    self.music.qNote(self.BF)

    #m14
    self.music.qNote(self.D)
    self.music.eNote(self.C)
    self.music.eNote(self.D)
    self.music.qNote(self.BF)

    #m15
    self.music.qNote(self.D)
    self.music.eNote(self.C)
    self.music.eNote(self.D)
    self.music.qNote(self.BF)

    #m16
    self.music.qNote(self.D)
    self.music.eNote(self.C)
    self.music.eNote(self.D)
    self.music.qNote(self.BF)

    #m17
    self.music.qNote(self.G)
    self.music.eNote(self.G)
    self.music.eNote(self.G)
    self.music.eNote(self.F)
    self.music.eNote(self.E)
    
    #m18
    self.music.qNote(self.D)
    self.music.eNote(self.D)
    self.music.eNote(self.D)
    self.music.eNote(self.C)
    self.music.eNote(self.BF)

    #m19
    self.music.qNote(self.C)
    self.music.eNote(self.C)
    self.music.eNote(self.C)
    self.music.eNote(self.D)
    self.music.eNote(self.C)

    #m20
    self.music.qNote(self.BF)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    self.music.qNote(self.g)
    
    #m21
    self.music.eNote(self.d)
    self.music.eNote(self.e)
    self.music.eNote(self.fS)
    self.music.eNote(self.g)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    
    #m22
    self.music.eNote(self.C)
    self.music.eNote(self.D)
    self.music.qNote(self.C)
    self.music.qNote(self.BF)

    #m23
    self.music.eNote(self.d)
    self.music.eNote(self.e)
    self.music.eNote(self.fS)
    self.music.eNote(self.g)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    
    #m24
    self.music.eNote(self.C)
    self.music.eNote(self.D)
    self.music.qNote(self.C)
    self.music.qNote(self.BF)

    #m25
    self.music.qNote(self.BF)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    self.music.qNote(self.g)

    #m26
    self.music.qNote(self.BF)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    self.music.qNote(self.g)

    #m27
    self.music.qNote(self.BF)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    self.music.qNote(self.g)

    #m28
    self.music.qNote(self.BF)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    self.music.qNote(self.g)

    #m29
    self.music.qNote(self.BF)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    self.music.qNote(self.g)

    #m30
    self.music.qNote(self.BF)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    self.music.qNote(self.g)

    #m31
    self.music.qNote(self.BF)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    self.music.qNote(self.g)

    #m32
    self.music.qNote(self.BF)
    self.music.eNote(self.A)
    self.music.eNote(self.BF)
    self.music.qNote(self.g)

    #m33
    self.music.dHalfNote(self.g)
    

  def bass(self):
    #m1
    self.music.dHalfNote(self.g)
    time.sleep(.3)

    #m2
    self.music.dHalfNote(self.f)
    time.sleep(.3)

    #m3
    self.music.dHalfNote(self.dS)
    time.sleep(.3)

    #m4
    self.music.dHalfNote(self.d)
    time.sleep(.3)

    #m5
    self.music.dHalfNote(self.g)
    time.sleep(.3)

    #m6
    self.music.dHalfNote(self.f)
    time.sleep(.3)

    #m7
    self.music.dHalfNote(self.dS)
    time.sleep(.3)
    
    #m8
    self.music.dHalfNote(self.d)
    time.sleep(.3)

    #m9
    self.music.dHalfNote(self.c)
    time.sleep(.3)

    #m10
    self.music.dHalfNote(self.d)
    time.sleep(.3)

    #m11
    self.music.dHalfNote(self.c)
    time.sleep(.3)

    #m12
    self.music.dHalfNote(self.d)
    time.sleep(.3)
    
    #m13
    self.music.dHalfNote(self.d)
    time.sleep(.3)

    #m14
    self.music.dHalfNote(self.e)
    time.sleep(.3)

    #m15
    self.music.dHalfNote(self.f)
    time.sleep(.3)

    #m16
    self.music.qNote(self.e)
    self.music.qNote(self.dS)
    time.sleep(.1)
    self.music.qNote(self.d)

    #m17
    self.music.dHalfNote(self.d)
    time.sleep(.4)

    #m18
    self.music.dHalfNote(self.bF)
    time.sleep(.4)

    #m19
    self.music.dHalfNote(self.bF)
    time.sleep(.4)

    #m20
    self.music.dHalfNote(self.bF)
    time.sleep(.3)
    
    #m21
    self.music.dHalfNote(self.fS)
    time.sleep(.5)

    #m22
    self.music.hNote(self.A)
    time.sleep(.2)
    self.music.qNote(self.g)

    #m23
    self.music.dHalfNote(self.fS)
    time.sleep(.5)

    #m24
    self.music.hNote(self.A)
    time.sleep(.2)
    self.music.qNote(self.g)

    #m25
    self.music.dHalfNote(self.g)
    time.sleep(.3)

    #m26
    self.music.dHalfNote(self.g)
    time.sleep(.3)

    #m27
    self.music.dHalfNote(self.g)
    time.sleep(.3)

    #m28
    self.music.dHalfNote(self.g)
    time.sleep(.3)

    #m29
    self.music.dHalfNote(self.g)
    time.sleep(.3)

    #m30
    self.music.dHalfNote(self.g)
    time.sleep(.3)

    #m31
    self.music.dHalfNote(self.g)
    time.sleep(.3)

    #m32
    self.music.dHalfNote(self.g)
    time.sleep(.3)

    #m33
    self.music.dHalfNote(self.g)

  def startsong(self, progress_callback):
    # Setting up threads and starting them
    self.win.updatelabel2("Carol of the Bells is Playing!")

    #Set progress Bar Max
    #self.win.setProgressBarMax( Time of Song in seconds * (normal song tempo / self.win.getTempoValue))
    self.win.setProgressBarMax(math.floor(1599.09-221.03*math.log(self.win.getTempoValue())))

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