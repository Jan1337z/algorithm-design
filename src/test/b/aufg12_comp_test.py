import unittest
import ueb.b.aufg12_comp as candidate

class Test_comp(unittest.TestCase):
    
    def test_1(self):
        m = 10
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1,2}
        G[1] |= {0,2}
        G[2] |= {0,1,6,7}
        G[3] |= {4}
        G[4] |= {3}
        # G[5] |= 
        G[6] |= {2,7}
        G[7] |= {2,6}
        G[8] |= {9}
        G[9] |= {8}
        
        Z = candidate.comp(G)
        
        self.assertEquals(Z, [{0,1,2,6,7}, {3,4}, {5}, {8,9}])
        
    def test_2(self):
        m = 6
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1,2}
        G[1] |= {0,2}
        G[2] |= {0,1}
        G[3] |= {4,5}
        G[4] |= {3,5}
        G[5] |= {3,4}
        
        Z = candidate.comp(G)
        
        self.assertEquals(Z, [{0,1,2}, {3,4,5}])
        
    def test_3(self):
        m = 6
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1,2,3}
        G[1] |= {0,2}
        G[2] |= {0,1}
        G[3] |= {0,4,5}
        G[4] |= {3,5}
        G[5] |= {3,4}
        
        Z = candidate.comp(G)
        
        self.assertEquals(Z, [{0,1,2,3,4,5}])
        
    def test_4(self):
        m = 10
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        
        Z = candidate.comp(G)
        
        self.assertEquals(Z, [{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}])
        
    def test_5(self):
        m = 10
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        
        # vollstaendiger Graph
        for i in range(m):
            for j in range(m):
                if i != j:
                    G[i] |= {j}
        
        Z = candidate.comp(G)
        
        self.assertEquals(Z, [{0,1,2,3,4,5,6,7,8,9}])
        
    def test_6(self):
        m = 6
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1}
        G[1] |= {0}
        G[2] |= {3}
        G[3] |= {2}
        G[4] |= {5}
        G[5] |= {4}
        
        Z = candidate.comp(G)
        
        self.assertEquals(Z, [{0,1}, {2,3}, {4,5}])

# Testausfuehrung via PyShell
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_comp)
# unittest.TextTestRunner(verbosity=2).run(suite)    

