
# MINIMUM SPANNING TREE

# Greedy-Entwurfsmuster
# Eingabe: zusammenhaengender Graph G mit Kantenkosten

def prim(G):
    m = len(G)
    # (geschaetzte) Kosten für die Anbindung von Knoten an den Spannbaum
    # mittels einer weiteren Kante
    d = [None]*m               
    d[0] = 0                    # beginne mit bel. Knoten, hier 0
    p = [None]*m                # Nachbarknoten merken
    Q = {u for u in range(m)}   # alle Knoten
    T = set()                   # Ergebnis: Spannbaum als Kantenmenge
    c = 0                       #           und dessen Kosten
    while Q:
        # Auswahl von v mit kleinstem d-Wert
        (_,v) = min({(d[u],u) for u in Q if d[u]!= None})
        # v aus Q entfernen
        Q.remove(v)
        # Kante in den Spannbaum einfuegen
        T.add(frozenset((p[v],v)))
        c += d[v]
        # Kosten fuer die Anbindung der Nachbarn von v aktualisieren
        for u in set(G[v]) & Q:
            alt = G[v][u]                 # alternative Kosten
            if d[u]==None or alt < d[u]:
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
print(prim(G))

# Laufzeit wie bei dijkstra
