
# Multiplikation zweier m-Bit-Zahlen 
# nach Schulmethode in O(m) wg Addition in O(1)
# 

def mult_naiv(x,y):
    if x < 0:           # neg. VZ auf y uebertragen
        x,y = -x,-y
    erg = 0
    while x > 0:        # O(m)
        if x & 1:       # letztes Bit ist 1 
            erg += y    # O(1) 
        y <<= 1         # Linksshift, O(1)
        x >>= 1         # Rechtsshift, O(1)
    return erg

print(mult_naiv(12,13))
print(mult_naiv(-12,13))