import threading
import time
import RPi.GPIO as GPIO
import music

b = 1
a = 2
g = 3
e = 7 
A = 4
f = 3
bF = 8
d = 13
c = 14

music.tempo = music.updateTempo(140)

def melody():
  #m1
  music.qNote(g)
  music.eNote(g)
  music.eNote(A)
  music.qNote(g)
  music.qNote(e)

  #m2s
  music.qNote(c)
  music.qNote(e)
  music.hNote(g)

  #m3
  music.qNote(A)
  music.qNote(A)
  music.qNote(g)
  music.qNote(e)

  #m4
  music.qNote(d)
  music.qNote(g)
  music.hNote(g)

  #m5
  music.qNote(g)
  music.eNote(g)
  music.eNote(A)
  music.qNote(g)
  music.eNote(e)
  music.eNote(d)

  #m6
  music.qNote(c)
  music.qNote(e)
  music.hNote(g)

  #m7
  music.qNote(A)
  music.eNote(A)
  music.eNote(A)
  music.eNote(g)
  music.eNote(g)
  music.qNote(e)

  #m8
  music.qNote(d)
  music.qNote(g)
  music.hNote(c)

  #m9
  music.qNote(f)
  music.qNote(f)
  music.hNote(A)

  #m10
  music.qNote(g)
  music.eNote(g)
  music.eNote(g)
  music.hNote(e)

  #m11
  music.qNote(d)
  music.qNote(d)
  music.qNote(f)

  #m12
  music.qNote(e)
  music.eNote(g)
  music.eNote(g)
  music.qNote(c)
  music.qNote(e)

  #m13
  music.qNote(g)
  music.eNote(g)
  music.eNote(A)
  music.qNote(g)
  music.qNote(e)

  #m14
  music.qNote(f)
  music.qNote(g)
  music.qNote(A)
  music.qNoteRest()

  #m15
  music.qNote(g)
  music.eNote(g)
  music.eNote(A)
  music.qNote(g)
  music.eNote(e)
  music.eNote(e)

  #m16
  music.qNote(d)
  music.qNote(g)
  music.qNote(c)
  

def bass():
  #m1
  music.hNote(c)
  music.hNote(g)

  #m2
  music.hNote(c)
  music.hNote(e)

  #m3
  music.hNote(f)
  music.hNote(e)

  #m4
  music.qNote(b)
  music.qNote(a)
  music.qNote(g)
  music.qNote(b)

  #m5
  music.hNote(c)
  music.hNote(g)

  #m6
  music.hNote(c)
  music.hNote(e)

  #m7
  music.hNote(f)
  music.hNote(e)

  #m8
  music.hNote(f)
  music.qNote(e)
  music.qNote(c)

  #m9
  music.wNote(f)

  #m10
  music.wNote(e)

  #m11
  music.wNote(d)

  #m12
  music.wNote(c)

  #m13
  music.hNote(c)
  music.hNote(bF)

  #m14
  music.qNote(A)
  music.qNote(g)
  music.qNote(f)
  music.qNoteRest
  
  #m15
  music.hNote(c)
  music.hNote(g)

  #m16
  music.hNote(b)
  music.hNote(c)

# Setting up threads and starting them
high = threading.Thread(target=melody)
high.start()

low = threading.Thread(target=bass)
low.start()

high.join()
low.join()