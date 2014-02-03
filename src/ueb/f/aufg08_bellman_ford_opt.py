
# Bellman-Ford: INT SHORTEST PATH via DP

# optimierte Version

# Dynamic Programming
# Eingabe: Digraph ohne negative Kreise, Startknoten s
# Aufruf erfolgt mit Umkehrgraph wegen Zugriff auf Vorgaenger
# 
def bellman_ford_opt(G,s):
    m = len(G)
    opt = [None]*m
    last_v = [None]*m
    opt[s] = 0
    changed = False
    for _ in range(1,m):
        changed = False
        for v in range(m):
            
            for u in G[v]:
                if(opt[u]!=None):
                    alt = G[v][u] + opt[u]
                    if(opt[v] == None or alt<opt[v]):
                        opt[v] = alt
                        last_v[v] = u
                        changed = True
    if not changed: pass
    
    # konstruiere G_BF
    G_BF = [set() for _ in range(m)]
    for i in range(m):
        if last_v[i] != None:
            G_BF[last_v[i]].add(i)
        
    
    return opt, G_BF


# from vl.lek11.bellman_ford import reverse_weighted, define_G
# G = [   {1:2, 2:1},    # Nachfolger von s
#             {3:3},             # von u
#             {},                # von v
#             {2:-6}             # von w
#         ]
# print(bellman_ford_opt(reverse_weighted(G),0))

