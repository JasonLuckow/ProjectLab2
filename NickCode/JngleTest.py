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

#music1.updateTempo(180)

def melody():
  #m1
  music1.qNote(d)
  music1.qNote(B)
  music1.qNote(A)
  music1.qNote(g)

  # #m2
  music1.dHalfNote(d)
  music1.eNote(d)
  music1.eNote(d)

  #m3
  music1.qNote(d)
  music1.qNote(B)
  music1.qNote(A)
  music1.qNote(g)

  #m4
  music1.dHalfNote(e)
  music1.qNote(e)

  #m5
  music1.qNote(e)
  music1.qNote(C)
  music1.qNote(B)
  music1.qNote(A)

  #m6
  music1.dHalfNote(fS)
  music1.qNote(fS)

  #m7
  music1.qNote(D)
  music1.qNote(D)
  music1.qNote(C)
  music1.qNote(A)

  #m8
  music1.wNote(B)
  time.sleep(.1)

  #m9
  music1.qNote(d)
  music1.qNote(B)
  music1.qNote(A)
  music1.qNote(g)

  #m10
  music1.dHalfNote(d)
  music1.eNote(d)
  music1.eNote(d)

  #m11
  music1.qNote(d)
  music1.qNote(B)
  music1.qNote(A)
  music1.qNote(g)

  #m12
  music1.dHalfNote(e)
  music1.qNote(e)

  #m13
  music1.qNote(e)
  music1.qNote(C)
  music1.qNote(B)
  music1.qNote(A)

  #m14
  music1.qNote(D)
  music1.qNote(D)
  music1.qNote(D)
  music1.qNote(D)

  #m15
  music1.qNote(E)
  music1.qNote(D)
  music1.qNote(C)
  music1.qNote(A) 

  #m16
  music1.wNote(g)
  time.sleep(.1)

  #m17
  music1.qNote(B)
  music1.qNote(B)
  music1.hNote(B)
  time.sleep(.1)

  #m18
  music1.qNote(B)
  music1.qNote(B)
  music1.hNote(B)
  time.sleep(.1)

  #m19
  music1.qNote(B)
  music1.qNote(D)
  music1.dQuarterNote(g)
  music1.eNote(A)

  #m20
  music1.dHalfNote(B)
  music1.qNoteRest()
  time.sleep(.3)

  #m21
  music1.qNote(C)
  music1.qNote(C)
  music1.dQuarterNote(C)
  music1.eNote(C)

  #m22
  music1.qNote(C)
  music1.qNote(B)
  music1.qNote(B)
  music1.eNote(B)
  music1.eNote(B)

  #m23
  music1.qNote(B)
  music1.qNote(A)
  music1.qNote(A)
  music1.qNote(B)

  #m24
  music1.hNote(A)
  time.sleep(.1)
  music1.hNote(D)
  time.sleep(.1)

  #m17 repeat
  music1.qNote(B)
  music1.qNote(B)
  music1.hNote(B)
  time.sleep(.1)

  #m18 repeat
  music1.qNote(B)
  music1.qNote(B)
  music1.hNote(B)
  time.sleep(.1)

  #m19 repeat
  music1.qNote(B)
  music1.qNote(D)
  music1.dQuarterNote(g)
  music1.eNote(A)

  #m20 repeat
  music1.dHalfNote(B)
  music1.qNoteRest()
  time.sleep(.3)

  #m21 repeat
  music1.qNote(C)
  music1.qNote(C)
  music1.dQuarterNote(C)
  music1.eNote(C)

  #m22 repeat
  music1.qNote(C)
  music1.qNote(B)
  music1.qNote(B)
  music1.eNote(B)
  music1.eNote(B)

  #m23 repeat
  music1.qNote(D)
  music1.qNote(D)
  music1.qNote(C)
  music1.qNote(A)

  #m24 repeat
  music1.hNote(g)
  music1.qNote(G)

