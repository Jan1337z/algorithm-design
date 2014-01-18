
# Flussnetzwerk Bsp 12.2 aus der VL
# Knotennummern: s=0, u=1, v=2, t=3
# Kantenkosten = Kapazitaeten
def define_G():
    G = [   {1:20, 2:10},  # Nachfolger von s (Quelle)
            {2:30, 3:10},  # von u
            {3:20},        # von v
            {}             # von t (Senke)
        ]
    return G

G = define_G()
print('G:',G)

# Repraesentation eines Flusses als Abb: E -> R^+
f = {(u,v):0 for u in range(len(G)) for v in G[u]}  # O(m+k)
# Fluss aus Bsp. 12.7
f[0,1]=20
f[1,2]=20
f[2,3]=20
print('f:',f)


# bestimme Residualgraph mit Vorwaerts- und Rueckwaertskanten
# zu gegebenem Flussnetzwerk G und Fluss f in O(m+k)
def residual_graph(G,f):
    m = len(G)
    Gf = [{} for _ in range(m)]     # O(m)
    for u in range(m):              # fuer alle e in G, O(m+k)
        for v in G[u]:
            if f[u,v] < G[u][v]:    # Restkapazitaet > 0, also Vorwaertskante einfuegen
                Gf[u][v] = G[u][v] - f[u,v]
            if f[u,v] > 0:          # Fluss > 0, also Rueckwaertskante einfuegen
                Gf[v][u] = f[u,v]
    return Gf

# Vgl. Beispiel 12.9
Gf = residual_graph(G,f)
print('Gf:',Gf)
