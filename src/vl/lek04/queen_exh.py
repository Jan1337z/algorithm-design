

# a NiCHT in sol(m) gdw.
#   es ex. i<j mit ... ODER ... 
#
def sol_queen(m,a):
    for i in range(m):
        for j in range(i+1,m):
            if a[i]==a[j] or abs(a[i]-a[j])==abs(i-j):
                return False
    return True

from itertools import product

def queen_exhaustive(m):
    # alle Kandidaten aus {0,..,m-1}^m
    for a in product(range(m),repeat=m):    
        if sol_queen(m,a):
            return 1, a
    return 0



# for m in range(2,10):
#     print('m =',m, queen_exhaustive(m))


# Laufzeit
#
# def sol_queen(m,a):
#     for i in range(m):                # O(m)
#         for j in range(i+1,m):        # O(m)
#             if a[i]==a[j] or abs(a[i]-a[j])==abs(i-j):    # O(1)
#                 return False                              # O(1)
#     return True                                           # O(1)

# def queen_exhaustive(m):
#     # alle Kandidaten aus {0,..,m-1}^(m-1)
#     for a in product(range(m),repeat=m):    # O(m^m)
#         if sol_queen(m,a):                  # O(m^2)
#             return 1, a                     # O(1)
#     return 0                                # O(1)