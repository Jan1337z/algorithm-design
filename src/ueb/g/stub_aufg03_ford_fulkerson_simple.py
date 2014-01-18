
# geaenderte Tiefensuche: Kanten mit Restkap r(e)=0 ignorieren
def dfs_not_0(G,s):
    # todo
    return set(), []    

#
from vl.lek12.ford_fulkerson import get_path
from vl.lek12.augment import bottleneck
from copy import deepcopy

# vereinfachte Implementierung von ford_fulkerson
def ford_fulkerson_simple(G,s,t):
    # a. in Gf schon alle Rueckwaertskanten mit (Rest-)Kapazitaet r(e)=0 einfuegen
    # todo
    # b. Pfad suchen, aber dabei Kanten mit r(e)=0 ignorieren
    # todo
    # c. Pfadkanten aktualisieren     
    # todo
    # d. Flusswert bestimmen
    return 0    

# Bsp
def define_G():
    G = [   {1:20, 2:10},  # Nachfolger von s (Quelle)
            {2:30, 3:10},  # von u
            {3:20},        # von v
            {}             # von t (Senke)
        ]
    return G

G = define_G()
print(ford_fulkerson_simple(G,0,3))


