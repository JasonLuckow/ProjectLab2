import threading
import time
import RPi.GPIO as GPIO
import music

b = 1
a = 2
g = 3
D = 4
C = 5
e = 7 
G = 8
E = 10
fS = 11
d = 13
c = 14

music.tempo = music.updateTempo(120)

def melody():
  #m1
  music.wNoteRest()

  #m2s
  music.wNoteRest()

  #m3
  music.dHalfNote(c)
  music.qNote(d)

  #m4
  music.hNote(e)
  music.qNote(e)
  music.qNote(e)

  #m5
  music.eNote(f)
  music.eNote(e)
  music.qNote(f)
  music.hNote(e)

  #m6
  music.hNote(e)
  music.hNoteRest(e)

  #m7
  music.qNoteRest()
  music.qNote(c)
  music.qNote(c)
  music.qNote(d)

  #m8
  music.qNote(e)
  music.qNote(e)
  music.qNote(e)
  music.qNote(e)

  #m9
  music.eNote(f)
  music.eNote(e)
  music.qNote(f)
  music.hNote(e)

  #m10
  music.hNote(e)
  music.hNoteRest(e)

  #m11
  music.qNoteRest()
  music.qNote(d)
  music.qNote(e)
  music.qNote(f)

  #m12
  music.qNote(g)
  music.qNote(g)
  music.qNote(g)
  music.qNote(a)

  #m13
  music.eNote(g)
  music.eNote(f)
  music.qNote(e)
  music.hNote(d)

  #m14
  music.hNote(d)
  music.hNoteRest()

  #m15
  music.qNoteRest()
  music.qNote(d)
  music.qNote(e)
  music.qNote(f)

  #m16
  music.qNote(g)
  music.qNote(g)
  music.qNote(g)
  music.qNote(a)

  #m17
  music.eNote(bF)
  music.eNote(a)
  music.qNote(g)
  music.hNote(f)

  #m18
  music.eNote(a)
  music.eNote(g)
  music.qNote(f)
  music.hNote(e)

  #m19
  music.eNote(g)
  music.eNote(f)
  music.qNote(e)
  music.hNote(d)

  #m20
  music.wNote(e)

  #m21
  music.dHalfNote(c)
  music.qNote(d)

  #m22
  music.qNote(e)
  music.qNote(e)
  music.qNote(e)
  music.qNote(e)

  #m23
  music.eNote(f)
  music.eNote(e)
  music.qNote(f)
  music.hNote(e)

  #m24
  music.hNote(e)
  music.hNoteRest()

  #m25
  music.eNote(d)
  music.eNote(c)
  music.qNote(d)
  music.hNote(c)

  #m26
  music.wNote(c)

  #n27
  music.wNoteRest()
  

def bass():
  #m1
  music.hNote(g)
  music.qNote(c)
  music.qNote(g)

  #m2
  music.hNote(g)
  music.qNote(c)
  music.qNote(g)

  #m3
  music.wNote(g)

  #m4
  music.wNote(g)

  #m5
  music.wNote(g)

  #m6
  music.hNote(c)
  music.hNote(g)

  #m7
  music.wNote(g)

  #m8
  music.wNote(g)

  #m9
  music.wNote(g)

  #m10
  music.hNote(c)
  music.hNote(g)

  #m11
  music.wNote(d)

  #m12
  music.wNote(g)

  #m13
  music.hNote(c)
  music.hNote(g)

  #m14
  music.hNote(g)
  music.hNote(g)

  #m15
  music.wNote(g)

  #m16
  music.wNote(c)

  #m17
  music.wNote(f)

  #m18
  music.wNote(c)

  #m19
  music.wNote(g)

  #m20
  music.hNote(g)
  music.hNote(g)

  #m21
  music.wNote(g)

  #m22
  music.wNote(g)

  #m23
  music.wNote(g)

  #m24
  music.hNote(c)
  music.hNote(g)

  #m25
  music.wNote(g)

  #m26
  music.hNote(c)
  music.hNote(g)

  #m27
  music.wNote(g)


# Setting up threads and starting them
high = threading.Thread(target=melody)
high.start()

low = threading.Thread(target=bass)
low.start()

high.join()
low.join()