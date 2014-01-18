
# liefert dict mit (v:indeg(v))-Paaren in O(m+k)
def indeg(G):
    # todo
    return {}

# topologische Sortierung und Test auf Kreisfreiheit fuer Digraphen
# defaults werden bei Fktdeklaration ausgewertet
# count = (Rest-)Knotenmenge mit verbleibendem Eingangsgrad
def top_order(G, count = None, order = None):
    # to do
    return order

# Digraph ohne Kreis
def define_diG1():
    m = 7
    G = [set() for _ in range(m)]   # alle Mengen leer anlegen
    G[0] |= {1,2,3}
    G[1] |= {2,4}
    G[2] |= {6}
    G[3] |= {6}
    G[4] |= {2}
    G[5] |= {2,4,6}
    # G[6] |= 
    return G

# Digraph mit Kreis
def define_diG2():
    m = 3
    G = [set() for _ in range(m)]   # alle Mengen leer anlegen
    G[0] |= {1}
    G[1] |= {2}
    G[2] |= {1}
    return G

G = define_diG1()
print(top_order(G))

G = define_diG2()
print(top_order(G))

