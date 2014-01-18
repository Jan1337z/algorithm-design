import unittest
import ueb.b.aufg07_adjmatrix as candidate

# Testfaelle fuer Umwandlung von Adjazenzmatrix zu Adjazenzmengen und umgekehrt
class Test_to_from_matrix(unittest.TestCase):
    
    def test_1(self):
        A = []
        A.append([0,1,1,0,0])
        A.append([1,0,1,1,1])
        A.append([1,1,0,1,1])
        A.append([0,1,1,0,1])
        A.append([0,1,1,1,0])
        
        B = candidate.from_matrix(A)
        
        G = [set() for _ in range(5)]   # alle Mengen leer anlegen
        G[0] |= {1,2}
        G[1] |= {0,2,3,4}
        G[2] |= {0,1,3,4}
        G[3] |= {1,2,4}
        G[4] |= {1,2,3}
        
        self.assertEqual(B, G)
        
        C = candidate.to_matrix(G)
        
        self.assertEqual(C, A)
        
    def test_2(self):
        A = []
        A.append([0,0,1,1,0])
        A.append([0,0,1,1,1])
        A.append([1,1,0,0,1])
        A.append([1,1,0,0,1])
        A.append([0,1,1,1,0])
        
        B = candidate.from_matrix(A)
        
        G = [set() for _ in range(5)]   # alle Mengen leer anlegen
        G[0] |= {2,3}
        G[1] |= {2,3,4}
        G[2] |= {0,1,4}
        G[3] |= {0,1,4}
        G[4] |= {1,2,3}
        
        self.assertEqual(B, G)
        
        C = candidate.to_matrix(G)
        
        self.assertEqual(C, A)
        
    def test_3(self):
        A = []
        A.append([0,0,0,0,0])
        A.append([0,0,0,0,0])
        A.append([0,0,0,0,0])
        A.append([0,0,0,0,0])
        A.append([0,0,0,0,0])
        
        B = candidate.from_matrix(A)
        
        G = [set() for _ in range(5)]   # alle Mengen leer anlegen
        
        self.assertEqual(B, G)
        
        C = candidate.to_matrix(G)
        
        self.assertEqual(C, A)
        
    def test_4(self):
        A = []
        A.append([0,0])
        A.append([0,0])
        
        
        B = candidate.from_matrix(A)
        
        G = [set() for _ in range(2)]   # alle Mengen leer anlegen
        
        self.assertEqual(B, G)
        
        C = candidate.to_matrix(G)
        
        self.assertEqual(C, A)
        
    def test_5(self):
        A = []
        A.append([0,1])
        A.append([1,0])
        
        
        B = candidate.from_matrix(A)
        
        G = [set() for _ in range(2)]   # alle Mengen leer anlegen
        G[0] |= {1}
        G[1] |= {0}
        
        self.assertEqual(B, G)
        
        C = candidate.to_matrix(G)
        
        self.assertEqual(C, A)
        
    def test_6(self):
        A = []
        A.append([0])
        
        B = candidate.from_matrix(A)
        
        G = [set() for _ in range(1)]   # alle Mengen leer anlegen
        
        self.assertEqual(B, G)
        
        C = candidate.to_matrix(G)
        
        self.assertEqual(C, A)
        
    def test_7(self):
        A = []
        A.append([0,1,1,1,1])
        A.append([1,0,1,1,1])
        A.append([1,1,0,1,1])
        A.append([1,1,1,0,1])
        A.append([1,1,1,1,0])
        
        B = candidate.from_matrix(A)
        
        G = [set() for _ in range(5)]   # alle Mengen leer anlegen
        G[0] |= {1,2,3,4}
        G[1] |= {0,2,3,4}
        G[2] |= {0,1,3,4}
        G[3] |= {0,1,2,4}
        G[4] |= {0,1,2,3}
        
        self.assertEqual(B, G)
        
        C = candidate.to_matrix(G)
        
        self.assertEqual(C, A)

# Testausfuehrung via PyShell
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_to_from_matrix)
# unittest.TextTestRunner(verbosity=2).run(suite)
