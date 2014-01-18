import unittest
import ueb.b.aufg11_bfs_numpaths as candidate

# Test mit ungerichteten Graphen
class Test_bfs_numpaths(unittest.TestCase):
    
    def test_1(self):
        m = 10
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1,2}
        G[1] |= {0,2,3,4}
        G[2] |= {0,1,4,6,7}
        G[3] |= {1,4}
        G[4] |= {1,2,3,5}
        G[5] |= {4}
        G[6] |= {2,7}
        G[7] |= {2,6}
        G[8] |= {9}
        G[9] |= {8}
        
        S = candidate.bfs_numpaths(G, 0)
        self.assertEqual(S, [1,1,1,1,2,2,1,1,0,0])
        
    def test_2(self):
        m = 10
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1,2}
        G[1] |= {0,2,3,4}
        G[2] |= {0,1,4,6,7}
        G[3] |= {1,4}
        G[4] |= {1,2,3,5}
        G[5] |= {4}
        G[6] |= {2,7}
        G[7] |= {2,6}
        G[8] |= {9}
        G[9] |= {8}
        
        S = candidate.bfs_numpaths(G, 4)
        self.assertEqual(S, [2,1,1,1,1,1,1,1,0,0])
        
    def test_3(self):
        m = 10
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1,2}
        G[1] |= {0,2,3,4}
        G[2] |= {0,1,4,6,7}
        G[3] |= {1,4}
        G[4] |= {1,2,3,5}
        G[5] |= {4}
        G[6] |= {2,7}
        G[7] |= {2,6}
        G[8] |= {9}
        G[9] |= {8}
        
        S = candidate.bfs_numpaths(G, 6)
        self.assertEqual(S, [1,1,1,2,1,1,1,1,0,0])
        
    def test_4(self):
        m = 1
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
                
        S = candidate.bfs_numpaths(G, 0)
        self.assertEqual(S, [1])
        
    def test_5(self):
        m = 2
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1}
        G[1] |= {0}
                
        S = candidate.bfs_numpaths(G, 0)
        self.assertEqual(S, [1, 1])
        
    def test_6(self):
        m = 8
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1,2}
        G[1] |= {0,3}
        G[2] |= {0,3,4}
        G[3] |= {1,2,5}
        G[4] |= {2,5,6}
        G[5] |= {3,4,6}
        G[6] |= {4,5,7}
        G[7] |= {6}
                
        S = candidate.bfs_numpaths(G, 0)
        self.assertEqual(S, [1, 1, 1, 2, 1, 3, 1, 1])
        
    def test_7(self):
        m = 8
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1,2,3,4,5,6,7}
        G[1] |= {0}
        G[2] |= {0}
        G[3] |= {0}
        G[4] |= {0}
        G[5] |= {0}
        G[6] |= {0}
        G[7] |= {0}
                
        S = candidate.bfs_numpaths(G, 0)
        self.assertEqual(S, [1, 1, 1, 1, 1, 1, 1, 1])
        
    def test_8(self):
        m = 8
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1,2,3}
        G[1] |= {0,4,5}
        G[2] |= {0,5}
        G[3] |= {0,5}
        G[4] |= {1,5,7}
        G[5] |= {1,2,3,4,6,7}
        G[6] |= {5}
        G[7] |= {4,5}
                
        S = candidate.bfs_numpaths(G, 0)
        self.assertEqual(S, [1, 1, 1, 1, 1, 3, 3, 4])
        
    def test_9(self):
        m = 8
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        
        # vollstaendiger Graph
        for i in range(m):
            for j in range(m):
                if i != j:
                    G[i] |= {j}
                
        S = candidate.bfs_numpaths(G, 0)
        self.assertEqual(S, [1, 1, 1, 1, 1, 1, 1, 1])
        
    def test_10(self):
        m = 8
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        
        # vollstaendiger Graph
        for i in range(m):
            for j in range(m):
                if i != j:
                    G[i] |= {j}
                
        S = candidate.bfs_numpaths(G, 4)
        self.assertEqual(S, [1, 1, 1, 1, 1, 1, 1, 1])

# Testausfuehrung via PyShell
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_bfs_numpaths)
# unittest.TextTestRunner(verbosity=2).run(suite)    
