

from vl.lek12.augment import augment,bottleneck
from vl.lek12.residual_graph import residual_graph

# s-t-Pfad als Knotenfolge, O(m)
def get_path(v,parent):
    if v == None: return []     # s erreicht
    return get_path(parent[v],parent) + [v] 

from vl.lek03.dfs import dfs
# Eingabe: Flussnetzwerk G, Quelle s, Senke t
# o.b.d.A. alle Knoten sind von s aus erreichbar,
#          und in G ex. max. eine der Kanten (u,v) und (v,u)
def ford_fulkerson(G,s,t):
    # Fluss mit 0 initialisieren und ersten Pfad suchen
    f = {(u,v):0 for u in range(len(G)) for v in G[u]}      # O(m+k)         
    Gf = residual_graph(G,f)    # hier ist Gf = G           # O(m+k)
    R,parent = dfs(Gf,s)        # Pfad suchen               # O(m+k)
    while t in R:               # ex. s-t-Pfad in Gf ?      # O(C)  
        P = get_path(t,parent)      # Pfad als Knotenfolge      # O(m)
        b = bottleneck(P,Gf)        # min. Kap. entlang P       # O(m)
        f = augment(f,P,b)          # f um b erhoehen           # O(m)
        Gf = residual_graph(G,f)    # neuer Residualgraph       # O(m+k)
        R,parent = dfs(Gf,s)        # Pfad in Gf suchen         # O(m+k)
    return f, sum(f[s,u] for u in G[s])

from vl.lek12.residual_graph import G
print(ford_fulkerson(G,0,3))


