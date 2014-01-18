
# Bellman-Ford: INT SHORTEST PATH via DP


# Dynamic Programming
# Eingabe: Digraph ohne negative Kreise, Startknoten s
# Aufruf erfolgt mit Umkehrgraph wegen Zugriff auf Vorgaenger
# 
def bellman_ford(G,s):
    m = len(G)
    opt = [[None]*m]                # Init. fuer i = 0
    opt[0][s] = 0
    for i in range(1,m):            # fuer alle Pfadlaengen
        opt.append(opt[i-1][:])     # Kopie uebernehmen
        for v in range(m):          # Pfadlaenge i ggf. aktualisieren
            # Vorgaenger von v via Umkehrgraph: 
            #   (u,v) Kante in G gdw (v,u) Kante in Grev
            for u in G[v]:          # Vorgaenger (!) u von v
                if opt[i-1][u] != None:             # schon erreicht?   
                    alt = opt[i-1][u] + G[v][u]     # c(v,u) statt c(u,v) wg Grev
                    # Verbesserung?
                    if opt[i][v]== None or alt < opt[i][v]:
                        opt[i][v] = alt        
    print(opt)
    return opt[m-1]


# Umkehrgraph eines Digraphen mit Kantengewichten (vgl. Aufgabe B.14)
def reverse_weighted(G):
    m = len(G)
    Grev = [{} for _ in range(m)]
    for u in range(m):
        for v,c in G[u].items():
            Grev[v][u] = c
    return Grev


# Bsp 11.2 aus der VL
# Knotennummern: s=0, u=1, w=2, v=3
def define_G():
    G = [   {1:2, 3:1},        # Nachfolger von s
            {2:3},             # von u
            {3:-6},            # von w
            {}                 # von v
        ]
    return G

G = define_G()
print(bellman_ford(reverse_weighted(G),0))

