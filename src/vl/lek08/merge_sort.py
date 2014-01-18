
#
# verwendet merge aus Uebung A.5
from ueb.a.aufg05_merge import merge
# 
def merge_sort(a):
    m = len(a)
    # 1. Rekursionsanker
    if m <= 1: return a        # O(1)
    # 2. Divide-Schritt
    a1 = a[:m//2]              # O(m)
    a2 = a[len(a1):]           # O(m)
    # 3. rekursive Aufrufe
    b1 = merge_sort(a1)        # ?
    b2 = merge_sort(a2)        # ?
    # 4. Conquer-Schritt
    b = merge(b1,b2)           # O(m)
    return b                   # O(1)

a = [53,24,-12,54,0,22,-12]
print(merge_sort(a))
