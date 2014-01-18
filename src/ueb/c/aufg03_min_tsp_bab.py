
# Min TSP

# verwendet m_min_tsp
from ueb.c.aufg03_min_tsp_exh import m_min_tsp

# untere Schranke:
#  Kosten der Teilstrecke p ohne Rueckweg
def u_min_tsp(D,p):
    if len(p) == 0: return 0
    cost = 0
    current = 0
    for destination in range(1,len(p)):
        cost += D[p[current]][p[destination]]
        current = destination   
    return cost


# Entwurfsmuster Branch and Bound
def min_tsp_bab(D):
    opt = float("inf")
    m = len(D)
    M = [()]
    while M:
        t_prev = M.pop()
        if u_min_tsp(D,t_prev) < opt:
            for a in range(m):
                t = t_prev + (a,)
                if len(t) == len(set(t)):
                    if len(t) == m:
                            t_value = m_min_tsp(m, D, t)
                            if(t_value < opt): opt = t_value
                    else: 
                        M.append(t)
                
                
    return opt


# print(min_tsp_bab([[0,1,1],[1,0,1],[1,1,0]]))
# print(min_tsp_bab([[0,13,2],[7,0,2],[3,8,0]]))
# print(min_tsp_bab([[0,13,2],[7,0,2],[1,8,0]]))

