
# (SINGLE-SOURCE) SHORTEST PATH

# Greedy-Entwurfsmuster
# Eingabe: Digraph G mit Kantenkosten, Startknoten s

def dijkstra(G,s):
    m = len(G)
    d = [None]*m                # (geschaetzte) Pfadkosten
    d[s] = 0                    # sind 0 fuer den Startknoten
    Q = {u for u in range(m)}   # alle Knoten
    while Q:
        # Auswahl von v mit kleinstem d-Wert
        (_,v) = min({(d[u],u) for u in Q if d[u]!= None})
        # v aus Q entfernen, d[v] ist endgueltig
        Q.remove(v)
        # Schaetzungen fuer Nachfolger von v aktualisieren
        for u in G[v]:
            alt = d[v] + G[v][u]            # alternative Kosten
            if d[u]==None or alt < d[u]:
                d[u] = alt
    return d


# Bsp aus der VL
# Knotennummern: s=0, u=1, x=2, y=3, v=4, z=5
def define_G():
    G = [   {1:1, 4:4, 2:2},   # Nachfolger von s
            {3:3, 4:1},        # von u
            {4:2, 5:3},        # von x
            {},                # von y
            {3:1, 5:2},        # von v
            {}                 # von z
        ]
    return G

G = define_G()
print(dijkstra(G,0))

# Laufzeit
# def dijkstra(G,s):
#     m = len(G)                  # O(1)
#     d = [None]*m                # O(m)
#     d[s] = 0                    # O(1)
#     Q = {u for u in range(m)}   # O(m)
#     while Q:                    # O(m) Iterationen:
#         (_,v) = min({(d[u],u) for u in Q if d[u]!= None}) # O(m)   
#         Q.remove(v)                                       # O(1)
#         for u in G[v]:                                    # O(deg(v))
#             alt = d[v] + G[v][u]                          # O(1)
#             if d[u]==None or alt < d[u]:                  # O(1)
#                 d[u] = alt                                # O(1)
#     return d                                              # O(1)


