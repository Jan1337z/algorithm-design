

# drittes Argument kann weggelassen werden, weil default-Wert vorhanden
# default-Wert wird bereits bei Fktdeklaration gesetzt
def dfs_rec(G, u, explored = None):
    # todo
    return explored


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
expl = dfs_rec(G,0)
# Ergebnismenge
R = { u for u in range(len(G)) if expl[u]}
print(R)

G=[{1},{0,2},{1,3,4,5},{2,4},{2,3},{2}]
# Ergebnismenge
R = { u for u in range(len(G)) if dfs_rec(G,1)}
print(R)


