
# MINIMUM INTERVAL PARTITIONING

# ist Intervallmenge M kompatibel?
def compatible(L,M):
    deadline = -1
    for i in sorted(M):
        s,f = L[i]
        if s < deadline: return False
        deadline = f
    return True

# zulaessige Loesung:
# - r ist stets total
# - jede Intervallmenge pro Ressource ist kompatibel
def sol_min_intpart(L,r):
    for R in r:
        if not compatible(L, R): return False
    return True

# Bewertungsfunktion:
# - Kardinalitaet Wertebereich von r
def m_min_intpart(L,r):
    resources = 0
    for R in r:
        if(len(R)!=0): resources += 1 
    return resources

# Entwurfsmuster Exhaustive Search
from itertools import product

def min_intpart_exhaustive(L):
    m = len(L)
    C = [] 
    opt = m
    # create product like 0000, 0011, ... (for m=4)
    #
    # Example for 1122
    #
    # interval           i_1  i_2  i_3  i_4 
    # target resource     1    1    2    2  
    # interval 1 -> resource 1
    # interval 2 -> resource 1
    # interval 3 -> resource 2
    # interval 3 -> resource 2
    
    for order in product(*[range(i) for i in range(1,m+1)]):
        # create new list with m resources
        candidate = [[] for _ in range(m)] 
        # c_i    index of intervals
        # r_i    resource for interval
        # put each interval in the target resource
        for c_i, r_i in enumerate(order):
            candidate[r_i].append(c_i)
        C.append(candidate)
        
        for y in C:
            if sol_min_intpart(L, y):
                value = m_min_intpart(L, y)
                if value < opt:
                    opt = value      
    return opt
    
    
# print(min_intpart_exhaustive([(0,2),(1,3),(0,3),(2,4)]))
# print(min_intpart_exhaustive([(0,2),(0,3),(2,3),(3,4)]))


