import unittest
import ueb.d.aufg03_min_rest_greedy as candidate

class Test_min_rest_greedy(unittest.TestCase):
    
    def test_1(self):
        L = 20
        d = 4
        r = [3,7,11,15,19]
        exp = [3,7,11,15,19]
        
        self.assertEqual(candidate.min_rest_greedy(L, d, r), exp)
    
    def test_2(self):
        L = 15
        d = 3
        r = [2,4,6,8,10,12,14]
        exp = [2,4,6,8,10,12]
        
        self.assertEqual(candidate.min_rest_greedy(L, d, r), exp)
    
    def test_3(self):
        L = 15
        d = 4
        r = [2,4,6,8,10,12,14]
        exp = [4,8,12]
        
        self.assertEqual(candidate.min_rest_greedy(L, d, r), exp)
    
    def test_4(self):
        L = 240
        d = 100
        r = [0,40,80,120,160,200,240]
        exp = [80,160]
        
        self.assertEqual(candidate.min_rest_greedy(L, d, r), exp)
    
    def test_5(self):
        L = 20
        d = 20
        r = [2,4,6,8,10,12,14]
        exp = []
        
        self.assertEqual(candidate.min_rest_greedy(L, d, r), exp)
    
    def test_6(self):
        L = 15
        d = 20
        r = [2,4,6,8,10,12,14]
        exp = []
        
        self.assertEqual(candidate.min_rest_greedy(L, d, r), exp)
    
    def test_7(self):
        L = 0
        d = 0
        r = []
        exp = []
        
        self.assertEqual(candidate.min_rest_greedy(L, d, r), exp)
    
    def test_8(self):
        L = 0
        d = 20
        r = []
        exp = []
        
        self.assertEqual(candidate.min_rest_greedy(L, d, r), exp)
    
    def test_9(self):
        L = 40
        d = 20
        r = [20]
        exp = [20]
        
        self.assertEqual(candidate.min_rest_greedy(L, d, r), exp)

# Testausfuehrung via PyShell
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_min_rest_greedy)
# unittest.TextTestRunner(verbosity=2).run(suite)
