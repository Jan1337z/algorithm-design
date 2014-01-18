
# Anzahl kuerzester Pfade (bzgl Kantenanzahl)
# verwendet bfs
from vl.lek03.bfs import bfs

def bfs_numpaths(G,s):
    # todo
    return []


def define_G():
    m = 10
    G = [set() for _ in range(m)]   # alle Mengen leer anlegen
    G[0] |= {1,2}
    G[1] |= {0,2,3,4}
    G[2] |= {0,1,4,6,7}
    G[3] |= {1,4}
    G[4] |= {1,2,3,5}
    G[5] |= {4}
    G[6] |= {2,7}
    G[7] |= {2,6}
    G[8] |= {9}
    G[9] |= {8}
    return G

G = define_G()
print(bfs_numpaths(G,0))


