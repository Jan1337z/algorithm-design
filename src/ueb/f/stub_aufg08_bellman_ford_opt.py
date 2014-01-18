
# Bellman-Ford: INT SHORTEST PATH via DP

# optimierte Version

# Dynamic Programming
# Eingabe: Digraph ohne negative Kreise, Startknoten s
# Aufruf erfolgt mit Umkehrgraph wegen Zugriff auf Vorgaenger
# 
def bellman_ford_opt(G,s):
    m = len(G)
    opt = [None]*m                  
    # todo      
    # konstruiere G_BF
    G_BF = [set() for _ in range(m)]
    # todo
    return opt, G_BF


from vl.lek11.bellman_ford import reverse_weighted, define_G
G = define_G()
print(bellman_ford_opt(reverse_weighted(G),0))

