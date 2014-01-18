import unittest
import ueb.b.aufg14_strong_comp as candidate

class Test_strong_comp(unittest.TestCase):
    
    def test_1(self):
        m = 10
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {2}
        G[1] |= {0,2}
        G[2] |= {0,1,6,7}
        G[3] |= {4}
        G[4] |= {3}
        # G[5] |= 
        # G[6] |= 
        G[7] |= {2,6}
        G[8] |= {9}
        # G[9] |=
        
        Z = candidate.strong_comp(G)
        
        self.assertEquals(Z, [{0,1,2,7}, {3,4}, {5}, {6}, {8}, {9}])
        
    def test_2(self):
        m = 6
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1}
        G[1] |= {2}
        G[2] |= {0}
        # G[3] |= 
        G[4] |= {3,5}
        #G[5] |= 
                
        Z = candidate.strong_comp(G)
        
        self.assertEquals(Z, [{0, 1, 2}, {3}, {4}, {5}])
        
    def test_3(self):
        m = 6
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1,2,3}
        G[1] |= {0,2}
        G[2] |= {0,1}
        G[3] |= {0,4,5}
        G[4] |= {3,5}
        G[5] |= {3,4}
        
        Z = candidate.strong_comp(G)
        
        self.assertEquals(Z, [{0,1,2,3,4,5}])
        
    def test_4(self):
        m = 10
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        
        Z = candidate.strong_comp(G)
        
        self.assertEquals(Z, [{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}])
        
    def test_5(self):
        m = 10
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        
        # vollstaendiger Graph
        for i in range(m):
            for j in range(m):
                if i != j:
                    G[i] |= {j}
        
        Z = candidate.strong_comp(G)
        
        self.assertEquals(Z, [{0,1,2,3,4,5,6,7,8,9}])
        
    def test_6(self):
        m = 6
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        # G[0] |= 
        G[1] |= {0}
        G[2] |= {3}
        G[3] |= {2}
        G[4] |= {5}
        # G[5] |= 
        
        Z = candidate.strong_comp(G)
        
        self.assertEquals(Z, [{0}, {1}, {2, 3}, {4}, {5}])
        
    def test_7(self):
        m = 10
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {2}
        G[1] |= {0,2}
        G[2] |= {0,1,7}
        G[3] |= {4}
        # G[4] |= 
        # G[5] |= 
        G[6] |= {2,7}
        G[7] |= {2,6}
        # G[8] |=
        G[9] |= {8}
        
        Z = candidate.strong_comp(G)
        
        self.assertEquals(Z, [{0, 1, 2, 6, 7}, {3}, {4}, {5}, {8}, {9}])
        
    def test_8(self):
        m = 10
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {2}
        G[1] |= {0,2}
        G[2] |= {0,7}
        G[3] |= {4}
        # G[4] |= 
        # G[5] |= 
        G[6] |= {7}
        G[7] |= {6}
        # G[8] |=
        G[9] |= {3,8}
        
        Z = candidate.strong_comp(G)
        
        self.assertEquals(Z, [{0, 2}, {1}, {3}, {4}, {5}, {6, 7}, {8}, {9}])
        
    def test_9(self):
        m = 1
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        
        Z = candidate.strong_comp(G)
        
        self.assertEquals(Z, [{0}])

# Testausfuehrung via PyShell
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_strong_comp)
# unittest.TextTestRunner(verbosity=2).run(suite)
