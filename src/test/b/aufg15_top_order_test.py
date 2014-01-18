from collections import deque
import unittest
import ueb.b.aufg15_top_order as candidate

def check_toporder(G, toporder):
    
    m = len(G)
    indeg = {u:0 for u in range(m)}
    for u in range(m):
        for v in G[u]:
            indeg[v] += 1
    
    Q = deque(toporder)  
    
    while Q:
        v = Q.popleft()
        if indeg[v] != 0:
            return False
        else:
            for u in G[v]:
                indeg[u] -= 1
    
    return True

class Test_top_order(unittest.TestCase):
    
    def test_1(self):
        m = 7
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1,2,3}
        G[1] |= {2,4}
        G[2] |= {6}
        G[3] |= {6}
        G[4] |= {2}
        G[5] |= {2,4,6}
        # G[6] |= 
        
        t = candidate.top_order(G)
        self.assertTrue(check_toporder(G, t))
    
    def test_2(self):
        m = 3
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1}
        G[1] |= {2}
        G[2] |= {1}
        
        t = candidate.top_order(G)
        self.assertTrue(t[-1] == 'G nicht kreisfrei')
        
    def test_3(self):
        m = 6
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1,2}
        G[1] |= {4,5}
        G[2] |= {3,5}
        G[3] |= {5}
        G[4] |= {5}
        # G[5] |= 
        
        t = candidate.top_order(G)
        self.assertTrue(check_toporder(G, t))
        
    def test_4(self):
        m = 6
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1,2}
        G[1] |= {4,5}
        G[2] |= {3,5}
        G[3] |= {5}
        G[4] |= {5}
        G[5] |= {4} 
        
        t = candidate.top_order(G)
        self.assertTrue(t[-1] == 'G nicht kreisfrei')
        
    def test_5(self):
        m = 7
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1,2}
        G[1] |= {3}
        G[2] |= {3}
        G[3] |= {4,5}
        G[4] |= {6}
        G[5] |= {6} 
        
        t = candidate.top_order(G)
        self.assertTrue(check_toporder(G, t))
        
    def test_6(self):
        m = 9
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1,2,3,4}
        G[1] |= {5}
        G[2] |= {6}
        G[3] |= {6}
        G[4] |= {6}
        G[5] |= {7,8}
        G[6] |= {7}
        # G[7] |=
        # G[8] |= 
        
        t = candidate.top_order(G)
        self.assertTrue(check_toporder(G, t))
        
    def test_7(self):
        m = 6
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1,2,3,4,5}
        
        t = candidate.top_order(G)
        self.assertTrue(check_toporder(G, t))
        
    def test_8(self):
        m = 6
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        
        t = candidate.top_order(G)
        self.assertTrue(check_toporder(G, t))
        
    def test_9(self):
        m = 2
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1}
        G[1] |= {0}
        
        t = candidate.top_order(G)
        self.assertTrue(t[-1] == 'G nicht kreisfrei')

# Testausfuehrung via PyShell
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_top_order)
# unittest.TextTestRunner(verbosity=2).run(suite)
