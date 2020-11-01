import threading
import time
import RPi.GPIO as GPIO
import music

bF = 14
b = 15
c = 16
d = 25
dS = 5
e = 7
f = 13
fS = 0
g = 8
A = 12
BF = 9
B = 20
C = 18
D = 24
DS = 6
E = 1
F = 26
G = 21

#music.updateTempo(180)

def melody():
  #m1
  music.qNote(d)
  music.qNote(B)
  music.qNote(A)
  music.qNote(g)

  # #m2
  music.dHalfNote(d)
  music.eNote(d)
  music.eNote(d)

  #m3
  music.qNote(d)
  music.qNote(B)
  music.qNote(A)
  music.qNote(g)

  #m4
  music.dHalfNote(e)
  music.eNote(e)
  music.eNote(e)

  #m5
  music.qNote(e)
  music.qNote(C)
  music.qNote(B)
  music.qNote(A)

  #m6
  music.dHalfNote(fS)
  music.qNote(fS)

  #m7
  music.qNote(D)
  music.qNote(D)
  music.qNote(C)
  music.qNote(A)

  #m8
  music.wNote(B)
  time.sleep(.1)

  #m9
  music.qNote(d)
  music.qNote(B)
  music.qNote(A)
  music.qNote(g)

  #m10
  music.dHalfNote(d)
  music.eNote(d)
  music.eNote(d)

  #m11
  music.qNote(d)
  music.qNote(B)
  music.qNote(A)
  music.qNote(g)

  #m12
  music.dHalfNote(e)
  music.qNote(e)

  #m13
  music.qNote(e)
  music.qNote(C)
  music.qNote(B)
  music.qNote(A)

  #m14
  music.qNote(D)
  music.qNote(D)
  music.qNote(D)
  music.qNote(D)

  #m15
  music.qNote(E)
  music.qNote(D)
  music.qNote(C)
  music.qNote(A) 

  #m16
  music.wNote(g)
  time.sleep(.1)

  #m17
  music.qNote(B)
  music.qNote(B)
  music.hNote(B)
  time.sleep(.1)

  #m18
  music.qNote(B)
  music.qNote(B)
  music.hNote(B)
  time.sleep(.1)

  #m19
  music.qNote(B)
  music.qNote(D)
  music.dQuarterNote(g)
  music.eNote(A)

  #m20
  music.dHalfNote(B)
  music.qNoteRest()
  time.sleep(.3)

  #m21
  music.qNote(C)
  music.qNote(C)
  music.dQuarterNote(C)
  music.eNote(C)

  #m22
  music.qNote(C)
  music.qNote(B)
  music.qNote(B)
  music.eNote(B)
  music.eNote(B)

  #m23
  music.qNote(B)
  music.qNote(A)
  music.qNote(A)
  music.qNote(B)

  #m24
  music.hNote(A)
  time.sleep(.1)
  music.hNote(D)
  time.sleep(.1)

  #m17 repeat
  music.qNote(B)
  music.qNote(B)
  music.hNote(B)
  time.sleep(.1)

  #m18 repeat
  music.qNote(B)
  music.qNote(B)
  music.hNote(B)
  time.sleep(.1)

  #m19 repeat
  music.qNote(B)
  music.qNote(D)
  music.dQuarterNote(g)
  music.eNote(A)

  #m20 repeat
  music.dHalfNote(B)
  music.qNoteRest()
  time.sleep(.3)

  #m21 repeat
  music.qNote(C)
  music.qNote(C)
  music.dQuarterNote(C)
  music.eNote(C)

  #m22 repeat
  music.qNote(C)
  music.qNote(B)
  music.qNote(B)
  music.eNote(B)
  music.eNote(B)

  #m23 repeat
  music.qNote(D)
  music.qNote(D)
  music.qNote(C)
  music.qNote(A)

  #m24 repeat
  music.hNote(g)
  music.qNote(G)

def bass():
  #m1
  music.hNote(g)
  time.sleep(.1)
  music.hNote(d)
  time.sleep(.1)

  #m2
  music.hNote(g)
  music.hNote(d)
  time.sleep(.1)

  #m3
  music.hNote(g)
  time.sleep(.1)
  music.hNote(d)
  time.sleep(.1)

  #m4
  music.hNote(c)
  music.hNote(g)
  time.sleep(.1)

  #m5
  music.hNote(c)
  time.sleep(.1)
  music.hNote(g)
  time.sleep(.1)

  #m6
  music.hNote(d)
  music.hNote(A)

  #m7
  music.hNote(d)
  time.sleep(.1)
  music.hNote(d)
  time.sleep(.1)

  #m8
  music.hNote(g)
  music.hNote(d)
  
  #m9
  music.hNote(g)
  time.sleep(.1)
  music.hNote(d)
  time.sleep(.1)

  #m10
  music.hNote(g)
  music.hNote(d)
  time.sleep(.1)

  #m11
  music.hNote(g)
  time.sleep(.1)
  music.hNote(d)
  time.sleep(.1)

  #m12
  music.hNote(c)
  music.hNote(g)

  #m13
  music.hNote(c)
  time.sleep(.1)
  music.hNote(g)
  time.sleep(.1)

  #m14
  music.hNote(d)
  time.sleep(.1)
  music.hNote(d)
  time.sleep(.1)

  #m15
  music.hNote(fS)
  time.sleep(.1)
  music.hNote(d)
  time.sleep(.1)

  #m16
  music.hNote(g)
  music.hNote(d)

  #m17
  music.qNote(g)
  music.qNote(g)
  music.qNote(d)
  music.qNote(g)

  #m18
  music.qNote(g)
  music.qNote(g)
  music.qNote(d)
  music.qNote(g)

  #m19
  music.qNote(g)
  music.qNote(g)
  music.qNote(d)
  music.qNote(g)

  #m20
  music.qNote(g)
  music.qNote(G)
  music.qNote(d)
  music.qNote(G)

  #m21
  music.qNote(c)
  music.qNote(C)
  music.qNote(g)
  music.qNote(C)

  #m22
  music.qNote(g)
  music.qNote(G)
  music.qNote(d)
  music.qNote(G)
  time.sleep(.1)

  #m23
  music.qNote(g)
  music.qNote(G)
  music.qNote(d)
  music.qNote(G)

  #m24
  music.qNote(d)
  music.qNote(c)
  music.qNote(b)
  music.qNote(A)

  #m17 repeat
  music.qNote(g)
  music.qNote(g)
  music.qNote(d)
  music.qNote(g)

  #m18 repeat
  music.qNote(g)
  music.qNote(g)
  music.qNote(d)
  music.qNote(g)

  #m19 repeat
  music.qNote(g)
  music.qNote(g)
  music.qNote(d)
  music.qNote(g)

  #m20 repeat
  music.qNote(g)
  music.qNote(G)
  music.qNote(d)
  music.qNote(G)

  #m21 repeat
  music.qNote(c)
  music.qNote(C)
  music.qNote(g)
  music.qNote(C)
  time.sleep(.5)

  #m22 repeat
  music.qNote(g)
  music.qNote(G)
  music.qNote(d)
  music.qNote(G)
  time.sleep(.1)

  #m23 repeat
  music.qNote(d)
  music.qNote(d)
  music.qNote(e)
  music.qNote(fS)

  #m24 repeat
  music.hNote(G)
  music.qNote(g)

# Setting up threads and starting them
high = threading.Thread(target=melody)
high.start()

low = threading.Thread(target=bass)
low.start()

high.join()
low.join()