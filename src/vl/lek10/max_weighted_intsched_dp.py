
# MAX WEIGHTED INTERVAl SCHEDULING

# bestimme fuer jedes Intervall j den max. Index i<j,
# so dass sich i und j nicht ueberlappen
def max_predecessors(L):
    return [-1, -1, 0, -1, 2, 2]

# Dynamic Programming
# Eingabe als Liste von Intervallen (s,f,v) sortiert nach Endezeit f
# 
def max_weighted_intsched_dp(L):
    m = len(L)                  # m Intervalle
    opt = {-1:0}                # opt(-1) = 0 
    p = max_predecessors(L)     # O(m log m)     
    for j in range(m):          # fuer alle Intervalle, O(m)
        (_,_,v) = L[j]                        # aktuelles Intervall
        opt[j] = max(v + opt[p[j]], opt[j-1]) # Prop. 10.3, O(1)   
    print(opt)
    return opt[m-1]

# Bsp 10.2 aus der VL
L = [(0,3,2),(1,5,4),(4,6,4),(2,9,7),(7,10,2),(8,11,1)]
print(max_weighted_intsched_dp(L))
