import threading
import time
import RPi.GPIO as GPIO
import music

b = 16
bShh = 17
a = 18
aShh = 19
g = 20
gShh = 21
f = 22
fShh = 23
e = 24
eShh = 25
d = 26
dShh = 27
c = 1

def melody():
  #m1
  music.qNote(d)
  music.eNote(b)
  music.eNote(a)
  music.qNote(g)

  #m2
  music.dHalfNote(d)
  music.eNote(d)
  music.eNote(d)

  #m3
  music.qNote(d)
  music.eNote(b)
  music.eNote(a)
  music.qNote(g)

  #m4
  music.dHalfNote(e)
  music.eNote(e)
  music.eNote(e)


def bass():
  #m1
  music.hNote(g)
  music.hNote(d)

  #m2
  music.hNote(g)
  music.hNote(d)

  #m3
  music.hNote(g)
  music.hNote(d)

  #m4
  music.hNote(c)
  music.hNote(g)

# Setting up threads and starting them
high = threading.Thread(target=melody)
high.start()

low = threading.Thread(target=bass)
low.start()

high.join()
low.join()


    