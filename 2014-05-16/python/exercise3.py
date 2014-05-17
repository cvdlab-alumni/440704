from lar_cc import *
from pyplasm import *



def merging_numbering_elimination (master, toMerge, shape, sizePattern):
	V,CV = master
	blocchiMaster = len(CV)-1
	scelta = []
	toRemove = []
	


	diagram = assemblyDiagramInit(shape)(sizePattern)
	master = diagram2cell(diagram,master,toMerge)


	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
	VIEW(hpc)

	fine = True 
	while (fine):
		inserimento = input('Inserisci un numero (-1 quando vuoi terminare): ')
		scelta.append(inserimento)
		if (inserimento == -1):
			fine = False


	toRemove = scelta
	master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
	DRAW(master)


#Prova per verificare il funzionamento

DRAW = COMP([VIEW,STRUCT,MKPOLS])

master = assemblyDiagramInit([5,5,2])([[.3,3.2,.1,5,.3],[.3,4,.1,2.9,.3],[.3,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
VIEW(hpc)

toRemove = [13,33,17,37]
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
VIEW(hpc)





merging_numbering_elimination(master, 29, [3,1,2], [[2,1,2],[.3],[2.2,.5]])




