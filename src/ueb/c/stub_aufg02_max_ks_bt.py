
# MAX KNAPSACK

# verwendet sol_max_ks, m_max_ks
from ueb.c.aufg02_max_ks_exh import sol_max_ks, m_max_ks

# vereinfachtes Backtracking-Kriterium:
#   Teilloesung noch zulaessig?
def K_max_ks(s,v,S,t):
    # todo
    return False

# Entwurfsmuster Backtracking
def max_ks_backtracking(s,v,S):
    opt = -1
    # todo
    return opt


# Bsp m=4, S=7
print(max_ks_backtracking([3,2,1,5],[3,1,1,4],7))
print(max_ks_backtracking([3,8,1,5],[3,1,1,4],8))
