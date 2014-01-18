import unittest
import ueb.d.aufg01_min_intpart_greedy as candidate_greedy

class Test_min_intpart_greedy(unittest.TestCase):
    
    # Testfälle für die Funktion "sol_min_intpart_greedy"
    def test_sol_min_intpart_1(self):
        L = [(0,2),(0,3),(1,3),(2,4)]
        
        self.assertEqual(candidate_greedy.min_intpart_greedy(L), 3)
    
    def test_sol_min_intpart_2(self):
        L = [(0,2),(0,3),(2,3),(3,4)]
        
        self.assertEqual(candidate_greedy.min_intpart_greedy(L), 2)
    
    def test_sol_min_intpart_3(self):
        L = [(0,3),(4,6),(6,7),(7,9)]
        
        self.assertEqual(candidate_greedy.min_intpart_greedy(L), 1)
    
    def test_sol_min_intpart_4(self):
        L = [(0,2)]
        
        self.assertEqual(candidate_greedy.min_intpart_greedy(L), 1)
    
    def test_sol_min_intpart_5(self):
        L = [(0,2),(0,2),(0,2),(0,2)]
        
        self.assertEqual(candidate_greedy.min_intpart_greedy(L), 4)
        
    def test_sol_min_intpart_6(self):
        L = [(0,3),(0,4),(4,6),(5,7),(8,10),(0,12),(9,13),(15,16),(14,17)]
        
        self.assertEqual(candidate_greedy.min_intpart_greedy(L), 3)
    
    def test_sol_min_intpart_7(self):
        L = [(0,1),(0,2),(1,3),(2,5),(2,4),(2,3),(5,7)]
        
        self.assertEqual(candidate_greedy.min_intpart_greedy(L), 4)

# Testausfuehrung via PyShell
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_min_intpart_greedy)
# unittest.TextTestRunner(verbosity=2).run(suite)
