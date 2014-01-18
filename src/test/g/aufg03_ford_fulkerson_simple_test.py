import ueb.g.aufg03_ford_fulkerson_simple as candidate
import unittest

# Testfaelle fuer ford_fulkerson_simple

class Test_ford_fulkerson_simple(unittest.TestCase):
    
    def test_1(self):
        G = [   {1:20, 2:10},  # Nachfolger von s (Quelle)
                {2:30, 3:10},  # von u
                {3:20},        # von v
                {}             # von t (Senke)
            ]
        
        self.assertEqual(candidate.ford_fulkerson_simple(G, 0, 3), 30)
        
        
    def test_2(self):
        G = [   {1:2, 2:5},  
                {3:1, 4:2},  
                {3:5},       
                {4:2, 5:3},
                {5:4},
                {}
            ]
        
        self.assertEqual(candidate.ford_fulkerson_simple(G, 0, 5), 7)
        
        
    def test_3(self):
        G = [   {1:2, 2:5},  
                {3:1, 4:2},  
                {3:4},       
                {4:2, 5:3},
                {5:4},
                {}
            ]
        
        self.assertEqual(candidate.ford_fulkerson_simple(G, 0, 5), 6)
        
        
    def test_4(self):
        G = [   {1:3, 2:4, 3:2},  
                {5:2, 4:2},  
                {4:4},       
                {4:1, 7:2},
                {5:1, 6:2, 7:5},
                {8:2},
                {8:3},
                {8:8},
                {}
            ]
        
        self.assertEqual(candidate.ford_fulkerson_simple(G, 0, 8), 9)
        
    
    def test_5(self):
        G = [   {1:30, 2:30},  
                {3:30, 2:1},  
                {3:30},       
                {}                
            ]
        
        self.assertEqual(candidate.ford_fulkerson_simple(G, 0, 3), 60)
        
        
    def test_6(self):
        G = [   {1:4, 5:2},  
                {2:2, 6:2},  
                {3:3, 7:1},       
                {4:1, 8:3},
                {},
                {1:1, 6:2},
                {2:2, 7:2},
                {3:1, 8:1},
                {4:4}                
            ]
        
        self.assertEqual(candidate.ford_fulkerson_simple(G, 0, 4), 5)
        
        
    def test_7(self):
        G = [   {1:10, 2:10, 3:2},  
                {4:1, 2:9},  
                {4:1, 3:18},       
                {4:20},
                {}                
            ]
        
        self.assertEqual(candidate.ford_fulkerson_simple(G, 0, 4), 22)


# Testausfuehrung via PyShell
# if __name__ == "__main__":
#     suite = unittest.TestLoader().loadTestsFromTestCase(Test_ford_fulkerson_simple)
#     unittest.TextTestRunner(verbosity=2).run(suite)
