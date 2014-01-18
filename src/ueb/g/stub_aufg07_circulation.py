
from vl.lek12.ford_fulkerson import ford_fulkerson

# Eingabe: Flussnetzwerk mit Bedarfswerten
def circulation(G,d):
    m = len(G)
    # Mengen S und T bestimmen, Laufzeit ?
    #        
    # Quelle s einfuehren, s mit S verbinden, Kap. -d[u], Laufzeit ?
    #
    # Senke t einfuehren, T mit t verbinden, Laufzeit ?
    #
    # Aufruf MAX FLOW-Algo, Laufzeit ?
    #
    return False

# Bsp
def define_G():
    G = [   {1:3, 2:3},
            {2:2, 3:2},
            {3:2},
            {}        ]
    return G

G = define_G()
d = [-3,-3,2,4]
print(circulation(G,d))


