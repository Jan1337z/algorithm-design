import ueb.g.aufg05_max_bipartite_matching as candidate
import unittest

# Testfaelle fuer max_bipartite_matching

class Test_max_bipartite_matching(unittest.TestCase):
    
    def test_1(self):
        
        # Bsp        
        G = [   {4, 5},
                {4, 6},
                {5},
                {5,6},
                {0,1},
                {0,2,3},
                {1,3}
             ]
            
        (M, len) = candidate.max_bipartite_matching(G)
        self.assertEqual(len, 3)
        
        
    def test_2(self):
           
        G = [   {5},
                {5, 7},
                {6, 7, 8},
                {7, 8},
                {8},
                {0, 1},
                {2},
                {1, 2, 3},
                {2, 3, 4}
             ]
            
        (M, len) = candidate.max_bipartite_matching(G)
        self.assertEqual(len, 4)
        
        
    def test_3(self):
              
        G = [   {4},
                {4},
                {5, 6},
                {6, 7},
                {0, 1},
                {2},
                {2, 3},
                {3}
             ]
            
        (M, len) = candidate.max_bipartite_matching(G)
        self.assertEqual(len, 3)
        
    
    def test_4(self):
              
        G = [   {4},
                {4, 5},
                {5, 6, 7},
                {7, 8},
                {0, 1},
                {1, 2},
                {2},
                {2, 3},
                {3}
             ]
            
        (M, len) = candidate.max_bipartite_matching(G)
        self.assertEqual(len, 4)
        
        
    def test_5(self):
             
        G = [   {4},
                {4},
                {5},
                {5},
                {0, 1},
                {2, 3},
                set(),
                set()
             ]
            
        (M, len) = candidate.max_bipartite_matching(G)
        self.assertEqual(len, 2)
        
        
    def test_6(self):
                 
        G = [   set(),
                {4, 5},
                {6},
                {6},
                {1},
                {1},
                {2, 3},
                set()
             ]
            
        (M, len) = candidate.max_bipartite_matching(G)
        self.assertEqual(len, 2)
        
        
    def test_7(self):
                 
        G = [   {1, 2, 3, 4},
                {5, 0},
                {0},
                {0},
                {0, 6},
                {1},
                {4}
             ]
            
        (M, len) = candidate.max_bipartite_matching(G)
        self.assertEqual(len, 3)
        
        
    def test_8(self):
                 
        G = [   set()
             ]
            
        (M, len) = candidate.max_bipartite_matching(G)
        self.assertEqual(len, 0)
        
        
    def test_9(self):
                 
        G = [   set(),
                set()
             ]
            
        (M, len) = candidate.max_bipartite_matching(G)
        self.assertEqual(len, 0)
        
        
    def test_10(self):
                 
        G = [   {1},
                {0}
             ]
            
        (M, len) = candidate.max_bipartite_matching(G)
        self.assertEqual(len, 1)


# Testausfuehrung via PyShell
# if __name__ == "__main__":
#     suite = unittest.TestLoader().loadTestsFromTestCase(Test_max_bipartite_matching)
#     unittest.TextTestRunner(verbosity=2).run(suite)
