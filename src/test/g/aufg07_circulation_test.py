import ueb.g.aufg07_circulation as candidate
import unittest

# Testfaelle fuer circulation

class Test_circulation(unittest.TestCase):
    
    # Positiv-Fälle
    
    def test_1 (self):
        
        G = [   {1:2},
            {2:2, 3:2},
            {0:2},
            {2:4}      ]
        
        d = [-2, 1, 4, -3]
                        
        self.assertTrue(candidate.circulation(G,d))
    
    # Beispiel aus VL
    def test_2(self):
        
        G = [   {1:3, 2:3},
            {2:2, 3:2},
            {3:2},
            {}        ]
        
        d = [-3,-3,2,4]
                        
        self.assertTrue(candidate.circulation(G,d))
        
        
    def test_3(self):
        
        G = [   {1:2, 2:3, 3:1},
            {3:3},
            {3:3},
            {}        ]
        
        d = [-5,1,1,3]
                        
        self.assertTrue(candidate.circulation(G,d))
        
        
    def test_4(self):
        
        G = [   {1:3},
            {3:3},
            {0:3},
            {2:3}     ]
        
        d = [-3,3,3,-3]
                        
        self.assertTrue(candidate.circulation(G,d))


    def test_5(self):
        
        G = [   {1:4},
            {2:5},
            {0:1}      ]
        
        d = [-3,-2,5]
                        
        self.assertTrue(candidate.circulation(G,d))
        
        
    def test_6(self):
        
        G = [   {}    ]
            
        d = [0]
                        
        self.assertTrue(candidate.circulation(G,d))
        
        
        
    # Negativ-Fälle 
        
    def test_7(self):
        
        G = [   {1:2},
            {2:2},
            {0:1}      ]
        
        d = [-3,1,2]
                        
        self.assertFalse(candidate.circulation(G,d))
        
        
    def test_8(self):
        
        G = [   {1:1},
            {2:0},
            {0:5}      ]
        
        d = [3,2,-5]
                        
        self.assertFalse(candidate.circulation(G,d))
        
        
    def test_9(self):
        
        G = [   {1:1},
            {2:2, 3:2},
            {0:2},
            {2:4}      ]
        
        d = [-2, 1, 4, -3]
                        
        self.assertFalse(candidate.circulation(G,d))
        
        
    def test_10(self):
        
        G = [   {1:0},
                {0:2}   ]
        
        d = [-2, 2]
                        
        self.assertFalse(candidate.circulation(G,d))
        
       

# Testausfuehrung via PyShell
# if __name__ == "__main__":
#     suite = unittest.TestLoader().loadTestsFromTestCase(Test_circulation)
#     unittest.TextTestRunner(verbosity=2).run(suite)
