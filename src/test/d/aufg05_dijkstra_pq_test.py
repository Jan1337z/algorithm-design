import unittest
import ueb.d.aufg05_dijkstra_pq as candidate

class Test_dijkstra_pq(unittest.TestCase):
    
    def test_1(self):
        G = [   {1:1, 4:4, 2:2},
            {3:3, 4:1},
            {4:2, 5:3},
            {},
            {3:1, 5:2},
            {}
        ]
        
        d = candidate.dijkstra_pq(G,0)
        
        self.assertEqual(d, [0, 1, 2, 3, 2, 4])
        
    def test_2(self):
        G = [   {1:2, 2:1, 3:2, 6:4},
            {4:1},
            {4:4, 5:1, 0:6},
            {5:1},
            {},
            {6:1},
            {}
        ]
        
        d = candidate.dijkstra_pq(G,0)
        
        self.assertEqual(d, [0, 2, 1, 2, 3, 2, 3])
        
    def test_3(self):
        G = [   {1:2, 2:1, 3:2, 6:4},
            {4:1},
            {4:4, 5:1, 0:6},
            {5:1},
            {},
            {6:1},
            {}
        ]
        
        d = candidate.dijkstra_pq(G,2)
        
        self.assertEqual(d, [6, 8, 0, 8, 4, 1, 2])
        
    def test_4(self):
        G = [   {1:1, 2:2, 3:3, 6:9, 4:5},
            {6:7, 3:1},
            {5:3},
            {4:4},
            {},
            {6:1},
            {}
        ]
        
        d = candidate.dijkstra_pq(G,0)
        
        self.assertEqual(d, [0, 1, 2, 2, 5, 5, 6])
        
    def test_5(self):
        G = [   {1:3, 2:5, 3:6},
            {0:3, 2:1, 3:2},
            {0:5, 1:1, 3:2},
            {0:6, 1:2, 2:2},
        ]
        
        d = candidate.dijkstra_pq(G,3)
        
        self.assertEqual(d, [5, 2, 2, 0])
        
    def test_6(self):
        G = [   {1:3, 2:5, 3:6},
            {0:3, 2:1, 3:2},
            {0:5, 1:1, 3:2},
            {0:6, 1:2, 2:2},
        ]
        
        d = candidate.dijkstra_pq(G,0)
        
        self.assertEqual(d, [0, 3, 4, 5])
        
    def test_7(self):
        G = [{}]
        
        d = candidate.dijkstra_pq(G,0)
        
        self.assertEqual(d, [0])
        
    def test_8(self):
        G = [{1:4, 2:3, 3:2},
             {},
             {},
             {}]
        
        d = candidate.dijkstra_pq(G,0)
        
        self.assertEqual(d, [0, 4, 3, 2])
        
    def test_9(self):
        G = [{1:1},
             {2:2},
             {3:3},
             {}]
        
        d = candidate.dijkstra_pq(G,0)
        
        self.assertEqual(d, [0, 1, 3, 6])

# Testausfuehrung via PyShell
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_dijkstra_pq)
# unittest.TextTestRunner(verbosity=2).run(suite)
