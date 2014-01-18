import ueb.f.aufg08_bellman_ford_opt as candidate
import unittest
from vl.lek11.bellman_ford import reverse_weighted

# Testfaelle fuer max_ap_dp

class Test_bellman_ford_opt(unittest.TestCase):
    
    def test_1(self):
        
        G = [   {1:2, 2:1},    # Nachfolger von s
            {3:3},             # von u
            {},                # von v
            {2:-6}             # von w
        ]
        
        s = 0
        
        opt = [0, 2, -1, 5]
        bf = [{1}, {3}, set(), {2}]
        
        self.assertEqual(candidate.bellman_ford_opt(reverse_weighted(G), s), (opt, bf))
        
    def test_2(self):
        
        G = [   {1:-2, 2:-1},
            {2:2},             
            {}            
        ]
        
        s = 0
        
        opt = [0, -2, -1]
        bf = [{1,2}, set(), set()]
        
        self.assertEqual(candidate.bellman_ford_opt(reverse_weighted(G), s), (opt, bf))
        
    def test_3(self):
        
        G = [   {1:-1, 2:7, 3:2},
            {3:2},             
            {},
            {2:5}            
        ]
        
        s = 0
        
        opt = [0, -1, 6, 1]
        bf = [{1}, {3}, set(), {2}]
        
        self.assertEqual(candidate.bellman_ford_opt(reverse_weighted(G), s), (opt, bf))
        
    def test_4(self):
        
        G = [   {1:1},
            {2:-1},             
            {3:1},
            {4:-1},
            {}         
        ]
        
        s = 0
        
        opt = [0, 1, 0, 1, 0]
        bf = [{1}, {2}, {3}, {4}, set()]
        
        self.assertEqual(candidate.bellman_ford_opt(reverse_weighted(G), s), (opt, bf))
        
    def test_5(self):
        
        G = [             
            {}            
        ]
        
        s = 0
        
        opt = [0]
        bf = [set()]
        
        self.assertEqual(candidate.bellman_ford_opt(reverse_weighted(G), s), (opt, bf))
        
    def test_6(self):
        
        G = [   {},
            {0:3, 3:-1},             
            {1:4},
            {2:-2}            
        ]
        
        s = 1
        
        opt = [3, 0, -3, -1]
        bf = [set(), {0,3}, set(), {2}]
        
        self.assertEqual(candidate.bellman_ford_opt(reverse_weighted(G), s), (opt, bf))
        
    def test_7(self):
        
        G = [   {1:-1, 2:-1, 3:-1, 4:-1},
            {},             
            {},
            {},
            {}    
        ]
        
        s = 0
        
        opt = [0, -1, -1, -1, -1]
        bf = [{1,2,3,4}, set(), set(), set(), set()]
        
        self.assertEqual(candidate.bellman_ford_opt(reverse_weighted(G), s), (opt, bf))
        
    def test_8(self):
        
        G = [   {1:4, 2:3, 5:-1},
            {3:1},             
            {5:-3, 3:-1},
            {4:4},
            {3:-3},
            {4:2}            
        ]
        
        s = 0
        
        opt = [0, 4, 3, -2, 1, -1]
        bf = [{1,2,5}, set(), set(), set(), {3}, {4}]
        
        self.assertEqual(candidate.bellman_ford_opt(reverse_weighted(G), s), (opt, bf))

# Testausfuehrung via PyShell
# if __name__ == "__main__":
#     suite = unittest.TestLoader().loadTestsFromTestCase(Test_bellman_ford_opt)
#     unittest.TextTestRunner(verbosity=2).run(suite)