def bass():
  #m1
  music1.hNote(g)
  time.sleep(.1)
  music1.hNote(d)
  time.sleep(.1)

  #m2
  music1.hNote(g)
  music1.hNote(d)
  time.sleep(.1)

  #m3
  music1.hNote(g)
  time.sleep(.1)
  music1.hNote(d)
  time.sleep(.1)

  #m4
  music1.hNote(c)
  music1.hNote(g)

  #m5
  music1.hNote(c)
  time.sleep(.1)
  music1.hNote(g)
  time.sleep(.1)

  #m6
  music1.hNote(d)
  music1.hNote(A)

  #m7
  music1.hNote(d)
  time.sleep(.1)
  music1.hNote(d)
  time.sleep(.1)

  #m8
  music1.hNote(g)
  music1.hNote(d)
  
  #m9
  music1.hNote(g)
  time.sleep(.1)
  music1.hNote(d)
  time.sleep(.1)

  #m10
  music1.hNote(g)
  music1.hNote(d)
  time.sleep(.1)

  #m11
  music1.hNote(g)
  time.sleep(.1)
  music1.hNote(d)
  time.sleep(.1)

  #m12
  music1.hNote(c)
  music1.hNote(g)

  #m13
  music1.hNote(c)
  time.sleep(.1)
  music1.hNote(g)
  time.sleep(.1)

  #m14
  music1.hNote(d)
  time.sleep(.1)
  music1.hNote(d)
  time.sleep(.1)

  #m15
  music1.hNote(fS)
  time.sleep(.1)
  music1.hNote(d)
  time.sleep(.1)

  #m16
  music1.hNote(g)
  music1.hNote(d)

  #m17
  music1.qNote(g)
  music1.qNote(g)
  music1.qNote(d)
  music1.qNote(g)

  #m18
  music1.qNote(g)
  music1.qNote(g)
  music1.qNote(d)
  music1.qNote(g)

  #m19
  music1.qNote(g)
  music1.qNote(g)
  music1.qNote(d)
  music1.qNote(g)

  #m20
  music1.qNote(g)
  music1.qNote(G)
  music1.qNote(d)
  music1.qNote(G)

  #m21
  music1.qNote(c)
  music1.qNote(C)
  music1.qNote(g)
  music1.qNote(C)

  #m22
  music1.qNote(g)
  music1.qNote(G)
  music1.qNote(d)
  music1.qNote(G)
  time.sleep(.1)

  #m23
  music1.qNote(g)
  music1.qNote(G)
  music1.qNote(d)
  music1.qNote(G)

  #m24
  music1.qNote(d)
  music1.qNote(c)
  music1.qNote(b)
  music1.qNote(A)

  #m17 repeat
  music1.qNote(g)
  music1.qNote(g)
  music1.qNote(d)
  music1.qNote(g)

  #m18 repeat
  music1.qNote(g)
  music1.qNote(g)
  music1.qNote(d)
  music1.qNote(g)

  #m19 repeat
  music1.qNote(g)
  music1.qNote(g)
  music1.qNote(d)
  music1.qNote(g)

  #m20 repeat
  music1.qNote(g)
  music1.qNote(G)
  music1.qNote(d)
  music1.qNote(G)

  #m21 repeat
  music1.qNote(c)
  music1.qNote(C)
  music1.qNote(g)
  music1.qNote(C)

  #m22 repeat
  music1.qNote(g)
  music1.qNote(G)
  music1.qNote(d)
  music1.qNote(G)
  time.sleep(.1)

  #m23 repeat
  music1.qNote(d)
  music1.qNote(d)
  music1.qNote(e)
  music1.qNote(fS)

  #m24 repeat
  music1.hNote(G)
  music1.qNote(g)

# Setting up threads and starting them
high = threading.Thread(target=melody)
high.start()

low = threading.Thread(target=bass)
low.start()

high.join()
low.join()