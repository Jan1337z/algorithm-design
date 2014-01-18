
# MAX KNAPSACK

# zulaessige Loesung, auch fuer Teilloesungen
def sol_max_ks(s,v,S,t):
    # todo
    return False

# Bewertungsfunktion, auch fuer Teilloesungen
def m_max_ks(s,v,S,t):
    # todo
    return 0

# Entwurfsmuster Exhaustive Search
from itertools import product
def max_ks_exhaustive(s,v,S):            
    opt = -1
    # todo
    return opt


# Bsp m=4, S=7
print(max_ks_exhaustive([3,2,1,5],[3,1,1,4],7))
print(max_ks_exhaustive([3,2,1,5],[3,1,1,4],8))



