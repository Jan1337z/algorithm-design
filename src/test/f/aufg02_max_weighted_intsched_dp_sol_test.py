import ueb.f.aufg02_max_weighted_intsched_dp_sol as candidate
import unittest

# Testfaelle fuer max_weighted_intsched_dp_sol
#
# Ergebnismenge ist eindeutig, weil in der Aufgabe angegeben ist, 
# wie bei Mehrdeutigkeit weitergemacht werden soll

class Test_max_weighted_intsched_dp_sol(unittest.TestCase):
    
    def test_1(self):
        L = [(0,3,2),(1,5,4),(4,6,4),(2,9,7),(7,10,2),(8,11,1)]
        R = {0, 2, 4}
        
        self.assertEqual(candidate.max_weighted_intsched_dp_sol(L), R)
        
    def test_2(self):
        L = [(0,3,2),(1,5,4),(4,6,4),(2,9,7),(7,10,2),(8,11,3)]
        R = {0, 2, 5}
        
        self.assertEqual(candidate.max_weighted_intsched_dp_sol(L), R)
        
    def test_3(self):
        L = [(0,3,2),(1,5,4),(4,6,4),(2,9,10),(7,10,2),(8,11,3)]
        R = {3}
        
        self.assertEqual(candidate.max_weighted_intsched_dp_sol(L), R)
        
    def test_4(self):
        L = [(0,3,2),(1,5,4),(4,6,4),(2,9,7),(7,10,3),(8,11,3)]
        R = {0, 2, 4}
        
        self.assertEqual(candidate.max_weighted_intsched_dp_sol(L), R)
        
    def test_5(self):
        L = [(0,3,2),(1,5,4),(4,6,2),(2,9,6),(7,10,2),(8,11,2)]
        R = {3}
        
        self.assertEqual(candidate.max_weighted_intsched_dp_sol(L), R)
        
    def test_6(self):
        L = [(0,3,2),(0,3,2),(0,3,2)]
        R = {0}
        
        self.assertEqual(candidate.max_weighted_intsched_dp_sol(L), R)
        
    def test_7(self):
        L = [(0,3,2)]
        R = {0}
        
        self.assertEqual(candidate.max_weighted_intsched_dp_sol(L), R)

# Testausfuehrung via PyShell
# if __name__ == "__main__":
#     suite = unittest.TestLoader().loadTestsFromTestCase(Test_max_weighted_intsched_dp_sol)
#     unittest.TextTestRunner(verbosity=2).run(suite)
