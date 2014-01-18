
# sol_queen vorher deklarieren
from vl.lek04.queen_exh import sol_queen

# Backtracking-Kriterium
def K_queen(m,t):
    l = len(t)-1        # Index der neuen Dame
    for i in range(l):
        if t[i]==t[l] or abs(t[i]-t[l])==abs(i-l):
            return False
    return True

def queen_backtracking(m):
    M = {()}
    while M:
        t_prev = M.pop()
        for a in range(m):          # bei QUEEN ist k=m
            t = t_prev + (a,)       # neues Tupel
            if len(t) == m:
                if sol_queen(m,t): return 1,t
            else:
                if K_queen(m,t):
                    M.add(t)
                else:
                    pass
    return 0


# for m in range(2,15):
#     print('m =',m, queen_backtracking(m))