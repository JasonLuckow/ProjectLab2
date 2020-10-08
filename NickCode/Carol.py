import threading
import time
import RPi.GPIO as GPIO
import music

bF = 16
bFShh = 17
a = 18
aShh = 19
g = 20
gShh = 21
f = 22
fShh = 23
eF = 24
eFShh = 25
d = 26
dShh = 27

def melody():
  #m1
  music.qNote(bF)
  music.eNote(a)
  music.eNote(bF)
  music.qNote(g)

  #m2
  music.qNote(bF)
  music.eNote(a)
  music.eNote(bF)
  music.qNote(g)

  #m3
  music.qNote(bF)
  music.eNote(a)
  music.eNote(bF)
  music.qNote(g)

  #m4
  music.qNote(bF)
  music.eNote(a)
  music.eNote(bF)
  music.qNote(g)

  #m5
  music.qNote(bF)
  music.eNote(a)
  music.eNote(bF)
  music.qNote(g)

  #m6
  music.qNote(bF)
  music.eNote(a)
  music.eNote(bF)
  music.qNote(g)

  #m7
  music.qNote(bF)
  music.eNote(a)
  music.eNote(bF)
  music.qNote(g)

  #m8
  music.qNote(bF)
  music.eNote(a)
  music.eNote(bF)
  music.qNote(g)

  #m9
  music.qNote(bF)
  music.eNote(a)
  music.eNote(bF)
  music.qNote(g)

  #m10
  music.qNote(bF)
  music.eNote(a)
  music.eNote(bF)
  music.qNote(g)

  #m11
  music.qNote(bF)
  music.eNote(a)
  music.eNote(bF)
  music.qNote(g)

  #m12
  music.qNote(bF)
  music.eNote(a)
  music.eNote(bF)
  music.qNote(g)

def bass():
  #m1
  music.dHalfNote(g)

  #m2
  music.dHalfNote(f)

  #m3
  music.dHalfNote(eF)

  #m4
  music.dHalfNote(d)

  #m5
  music.dHalfNote(g)

  #m6
  music.dHalfNote(f)

  #m7
  music.dHalfNote(eF)

  #m8
  music.dHalfNote(d)

  #m9
  music.dHalfNote(c)

  #m10
  music.dHalfNote(d)

  #m11
  music.dHalfNote(c)

  #m12
  music.dHalfNote(d)

# Setting up threads and starting them
high = threading.Thread(target=melody)
high.start()

low = threading.Thread(target=bass)
low.start()

high.join()
low.join()


    