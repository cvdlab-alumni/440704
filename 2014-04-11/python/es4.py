#esercizio 4 per il completamento dell'esercizio 3




from pyplasm import *


vertici = [[9.6,0],[43.6,0],[43.6,20],[9.6,20]]
celle = [[1,2,3,4]]
base =  MKPOL([vertici,celle,None])



base = (COLOR([0.76,0.69,0.57])) (STRUCT([PROD([base,Q(7.2)])]))



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




scalini = (COLOR([1,0.64,0])) (STRUCT([scalino1,scalino2,scalino3,scalino4,scalino5,scalino6,scalino7,
	scalino8,scalino9,scalino10,scalino11,scalino12]))



base2 = T([1,2])([9.6,1.2])(CUBOID([31.6,17.6]))




plinto =  CUBOID([2.8,2.8,0.6])
xPlinti1 = T([1,2,3])([9.6,1.2,7.2])(STRUCT([plinto,T(1)(4.8)]*7)) 
xPlinti2 = T([1,2,3])([9.6,16,7.2])(STRUCT([plinto,T(1)(4.8)]*7))

yPlinto1porta = T([1,2,3])([9.6,5.6,7.2])(plinto)
yPlinto2porta = T([1,2,3])([9.6,11.6,7.2])(plinto)
yPlinti2 = T([1,2,3])([38.4,1.2,7.2])(STRUCT([plinto,T(2)(4.8)]*3))


plinti = (COLOR([1,0.49,0.31])) (STRUCT([xPlinti1,xPlinti2,yPlinto1porta,yPlinto2porta,yPlinti2]))

colonna = CYLINDER([1,13]) (20)


colonnex1 = T([1,2,3])([11,2.6,7.8])(STRUCT([colonna,T(1)(4.8)]*7))
colonnex2 = T([1,2,3])([11,17.4,7.8])(STRUCT([colonna,T(1)(4.8)]*7))

ycolonna1porta = T([1,2,3])([11,7,7.8])(colonna)
ycolonna2porta = T([1,2,3])([11,13,7.8])(colonna)
colonney2 = T([1,2,3])([39.8,7.4,7.8])(STRUCT([colonna,T(2)(4.8)]*2))

colonne = (COLOR([1, 0.38, 0.27])) (STRUCT([colonnex1,colonnex2,ycolonna1porta,ycolonna2porta,colonney2]))

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


baseGiusta = DIFFERENCE([baseQuasiGiusta, rettangolino])



baseGiusta = PROD([baseGiusta,Q(13.6)])

baseGiusta = T(3)(7.2)(baseGiusta)

baseGiustaColorata = (COLOR([1,0.64,0])) (STRUCT([baseGiusta]))




baseIntorno = T(1)(9.6)(CUBOID([34,20]))


baseIntornoVera = DIFFERENCE([baseIntorno, base2])

baseIntornoVera = PROD([baseIntornoVera,Q(7.2)])

baseIntornoVeraColorata = (COLOR([0.76,0.69,0.57])) (STRUCT([baseIntornoVera]))





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


tettoPunta = (COLOR([0.76,0.69,0.57])) (STRUCT([provaTettoCompleto,tettoAlto]))



porta = T([1,2,3])([20.6,7.8,7.2])(CUBOID([1.6,4.4,13.6]))
portaColorata = (COLOR([0.80,0.52,0.24]))(STRUCT([porta]))



tempioDiPortuno = STRUCT([base,portaColorata,tettoPunta,scalini,plinti,colonne,baseGiustaColorata,baseIntornoVeraColorata])

#Da qui gli edifici

pianoGenerale1 = COLOR([0.01,0.75,0.23]) (CUBOID([500,500]))
pianoGenerale2 = COLOR([0.01,0.75,0,23]) (CUBOID([500,-100]))
pianoGenerale3 = COLOR([0.01,0.75,0,23]) (CUBOID([-500,-100]))
pianoGenerale4 = COLOR([0.01,0.75,0,23]) (CUBOID([-500,500]))

edificio1 = COLOR([0.80,0.50,0.20]) (CUBOID([24,30,35]))

finestra1 = COLOR ([0.67,0.80,0.94]) (CUBOID([4,0,7]))
finestra2 = COLOR ([0.67,0.80,0.94]) (CUBOID([0,4,7]))

