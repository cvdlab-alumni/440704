from pyplasm import *
q = QUOTE([2,-1,2,-1,4,-1,2,-1,2,-1,1])
base = PROD([q,q])
tot = PROD([base,Q(5)])
VIEW(tot)