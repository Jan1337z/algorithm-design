
# MAX KNAPSACK

# verwendet sol_max_ks, m_max_ks, K_max_ks 
from ueb.c.aufg02_max_ks_exh import sol_max_ks, m_max_ks
from ueb.c.aufg02_max_ks_bt import K_max_ks


# obere Schranke:
# Bewertung der Teilloesung t + Werte aller restlichen Gegenstaende
def o_max_ks(s,v,S,t):
    # todo
    return 0

# Entwurfsmuster Branch and Bound
def max_ks_bab(s,v,S):
    opt = -1
    # todo
    return opt


# Bsp m=4, S=7
print(max_ks_bab([3,2,1,5],[3,1,1,4],7))
print(max_ks_bab([3,8,1,5],[3,1,1,4],8))
