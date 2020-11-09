import threading
import time
import RPi.GPIO as GPIO
import music1

bF = 14
b = 24
c = 16
d = 25
dS = 4
e = 7
f = 19
fS = 17
g = 8
A = 12
BF = 22
B = 20
C = 18
D = 15
DS = 13
E = 1
F = 6
G = 21

def melody():
  #m1
  music1.qNote(g)
  music1.eNote(g)
  music1.eNote(A)
  music1.qNote(g)
  music1.qNote(e)

  #m2s
  music1.qNote(c)
  music1.qNote(e)
  music1.hNote(g)

  #m3
  music1.qNote(A)
  music1.qNote(A)
  music1.qNote(g)
  music1.qNote(e)

  #m4
  music1.qNote(d)
  music1.qNote(g)
  music1.hNote(g)

  #m5
  music1.qNote(g)
  music1.eNote(g)
  music1.eNote(A)
  music1.qNote(g)
  music1.eNote(e)
  music1.eNote(d)

  #m6
  music1.qNote(c)
  music1.qNote(e)
  music1.hNote(g)

  #m7
  music1.qNote(A)
  music1.eNote(A)
  music1.eNote(A)
  music1.eNote(g)
  music1.eNote(g)
  music1.qNote(e)

  #m8
  music1.qNote(d)
  music1.qNote(g)
  music1.hNote(c)

  #m9
  music1.qNote(f)
  music1.qNote(f)
  music1.hNote(A)

  #m10
  music1.qNote(g)
  music1.eNote(g)
  music1.eNote(g)
  music1.hNote(e)

  #m11
  music1.qNote(d)
  music1.qNote(d)
  music1.qNote(f)

  #m12
  music1.qNote(e)
  music1.eNote(g)
  music1.eNote(g)
  music1.qNote(c)
  music1.qNote(e)

  #m13
  music1.qNote(g)
  music1.eNote(g)
  music1.eNote(A)
  music1.qNote(g)
  music1.qNote(e)

  #m14
  music1.qNote(f)
  music1.qNote(g)
  music1.qNote(A)
  music1.qNoteRest()

  #m15
  music1.qNote(g)
  music1.eNote(g)
  music1.eNote(A)
  music1.qNote(g)
  music1.eNote(e)
  music1.eNote(e)

  #m16
  music1.qNote(d)
  music1.qNote(g)
  music1.qNote(c)
  

def bass():
  #m1
  music1.hNote(c)
  music1.hNote(g)

  #m2
  music1.hNote(c)
  music1.hNote(e)

  #m3
  music1.hNote(f)
  music1.hNote(e)

  #m4
  music1.qNote(b)
  music1.qNote(a)
  music1.qNote(g)
  music1.qNote(b)

  #m5
  music1.hNote(c)
  music1.hNote(g)

  #m6
  music1.hNote(c)
  music1.hNote(e)

  #m7
  music1.hNote(f)
  music1.hNote(e)

  #m8
  music1.hNote(f)
  music1.qNote(e)
  music1.qNote(c)

  #m9
  music1.wNote(f)

  #m10
  music1.wNote(e)

  #m11
  music1.wNote(d)

  #m12
  music1.wNote(c)

  #m13
  music1.hNote(c)
  music1.hNote(bF)

  #m14
  music1.qNote(A)
  music1.qNote(g)
  music1.qNote(f)
  music1.qNoteRest
  
  #m15
  music1.hNote(c)
  music1.hNote(g)

  #m16
  music1.hNote(b)
  music1.hNote(c)

# Setting up threads and starting them
high = threading.Thread(target=melody)
high.start()

low = threading.Thread(target=bass)
low.start()

high.join()
low.join()