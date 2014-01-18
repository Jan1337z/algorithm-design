
# MIN TSP
# zulaessige Loesungen: jede Permutation ist zulaessig

# Bewertungsfunktion
def m_min_tsp(m,D,p):
    cost = D[p[-1]][p[0]]
    current = 0
    for destination in range(1,len(p)):
        cost += D[p[current]][p[destination]]
        current = destination
    return cost


# Entwurfsmuster Exhaustive Search
from itertools import permutations
def min_tsp_exhaustive(D): 
    min = float("inf")
    m = len(D)
    C = permutations(range(0,m),m)
    for y in C:
        y_cost = m_min_tsp(m, D, y) 
        if y_cost <= min: min = y_cost 
    return min

# Bsp
# print(min_tsp_exhaustive([[0,13,2],[7,0,2],[3,8,0]]))
