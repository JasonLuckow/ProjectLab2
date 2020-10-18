import threading
import time
import RPi.GPIO as GPIO
import music

bF, bFShh = 1
a, aShh = 2
g, gShh = 3
D, DShh = 4
C, CShh = 5
eF, eFShh = 6
e, eShh = 7 
G, GShh = 8
F, FShh = 9
E, EShh = 10
fS, fSShh = 11
f, fShh = 12
d, dShh = 13
c, cShh = 14

def melody():
  #m1
  music.qNote(bF, bFShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  music.qNote(g, gShh)

  #m2
  music.qNote(bF, bFShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  music.qNote(g, gShh)

  #m3
  music.qNote(bF, bFShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  music.qNote(g, gShh)

  #m4
  music.qNote(bF, bFShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  music.qNote(g, gShh)

  #m5
  music.qNote(bF, bFShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  music.qNote(g, gShh)

  #m6
  music.qNote(bF, bFShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  music.qNote(g, gShh)

  #m7
  music.qNote(bF, bFShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  music.qNote(g, gShh)

  #m8
  music.qNote(bF, bFShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  music.qNote(g, gShh)

  #m9
  music.qNote(bF, bFShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  music.qNote(g, gShh)

  #m10
  music.qNote(bF, bFShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  music.qNote(g, gShh)

  #m11
  music.qNote(bF, bFShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  music.qNote(g, gShh)

  #m12
  music.qNote(bF, bFShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  music.qNote(g, gShh)

  #m13
  music.qNote(D, DShh)
  music.eNote(C, CShh)
  music.eNote(D, DShh)
  music.qNote(bF, bFShh)

  #m14
  music.qNote(D, DShh)
  music.eNote(C, CShh)
  music.eNote(D, DShh)
  music.qNote(bF, bFShh)

  #m15
  music.qNote(D, DShh)
  music.eNote(C, CShh)
  music.eNote(D, DShh)
  music.qNote(bF, bFShh)

  #m16
  music.qNote(D, DShh)
  music.eNote(C, CShh)
  music.eNote(D, DShh)
  music.qNote(bF, bFShh)

  #m17
  music.qNote(g, gShh)
  music.eNote(g, gShh)
  music.eNote(g, gShh)
  music.eNote(F, FShh)
  music.eNote(e, eShh)
  
  #m18
  music.qNote(D, DShh)
  music.eNote(D, DShh)
  music.eNote(D, DShh)
  music.eNote(C, CShh)
  music.eNote(bF, bFShh)

  #m19
  music.qNote(D, DShh)
  music.eNote(D, DShh)
  music.eNote(D, DShh)
  music.eNote(C, CShh)
  music.eNote(bF, bFShh)

  #m20
  music.qNote(bF, bFShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  music.qNote(g, gShh)
  
  #m21
  music.eNote(eF, eFShh)
  music.eNote(e, eShh)
  music.eNote(fS, fSShh)
  music.eNote(g, gShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  
  #m22
  music.eNote(C, CShh)
  music.eNote(D, DShh)
  music.qNote(C, CShh)
  music.qNote(bF, bFShh)

  #m23
  music.eNote(eF, eFShh)
  music.eNote(e, eShh)
  music.eNote(fS, fSShh)
  music.eNote(g, gShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  
  #m24
  music.eNote(C, CShh)
  music.eNote(D, DShh)
  music.qNote(C, CShh)
  music.qNote(bF, bFShh)

  #m25
  music.qNote(bF, bFShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  music.qNote(g, gShh)

  #m26
  music.qNote(bF, bFShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  music.qNote(g, gShh)

  #m27
  music.qNote(bF, bFShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  music.qNote(g, gShh)

  #m28
  music.qNote(bF, bFShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  music.qNote(g, gShh)

  #m29
  music.qNote(bF, bFShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  music.qNote(g, gShh)

  #m30
  music.qNote(bF, bFShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  music.qNote(g, gShh)

  #m31
  music.qNote(bF, bFShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  music.qNote(g, gShh)

  #m32
  music.qNote(bF, bFShh)
  music.eNote(a, aShh)
  music.eNote(bF, bFShh)
  music.qNote(g, gShh)

  #m33
  music.dHalfNote(g, gShh)

def bass():
  #m1
  music.dHalfNote(g, gShh)

  #m2
  music.dHalfNote(F, FShh)

  #m3
  music.dHalfNote(eF, eFShh)

  #m4
  music.dHalfNote(D, DShh)

  #m5
  music.dHalfNote(g, gShh)

  #m6
  music.dHalfNote(F, FShh)

  #m7
  music.dHalfNote(eF, eFShh)

  #m8
  music.dHalfNote(D, DShh)

  #m9
  music.dHalfNote(C, CShh)

  #m10
  music.dHalfNote(D, DShh)

  #m11
  music.dHalfNote(C, CShh)

  #m12
  music.dHalfNote(D, DShh)
  
  #m13
  music.dHalfNote(D, DShh)

  #m14
  music.dHalfNote(e, eShh)

  #m15
  music.dHalfNote(F, FShh)

  #m16
  music.qNote(e, eShh)
  music.qNote(eF, eFShh)
  music.qNote(D, DShh)

  #m17
  music.dHalfNote(D, DShh)

  #m18
  music.dHalfNote(bF, bFShh)

  #m19
  music.dHalfNote(bF, bFShh)

  #m20
  music.dHalfNote(bF, bFShh)
  
  #m21
  music.dHalfNote(fS, fSShh)

  #m22
  music.hNote(a, aShh)
  music.qNote(g, gShh)

  #m23
  music.dHalfNote(fS, fSShh)

  #m24
  music.hNote(a, aShh)
  music.qNote(g, gShh)

  #m25
  music.dHalfNote(g, gShh)

  #m26
  music.dHalfNote(g, gShh)

  #m27
  music.dHalfNote(g, gShh)

  #m28
  music.dHalfNote(g, gShh)

  #m29
  music.dHalfNote(g, gShh)

  #m30
  music.dHalfNote(g, gShh)

  #m31
  music.dHalfNote(g, gShh)

  #m32
  music.dHalfNote(g, gShh)

  #m33
  music.dHalfNote(g, gShh)

# Setting up threads and starting them
high = threading.Thread(target=melody)
high.start()

low = threading.Thread(target=bass)
low.start()

high.join()
low.join()