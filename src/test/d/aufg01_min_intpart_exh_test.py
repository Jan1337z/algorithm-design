import unittest
import ueb.d.aufg01_min_intpart_exh as candidate_exh

class Test_min_intpart_exh(unittest.TestCase):
    
    # Testfälle für die Funktion "compatible"
    def test_compatible_1(self):
        L = [(0,3),(0,4),(4,6),(5,7),(8,10),(0,12),(9,13),(15,16),(14,17)]
        M = {0,2,5}
        
        self.assertFalse(candidate_exh.compatible(L, M))
    
    def test_compatible_2(self):
        L = [(0,3),(0,4),(4,6),(5,7),(8,10),(0,12),(9,13),(15,16),(14,17)]
        M = {0,3,4,7}
        
        self.assertTrue(candidate_exh.compatible(L, M))
    
    def test_compatible_3(self):
        L = [(0,3),(0,4),(4,6),(5,7),(8,10),(0,12),(9,13),(15,16),(14,17)]
        M = {1,2}
        
        self.assertTrue(candidate_exh.compatible(L, M))
    
    def test_compatible_4(self):
        L = [(0,3),(0,4),(4,6),(5,7),(8,10),(0,12),(9,13),(15,16),(14,17)]
        M = {4,8,3,1}
        
        self.assertTrue(candidate_exh.compatible(L, M))
    
    def test_compatible_5(self):
        L = [(0,3),(0,4),(4,6),(5,7),(8,10),(0,12),(9,13),(15,16),(14,17)]
        M = {5,8}
        
        self.assertTrue(candidate_exh.compatible(L, M))
    
    def test_compatible_6(self):
        L = [(0,3),(0,4),(4,6),(5,7),(8,10),(0,12),(9,13),(15,16),(14,17)]
        M = {4,6}
        
        self.assertFalse(candidate_exh.compatible(L, M))
    
    def test_compatible_7(self):
        L = [(0,3),(0,4),(4,6),(5,7),(8,10),(0,12),(9,13),(15,16),(14,17)]
        M = set()
        
        self.assertTrue(candidate_exh.compatible(L, M))
    
    def test_compatible_8(self):
        L = [(0,3),(0,3),(0,3)]
        M = {0,1,2}
        
        self.assertFalse(candidate_exh.compatible(L, M))
    
    def test_compatible_9(self):
        L = [(0,3),(0,3),(0,3)]
        M = {1,2}
        
        self.assertFalse(candidate_exh.compatible(L, M))
    
    def test_compatible_10(self):
        L = [(0,3),(0,3),(0,3)]
        M = set()
        
        self.assertTrue(candidate_exh.compatible(L, M))
    
    
    # Testfälle für die Funktion "sol_min_intpart_exhaustive"
    def test_sol_min_intpart_1(self):
        L = [(0,2),(0,3),(1,3),(2,4)]
        
        self.assertEqual(candidate_exh.min_intpart_exhaustive(L), 3)
    
    def test_sol_min_intpart_2(self):
        L = [(0,2),(0,3),(2,3),(3,4)]
        
        self.assertEqual(candidate_exh.min_intpart_exhaustive(L), 2)
    
    def test_sol_min_intpart_3(self):
        L = [(0,3),(4,6),(6,7),(7,9)]
        
        self.assertEqual(candidate_exh.min_intpart_exhaustive(L), 1)
    
    def test_sol_min_intpart_4(self):
        L = [(0,2)]
        
        self.assertEqual(candidate_exh.min_intpart_exhaustive(L), 1)
    
    def test_sol_min_intpart_5(self):
        L = [(0,2),(0,2),(0,2),(0,2)]
        
        self.assertEqual(candidate_exh.min_intpart_exhaustive(L), 4)
    
    def test_sol_min_intpart_7(self):
        L = [(0,1),(0,2),(1,3),(2,5),(2,4),(2,3),(5,7)]
        
        self.assertEqual(candidate_exh.min_intpart_exhaustive(L), 4)

# Testausfuehrung via PyShell
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_min_intpart_exh)
# unittest.TextTestRunner(verbosity=2).run(suite)
