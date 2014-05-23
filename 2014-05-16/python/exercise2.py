from pyplasm import *
from lar_cc import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])

def trasparente(oggetto):
    return MATERIAL([1,1,1,0.1, 0,0,0.8,0.5, 1,1,1,0.1, 1,1,1,0.1, 100])(oggetto)

master = assemblyDiagramInit([9,9,2])([[0.3,3.5,0.1,4,0.1,2.5,0.1,2,0.3],[0.3,1.7,0.1,1.7,0.1,0.7,0.1,1.7,0.3],[.3,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,.5)
#VIEW(hpc)

toRemove = [21,25,29,33,67,65,69,61,59,57,105,141,97,133,93,111,129,31,63,79,115,99,43,83,81,101,99,119,117,137,135]
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
#DRAW(master)

#per fare la porta

#cella della porta
toMerge = 49

diagram = assemblyDiagramInit([3,1,2])([[1.5,1,1.5],[.3],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.5)
#VIEW(hpc)

toRemove = [133]
master = master[0], [cell for k,cell in enumerate(master[1]) if not(k in toRemove)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.5)
#VIEW(hpc)

#finestre
#cella della finestra
#finesra principale
toMerge = 57
diagram = assemblyDiagramInit([3,1,3])([[0.5,3,0.5],[0.3],[0.3,2,0.4]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.5)
#VIEW(hpc)


#############prova per colorare la finestra principale
toRemove = [139,138]
master2 = master[0], [cell for k,cell in enumerate(master[1]) if (k in toRemove)]
hpc2 = trasparente((STRUCT(MKPOLS(master2))))
#VIEW(hpc2)
#############


toRemove = [139]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)


#Da qui le altre finestre
#sinistra
toMerge = 30
diagram = assemblyDiagramInit([3,1,3])([[0.4,0.4,0.4],[0.3],[1.3,0.8,0.6]])#modifico
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.5)
#VIEW(hpc)
toRemove = [146]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

#destra

toMerge = 83
diagram = assemblyDiagramInit([3,1,3])([[0.4,0.4,0.4],[0.3],[1.3,0.8,0.6]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.5)
#VIEW(hpc)
toRemove = [153]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

#destra destra
toMerge = 109
diagram = assemblyDiagramInit([3,1,3])([[0.4,0.4,0.4],[0.3],[1.3,0.8,0.6]]) #modifico qui
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.5)
#VIEW(hpc)
toRemove = [160]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

#MISURE DELLE PORTE

#in basso a sinistra
toMerge = 22

diagram = assemblyDiagramInit([3,1,2])([[2,1,.5],[.3],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.5)
#VIEW(hpc)
toRemove = [165]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

#in alto a sinistra
toMerge = 24

diagram = assemblyDiagramInit([3,1,2])([[0.5,1,2],[.3],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.5)
#VIEW(hpc)
toRemove = [169]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

#in basso a destra
toMerge = 73

diagram = assemblyDiagramInit([3,1,2])([[0.5,1,2],[.3],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.5)
#VIEW(hpc)
toRemove = [173]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

#in alto a destra
toMerge = 77

diagram = assemblyDiagramInit([3,1,2])([[0.5,1,2],[.3],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.5)
#VIEW(hpc)
toRemove = [177]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

#in alto a destra destra
toMerge = 102

diagram = assemblyDiagramInit([3,1,2])([[0.5,1,1.5],[.3],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.5)
#VIEW(hpc)

toRemove = [181]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

#effetto trasparente
hpc = STRUCT(MKPOLS(master))
VIEW(STRUCT([hpc,hpc2]))






# Da qui l'esercizio 2

appartamenti = assemblyDiagramInit([2,4,4])([2*[12.9],[1.5,4.7,1.5,4.7],4*[3.2]])
V,CV = appartamenti
hpc = SKEL_1(STRUCT(MKPOLS(appartamenti)))
hpc = cellNumbering (appartamenti,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)


master2 = larApply(r(0,0,PI*2))(master)
appartamenti = diagram2cell(master2,appartamenti,4)
appartamenti = diagram2cell(master2,appartamenti,4)
appartamenti = diagram2cell(master2,appartamenti,4)
appartamenti = diagram2cell(master2,appartamenti,4)
appartamenti = diagram2cell(master,appartamenti,8)
appartamenti = diagram2cell(master,appartamenti,8)
appartamenti = diagram2cell(master,appartamenti,8)
appartamenti = diagram2cell(master,appartamenti,8)
master3 = larApply(r(0,0,PI*2))(master)
appartamenti = diagram2cell(master3,appartamenti,12)
appartamenti = diagram2cell(master3,appartamenti,12)
appartamenti = diagram2cell(master3,appartamenti,12)
appartamenti = diagram2cell(master3,appartamenti,12)
appartamenti = diagram2cell(master,appartamenti,16)
appartamenti = diagram2cell(master,appartamenti,16)
appartamenti = diagram2cell(master,appartamenti,16)
appartamenti = diagram2cell(master,appartamenti,16)

toRemove = [0]
appartamenti = appartamenti[0], [cell for k,cell in enumerate(appartamenti[1]) if not (k in toRemove)]
toRemove = [0]
appartamenti = appartamenti[0], [cell for k,cell in enumerate(appartamenti[1]) if not (k in toRemove)]
toRemove = [0]
appartamenti = appartamenti[0], [cell for k,cell in enumerate(appartamenti[1]) if not (k in toRemove)]
toRemove = [0]
appartamenti = appartamenti[0], [cell for k,cell in enumerate(appartamenti[1]) if not (k in toRemove)]
toRemove = [0]
appartamenti = appartamenti[0], [cell for k,cell in enumerate(appartamenti[1]) if not (k in toRemove)]
toRemove = [0]
appartamenti = appartamenti[0], [cell for k,cell in enumerate(appartamenti[1]) if not (k in toRemove)]
toRemove = [0]
appartamenti = appartamenti[0], [cell for k,cell in enumerate(appartamenti[1]) if not (k in toRemove)]
toRemove = [0]
appartamenti = appartamenti[0], [cell for k,cell in enumerate(appartamenti[1]) if not (k in toRemove)]
toRemove = [0]
appartamenti = appartamenti[0], [cell for k,cell in enumerate(appartamenti[1]) if not (k in toRemove)]
toRemove = [0]
appartamenti = appartamenti[0], [cell for k,cell in enumerate(appartamenti[1]) if not (k in toRemove)]
toRemove = [0]
appartamenti = appartamenti[0], [cell for k,cell in enumerate(appartamenti[1]) if not (k in toRemove)]
toRemove = [0]
appartamenti = appartamenti[0], [cell for k,cell in enumerate(appartamenti[1]) if not (k in toRemove)]
toRemove = [0]
appartamenti = appartamenti[0], [cell for k,cell in enumerate(appartamenti[1]) if not (k in toRemove)]
toRemove = [0]
appartamenti = appartamenti[0], [cell for k,cell in enumerate(appartamenti[1]) if not (k in toRemove)]
toRemove = [0]
appartamenti = appartamenti[0], [cell for k,cell in enumerate(appartamenti[1]) if not (k in toRemove)]
toRemove = [0]
appartamenti = appartamenti[0], [cell for k,cell in enumerate(appartamenti[1]) if not (k in toRemove)]


hpc = (SKEL_1(STRUCT(MKPOLS(appartamenti))))
hpc = (STRUCT(MKPOLS(appartamenti)))
hpc = cellNumbering (appartamenti,hpc)(range(len(CV)),CYAN,2)
VIEW(hpc)




#VIEW(STRUCT( MKPOLS(appartamenti) ))


hpc = STRUCT(MKPOLS(appartamenti))
appartamentiTraslatiZ = COLOR([0.9,0.86,0.51])(T(3)(5)(hpc))
#VIEW(appartamentiTraslatiZ) ALTRA VIEW


#vertici
V = [ [0,2],[25.8,2],[25.8,11],[0,11] ]

#celle-> che in questo caso sono 5: 0,1,2,3,4->indicare i vertici

FV = [ [0,1,2,3,0] ]


modelFaces = V,FV
V0 = AA(LIST)([5.,8.2,11.4,14.6])
C0V = AA(LIST)(range(4))

modelFloor = V0,C0V

mod1D = larModelProduct([modelFaces,modelFloor])

corridoi = COLOR([0.6,0.46,0.33])(EXPLODE(1,1,1)(MKPOLS(mod1D)))

#VIEW(corridoi)

#VIEW(STRUCT([appartamentiTraslatiZ,corridoi])) ALTRA VIEW

#parte sotto con curve

colonna = COLOR([1,0.99,0.81])(CYLINDER([1,5]) (50))

colonna1 = T([1,2])([1,2.2])(colonna)
colonna2 = T([1,2])([24.8,2.2])(colonna)
colonna3 = T([1,2])([24.8,11.2])(colonna)
colonna4 = T([1,2])([1,11.2])(colonna)

colonne = STRUCT([colonna1,colonna2,colonna3,colonna4])

#VIEW(STRUCT([appartamentiTraslatiZ,corridoi,colonne])) SECONDA VIEW





#curveBezier

dom = (POWER([INTERVALS(1)(30),INTERVALS(1)(30)]))

controlli1 = [[-3,6.5],[-3,-1],[12.9,-1],[28.8,-1],[28.8,6.5]]
bezierContorno1 = BEZIER(S1)(controlli1)
controlli2 = [[-3,6.5],[-3,14],[12.9,14],[28.8,14],[28.8,6.5]]
bezierContorno2 = BEZIER(S1)(controlli2)
contornoTot = MAP(BEZIER(S2)([bezierContorno1,bezierContorno2]))(dom)
contornoTotCol = COLOR([0.01,0.75,0.24])(contornoTot)


controls1 = [[-3,6.5,0],[6.45,4.5,0],[12.9,-1,0],[19.35,4.5,0],[28.8,6.5,0]]
bezier1 = BEZIER(S1)(controls1)

controls2 = [[-3,6.5,0],[6.45,8.5,0],[12.9,14,0],[19.35,8.5,0],[28.8,6.5,0]]
bezier2 = BEZIER(S1)(controls2)


solidoBase = MAP( BEZIER(S2)([bezier1,bezier2]))(dom)


controls3 = [[-3,6.5,1.5],[6.45,4.5,1.5],[12.9,-1,1.5],[19.35,4.5,1.5],[28.8,6.5,1.5]]
bezier3 = BEZIER(S1)(controls3)

controls4 = [[-3,6.5,1.5],[6.45,8.5,1.5],[12.9,14,1.5],[19.35,8.5,1.5],[28.8,6.5,1.5]]
bezier4 = BEZIER(S1)(controls4)

solidoAlto = MAP( BEZIER(S2)([bezier3,bezier4]))(dom)

#solidoFinale = MAP( BEZIER(S2)([solidoBase,solidoAlto]))(POWER([INTERVALS(1)(30),INTERVALS(1)(30)]))
solidoLaterale1 = MAP( BEZIER(S2)([bezier1,bezier3]))(dom)
solidoLaterale2 = MAP( BEZIER(S2)([bezier2,bezier4]))(dom)

figuraCurva = COLOR(GREEN)(STRUCT([solidoBase,solidoAlto,solidoLaterale1,solidoLaterale2]))

figuraCurva2 = R([1,2])(-PI/2)(figuraCurva)
figuraCurvaT = T([1,2])([6,19])(figuraCurva2)

#VIEW(figuraCurva) TERZA VIEW




#VIEW(solidoFinale)

#vasi
vaso = COLOR([0.94,0.86,0.51])(CYLINDER([1.5,3])(50))
vasoPerDiff = COLOR([0.4,0.26,0.15])(CYLINDER([1.2,3])(50))
vasoVero = STRUCT([vaso,vasoPerDiff])
origine = (MK)([0,0,0])
puntoO = (MK)([0.1,0.1,0])
puntoO1 = (MK)([0.1,0.15,0])
puntoCaso1 = (MK)([0.5,0,5])
puntoCaso2 = (MK)([0,0.5,5])
puntoCaso3 = (MK)([0.5,0.5,5])
puntoCaso3O = (MK)([0.56,0.56,5])
puntoCaso3O1 = (MK)([0.58,0.56,5])
puntoCaso4 = (MK)([1,0.5,5])
puntoCaso5 = (MK)([0.5,1,5])
gambo1 = JOIN([origine,puntoCaso3])
gambo2 = JOIN([puntoO,puntoCaso3O])
gambo3 = JOIN([puntoO1,puntoCaso3O1])
gambo = COLOR(GREEN)(JOIN([gambo1,gambo2,gambo3]))
fiore = COLOR(YELLOW)(JOIN(AA(MK)(CIRCLE_POINTS(0.4,60))))
fioreC = COLOR(WHITE)(JOIN(AA(MK)(CIRCLE_POINTS(0.4,60))))
fiore1 = T([1,2,3])([0.5,0,5])(fiore)
fiore2 = T([1,2,3])([0,0.5,5])(fiore)
fiore3 = T([1,2,3])([0.5,0.5,5])(fioreC)
fiore4 = T([1,2,3])([1,0.5,5])(fiore)
fiore5 = T([1,2,3])([0.5,1,5])(fiore)
contenitore = STRUCT([vasoVero,gambo,fiore1,fiore2,fiore3,fiore4,fiore5])
nuovoContenitore = S([1,2,3])([0.3,0.3,0.3])(contenitore)

contenitori1 = T([1,2,3])([0,6.5,1.5])(STRUCT([nuovoContenitore,T(1)(2)]*14))
contenitori2 = T([1,2,3])([12.5,-4.5,1.5])(STRUCT([nuovoContenitore,T(2)(2)]*5))
contenitori3 = T([1,2,3])([12.5,8.5,1.5])(STRUCT([nuovoContenitore,T(2)(2)]*5))

corridoio = CUBOID([5,10,6])
corridoioNew = (COLOR([1,0.38,0.27])) (T([1,2])([12,3])(corridoio))



#scale laterali per le entrate


W,CW = spiralStair(0.2,2,0.5,0.1,1.7,5.5,18)
scalaSpirale = (COLOR([1,0.54,0.41]))(STRUCT(MKPOLS([W,CW])))
scalaSpiraleT1 = T([1,2])([-6.5,8])(scalaSpirale)
pavimento = (COLOR([1,0.54,0.41]))(CUBOID([6.2,1.5,0.1]))
pavimentoT1 = T([1,2,3])([-6.2,6.2,5])(pavimento)
scalino = (COLOR([1,0.54,0.41]))(T([1,2,3])([-6.5,6.2,4.7])(CUBOID([0.3,1.5,0.3])))


W1,CW1 = spiralStair(0.2,2,0.5,0.1,2,3.5,18)
scalaSpirale23 = (COLOR([1,0.54,0.41]))(STRUCT(MKPOLS([W1,CW1])))
scalaSpiraleR23 = R([1,2])(PI/2)(scalaSpirale23)
scalaSpiraleT23 = T([1,2,3])([-3,5.7,8.1])(scalaSpiraleR23)
pavimento23 = T([1,2,3])([-3,6.2,8.2])(CUBOID([3,1.5,0.1]))
pavimento23Sopra = T([1,2,3])([-2.5,6.2,11.4])(CUBOID([2.5,1.5,0.1]))
pavimentoVicino23 = T([1,2,3])([-2.5,5.5,11.5])(CUBOID([1.5,0.8,0.1]))
pavimentoTot23 = (COLOR([1,0.54,0.41]))(STRUCT([pavimento23,pavimentoVicino23,pavimento23Sopra]))



W2,CW2 = spiralStair(0.2,2,0.5,0.1,2,3.5,18)
scalaSpirale12 = (COLOR([1,0.54,0.41]))(STRUCT(MKPOLS([W2,CW2])))
scalaSpiraleR12 = R([1,2])(PI*3/2)(scalaSpirale12)
scalaSpiraleT12 = T([1,2,3])([28.8,8.2,4.9])(scalaSpiraleR12)
pavimento12 = T([1,2,3])([25.8,6.2,5])(CUBOID([3,1.5,0.1]))
pavimento12Sopra = T([1,2,3])([25.8,6.2,8.2])(CUBOID([2.5,1.5,0.1]))
pavimentoVicino12 = T([1,2,3])([26.8,7.5,8.3])(CUBOID([1.5,0.8,0.1]))
pavimentoTot12 = (COLOR([1,0.54,0.41]))(STRUCT([pavimento12,pavimentoVicino12,pavimento12Sopra]))

W3,CW3 = spiralStair(0.2,2,0.5,0.1,2,3.5,18)
scalaSpirale34 = (COLOR([1,0.54,0.41]))(STRUCT(MKPOLS([W3,CW3])))
scalaSpiraleR34 = R([1,2])(PI*3/2)(scalaSpirale34)
scalaSpiraleT34 = T([1,2,3])([28.8,8.2,11.3])(scalaSpiraleR34)
pavimento34 = T([1,2,3])([25.8,6.2,11.3])(CUBOID([3,1.5,0.1]))
pavimento34Sopra = T([1,2,3])([25.8,6.2,14.6])(CUBOID([2.5,1.5,0.1]))
pavimentoVicino34 = T([1,2,3])([26.8,7.5,14.7])(CUBOID([1.5,0.8,0.1]))
pavimentoTot34 = (COLOR([1,0.54,0.41]))(STRUCT([pavimento34,pavimentoVicino34,pavimento34Sopra]))


pianoColorato = (COLOR([0.01,0.75,0.23]))(CUBOID([45,35,0]))#cambiare colore
pianoColoratoT = T([1,2])([-12,-12])(pianoColorato)

#balconcini altezza totale 1.3??

base = CUBOID([3.2,1.6,0.1])
baseDaLevare = CUBOID([3,1.5,0.05])
baseDaLevareT = T([1,2,3])([0.1,0.1,0.05])(baseDaLevare)
baseBalconcino = DIFFERENCE([base, baseDaLevareT]) #base alta 0.1


gamba1 = CUBOID([0.1,0.1,1.3])
gamba2 = T(1)(0.3)(gamba1)
gambe = STRUCT([gamba1,gamba2])
puntiCurva1B = [[0.1,0,1.3],[0.2,0,1.5],[0.3,0,1.3]]
puntiCurva1A = [[0,0,1.3],[0.2,0,1.8],[0.4,0,1.3]]
curva1B = BEZIER(S1)(puntiCurva1B)
curva1A = BEZIER(S1)(puntiCurva1A)
curvaVicina1 = MAP( BEZIER(S2)([curva1B,curva1A]))(dom)
'''puntiCurva2B = [[0.1,0.1,1.3],[0.2,0.1,1.5],[0.3,0.1,1.3]]
puntiCurva2A = [[0,0.1,1.3],[0.2,0.1,1.8],[0.4,0.1,1.3]]
curva2B = BEZIER(S1)(puntiCurva2B)
curva2A = BEZIER(S1)(puntiCurva2A)
curvaVicina2 = MAP( BEZIER(S2)([curva2B,curva2A]))(dom)
dec1 = MAP( BEZIER(S2) ([curva1B,curva2B])) (dom)
dec2 = MAP( BEZIER(S2) ([curva1A,curva2A])) (dom)'''


baseDaLevareND = CUBOID([3,1.5,0.1])
baseDaLevareTND = T([1,2])([0.1,0.1])(baseDaLevareND)
baseSopraNDDIFF = DIFFERENCE([baseBalconcino,baseDaLevareTND])
baseSopraND = T(3)(1.3)(baseSopraNDDIFF)


decorazione = STRUCT([gambe, curvaVicina1]) #levo dec1, dec2, curva vicina2
decorazioni = T([1,2,3])([0,0,0])(STRUCT([decorazione,T(1)(0.4)]*8))
decorazioneND = STRUCT([gambe]) #levo dec1, dec2, curva vicina2
decorazioniND = T([1,2,3])([0,0,0])(STRUCT([decorazioneND,T(1)(0.4)]*8))

decorazioneR = R([1,2])(PI/2)(decorazione)
decorazioneT = T(1)([0.1])(decorazioneR)
decorazioneRND = R([1,2])(PI/2)(decorazioneND)
decorazioneTND = T(1)([0.1])(decorazioneRND)


decorazioneSX = T([1,2,3])([0,0,0])(STRUCT([decorazioneT,T(2)(0.4)]*4))
decorazioneDX = T(1)(3.1)(decorazioneSX)
decorazioneSXND = T([1,2,3])([0,0,0])(STRUCT([decorazioneTND,T(2)(0.4)]*4))
decorazioneDXND = T(1)(3.1)(decorazioneSXND)

decorazioneR = R([1,2])(PI)(decorazione)
decorazioneR = R([1,2])(PI/2)(decorazioneR)
decorazioneT = T(2)(0.4)(decorazioneR)
decorazioneSX = T([1,2,3])([0,0,0])(STRUCT([decorazioneT,T(2)(0.4)]*4))
decorazioneRND = R([1,2])(PI)(decorazioneND)
decorazioneRND = R([1,2])(PI/2)(decorazioneRND)
decorazioneTND = T(2)(0.4)(decorazioneRND)
decorazioneSXND = T([1,2,3])([0,0,0])(STRUCT([decorazioneTND,T(2)(0.4)]*4))



balcone = STRUCT([baseBalconcino, decorazioni, decorazioneSX, decorazioneDX])

balconeND = STRUCT([baseBalconcino, decorazioniND, decorazioneSXND, decorazioneDXND, baseSopraND])


balconeTND = T([1,2,3])([4.3,-0.1,5.4])(balconeND)

balconeT = T([1,2,3])([4.3,-0.1,5.4])(balcone)

balconi1 = T([1,2,3])([0,0,0])(STRUCT([balconeT,T(3)(3.15)]*4))
balconi1ND = T([1,2,3])([0,0,0])(STRUCT([balconeTND,T(3)(3.15)]*4))

balconi2ND = T([1,2,3])([0,0,0])(STRUCT([balconi1ND,T(1)(12.9)]*2))
balconi2 = T([1,2,3])([0,0,0])(STRUCT([balconi1,T(1)(12.9)]*2))

balconi3ND = R([1,2])(PI)(balconi1ND)
balconi3NDT = T ([1,2])([11.8,13.9])(balconi3ND)
balconi3 = R([1,2])(PI)(balconi1)
balconi3T = T ([1,2])([11.8,13.9])(balconi3)

balconi4ND = T([1,2,3])([0,0,0])(STRUCT([balconi3NDT,T(1)(12.9)]*2))
balconi4 = T([1,2,3])([0,0,0])(STRUCT([balconi3T,T(1)(12.9)]*2))

VIEW(balcone)
VIEW(balconeND)

balconiND = COLOR([1,0.75,0])(STRUCT([balconi1ND,balconi2ND,balconi3NDT,balconi4ND]))
balconi = COLOR([1,0.75,0])(STRUCT([balconi1,balconi2,balconi3T,balconi4]))

#finestre principali trasparenti
hpc2 = T([2,3])([-4.9,5.18])(hpc2)
finestre1 = T([1,2,3])([0,0,0])(STRUCT([hpc2,T(3)(3.2)]*4))
finestre2 = T([1,2,3])([0,0,0])(STRUCT([finestre1,T(1)(12.9)]*2))
finestre3 = T([1,2,3])([0,0,0])(STRUCT([finestre1,T(2)(10.6)]*2))
finestre4 = T([1,2,3])([0,0,0])(STRUCT([finestre3,T(1)(12.9)]*2))

finestre = STRUCT([finestre1,finestre2,finestre3,finestre4])





VIEW(STRUCT([appartamentiTraslatiZ,corridoi,colonne,figuraCurva,contenitori1,contenitori2,contenitori3,figuraCurvaT,
	contornoTotCol,scalaSpiraleT1,pavimentoT1,scalino,scalaSpiraleT23,pavimentoTot23,scalaSpiraleT12,pavimentoTot12,scalaSpiraleT34,
	pavimentoTot34,pianoColoratoT,balconiND,finestre]))




























