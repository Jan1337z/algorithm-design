import ueb.e.aufg04_max_sum as candidate
import unittest

# MAX SUM
# 

# Testfaelle fuer 
# max_sum_all
# max_prefix_sum
# max_sum_dac

class Test_max_sum(unittest.TestCase):
    
    def test_1(self):
        a = [3,-5,0,2,100,-2,-5,9]
        self.assertEqual(candidate.max_sum_all(a), 104)
        self.assertEqual(candidate.max_sum_dac(a), 104)
        self.assertEqual(candidate.max_prefix_sum(a), 102)
        
    def test_2(self):
        a = [-3,5,-1,2,-5,3]
        self.assertEqual(candidate.max_sum_all(a), 6)
        self.assertEqual(candidate.max_sum_dac(a), 6)
        self.assertEqual(candidate.max_prefix_sum(a), 3)
        
    def test_3(self):
        a = [13,-5,-1,7,-5,4]
        self.assertEqual(candidate.max_sum_all(a), 14)
        self.assertEqual(candidate.max_sum_dac(a), 14)
        self.assertEqual(candidate.max_prefix_sum(a), 14)
        
    def test_4(self):
        a = [3,-5,0,1,10,-2,-5,6]
        self.assertEqual(candidate.max_sum_all(a), 11)
        self.assertEqual(candidate.max_sum_dac(a), 11)
        self.assertEqual(candidate.max_prefix_sum(a), 9)
        
    def test_5(self):
        a = [3,-5,0,1,0,-2,-5,6]
        self.assertEqual(candidate.max_sum_all(a), 6)
        self.assertEqual(candidate.max_sum_dac(a), 6)
        self.assertEqual(candidate.max_prefix_sum(a), 3)
        
    def test_6(self):
        a = [-3,-9,-4,-5,-2,-1]
        self.assertEqual(candidate.max_sum_all(a), -1)
        self.assertEqual(candidate.max_sum_dac(a), -1)
        self.assertEqual(candidate.max_prefix_sum(a), -3)
        
    def test_7(self):
        a = [3,5,10,9,2,3]
        self.assertEqual(candidate.max_sum_all(a), 32)
        self.assertEqual(candidate.max_sum_dac(a), 32)
        self.assertEqual(candidate.max_prefix_sum(a), 32)
        
    def test_8(self):
        a = [3,-5,-10,-9,-2,-3]
        self.assertEqual(candidate.max_sum_all(a), 3)
        self.assertEqual(candidate.max_sum_dac(a), 3)
        self.assertEqual(candidate.max_prefix_sum(a), 3)
        
    def test_9(self):
        a = [3,-5,10,9,-2,-3]
        self.assertEqual(candidate.max_sum_all(a), 19)
        self.assertEqual(candidate.max_sum_dac(a), 19)
        self.assertEqual(candidate.max_prefix_sum(a), 17)

# Testausfuehrung via PyShell
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_max_sum)
# unittest.TextTestRunner(verbosity=2).run(suite)
