
from vl.lek12.ford_fulkerson import ford_fulkerson

# Eingabe: bipartiter Graph G
def max_bipartite_matching(G):
    m = len(G)
    # Partitionierung (X,Y) von V bestimmen, Laufzeit ?
    #
    # Kanten von X nach Y ausrichten, Laufzeit ?
    # 
    # Quelle s einfuehren, s mit X verbinden, Laufzeit ?
    #
    # Senke t einfuehren, Y mit t verbinden, , Laufzeit ?
    #
    # alle Kanten erhalten Kapazitaet 1, Laufzeit ?
    #
    # Aufruf MAX FLOW-Algo, Laufzeit ?
    #
    # Matching auslesen, O(m+k)
    #
    return set(), 0


# Bsp
def define_G():
    G = [   {4, 5},
            {4, 6},
            {5},
            {5,6},
            {0,1},
            {0,2,3},
            {1,3}
        ]
    return G

G = define_G()
print(max_bipartite_matching(G))


