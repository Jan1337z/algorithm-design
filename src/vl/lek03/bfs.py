

def bfs(G,s):
    m = len(G)
    L = [{s}]           # Liste der Schichten, mit L_0 init. 
    reached = [False]*m # bereits besuchte Knoten
    reached[s] = True   #
    parent = [None]*m   # Vorgaenger im BFS-Baum
                        # 
    while L[-1]:        # solange letzte Schicht L_i nicht leer
        S = set()           # naechste Schicht L_i+1 bestimmen
        for u in L[-1]:         # alle Nachbarn v von    
            for v in G[u]:      # u aus L_i
                if not reached[v]:  
                    S.add(v)
                    reached[v] = True
                    parent[v] = u
        L.append(S)
    return L[:-1], parent    # letzte Menge in L ist leer


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
print(bfs(G,0))

