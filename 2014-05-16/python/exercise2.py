from pyplasm import *
from lar_cc import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])

master = assemblyDiagramInit([9,9,2])([[0.3,3.5,0.1,4,0.1,2.5,0.1,2,0.3],[0.3,1.2,0.1,1.2,0.1,0.2,0.1,1.2,0.3],[.3,2.7]])
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
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.5)
#VIEW(hpc)

#finestre
#cella della finestra
#finesra principale
toMerge = 57
diagram = assemblyDiagramInit([3,1,3])([[1,2,1],[0.3],[1.3,1,0.4]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.5)
#VIEW(hpc)
toRemove = [139]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

toMerge = 15
diagram = assemblyDiagramInit([1,3,3])([[0.3],[0.2,0.6,0.2],[1.3,0.8,0.6]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.5)
#VIEW(hpc)
toRemove = [146]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

toMerge = 110
diagram = assemblyDiagramInit([3,1,3])([[0.4,0.4,0.4],[0.3],[1.3,0.8,0.6]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.5)
#VIEW(hpc)
toRemove = [153]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)


toMerge = 113
diagram = assemblyDiagramInit([1,3,3])([[0.3],[0.2,0.6,0.2],[1.3,0.8,0.6]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.5)
#VIEW(hpc)
toRemove = [160]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

#porte

toMerge = 21

diagram = assemblyDiagramInit([3,1,2])([[2,1,.5],[.3],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.5)
#VIEW(hpc)
toRemove = [165]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

toMerge = 23

diagram = assemblyDiagramInit([3,1,2])([[0.5,1,2],[.3],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.5)
#VIEW(hpc)
toRemove = [169]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

toMerge = 73

diagram = assemblyDiagramInit([3,1,2])([[0.5,1,2],[.3],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.5)
#VIEW(hpc)
toRemove = [173]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

toMerge = 77

diagram = assemblyDiagramInit([3,1,2])([[0.5,1,2],[.3],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.5)
#VIEW(hpc)
toRemove = [177]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

toMerge = 103

diagram = assemblyDiagramInit([3,1,2])([[0.5,1,1.5],[.3],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.5)
#VIEW(hpc)

toRemove = [181]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)




# Da qui l'esercizio 2

appartamenti = assemblyDiagramInit([2,4,4])([2*[12.9],[1.5,4.7,1.5,4.7],4*[3.2]])
V,CV = appartamenti
hpc = SKEL_1(STRUCT(MKPOLS(appartamenti)))
hpc = cellNumbering (appartamenti,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)


appartamenti = diagram2cell(master,appartamenti,4)
appartamenti = diagram2cell(master,appartamenti,4)
appartamenti = diagram2cell(master,appartamenti,4)
appartamenti = diagram2cell(master,appartamenti,4)
appartamenti = diagram2cell(master,appartamenti,8)
appartamenti = diagram2cell(master,appartamenti,8)
appartamenti = diagram2cell(master,appartamenti,8)
appartamenti = diagram2cell(master,appartamenti,8)
appartamenti = diagram2cell(master,appartamenti,12)
appartamenti = diagram2cell(master,appartamenti,12)
appartamenti = diagram2cell(master,appartamenti,12)
appartamenti = diagram2cell(master,appartamenti,12)
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
hpc = cellNumbering (appartamenti,hpc)(range(len(CV)),CYAN,2)
VIEW(hpc)




#VIEW(STRUCT( MKPOLS(appartamenti) ))


hpc = STRUCT(MKPOLS(appartamenti))
appartamentiTraslatiZ = COLOR([0.9,0.86,0.51])(T(3)(5)(hpc))
VIEW(appartamentiTraslatiZ)


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

VIEW(STRUCT([appartamentiTraslatiZ,corridoi]))

#parte sotto con curve

colonna = COLOR([1,0.99,0.81])(CYLINDER([1,5]) (50))

colonna1 = T([1,2])([1,2.2])(colonna)
colonna2 = T([1,2])([24.8,2.2])(colonna)
colonna3 = T([1,2])([24.8,11.2])(colonna)
colonna4 = T([1,2])([1,11.2])(colonna)

colonne = STRUCT([colonna1,colonna2,colonna3,colonna4])

VIEW(STRUCT([appartamentiTraslatiZ,corridoi,colonne]))





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

VIEW(figuraCurva)




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

scalinoNuovo = (COLOR([1,0.54,0.41]))(CUBOID([10,1,0.6]))
piano = (COLOR([1,0.54,0.41]))(CUBOID([3,3,0.1]))
pianoT = T([1,2,3])([4.5,-0.5,5.2])(piano)
prova = [T([2,3])([1,0.5]),scalinoNuovo]
scalaNuova = ((STRUCT(NN(34)(prova))))
scalaS = S([1,2,3])([0.3,0.3,0.3])(scalaNuova)
scalaT = T([1,2])([4.5,-11])(scalaS)

scalaCompleta = STRUCT([scalaT,pianoT])

scalaCompleta2 = scalaCompleta
scalaCompleta2T = T(1)(13)(scalaCompleta2)

scaleComplete = STRUCT([scalaCompleta,scalaCompleta2T])










VIEW(STRUCT([appartamentiTraslatiZ,corridoi,colonne,figuraCurva,contenitori1,contenitori2,contenitori3,figuraCurvaT,scaleComplete,
	contornoTotCol]))




























