

# alle Zusammenhangskomponenten eines unger. Graphen
# verwendet dfs
from vl.lek03.dfs import dfs

def comp(G):
    C = []  
    # todo
    return C


def define_G():
    m = 10
    G = [set() for _ in range(m)]   # alle Mengen leer anlegen
    G[0] |= {1,2}
    G[1] |= {0,2}
    G[2] |= {0,1,6,7}
    G[3] |= {4}
    G[4] |= {3}
    # G[5] |= 
    G[6] |= {2,7}
    G[7] |= {2,6}
    G[8] |= {9}
    G[9] |= {8}
    return G

G = define_G()
print(comp(G))

