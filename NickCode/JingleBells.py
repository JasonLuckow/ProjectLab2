import threading
import time
import RPi.GPIO as GPIO
import music

b, bShh = 1
a, aShh = 2
g, gShh = 3
D, DShh = 4
C, CShh = 5
e, eShh = 7 
G, GShh = 8
E, EShh = 10
fS, fSShh = 11
d, dShh = 13
c, cShh = 14

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

  #m5
  music.qNote(e)
  music.eNote(C)
  music.eNote(b)
  music.qNote(a)

  #m6
  music.dHalfNote(fS)
  music.qNote(fS)

  #m7
  music.qNote(D)
  music.eNote(D)
  music.eNote(C)
  music.qNote(a)

  #m8
  music.wNote(b)

  #m9
  music.qNote(d)
  music.eNote(b)
  music.eNote(a)
  music.qNote(g)

  #m10
  music.dHalfNote(d)
  music.eNote(d)
  music.eNote(d)

  #m11
  music.qNote(d)
  music.eNote(b)
  music.eNote(a)
  music.qNote(g)

  #m12
  music.dHalfNote(e)
  music.qNote(e)

  #m13
  music.qNote(e)
  music.qNote(C)
  music.qNote(b)
  music.qNote(a)

  #m14
  music.qNote(D)
  music.qNote(D)
  music.qNote(D)
  music.qNote(D)

  #m15
  music.qNote(E)
  music.qNote(D)
  music.qNote(C)
  music.qNote(a) 

  #m16
  music.wNote(g)

  #m17
  music.qNote(b)
  music.qNote(b)
  music.qNote(b)

  #m18
  music.qNote(b)
  music.qNote(b)
  music.qNote(b)

  #m19
  music.qNote(b)
  music.qNote(D)
  music.dQuarterNote(g)
  music.eNote(a)

  #m20
  music.dHalfNote(b)

  #m21
  music.qNote(C)
  music.qNote(C)
  music.dQuarterNote(C)
  music.qNote(C)

  #m22
  music.qNote(C)
  music.qNote(b)
  music.qNote(b)
  music.eNote(b)
  music.eNote(b)

  #m23
  music.qNote(b)
  music.qNote(a)
  music.qNote(a)
  music.qNote(b)

  #m24
  music.hNote(a)
  music.hNote(D)

  #m17 repeat
  music.qNote(b)
  music.qNote(b)
  music.qNote(b)

  #m18 repeat
  music.qNote(b)
  music.qNote(b)
  music.qNote(b)

  #m19 repeat
  music.qNote(b)
  music.qNote(D)
  music.dQuarterNote(g)
  music.eNote(a)

  #m20 repeat
  music.dHalfNote(b)

  #m21 repeat
  music.qNote(C)
  music.qNote(C)
  music.dQuarterNote(C)
  music.qNote(C)

  #m22 repeat
  music.qNote(C)
  music.qNote(b)
  music.qNote(b)
  music.eNote(b)
  music.eNote(b)

  #m23 repeat
  music.qNote(D)
  music.qNote(D)
  music.qNote(C)
  music.qNote(a)

  #m24 repeat
  music.hNote(g)
  music.qNote(G)

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

  #m5
  music.hNote(c)
  music.hNote(g)

  #m6
  music.hNote(d)
  music.hNote(a)

  #m7
  music.hNote(d)
  music.hNote(d)

  #m8
  music.hNote(g)
  music.hNote(d)

  #m9
  music.hNote(g)
  music.hNote(d)

  #m10
  music.hNote(g)
  music.hNote(d)

  #m11
  music.hNote(g)
  music.hNote(d)

  #m12
  music.hNote(c)
  music.hNote(g)

  #m13
  music.hNote(c)
  music.hNote(g)

  #m14
  music.hNote(d)
  music.hNote(d)

  #m15
  music.hNote(fS)
  music.hNote(d)

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

  #m23
  music.qNote(g)
  music.qNote(G)
  music.qNote(d)
  music.qNote(G)

  #m24
  music.qNote(d)
  music.qNote(c)
  music.qNote(b)
  music.qNote(a)

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

  #m22 repeat
  music.qNote(g)
  music.qNote(G)
  music.qNote(d)
  music.qNote(G)

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