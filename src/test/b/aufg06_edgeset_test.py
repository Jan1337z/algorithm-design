import unittest
import ueb.b.aufg06_edgeset as candidate

# Testfaelle fuer Graphen und Digraphen, leere Graphen, vollst. Graphen usw.
class Test_edgeset(unittest.TestCase):
    
    # Tests edgeset
    def test_1(self):
        G = [set() for _ in range(8)]   # alle Mengen leer anlegen
        G[0] |= {1}
        G[1] |= {0,2}
        G[2] |= {1,3,4}
        G[3] |= {2,4,6,7}
        G[4] |= {2,3}
        G[6] |= {3,7}
        G[7] |= {3,6}
        
        E = candidate.edgeset(G)
        self.assertEqual(E, {frozenset({0,1}), frozenset({1,0}), frozenset({1,2}), frozenset({2,1}), frozenset({2,3}), frozenset({2,4}), frozenset({3,2}), frozenset({3,4}), frozenset({3,6}), frozenset({3,7}), frozenset({4,2}), frozenset({4,3}), frozenset({6,3}), frozenset({6,7}), frozenset({7,3}), frozenset({7,6})})
        
    def test_2(self):
        G = [set() for _ in range(4)]   # alle Mengen leer anlegen
        G[0] |= {1, 2}
        G[1] |= {0,2}
        G[2] |= {0,1,3}               
        G[3] |= {2}
        
        E = candidate.edgeset(G)
        self.assertEqual(E, {frozenset([0,1]), frozenset([0,2]), frozenset([1,2]), frozenset([2,3])})
        
    def test_3(self):
        G = [set() for _ in range(4)]   # alle Mengen leer anlegen
        G[0] |= set()
        G[1] |= set()
        G[2] |= set()               
        G[3] |= set()
        
        E = candidate.edgeset(G)
        self.assertEqual(E, set())
        
    def test_4(self):
        G = [set() for _ in range(1)]   # alle Mengen leer anlegen
        G[0] |= set()
        
        E = candidate.edgeset(G)
        self.assertEqual(E, set())
        
    def test_5(self):
        G = [set() for _ in range(2)]   # alle Mengen leer anlegen
        G[0] |= {1}
        G[1] |= {0}
        
        E = candidate.edgeset(G)
        self.assertEqual(E, {frozenset([0,1])})
        
    def test_6(self):
        G = [set() for _ in range(5)]   # alle Mengen leer anlegen
        G[0] |= {1,4}
        G[1] |= {0,2}
        G[2] |= {1,3}
        G[3] |= {2,4}
        G[4] |= {3,0}
        
        E = candidate.edgeset(G)
        self.assertEqual(E, {frozenset([0,1]), frozenset([0,4]), frozenset([1,2]), frozenset([2,3]), frozenset([3,4])})
        
    def test_7(self):
        m = 7
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        for i in range(m):
            for j in range(m):
                if i != j:
                    G[i] |= {j}
                    
        E = candidate.edgeset(G)
        E_test = set()
        for i in range(m):
            for j in range(m):
                if i != j:
                    E_test |= {frozenset([i,j])}
                    
        self.assertEqual(E, E_test)
        
    
    # Tests edgeset_di
    def test_8(self):
        G = [set() for _ in range(8)]   # alle Mengen leer anlegen
        G[0] |= {1}
        G[1] |= {0,2}
        G[2] |= {1,3,4}               
        G[3] |= {2,4,6,7}
        G[4] |= {2,3}
        G[6] |= {3,7}
        G[7] |= {3,6}
        
        E = candidate.edgeset_di(G)
        self.assertEqual(E, {(0,1), (1,0), (1,2), (2,1), (2,3), (2,4), (3,2), (3,4), (3,6), (3,7), (4,2), (4,3), (6,3), (6,7), (7,3), (7,6)})
        
    def test_9(self):
        G = [set() for _ in range(4)]   # alle Mengen leer anlegen
        G[0] |= {1, 2}
        G[1] |= {0,2}
        G[2] |= {3}               
        G[3] |= {2}
        
        E = candidate.edgeset_di(G)
        self.assertEqual(E, {(0,1), (0,2), (1,0), (1,2), (2,3), (3,2)})
        
    def test_10(self):
        G = [set() for _ in range(4)]   # alle Mengen leer anlegen
        G[0] |= set()
        G[1] |= set()
        G[2] |= set()               
        G[3] |= set()
        
        E = candidate.edgeset_di(G)
        self.assertEqual(E, set())
        
    def test_11(self):
        G = [set() for _ in range(1)]   # alle Mengen leer anlegen
        G[0] |= set()
        
        E = candidate.edgeset_di(G)
        self.assertEqual(E, set())
        
    def test_12(self):
        G = [set() for _ in range(2)]   # alle Mengen leer anlegen
        G[0] |= {1}
        G[1] |= {0}
        
        E = candidate.edgeset_di(G)
        self.assertEqual(E, {(0,1), (1,0)})
        
    def test_13(self):
        G = [set() for _ in range(5)]   # alle Mengen leer anlegen
        G[0] |= {1,4}
        G[1] |= {0,2}
        G[2] |= {1,3}
        G[3] |= {2,4}
        G[4] |= {3,0}
        
        E = candidate.edgeset_di(G)
        self.assertEqual(E, {(0,1), (0,4), (1,0), (1,2), (2,1), (2,3), (3,2), (3,4), (4,3), (4,0)})
        
    def test_14(self):
        m = 7
        G = [set() for _ in range(m)]   # alle Mengen leer anlegen
        for i in range(m):
            for j in range(m):
                if i != j:
                    G[i] |= {j}
                    
        E = candidate.edgeset_di(G)
        E_test = set()
        for i in range(m):
            for j in range(m):
                if i != j:
                    E_test |= {(i,j)}
                    
        self.assertEqual(E, E_test)

# Testausfuehrung via PyShell
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_edgeset)
# unittest.TextTestRunner(verbosity=2).run(suite)
