

def dfs(G,s):
    m = len(G)
    S = [s]                 # Stack statt Rekursion
    explored = [False]*m    # alle Nachbarn bereits behandelt, O(m)
    parent = [None]*m       # Vorgaenger im DFS-Baum
    while S:
        u = S.pop()
        explored[u] = True  # 1. Markieren u
                            # 2. R wird beim return bestimmt
        for v in G[u]:      # 3. Fuer alle Kanten (u,v):
            if not explored[v]:  # falls nicht markiert
                S.append(v)      # Stack statt Rekursion
                parent[v] = u    # Vorgaenger merken
    return { u for u in range(m) if explored[u]}, parent    # O(m)


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
# print(dfs(G,0))
