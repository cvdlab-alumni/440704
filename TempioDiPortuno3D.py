from pyplasm import *

vertici = [[9.6,0],[43.6,0],[43.6,20],[9.6,20]]
celle = [[1,2,3,4]]
base =  MKPOL([vertici,celle,None])

#base = (COLOR(ORANGE)) (SKELETON(1)(STRUCT([PROD([base,Q(7.2)])])))

base = (COLOR(ORANGE)) (STRUCT([PROD([base,Q(7.2)])]))


#VIEW(base)
#VIEW(SKELETON(1)(base))

scalino = CUBOID([0.6,14.8])

scalino1 = T([1,2])([2.4,2.8])(scalino) 
scalino2 = T([1,2])([3,2.8])(scalino)
scalino3 = T([1,2])([3.6,2.8])(scalino)
scalino4 = T([1,2])([4.2,2.8])(scalino)
scalino5 = T([1,2])([4.8,2.8])(scalino)
scalino6 = T([1,2])([5.4,2.8])(scalino)
scalino7 = T([1,2])([6,2.8])(scalino)
scalino8 = T([1,2])([6.6,2.8])(scalino)
scalino9 = T([1,2])([7.2,2.8])(scalino)
scalino10 = T([1,2])([7.8,2.8])(scalino)
scalino11 = T([1,2])([8.4,2.8])(scalino)
scalino12 = T([1,2])([9,2.8])(scalino)

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
scalino11 = PROD([scalino11,Q(6.6)])
scalino12 = PROD([scalino12,Q(7.2)])




#scalini = (COLOR(YELLOW)) (SKELETON(1)(STRUCT([scalino1,scalino2,scalino3,scalino4,scalino5,scalino6,scalino7,
	#scalino8,scalino9,scalino10,scalino11,scalino12])))

scalini = (COLOR(YELLOW)) (STRUCT([scalino1,scalino2,scalino3,scalino4,scalino5,scalino6,scalino7,
	scalino8,scalino9,scalino10,scalino11,scalino12]))



base2 = T([1,2])([9.6,1.2])(CUBOID([32.8,17.6]))

#VIEW(SKELETON(1)(STRUCT([base,base2,scalino1,scalino2,scalino3,scalino4,scalino5,scalino6,scalino7,
	#scalino8,scalino9,scalino10,scalino11,scalino12])))



plinto =  CUBOID([2.8,2.8,0.6])
xPlinti1 = T([1,2,3])([9.6,1.2,7.2])(STRUCT([plinto,T(1)(4.8)]*7)) 
xPlinti2 = T([1,2,3])([9.6,16,7.2])(STRUCT([plinto,T(1)(4.8)]*7))

yPlinto1porta = T([1,2,3])([9.6,5.6,7.2])(plinto)
yPlinto2porta = T([1,2,3])([9.6,11.6,7.2])(plinto)
yPlinti2 = T([1,2,3])([38.4,1.2,7.2])(STRUCT([plinto,T(2)(4.8)]*3))



#plinti = (COLOR(RED)) (SKELETON(1)(STRUCT([xPlinti1,xPlinti2,yPlinto1porta,yPlinto2porta,yPlinti2])))
plinti = (COLOR(RED)) (STRUCT([xPlinti1,xPlinti2,yPlinto1porta,yPlinto2porta,yPlinti2]))

colonna = CYLINDER([1,13]) (20)
#VIEW(colonna)

colonnex1 = T([1,2,3])([11,2.6,7.8])(STRUCT([colonna,T(1)(4.8)]*7))
colonnex2 = T([1,2,3])([11,17.4,7.8])(STRUCT([colonna,T(1)(4.8)]*7))

ycolonna1porta = T([1,2,3])([11,7,7.8])(colonna)
ycolonna2porta = T([1,2,3])([11,13,7.8])(colonna)
colonney2 = T([1,2,3])([39.8,7.4,7.8])(STRUCT([colonna,T(2)(4.8)]*2))

#colonne = (COLOR(BLUE)) (SKELETON(1)(STRUCT([colonnex1,colonnex2,ycolonna1porta,ycolonna2porta,colonney2])))
colonne = (COLOR(BLUE)) (STRUCT([colonnex1,colonnex2,ycolonna1porta,ycolonna2porta,colonney2]))

