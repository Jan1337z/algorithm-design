
# CLOSEST PAIR
# 

# Euklidische Distanz
from math import sqrt
def d(p,q):
    x = (p[0]-q[0])**2
    y = (p[1]-q[1])**2
    return sqrt(x+y)

# Vergleich aller Paare
def cp_all_pairs(U):
    # Initialisierung mit zwei bel. Punkten
    p, q = U.pop(), U.pop()
    best = d(p,q)
    U |= {p,q}
    # alle Punktepaare
    for r in U:                         # O(#U^2)
        for s in U-{r}:
            dist = d(r,s)
            if dist < best:
                best,p,q = dist,r,s
    #print(p,q)
    return best


# U1 = {(12,4),(2,17),(3,3)}
# print(cp_all_pairs(U1))

# U2 = {(2,2), (3,4), (5,4)}
# print(cp_all_pairs(U2))


# Menge mit <= m zufaelligen Punkten in der Ebene
# ohne doppelte Koordinaten
from random import randrange
def rand_set(m):
    x =  list({randrange(m*m) for _ in range(m)})
    y =  list({randrange(m*m) for _ in range(m)})
    return set(zip(x,y))

#import timeit
#T = timeit.Timer('print(cp_all_pairs(U))', 'from __main__ import cp_all_pairs,U')
#for i in range(1,6):
#    U = rand_set(i*500)
#    t = T.repeat(1,1)  
#    print('#U =',len(U),'Dauer in sec : ', t)