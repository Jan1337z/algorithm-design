
# MINIMUM SPANNING TREE

# Verbesserung von prim mittels MinPrioQueue
from heapq import heappush, heappop

def prim_pq(G):
    m = len(G)
    # (geschaetzte) Kosten für die Anbindung von Knoten an den Spannbaum
    # mittels einer weiteren Kante
    
    p = [None]*m                # Nachbarknoten merken
    Q = [(float("inf"),u) for u in range(1,m)]
    heappush(Q,(0,0)) # startknoten hinzufuegen
    T = set()                   # Ergebnis: Spannbaum als Kantenmenge
    c = 0  
    
    while Q:
        # Auswahl von v mit kleinstem d-Wert
        (c_v,v) = heappop(Q)
        
        if not frozenset((p[v],v)) in T:
            # Kante in den Spannbaum einfuegen
            T.add(frozenset((p[v],v)))
            c += c_v
            # Kosten fuer die Anbindung der Nachbarn von v aktualisieren
            for u in set(G[v]) & {v for _,v in Q}:
                alt = G[v][u]                 # alternative Kosten
                if p[u] == None or alt < G[p[u]][u]:
                    heappush(Q,(alt,u))
                    p[u] = v 
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
