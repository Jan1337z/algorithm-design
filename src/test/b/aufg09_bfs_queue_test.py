import unittest
import ueb.b.aufg09_bfs_queue as candidate


# Test mit Graphen und Digraphen
class Test_bfs_queue(unittest.TestCase):
    
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
        
        r_test = {0,1,2,3,4,5,6,7}
        p1_test = [None, 0, 0, 1, 1, 4, 2, 2, None, None]
        p2_test = [None, 0, 0, 1, 2, 4, 2, 2, None, None]
        
        (r, p) = candidate.bfs_queue(G, 0)
        
        self.assertEqual(r, r_test)
        self.assertTrue(p == p1_test or p == p2_test)
        
    def test_2(self):
        m = 5
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1,2}
        G[1] |= {0,3}
        G[2] |= {0}
        G[3] |= {1,4}
        G[4] |= {3}
        
        
        r_test = {0,1,2,3,4}
        p_test = [None, 0, 0, 1, 3]
        
        (r, p) = candidate.bfs_queue(G, 0)
        
        self.assertEqual(r, r_test)
        self.assertEqual(p, p_test)
        
    def test_3(self):
        m = 1
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        
        r_test = {0}
        p_test = [None]
        
        (r, p) = candidate.bfs_queue(G, 0)
        
        self.assertEqual(r, r_test)
        self.assertEqual(p, p_test)
        
    def test_4(self):
        m = 5
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        
        r_test = {0}
        p_test = [None]*m
        
        (r, p) = candidate.bfs_queue(G, 0)
        
        self.assertEqual(r, r_test)
        self.assertEqual(p, p_test)
        
    def test_5(self):
        m = 7
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1,2}
        G[1] |= {0,3}
        G[2] |= {0}
        G[3] |= {1,4}
        G[4] |= {3}
        G[5] |= {6}
        G[6] |= {5}
        
        r_test = {5,6}
        p_test = [None, None, None, None, None, None, 5]
        
        (r, p) = candidate.bfs_queue(G, 5)
        
        self.assertEqual(r, r_test)
        self.assertEqual(p, p_test)
        
    def test_6(self):
        m = 7
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1,2}
        G[1] |= {0,3}
        G[2] |= {0}
        G[3] |= {1,4}
        G[4] |= {3}
        
        r_test = {5}
        p_test = [None, None, None, None, None, None, None]
        
        (r, p) = candidate.bfs_queue(G, 5)
        
        self.assertEqual(r, r_test)
        self.assertEqual(p, p_test)
    
    def test_7(self):
        m = 7
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        
        # vollstaendiger Graph
        for i in range(m):
            for j in range(m):
                if i != j:
                    G[i] |= {j}
        
        r_test = set(range(m))
        p_test = [None, 0, 0, 0, 0, 0, 0]
        
        (r, p) = candidate.bfs_queue(G, 0)
        
        self.assertEqual(r, r_test)
        self.assertEqual(p, p_test)
        
    def test_8(self):
        m = 7
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1}
        G[1] |= {0,2}
        G[2] |= {1,3}
        G[3] |= {2,4}
        G[4] |= {3,5}
        G[5] |= {4,6}
        G[6] |= {5}
        
        r_test = set(range(m))
        p_test = [None, 0, 1, 2, 3, 4, 5]
        
        (r, p) = candidate.bfs_queue(G, 0)
        
        self.assertEqual(r, r_test)
        self.assertEqual(p, p_test)
        
    def test_9(self):
        m = 10
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1,2}
        G[1] |= {2,3,4}
        G[2] |= {4,6,7}
        G[3] |= {4}
        G[4] |= {5}
        
        G[6] |= {7}
        
        G[8] |= {9}
        
        r_test = {0,1,2,3,4,5,6,7}
        p1_test = [None, 0, 0, 1, 1, 4, 2, 2, None, None]
        p2_test = [None, 0, 0, 1, 2, 4, 2, 2, None, None]
        
        (r, p) = candidate.bfs_queue(G, 0)
        
        self.assertEqual(r, r_test)
        self.assertTrue(p == p1_test or p == p2_test)
        
    def test_10(self):
        m = 10
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        G[0] |= {1}
        G[1] |= {2,3,4}
        G[2] |= {0,4,6,7}
        G[3] |= {4}
        G[4] |= {5}
        
        G[6] |= {7}
        
        G[8] |= {9}
        
        r_test = {0,1,2,3,4,5,6,7}
        p1_test = [None, 0, 1, 1, 1, 4, 2, 2, None, None]
        p2_test = [None, 0, 1, 1, 2, 4, 2, 2, None, None]
        
        (r, p) = candidate.bfs_queue(G, 0)
        
        self.assertEqual(r, r_test)
        self.assertTrue(p == p1_test or p == p2_test)
        
    def test_11(self):
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
        
        r_test = {8,9}
        p_test = [None, None, None, None, None, None, None, None, None, 8]
        
        (r, p) = candidate.bfs_queue(G, 8)
        
        self.assertEqual(r, r_test)
        self.assertTrue(p == p_test)

# Testausfuehrung via PyShell
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_bfs_queue)
# unittest.TextTestRunner(verbosity=2).run(suite)
