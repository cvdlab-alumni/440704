from pyplasm import *

vertici = [[0,0],[43.6,0],[43.6,20],[0,20]]
celle = [[1,2,3,4]]
base =  MKPOL([vertici,celle,None])
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

scalini = (COLOR(YELLOW)) (SKELETON(1)(STRUCT([scalino1,scalino2,scalino3,scalino4,scalino5,scalino6,scalino7,
	scalino8,scalino9,scalino10,scalino11,scalino12])))

base2 = T([1,2])([9.6,1.2])(CUBOID([32.8,17.6]))

#VIEW(SKELETON(1)(STRUCT([base,base2,scalino1,scalino2,scalino3,scalino4,scalino5,scalino6,scalino7,
	#scalino8,scalino9,scalino10,scalino11,scalino12])))



plinto =  CUBOID([2.8,2.8])
xPlinti1 = T([1,2])([9.6,1.2])(STRUCT([plinto,T(1)(4.8)]*7)) 
xPlinti2 = T([1,2])([9.6,16])(STRUCT([plinto,T(1)(4.8)]*7))

yPlinto1porta = T([1,2])([9.6,5.6])(plinto)
yPlinto2porta = T([1,2])([9.6,11.6])(plinto)
yPlinti2 = T([1,2])([38.4,1.2])(STRUCT([plinto,T(2)(4.8)]*3))

plinti = (COLOR(RED)) (SKELETON(1)(STRUCT([xPlinti1,xPlinti2,yPlinto1porta,yPlinto2porta,yPlinti2])))

colonna = CYLINDER([1,0]) (20)
#VIEW(colonna)

colonnex1 = T([1,2])([11,2.6])(STRUCT([colonna,T(1)(4.8)]*7))
colonnex2 = T([1,2])([11,17.4])(STRUCT([colonna,T(1)(4.8)]*7))

ycolonna1porta = T([1,2])([11,7])(colonna)
ycolonna2porta = T([1,2])([11,13])(colonna)
colonney2 = T([1,2])([39.8,7.4])(STRUCT([colonna,T(2)(4.8)]*2))

colonne = (COLOR(BLUE)) (SKELETON(1)(STRUCT([colonnex1,colonnex2,ycolonna1porta,ycolonna2porta,colonney2])))

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

baseGiustaColorata = (COLOR(GREEN)) (SKELETON(1)(STRUCT([baseGiusta])))




baseIntorno = T([1,2])([9.6,0.6]) (CUBOID([33.4,18.6]))


baseIntornoVera = DIFFERENCE([baseIntorno, base2])

baseIntornoVeraColorata = (COLOR(YELLOW)) (SKELETON(1)(STRUCT([baseIntornoVera])))



VIEW(baseIntorno)
VIEW(baseIntornoVera)







#baseGiustaAlt = PROD([baseGiusta, Q(5)])

#VIEW(colonnex1)
#VIEW(baseGiustaAlt)
#VIEW(STRUCT([colonnex1,baseGiustaAlt]))


VIEW((STRUCT([scalini,plinti,colonne,baseGiustaColorata,baseIntornoVeraColorata])))

#VIEW(STRUCT([baseGiusta]))

#VIEW((STRUCT([baseCCcompleta,colonney2,ycolonna1porta, ycolonna2porta, colonnex1,colonnex2,xPlinti1,xPlinti2,yPlinto1porta,yPlinto2porta,yPlinti2,base,base2,scalino1,scalino2,scalino3,scalino4,scalino5,scalino6,scalino7,
	#scalino8,scalino9,scalino10,scalino11,scalino12])))

