finestreFrontali1 = T([1,3])([2,25])(STRUCT([finestra1,T(1)(8)]*3))
finestreFrontali2 = T([1,3])([2,15])(STRUCT([finestra1,T(1)(8)]*3))
finestreLateraliS1 = T([2,3])([4,25])(STRUCT([finestra2,T(2)(6)]*4))
finestreLateraliS2 = T([2,3])([4,15])(STRUCT([finestra2,T(2)(6)]*4))
finestreLateraliD1 = T([1,2,3])([24,4,25])(STRUCT([finestra2,T(2)(6)]*4))
finestreLateraliD2 = T([1,2,3])([24,4,15])(STRUCT([finestra2,T(2)(6)]*4))
finestreDietro1 = T([1,2,3])([2,30,25])(STRUCT([finestra1,T(1)(8)]*3))
finestreDietro2 = T([1,2,3])([2,30,15])(STRUCT([finestra1,T(1)(8)]*3))

porta = COLOR([0.80,0.52,0.25]) (CUBOID([5,0,8]))
portone1 = T(1)(10)(porta)

palazzo = STRUCT([edificio1,finestreFrontali1,finestreFrontali2,finestreLateraliS1,finestreLateraliS2,finestreLateraliD1,
		finestreLateraliD2,finestreDietro1,finestreDietro2,portone1])



palazzoRuotato = R([1,2])(PI)(palazzo)

edificiDestra = T([1,2])([-76,-40])(STRUCT([palazzoRuotato,T(1)(-50)]*8))

edificiSinistra = T([1,2])([-100,70])(STRUCT([palazzo,T(1)(-50)]*8))


strada1 = COLOR(BROWN) (CUBOID([450,75]))
stradaPrincipale = T([1,2])([-500,-25])(strada1)

strada2  = COLOR(BROWN)(CUBOID([200,15]))
stradaPiccolaS = T([1,2])([-50,35])(strada2)
stradaPiccolaD = T([1,2])([-50,-25])(strada2)

stradaCongiunta = COLOR(BROWN)(CUBOID([15,150]))
stradaCongiuntaT = T([1,2])([150,-25])(stradaCongiunta)

stradaFinale = COLOR(BROWN)(CUBOID([350,20]))
stradaFinaleT = T([1,2])([150,105])(stradaFinale)


primoBlocco = COLOR([0.82,0.41,0.12])(CUBOID([40,50,90]))
secondoBlocco = COLOR([0.82,0.41,0.12])(CUBOID([20,30,60]))

primoBloccoT = T([1,2])([200,-15])(primoBlocco)
secondoBloccoT = T([1,2,3])([210,-5,90])(secondoBlocco)

punto = (MK)([220,10,200])

punta = COLOR([0.82,0.41,0.12])(JOIN([secondoBloccoT,punto]))

vetrate = COLOR([1,0.75,0])(CUBOID([0,50,10]))
vetrateT = T([1,2,3])([200,-15,70]) (vetrate)

#orologio
background = COLOR([1,0.75,0])(CIRCLE(10)([48,1]))
minute = T([1,2])([-0.05,-0.05])(CUBOID([9,1])) 
hour = T([1,2])([-0.1,-0.1])(CUBOID([7,2])) 
tick = T([1,2])([-1,8])(CUBOID([0.5,1])) 
ticks = STRUCT(NN(12)([ tick, R([1,2])(PI/6) ]))

def clock2D (h,m):
		return STRUCT ([ background , ticks , R([1,2])( PI/2 - (h + m/60)*PI/6 )(hour), R([1,2])( PI/2 - m*PI/30 )(minute) ])

def clock3D (h,m): 
	return STRUCT ([
COLOR([1,0.75,0])(PROD([ background , Q(2) ])),
T(3)(2.)(PROD([ ticks, Q(0.5) ])), T(3)(2),
R([1,2])( PI/2 - (h + m/60.)*PI/6 )(PROD([ hour, Q(0.3) ])),
T(3)(0.3),
R([1,2])( PI/2 - m*PI/30 )(PROD([ minute, Q(0.3) ])) ])

orologio = clock3D(5,20)


orologioRuotato = R([1,3])(PI/2)(orologio)


orologioTraslato = T([1,2,3])([210,10,130])(orologioRuotato)

