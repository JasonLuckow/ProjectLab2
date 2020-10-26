import threading
import time
import RPi.GPIO as GPIO
import music

BF = 9
A = 12
g = 8
D = 4
C = 5
eF = 5
e = 7 
G = 8
F = 9
E = 10
fS = 11
f = 13
d = 25
c = 14

music.tempo = music.updateTempo(120)

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
  """

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
  music.qNote(g)
  music.eNote(g)
  music.eNote(g)
  music.eNote(F)
  music.eNote(e)
  
  #m18
  music.qNote(D)
  music.eNote(D)
  music.eNote(D)
  music.eNote(C)
  music.eNote(BF)

  # #m19
  # music.qNote(D)
  # music.eNote(D)
  # music.eNote(D)
  # music.eNote(C)
  # music.eNote(BF)

  # #m20
  # music.qNote(BF)
  # music.eNote(A)
  # music.eNote(BF)
  # music.qNote(g)
  
  # #m21
  # music.eNote(eF)
  # music.eNote(e)
  # music.eNote(fS)
  # music.eNote(g)
  # music.eNote(A)
  # music.eNote(BF)
  
  # #m22
  # music.eNote(C)
  # music.eNote(D)
  # music.qNote(C)
  # music.qNote(BF)

  # #m23
  # music.eNote(eF)
  # music.eNote(e)
  # music.eNote(fS)
  # music.eNote(g)
  # music.eNote(A)
  # music.eNote(BF)
  
  # #m24
  # music.eNote(C)
  # music.eNote(D)
  # music.qNote(C)
  # music.qNote(BF)

  # #m25
  # music.qNote(BF)
  # music.eNote(A)
  # music.eNote(BF)
  # music.qNote(g)

  # #m26
  # music.qNote(BF)
  # music.eNote(A)
  # music.eNote(BF)
  # music.qNote(g)

  # #m27
  # music.qNote(BF)
  # music.eNote(A)
  # music.eNote(BF)
  # music.qNote(g)

  # #m28
  # music.qNote(BF)
  # music.eNote(A)
  # music.eNote(BF)
  # music.qNote(g)

  # #m29
  # music.qNote(BF)
  # music.eNote(A)
  # music.eNote(BF)
  # music.qNote(g)

  # #m30
  # music.qNote(BF)
  # music.eNote(A)
  # music.eNote(BF)
  # music.qNote(g)

  # #m31
  # music.qNote(BF)
  # music.eNote(A)
  # music.eNote(BF)
  # music.qNote(g)

  # #m32
  # music.qNote(BF)
  # music.eNote(A)
  # music.eNote(BF)
  # music.qNote(g)

  # #m33
  # music.dHAlfNote(g)
  """

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
  """

  #m9
  music.dHalfNote(c)

  #m10
  music.dHalfNote(d)

  #m11
  music.dHalfNote(c)

  #m12
  music.dHalfNote(d)
  
  #m13
  music.dHalfNote(d)

  #m14
  music.dHalfNote(e)

  #m15
  music.dHalfNote(f)

  #m16
  music.qNote(e)
  music.qNote(eF)
  music.qNote(d)

  #m17
  music.dHalfNote(d)

  #m18
  music.dHalfNote(bF)

  #m19
  music.dHalfNote(bF)

  #m20
  music.dHalfNote(bF)
  
  #m21
  music.dHalfNote(fS)

  #m22
  music.hNote(a)
  music.qNote(g)

  #m23
  music.dHalfNote(fS)

  #m24
  music.hNote(a)
  music.qNote(g)

  #m25
  music.dHalfNote(g)

  #m26
  music.dHalfNote(g)

  #m27
  music.dHalfNote(g)

  #m28
  music.dHalfNote(g)

  #m29
  music.dHalfNote(g)

  #m30
  music.dHalfNote(g)

  #m31
  music.dHalfNote(g)

  #m32
  music.dHalfNote(g)

  #m33
  music.dHalfNote(g)
  """

# Setting up threads and starting them
high = threading.Thread(target=melody)
high.start()

# low = threading.Thread(target=bass)
# low.start()

high.join()
# low.join()