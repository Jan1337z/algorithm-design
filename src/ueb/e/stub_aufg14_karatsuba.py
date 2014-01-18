
# Multiplikation zweier m-Bit-Zahlen 
# nach Entwurfsmuster DaC (Karatsuba)
# 
# setze fuer Add./Substr. O(m) an
#

def karatsuba(x,y):
    m,k = x.bit_length(), y.bit_length()
    #
    # 1. Rekursionsanker
    # Multiplikation durch konstant viele Additionen
    #
    #
    # 2. Divide
    # laengere Zahl wird in der Mitte geteilt
    #
    #
    # x und y aufteilen
    #
    # 3. Rekursionsaufrufe
    #
    #
    # 4. Conquer
    return 0

print(karatsuba(12,13))
print(karatsuba(-17,13))

