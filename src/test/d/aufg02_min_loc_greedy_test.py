import unittest
import ueb.d.aufg02_min_loc_greedy as candidate

class Test_min_loc_greedy(unittest.TestCase):
    
    def test_1(self):
        h = [0,3700,4001,8000,12000]
        
        self.assertEqual(len(candidate.min_loc_greedy(h)), 2)
    
    def test_2(self):
        h = [0,3700,4001,8000,12001]
        
        self.assertEqual(len(candidate.min_loc_greedy(h)), 2)
    
    def test_3(self):
        h = [0,1000,2000,4000,8000,12000,20000]
        
        self.assertEqual(len(candidate.min_loc_greedy(h)), 2)
    
    def test_4(self):
        h = [0,2500,3900,5100,8100,16100,50000]
        
        self.assertEqual(len(candidate.min_loc_greedy(h)), 3)
    
    def test_5(self):
        h = [0]
        
        self.assertEqual(len(candidate.min_loc_greedy(h)), 1)
    
    def test_6(self):
        h = [0,50000]
        
        self.assertEqual(len(candidate.min_loc_greedy(h)), 2)
    
    def test_7(self):
        h = [0, 4001, 8001]
        
        self.assertEqual(len(candidate.min_loc_greedy(h)), 2)

# Testausfuehrung via PyShell
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_min_loc_greedy)
# unittest.TextTestRunner(verbosity=2).run(suite)
