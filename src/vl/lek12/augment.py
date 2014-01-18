

# bestimme kleinste Restkapazitaet entlang P 
# Kapazitaeten im Residualgraph Gf sind stets > 0
def bottleneck(P,Gf):
    b = Gf[P[0]][P[1]]
    for i in range(1,len(P)-1):         # O(len(P)) 
        b = min(b, Gf[P[i]][P[i+1]])
    return b

# Eingabe: Fluss f, Pfad P, Erhoehungsbetrag b
# Fluss f wird um b entlang Pfad P erhoeht
# P ist Pfad im Residualgraph und enthaelt ggf. Rueckwaertskanten
def augment(f,P,b):
    for i in range(len(P)-1):   # fuer alle Kanten in P, daher O(len(P))
        e = (P[i],P[i+1])       
        if e in f:              # e ist Vorwaertskante:
            f[e] += b           #   erhoehe Fluss um b
        else:                   # e ist Rueckwaertskante
            (u,v) = e           #   verringere Fluss um b
            f[v,u] -= b         #   auf zugehoeriger Vorwaertskante
    return f

# weiterer Pfad in Gf mit Wert 10 moeglich, vgl. Bsp 12.9 und 12.11
from vl.lek12.residual_graph import Gf,f
P = [0,2,1,3]           # (s,v,u,t)
b = bottleneck(P,Gf)    # Wert 10
# f um b entlang P erhoehen
f = augment(f,P,b)
print('f nach augment:',f)
