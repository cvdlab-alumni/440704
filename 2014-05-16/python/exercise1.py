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
toRemove = [139]
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
VIEW(hpc)

toRemove = [181]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
DRAW(master)

#effetto trasparente
hpc = STRUCT(MKPOLS(master))
VIEW(STRUCT([hpc,hpc2]))
























