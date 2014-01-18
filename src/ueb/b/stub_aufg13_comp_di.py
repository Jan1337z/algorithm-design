
# verwendet comp
from ueb.b.aufg12_comp import comp

# alle Zusammenhangskomponenten eines Digraphen 
def comp_di(G):
    # todo
    return []
    
# Laufzeit ?


# gerichteter Graph
def define_diG():
    m = 10
    G = [set() for _ in range(m)]   # alle Mengen leer anlegen
    G[0] |= {2}
    G[1] |= {0,2}
    G[2] |= {0,1,7}
    G[3] |= {4}
    # G[4] |= 
    # G[5] |= 
    G[6] |= {2,7}
    G[7] |= {2,6}
    # G[8] |=
    G[9] |= {8}
    return G

# zugehöriger ungerichteter Graph: alle Kanten in beide Richtungen
def define_G():
    m = 10
    G = [set() for _ in range(m)]   # alle Mengen leer anlegen
    G[0] |= {1,2}
    G[1] |= {0,2}
    G[2] |= {0,1,6,7}
    G[3] |= {4}
    G[4] |= {3}
    # G[5] |= 
    G[6] |= {2,7}
    G[7] |= {2,6}
    G[8] |= {9}
    G[9] |= {8}
    return G


G = define_diG()
print(comp_di(G))
print(comp_di(G)==comp(define_G()))

