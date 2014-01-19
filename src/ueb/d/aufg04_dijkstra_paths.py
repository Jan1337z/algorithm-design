
# (SINGLE-SOURCE) SHORTEST PATH

# Ergaenzung von dijkstra um Pfade

def dijkstra_paths(G,s):
    m = len(G)
    # predecessor list p 
    p = [None]*m 
    
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
                # important:
                # only  change the predecessor if
                # you update the costs 
                p[u] = v
    return d, p


# s-v-Pfad bestimmen
def shortest_path(s,v,p):
    if(v == s):
        return [s]
    else:
        return shortest_path(s,p[v],p) + [v] 


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
d,p = dijkstra_paths(G,0)

print(shortest_path(0,3,p))
print(shortest_path(0,0,p))

