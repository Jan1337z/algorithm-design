
# MAX WEIGHTED INTERVAl SCHEDULING
# inkl. Bestimmung einer opt. Loesung


from ueb.f.aufg01_max_pred import max_predecessors

# Bestimme A_opt rekursiv
def find_sol(j, opt, p, A = None):
    # todo 
    return A

# Dynamic Programming
# Eingabe als Liste von Intervallen (s,f,v) sortiert nach Endezeit f
#
# NEU: Ausgabe einer optimalen Loesung
def max_weighted_intsched_dp_sol(L):
    # 
    return set()

# Bsp 10.2 aus der VL
L = [(0,3,2),(1,5,4),(4,6,4),(2,9,7),(7,10,2),(8,11,1)]
print(max_weighted_intsched_dp_sol(L))
