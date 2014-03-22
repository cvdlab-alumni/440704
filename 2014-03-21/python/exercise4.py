from pyplasm import *

scalino = CUBOID([1,10])



scalino1 = T([1,2])([2,3])(scalino) 
scalino2 = T([1,2])([3,3])(scalino)
scalino3 = T([1,2])([4,3])(scalino)
scalino4 = T([1,2])([5,3])(scalino)
scalino5 = T([1,2])([6,3])(scalino)
scalino6 = T([1,2])([7,3])(scalino)
scalino7 = T([1,2])([8,3])(scalino)
scalino8 = T([1,2])([9,3])(scalino)
scalino9 = T([1,2])([10,3])(scalino)
scalino10 = T([1,2])([11,3])(scalino)

scalino1 = PROD([scalino1,Q(0.6)])
scalino2 = PROD([scalino2,Q(1.2)])
scalino3 = PROD([scalino3,Q(1.8)])
scalino4 = PROD([scalino4,Q(2.4)])
scalino5 = PROD([scalino5,Q(3)])
scalino6 = PROD([scalino6,Q(3.6)])
scalino7 = PROD([scalino7,Q(4.2)])
scalino8 = PROD([scalino8,Q(4.8)])
scalino9 = PROD([scalino9,Q(5.4)])
scalino10 = PROD([scalino10,Q(6)])



scalini = (COLOR([1,0.54,0.41])) (STRUCT([scalino1,scalino2,scalino3,scalino4,scalino5,scalino6,scalino7,
	scalino8,scalino9,scalino10]))

corridoio = CUBOID([5,10,6])
corridoioNew = (COLOR([1,0.38,0.27])) (T([1,2])([12,3])(corridoio))

scalinoNuovo = (COLOR([1,0.54,0.41]))(T([1,2,3])([17,3,6]) (CUBOID([1,10,0.6])))
prova = [T([1,3])([1,0.5]),scalinoNuovo]
scalaNuova = ((STRUCT(NN(5)(prova))))



VIEW(STRUCT([scalinoNuovo,corridoioNew,scalini,scalaNuova]))