verticiCCcompleta = [[20.6,2.6],[39.8,2.6],[39.8,17.4],[20.6,17.4]]
celleCCcompleta = [[1,2,3,4]]
baseCCcompleta = MKPOL([verticiCCcompleta,celleCCcompleta,None])

verticiCCdentro = [[22.2,4.2],[38.2,4.2],[38.2,15.8],[22.2,15.8]]
celleCCdentro = [[1,2,3,4]]
baseCCdentro = MKPOL([verticiCCdentro,celleCCdentro,None])

baseQuasiGiusta = DIFFERENCE([baseCCcompleta,baseCCdentro])


verticiRet = [[20.6,7.8],[22.2,7.8],[22.2,12.2],[20.6,12.2]]
celleRet = [[1,2,3,4]]
rettangolino = MKPOL([verticiRet, celleRet,None])

#VIEW(rettangolino)

baseGiusta = DIFFERENCE([baseQuasiGiusta, rettangolino])



baseGiusta = PROD([baseGiusta,Q(13.6)])

baseGiusta = T(3)(7.2)(baseGiusta)

#baseGiustaColorata = (COLOR(GREEN)) (SKELETON(1)(STRUCT([baseGiusta])))
baseGiustaColorata = (COLOR(GREEN)) (STRUCT([baseGiusta]))




baseIntorno = T(1)(9.6)(CUBOID([34,20]))


baseIntornoVera = DIFFERENCE([baseIntorno, base2])

baseIntornoVera = PROD([baseIntornoVera,Q(7.2)])

#baseIntornoVeraColorata = (COLOR(YELLOW)) (SKELETON(1)(STRUCT([baseIntornoVera])))
baseIntornoVeraColorata = (COLOR(WHITE)) (STRUCT([baseIntornoVera]))



VIEW(baseIntorno)
VIEW(baseIntornoVera)


tetto = CUBOID([31.6,17.6,3])
tettoAlto = T([1,2,3])([9.6,1.2,20.8])(tetto) #come la base2


#punti al centro alti
a = (MK)([9.6,10,8]) 
b = (MK)([41.2,10,8])

#punti esterni
c = (MK) ([9.6,0.6,2.8])
d = (MK) ([9.6,19.4,2.8])

e = (MK) ([41.2,0.6,2.8])
f = (MK) ([41.2,19.4,2.8])

provaTettoCompleto = JOIN([a,b,c,d,e,f])

provaTettoCompleto = T(3)(20.8)(provaTettoCompleto)

VIEW(STRUCT([provaTettoCompleto,tettoAlto]))

#tettoPunta = (COLOR(PURPLE)) (SKELETON(1)(STRUCT([provaTettoCompleto,tettoAlto])))
tettoPunta = (COLOR(PURPLE)) (STRUCT([provaTettoCompleto,tettoAlto]))

#proviamo la porta

porta = T([1,2,3])([20.6,7.8,7.2])(CUBOID([1.6,4.4,13.6]))

#portaColorata = (COLOR(BROWN))(SKELETON(1)(STRUCT([porta])))
portaColorata = (COLOR(BROWN))(STRUCT([porta]))









#baseGiustaAlt = PROD([baseGiusta, Q(5)])

#VIEW(colonnex1)
#VIEW(baseGiustaAlt)
#VIEW(STRUCT([colonnex1,baseGiustaAlt]))


VIEW((STRUCT([base,portaColorata,tettoPunta,scalini,plinti,colonne,baseGiustaColorata,baseIntornoVeraColorata])))
#VIEW(STRUCT([baseGiusta]))

#VIEW((STRUCT([baseCCcompleta,colonney2,ycolonna1porta, ycolonna2porta, colonnex1,colonnex2,xPlinti1,xPlinti2,yPlinto1porta,yPlinto2porta,yPlinti2,base,base2,scalino1,scalino2,scalino3,scalino4,scalino5,scalino6,scalino7,
	#scalino8,scalino9,scalino10,scalino11,scalino12])))
