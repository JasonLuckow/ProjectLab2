import threading
import time
import RPi.GPIO as GPIO
import music

b = 17 
B = 20
A = 12
a = 16 
g = 8
D = 14
C = 18
e = 7
G = 6
E = 24
fS = 0
d = 25
c = 16

#music.updateTempo(180)

def melody():
  #m1
  music.qNote(d)
  music.eNote(B)
  music.eNote(A)
  music.qNote(g)

  #m2
  music.dHalfNote(d)
  music.eNote(d)
  music.eNote(d)

  #m3
  music.qNote(d)
  music.eNote(B)
  music.eNote(A)
  music.qNote(g)

  #m4
  music.dHalfNote(e)
  music.eNote(e)
  music.eNote(e)

  #m5
  music.qNote(e)
  music.eNote(C)
  music.eNote(B)
  music.qNote(A)

  #m6
  music.dHalfNote(fS)
  music.qNote(fS)

  #m7
  music.qNote(D)
  music.eNote(D)
  music.eNote(C)
  music.qNote(A)

  #m8
  music.wNote(B)
"""
  #m9
  music.qNote(d)
  music.eNote(B)
  music.eNote(A)
  music.qNote(g)

  #m10
  music.dHalfNote(d)
  music.eNote(d)
  music.eNote(d)

  #m11
  music.qNote(d)
  music.eNote(B)
  music.eNote(A)
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

  #m17
  music.qNote(B)
  music.qNote(B)
  music.qNote(B)

  #m18
  music.qNote(B)
  music.qNote(B)
  music.qNote(B)

  #m19
  music.qNote(B)
  music.qNote(D)
  music.dQuarterNote(g)
  music.eNote(A)

  #m20
  music.dHalfNote(B)

  #m21
  music.qNote(C)
  music.qNote(C)
  music.dQuarterNote(C)
  music.qNote(C)

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
  music.hNote(D)

  #m17 repeat
  music.qNote(B)
  music.qNote(B)
  music.qNote(B)

  #m18 repeat
  music.qNote(B)
  music.qNote(B)
  music.qNote(B)

  #m19 repeat
  music.qNote(B)
  music.qNote(D)
  music.dQuarterNote(g)
  music.eNote(A)

  #m20 repeat
  music.dHalfNote(B)

  #m21 repeat
  music.qNote(C)
  music.qNote(C)
  music.dQuarterNote(C)
  music.qNote(C)

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
  music.qNote(G)"""

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
  music.hNote(A)

  #m7
  music.hNote(d)
  music.hNote(d)

  #m8
  music.hNote(g)
  music.hNote(d)
"""
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
  music.qNote(g)"""

# Setting up threads and starting them
high = threading.Thread(target=melody)
high.start()

#low = threading.Thread(target=bass)
#low.start()

high.join()
#low.join()