cancello = COLOR([0.60,0.46,0.33])(CUBOID([0,20,40]))
cancelloTraslato = T(1)(200)(cancello)



baseCasa = CUBOID([100,40,40])
pianoSopra = CUBOID([100,40,2])
porta = COLOR([0.85,0.74,0.67])(CUBOID([20,0,14]))
portaT = T([1,2])([345,50])(porta)
finestrella = COLOR([0.67,0.80,0.94])(CUBOID([40,0,10]))
finestrellaT = T([1,2,3])([335,50,25])(finestrella)

baseCasaT = COLOR([1,0.84,0])(T ([1,2])([300,10])(baseCasa))
pianoSopraT = T ([1,2,3])([300,10,40])(pianoSopra)

puntoAlto = (MK) ([350,30,60])
costruzione = STRUCT([baseCasaT,portaT,finestrellaT])
costruzioneTetto = COLOR([0.75,0.25,0])(JOIN([puntoAlto,pianoSopraT]))


nuovoTempioDiPortuno = T(2)(-5) (S([1,2,3])([1.7,1.7,1.7])(tempioDiPortuno))

#fiume

fiume = COLOR([0,0.5,1])(CUBOID([100,200]))
fiumeT = T([1,2])([-500,300])(fiume)
fiume2 = COLOR([0,0.5,1])(CUBOID([500,50]))
fiume2T = T([1,2])([-500,300])(fiume2)
fiume3 = COLOR([0,0.5,1])(CUBOID([50,100]))
fiume3T = T([1,2])([0,250])(fiume3)
fiume4 = COLOR([0,0.5,1])(CUBOID([500,50]))
fiume4T = T([1,2])([0,200])(fiume4)

fiumeCompleto = STRUCT([fiumeT,fiume2T,fiume3T,fiume4T])

sentiero = COLOR([0.82,0.70,0.55])(CUBOID([2,20]))
sentieri = T([1,2])([-88,50])(STRUCT([sentiero,T(1)(-50)]*8))
sentieri2 = T([1,2])([-88,-45])(STRUCT([sentiero,T(1)(-50)]*8))
sentieroTempio = T([1,2])([-50,11])(CUBOID([75,2]))
sentieroBingBang = T([1,2])([165,11])(CUBOID([35,2]))
sentieroEdificio = T([1,2])([353,50])(CUBOID([2,55]))

tuttiSentieri = STRUCT([sentieri,sentieri2,sentieroTempio,sentieroBingBang,sentieroEdificio])



#DA QUI SI COMINCIANO AD INSERIRE NUOVI OGGETTI

troncoAbete = COLOR([0.4,0.26,0.13])(CYLINDER([2,22])(50))
circonferenza = JOIN(AA(MK)(CIRCLE_POINTS(8,60)))
circonferenzaT = T(3)(10)(circonferenza)
puntoAbete = (MK)([0,0,30])
chiomaAbete = COLOR([0.09,0.45,0.27])(JOIN([circonferenzaT,puntoAbete]))
abete = STRUCT([chiomaAbete,troncoAbete])



chioma = COLOR([0.33,0.4,0.2])(T(3)(17.9)(SPHERE(8)([60,60])))
tronco = COLOR([0.4,0.26,0.13])(CYLINDER([2,18])(50))

albero = STRUCT([tronco,chioma])
alberi = T([1,2])([-495,180])(STRUCT([albero,T(2)(40)]*4))
alberi4 = T([1,2])([-495,180])(STRUCT([albero,T(1)(30)]*33))
alberi6 = T([1,2])([-495,220])(STRUCT([albero,T(1)(30)]*17))
alberi8 = T([1,2])([-495,260])(STRUCT([albero,T(1)(30)]*17))
alberi10 = T([1,2])([-495,300])(STRUCT([albero,T(1)(30)]*17))

alberiConfine1 = T([1,2])([-400,355])(STRUCT([albero,T(2)(30)]*5))
abeti1 = T([1,2])([-400,385])(STRUCT([abete,T(1)(33)]*14))
abeti2 = T([1,2])([-400,415])(STRUCT([abete,T(1)(33)]*14))
abeti3 = T([1,2])([-400,445])(STRUCT([abete,T(1)(33)]*14))
abeti4 = T([1,2])([-400,475])(STRUCT([abete,T(1)(33)]*14))
alberoConfine2 = T([1,2])([-400,355])(STRUCT([albero,T(1)(33)]*14))
alberoConfine3 = T([1,2])([55,350])(STRUCT([albero,T(2)(-30)]*4))
alberoConfine4 = T([1,2])([55,260])(STRUCT([albero,T(1)(30)]*15))





