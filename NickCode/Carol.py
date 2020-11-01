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


#music.tempo = music.updateTempo(120)

def melody():
  #m1
  music.qNote(BF)
  music.eNote(A)
  music.eNote(BF)
  music.qNote(g)

  #m2
  music.qNote(BF)
  music.eNote(A)
  music.eNote(BF)
  music.qNote(g)

  #m3
  music.qNote(BF)
  music.eNote(A)
  music.eNote(BF)
  music.qNote(g)

  #m4
  music.qNote(BF)
  music.eNote(A)
  music.eNote(BF)
  music.qNote(g)


  #m5
  music.qNote(BF)
  music.eNote(A)
  music.eNote(BF)
  music.qNote(g)

  #m6
  music.qNote(BF)
  music.eNote(A)
  music.eNote(BF)
  music.qNote(g)

  #m7
  music.qNote(BF)
  music.eNote(A)
  music.eNote(BF)
  music.qNote(g)

  #m8
  music.qNote(BF)
  music.eNote(A)
  music.eNote(BF)
  music.qNote(g)

  #m9
  music.qNote(BF)
  music.eNote(A)
  music.eNote(BF)
  music.qNote(g)

  #m10
  music.qNote(BF)
  music.eNote(A)
  music.eNote(BF)
  music.qNote(g)

  #m11
  music.qNote(BF)
  music.eNote(A)
  music.eNote(BF)
  music.qNote(g)

  #m12
  music.qNote(BF)
  music.eNote(A)
  music.eNote(BF)
  music.qNote(g)

  #m13
  music.qNote(D)
  music.eNote(C)
  music.eNote(D)
  music.qNote(BF)

  #m14
  music.qNote(D)
  music.eNote(C)
  music.eNote(D)
  music.qNote(BF)

  #m15
  music.qNote(D)
  music.eNote(C)
  music.eNote(D)
  music.qNote(BF)

  #m16
  music.qNote(D)
  music.eNote(C)
  music.eNote(D)
  music.qNote(BF)

  #m17
  music.qNote(G)
  music.eNote(G)
  music.eNote(G)
  music.eNote(F)
  music.eNote(E)
  
  #m18
  music.qNote(D)
  music.eNote(D)
  music.eNote(D)
  music.eNote(C)
  music.eNote(BF)

  #m19
  music.qNote(C)
  music.eNote(C)
  music.eNote(C)
  music.eNote(D)
  music.eNote(C)

  #m20
  music.qNote(BF)
  music.eNote(A)
  music.eNote(BF)
  music.qNote(g)
  
  #m21
  music.eNote(d)
  music.eNote(e)
  music.eNote(fS)
  music.eNote(g)
  music.eNote(A)
  music.eNote(BF)
  
  #m22
  music.eNote(C)
  music.eNote(D)
  music.qNote(C)
  music.qNote(BF)

  #m23
  music.eNote(d)
  music.eNote(e)
  music.eNote(fS)
  music.eNote(g)
  music.eNote(A)
  music.eNote(BF)
  
  #m24
  music.eNote(C)
  music.eNote(D)
  music.qNote(C)
  music.qNote(BF)

  #m25
  music.qNote(BF)
  music.eNote(A)
  music.eNote(BF)
  music.qNote(g)

  #m26
  music.qNote(BF)
  music.eNote(A)
  music.eNote(BF)
  music.qNote(g)

  #m27
  music.qNote(BF)
  music.eNote(A)
  music.eNote(BF)
  music.qNote(g)

  #m28
  music.qNote(BF)
  music.eNote(A)
  music.eNote(BF)
  music.qNote(g)

  #m29
  music.qNote(BF)
  music.eNote(A)
  music.eNote(BF)
  music.qNote(g)

  #m30
  music.qNote(BF)
  music.eNote(A)
  music.eNote(BF)
  music.qNote(g)

  #m31
  music.qNote(BF)
  music.eNote(A)
  music.eNote(BF)
  music.qNote(g)

  #m32
  music.qNote(BF)
  music.eNote(A)
  music.eNote(BF)
  music.qNote(g)

  #m33
  music.dHalfNote(g)
  

def bass():
  #m1
  music.dHalfNote(g)
  time.sleep(.3)

  #m2
  music.dHalfNote(f)
  time.sleep(.3)

  #m3
  music.dHalfNote(dS)
  time.sleep(.3)

  #m4
  music.dHalfNote(d)
  time.sleep(.3)

  #m5
  music.dHalfNote(g)
  time.sleep(.3)

  #m6
  music.dHalfNote(f)
  time.sleep(.3)

  #m7
  music.dHalfNote(dS)
  time.sleep(.3)
  
  #m8
  music.dHalfNote(d)
  time.sleep(.3)

  #m9
  music.dHalfNote(c)
  time.sleep(.3)

  #m10
  music.dHalfNote(d)
  time.sleep(.3)

  #m11
  music.dHalfNote(c)
  time.sleep(.3)

  #m12
  music.dHalfNote(d)
  time.sleep(.3)
  
  #m13
  music.dHalfNote(d)
  time.sleep(.3)

  #m14
  music.dHalfNote(e)
  time.sleep(.3)

  #m15
  music.dHalfNote(f)
  time.sleep(.3)

  #m16
  music.qNote(e)
  music.qNote(dS)
  time.sleep(.1)
  music.qNote(d)

  #m17
  music.dHalfNote(d)
  time.sleep(.4)

  #m18
  music.dHalfNote(bF)
  time.sleep(.4)

  #m19
  music.dHalfNote(bF)
  time.sleep(.4)

  #m20
  music.dHalfNote(bF)
  time.sleep(.3)
  
  #m21
  music.dHalfNote(fS)
  time.sleep(.5)

  #m22
  music.hNote(A)
  time.sleep(.2)
  music.qNote(g)

  #m23
  music.dHalfNote(fS)
  time.sleep(.3)

  #m24
  music.hNote(A)
  time.sleep(.2)
  music.qNote(g)

  #m25
  music.dHalfNote(g)
  time.sleep(.3)

  #m26
  music.dHalfNote(g)
  time.sleep(.3)

  #m27
  music.dHalfNote(g)
  time.sleep(.3)

  #m28
  music.dHalfNote(g)
  time.sleep(.3)

  #m29
  music.dHalfNote(g)
  time.sleep(.3)

  #m30
  music.dHalfNote(g)
  time.sleep(.3)

  #m31
  music.dHalfNote(g)
  time.sleep(.3)

  #m32
  music.dHalfNote(g)
  time.sleep(.3)

  #m33
  music.dHalfNote(g)

# Setting up threads and starting them
high = threading.Thread(target=melody)
high.start()

low = threading.Thread(target=bass)
low.start()

high.join()
low.join()