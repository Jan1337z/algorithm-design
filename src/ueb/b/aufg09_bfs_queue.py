 

from collections import deque

def bfs_queue(G,s):
    # empty parent array
    parent = [None for _ in G]
    # is node x already reached?
    # (without: cant say if startnode or not reached)
    reached = [False for _ in G]
    # only start vertex is reached
    reached_v = {s}
    # add start vertex to deque 
    q= deque([s])
    # start node is reached
    reached[s] = True
    
    while len(q):
        u = q.popleft()
        for v in G[u]:
            if(not reached[v]):
                reached[v] = True
                parent[v] = u
                q.append(v)
                reached_v.add(v)
    return reached_v, parent


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
print(bfs_queue(G,0))


# Vergleich mit bfs aus VL
from vl.lek03.bfs import bfs

for s in range(len(G)):
    print('s = ', s)
    L = bfs(G,s)[0]  # erste Komponente ist Liste der L_i
    # alle L_i vereinigen
    R = { u for i in range(len(L)) for u in L[i]}
    # Vergleich
    print(R == bfs_queue(G,s)[0])
    print(bfs(G,s)[1] == bfs_queue(G,s)[1])


