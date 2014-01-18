
# MAX KNAPSACK

# verwendet sol_max_ks, m_max_ks
from ueb.c.aufg02_max_ks_exh import sol_max_ks, m_max_ks

# vereinfachtes Backtracking-Kriterium:
#   Teilloesung noch zulaessig?
def K_max_ks(s,v,S,t):
    return sol_max_ks(s, v, S, t)

# Entwurfsmuster Backtracking
def max_ks_backtracking(s,v,S):
    m = len(s)
    opt = -1
    M = {()}
    while M:
        t_prev = M.pop()
        for a in range(2):
            t = t_prev + (a,)
            if K_max_ks(s, v, S, t):
                if len(t) == m:
                    c = m_max_ks(s, v, S, t)
                    if c > opt: opt = c
                else:
                    if K_max_ks(s, v, S, t):
                        M.add(t)
                    else:
                        pass
        
    return opt


# Bsp m=4, S=7
# print(max_ks_backtracking([3,2,1,5],[3,1,1,4],7))
# print(max_ks_backtracking([3,8,1,5],[3,1,1,4],8))
