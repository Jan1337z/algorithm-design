
# MAXIMUM INTERVAl SCHEDULING

# Greedy
# Eingabe als Liste von Intervallen (s,f) sortiert nach Endezeit f
# 
def max_intsched_greedy(L):
    A = {0}                     # Intervall 0 hat frueheste Endezeit
    (_,last) = L[0]             # letzte Endezeit in A merken
    for i in range(1,len(L)):   # Intervalle nach f sortiert
        (s,f) = L[i]            # aktuelles Intervall
        if s >= last:           # falls keine Ueberschneidung:   
            A.add(i)                # Loesung erweitern
            last = f
    return A

# Bsp aus der VL
L = [(0,3),(0,4),(4,6),(5,7),(8,10),(0,12),(9,13),(15,16),(14,17)]
print(max_intsched_greedy(L))
