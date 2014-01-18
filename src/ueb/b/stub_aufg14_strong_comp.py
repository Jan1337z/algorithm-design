

# verwendet dfs
from vl.lek03.dfs import dfs

# Umkehrgraph eines Digraphen
def reverse(G):
    # todo
    return []

# alle starken Zusammenhangskomponenten eines Digraphen
def strong_comp(G):
    C = []
    # todo
    return C


# gerichteter Graph
def define_diG():
    m = 10
    G = [set() for _ in range(m)]   # alle Mengen leer anlegen
    G[0] |= {2}
    G[1] |= {0,2}
    G[2] |= {0,7}
    G[3] |= {4}
    # G[4] |= 
    # G[5] |= 
    G[6] |= {7}
    G[7] |= {6}
    # G[8] |=
    G[9] |= {3,8}
    return G

G = define_diG()
Grev = reverse(G)

# G unveraendert
print(G == define_diG())
print(G == reverse(Grev))

print(strong_comp(G))
