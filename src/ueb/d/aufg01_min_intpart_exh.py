
# MINIMUM INTERVAL PARTITIONING

# ist Intervallmenge M kompatibel?
def compatible(L,M):
    deadline = -1
    for i in M:
        s,f = L[i]
        if s < deadline: return False
        deadline = f
    return True

# Bsp
L = [(0,3),(0,4),(4,6),(5,7),(8,10),(0,12),(9,13),(15,16),(14,17)]
print (compatible(L,{0,2,5}))
print (compatible(L,{0,3,4,7}))
print (compatible(L,{1,2}))
print (compatible(L,set()))


# zulaessige Loesung:
# - r ist stets total
# - jede Intervallmenge pro Ressource ist kompatibel
def sol_min_intpart(L,r):
    # todo
    return True

# Bewertungsfunktion:
# - Kardinalitaet Wertebereich von r
def m_min_intpart(L,r):
    # todo
    return 0

# Entwurfsmuster Exhaustive Search
from itertools import product
def min_intpart_exhaustive(L):            
    opt = ()
    # todo
    return opt


print(min_intpart_exhaustive([(0,2),(1,3),(0,3),(2,4)]))
print(min_intpart_exhaustive([(0,2),(0,3),(2,3),(3,4)]))