tuttiAlberi = STRUCT([alberi,alberi4,alberi6,alberi8,alberi10,alberiConfine1,alberoConfine2,alberoConfine3,alberoConfine4,abeti1,
				abeti2,abeti3,abeti4])

luce = COLOR([1,1,0])(T(3)(9.9)(SPHERE(1.5)([60,60])))
palo = COLOR([0.58,0.58,0.58])(CYLINDER([0.5,10])(50))

lampioncino = STRUCT([luce,palo])
lampioncini1 = T(2)(55)(STRUCT([lampioncino,T(1)(20)]*8))
lampioncini2 = T([1,2])([140,55])(STRUCT([lampioncino,T(2)(20)]*5))
lampioncini3 = T([1,2])([140,135])(STRUCT([lampioncino,T(1)(30)]*12))
lampioncini4 = T(2)(-30)(STRUCT([lampioncino,T(1)(20)]*9))
lampioncini5 = T([1,2])([170,100])(STRUCT([lampioncino,T(1)(30)]*11))
lampioncini6 = T([1,2])([170,100])(STRUCT([lampioncino,T(2)(-20)]*3))
tuttiLampioncini = STRUCT([lampioncini1,lampioncini2,lampioncini3,lampioncini4,lampioncini5,lampioncini6])


paloLampione = CYLINDER([0.5,20])(50)
paloTrasverso = CYLINDER([0.5,5])(50)
paloTrasversoR = R([1,3])(PI/6)(paloTrasverso)
paloTrasversoRT = T(3)(18)(paloTrasversoR)
pezzoLuce = CUBOID([4,1,1])
lucetta = COLOR(YELLOW)(CUBOID([4,1,0.5]))
luceT = T ([1,2,3]) ([-6,-0.5,20.5]) (lucetta)
pezzoLuceT = T([1,2,3])([-6,-0.5,21])(pezzoLuce)


lampione = STRUCT([paloLampione,paloTrasversoRT,pezzoLuceT,luceT])
lampioneFinale1 = R([1,2])(PI/2)(lampione)

lampioni1 = T([1,2])([-100,50])(STRUCT([lampioneFinale1,T(1)(-50)]*8))
lampioneFinale2 = R([1,2])(PI*3/2)(lampione)

lampioni2 = T([1,2])([-100,-25])(STRUCT([lampioneFinale2,T(1)(-50)]*8))

tuttiLampioni = STRUCT([lampioni1,lampioni2])




gamba1 = CUBOID([6,2,3])
gamba2 = T(2)(10)(CUBOID([6,2,3]))
base = T(3)(3)(CUBOID([6,12,1]))
schienale = T(3)(4)(CUBOID([1,12,5]))

panchina = STRUCT([gamba1,gamba2,base,schienale])
panchinaPiccola = S([1,2,3])([0.5,0.5,0.5])(panchina)



panchinaPiazzata = T([1,2])([-450,150])(STRUCT([panchinaPiccola,T(2)(-30)]*2))
panchine1 = T([1,2])([-450,120])(STRUCT([panchinaPiccola,T(1)(50)]*8))
panchine2 = T([1,2])([-450,150])(STRUCT([panchinaPiccola,T(1)(50)]*8))








VIEW(STRUCT([pianoGenerale1,pianoGenerale2,pianoGenerale3,pianoGenerale4,
		nuovoTempioDiPortuno,edificiDestra,edificiSinistra,stradaPrincipale,stradaPiccolaS,stradaPiccolaD,
		primoBloccoT,secondoBloccoT,punta,vetrateT,orologioTraslato,cancelloTraslato,stradaCongiuntaT,stradaFinaleT,
		costruzioneTetto,costruzione,fiumeCompleto,tuttiSentieri,
		tuttiAlberi,tuttiLampioncini,tuttiLampioni,panchinaPiazzata,panchine1,panchine2]))






















