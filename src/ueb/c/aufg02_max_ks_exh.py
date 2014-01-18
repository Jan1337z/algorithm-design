
# MAX KNAPSACK

# zulaessige Loesung, auch fuer Teilloesungen
def sol_max_ks(s,v,S,t):
    usedVolume = 0
    for i,isUsed in enumerate(t):
        if isUsed: usedVolume += s[i]
    return usedVolume <= S

# Bewertungsfunktion, auch fuer Teilloesungen
def m_max_ks(s,v,S,t):
    value = 0
    for i,isUsed in enumerate(t):
        if isUsed: value += v[i]
    return value

# Entwurfsmuster Exhaustive Search
from itertools import product
def max_ks_exhaustive(s,v,S):
    m = len(s)            
    opt = -1
    y = product((0,1),repeat=m)
    
    for t in y: 
        if sol_max_ks(s, v, S, t):
            t_value = m_max_ks(s, v, S, t)
            if  t_value > opt:
                opt = t_value
    return opt


# Bsp m=4, S=7
# print(max_ks_exhaustive([3,2,1,5],[3,1,1,4],7))
# print(max_ks_exhaustive([3,2,1,5],[3,1,1,4],8))



