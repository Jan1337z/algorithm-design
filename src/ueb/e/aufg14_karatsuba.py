
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
    if(m < 16 and k < 16): # if both integers have less then 16 bit
        result = 0
        for _ in range(abs(y)):
            if(y < 0):
                result -= x
            else: 
                result += x
        
        return result
    # 2. Divide
    # laengere Zahl wird in der Mitte geteilt
    
    center = max(m,k)
    center_2 = center//2
    
    
    # x und y aufteilen
    
    x_h =   x>>center_2
    x_l =   x - (x_h<<center_2)
    y_h =   y>>center_2
    y_l =   y - (y_h<<center_2)
    
    
    # 3. Rekursionsaufrufe
    
    a = karatsuba(x_h, y_h)
    b = karatsuba(x_l, y_l)
    c = karatsuba((x_h+x_l),(y_h+y_l))
    # 4. Conquer
    return c - b - a

print(karatsuba(12,13))
print(karatsuba(-17,13))

