
# CLOSEST PAIR
# 

# erzeuge sortierte Listen Vx und Vy fuer die Eingabe, O(m log m)
from operator import itemgetter
def make_initial_lists(U):
    #
    # Vx-Index ergaenzen und nach y-Koordninaten sortieren
    Vy = []
    #
    # Vy-Index ergaenzen und nach x-Koordninaten sortieren 
    Vx = []
    #
    return Vx,Vy 

# bestimme Paar mit kleinstem Abstand in Sy, O(#Sy)
#   darf nur aufgerufen werden, falls #Sy >= 2
def find_min(Sy):
    # betrachte fuer jeden Punkt die 15 naechsten Punkte
    # in der Liste, Paar mit min. Distanz merken
    return (0,0),(0,0)

# von aussen aufzurufende Funktion
from vl.lek08.cp_all_pairs import d
def cp(U):
    Vx,Vy = make_initial_lists(U)
    (p,q)=cp_dac(Vx,Vy)
    print(p,q)
    return d(p,q)

# Entwurfsmuster DaC
def cp_dac(Vx, Vy):
    m = len(Vx)
    #
    # 1. Rekursionsanker, fuer m=2 und m=3
    #
    # 2. Divide
    k = m//2        # Mitte  
    # Vy durchlaufen und in Ly und Ry aufteilen
    #   abh. davon, ob Referenz in li. oder re. Haelfte zeigt
    #
    # Vx aufteilen in Lx und Ly
    #
    # Referenzen Lx -> Ly und Rx -> Ry aktualisieren
    #
    # 3. Rekursionsaufrufe
    (l0,l1)=cp_dac(Lx, Ly)
    (r0,r1)=cp_dac(Rx, Ry)
    #
    # 4. Conquer
    # beste Teilloesung steht in l0,l1
    delta = d(l0,l1)
    if delta > d(r0,r1):
        delta, l0, l1 = d(r0,r1), r0, r1
    # Trennlinie
    x_T = Lx[-1][0]
    # Sy bestimmen 
    # falls #Sy<2, dann ist l0,l1 optimal
    if len(Sy)>=2:
        (s0,s1) = find_min(Sy)
        if d(s0,s1)<delta: return (s0,s1)
    return l0,l1


