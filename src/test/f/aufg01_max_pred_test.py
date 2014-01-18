import ueb.f.aufg01_max_pred as candidate
import unittest

# Testfaelle fuer max_predecessors(L)

class Test_max_pred(unittest.TestCase):
    
    def test_1(self):
        L = [(0,3,2),(1,5,4),(4,6,4),(2,9,7),(7,10,2),(8,11,1)]
        R = [-1, -1, 0, -1, 2, 2]
        
        self.assertEqual(candidate.max_predecessors(L), R)
        
    def test_2(self):
        L = [(0,3,2),(3,5,4),(4,6,4),(2,9,7),(7,10,2),(8,11,1)]
        R = [-1, 0, 0, -1, 2, 2]
        
        self.assertEqual(candidate.max_predecessors(L), R)
        
    def test_3(self):
        L = [(0,3,2),(3,5,4),(5,6,4),(2,9,7),(7,10,2),(9,11,1)]
        R = [-1, 0, 1, -1, 2, 3]
        
        self.assertEqual(candidate.max_predecessors(L), R)
        
    def test_4(self):
        L = [(0,2,2),(1,5,4),(3,5,4),(0,5,7),(4,6,2),(5,7,1)]
        R = [-1, -1, 0, -1, 0, 3]
        
        self.assertEqual(candidate.max_predecessors(L), R)
        
    def test_5(self):
        L = [(0,1,2),(1,2,4),(2,3,4),(3,4,7),(4,5,2),(5,6,1)]
        R = [-1, 0, 1, 2, 3, 4]
        
        self.assertEqual(candidate.max_predecessors(L), R)
        
    def test_6(self):
        L = [(0,1,2),(0,1,4),(0,1,4),(0,1,7),(0,1,2),(0,1,1)]
        R = [-1, -1, -1, -1, -1, -1]
        
        self.assertEqual(candidate.max_predecessors(L), R)
        
    def test_7(self):
        L = [(0,1,2),(0,1,4),(0,1,4),(0,1,7),(0,1,2),(1,2,1)]
        R = [-1, -1, -1, -1, -1, 4]
        
        self.assertEqual(candidate.max_predecessors(L), R)
        
    def test_8(self):
        L = [(0,1,2)]
        R = [-1]
        
        self.assertEqual(candidate.max_predecessors(L), R)

# Testausfuehrung via PyShell
# if __name__ == "__main__":
#     suite = unittest.TestLoader().loadTestsFromTestCase(Test_max_pred)
#     unittest.TextTestRunner(verbosity=2).run(suite)

