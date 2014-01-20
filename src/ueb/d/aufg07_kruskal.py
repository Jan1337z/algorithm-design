
# MINIMUM SPANNING TREE

# Vervollstaendigung von kruskal mit UnionFind
# verwendet die Klasse UnionFind
from vl.lek07.union_find import UnionFind

def kruskal(G):
    V = []
    T = set()
    cost = 0
    m = len(G)
    uf = UnionFind(m)
    for u,U in enumerate(G):
        for v in U:
            c_u_v = U[v]
            V.append((c_u_v,(u,v)))
            
    for e in sorted(V, key=lambda x: x[0]):
        c,(u,v) = e
        if(uf.find(u) != uf.find(v)):
            uf.union(uf.find(u), uf.find(v))
            T |= {frozenset((u,v))}
            cost += c 
    return T, cost


# Bsp aus der VL
# Knotennnummern: s=0, a=1, b=2, c=3, d=4, e=5, f=6, g=7 
def define_G():
    G = [   {1:2, 2:7, 3:10},   # s 
            {0:2, 2:8},         # a
            {0:7, 1:8},         # b
            {0:10, 4:1, 7:9},   # c
            {3:1, 5:3, 6:4},    # d  
            {4:3, 6:5, 7:6},    # e  
            {4:4, 5:5},         # f
            {3:9, 5:6}          # g
        ]
    return G

# G = define_G()
# print(kruskal(G))

