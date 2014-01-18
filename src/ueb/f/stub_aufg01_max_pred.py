
# verwendet merge
from ueb.a.aufg05_merge import merge

# bestimme fuer jedes Intervall j den max. Index i<j,
# so dass sich i und j nicht ueberlappen
def max_predecessors(L):
    # todo
    return []


# Bsp 10.2 aus der VL
L = [(0,3,2),(1,5,4),(4,6,4),(2,9,7),(7,10,2),(8,11,1)]
print(max_predecessors(L))

print(max_predecessors(L) == [-1, -1, 0, -1, 2, 2])
