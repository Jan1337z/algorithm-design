

# Kantenmenge E fuer Graphen  
def edgeset(G):
    E = set()                   
    # todo
    return E

# Kantenmenge E fuer Digraphen 
def edgeset_di(G):
    E = set()     
    # todo
    return E


# Bsp Graph
def define_G1():
    G = [set() for _ in range(8)]   # alle Mengen leer anlegen
    G[0] |= {1}
    G[1] |= {0,2}
    G[2] |= {1,3,4}               
    G[3] |= {2,4,6,7}
    G[4] |= {2,3}
    G[6] |= {3,7}
    G[7] |= {3,6}
    return G

# Bsp Digraph
def define_G2():
    G = [set() for _ in range(8)]   # alle Mengen leer anlegen
    G[0] |= {1}
    G[1] |= {0,2}
    G[2] |= {1,4}               
    G[3] |= {2,4,7}
    G[4] |= {2,3,5}
    G[5] |= {3,4}
    G[6] |= {7}
    return G

G = define_G1()
print(edgeset(G))

G = define_G2()
print(edgeset_di(G))
