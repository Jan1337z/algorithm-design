
# MINIMUM SPANNING TREE

# Verbesserung von prim mittels MinPrioQueue
from heapq import heappush, heappop

def prim_pq(G):
    m = len(G)
    # (geschaetzte) Kosten für die Anbindung von Knoten an den Spannbaum
    # mittels einer weiteren Kante
    d = [float("inf")]*m               
    d[0] = 0                    # beginne mit bel. Knoten, hier 0
    p = [None]*m                # Nachbarknoten merken
    Q = [(d[u],u) for u in range(m)]   # alle Knoten
    T = set()                   # Ergebnis: Spannbaum als Kantenmenge
    c = 0                       #           und dessen Kosten
    while Q:
        # Auswahl von v mit kleinstem d-Wert
        (_,v) = heappop(Q)
        # Kante in den Spannbaum einfuegen
        T.add(frozenset((p[v],v)))
        c += d[v]
        # Kosten fuer die Anbindung der Nachbarn von v aktualisieren
        for u in set(G[v]) & {v for _,v in Q}:
            alt = G[v][u]                 # alternative Kosten
            if alt < d[u]:
                heappush(Q,(alt,u))
                d[u] = alt
                p[u] = v                  # Nachbar merken
    return T-{frozenset((None,0))}, c                # erster Knoten 0 hat keinen Vorgaenger

   

# Bsp aus der VL
def define_G():
    G = [   {1:4, 2:1, 3:3}, 
            {0:4, 2:4, 3:4}, 
            {0:1, 1:4, 3:2, 5:4},
            {0:3, 1:4, 2:2, 5:6},  
            {5:5},  
            {2:4, 3:6, 4:5}  
        ]
    return G

G = define_G()
print(prim_pq(G))
