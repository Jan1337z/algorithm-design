import unittest
import ueb.d.aufg04_dijkstra_paths as candidate

class Test_dijkstra_paths(unittest.TestCase):
    
    
    def test_1(self):
        G = [   {1:1, 4:4, 2:2},
            {3:3, 4:1},
            {4:2, 5:3},
            {},
            {3:1, 5:2},
            {}
        ]
        
        d,p = candidate.dijkstra_paths(G,0)
        
        path = candidate.shortest_path(0, 3, p)
        self.assertEqual(path, [0,1,4,3])
        
        path = candidate.shortest_path(0, 5, p)
        self.assertEqual(path, [0,1,4,5])
        
        self.assertEqual(d, [0, 1, 2, 3, 2, 4])
        self.assertEqual(p, [None, 0, 0, 4, 1, 4])
        
    def test_2(self):
        G = [   {1:2, 2:1, 3:2, 6:4},
            {4:1},
            {4:4, 5:1, 0:6},
            {5:1},
            {},
            {6:1},
            {}
        ]
        
        d,p = candidate.dijkstra_paths(G,0)
        
        path = candidate.shortest_path(0, 3, p)
        self.assertEqual(path, [0,3])
        
        path = candidate.shortest_path(0, 5, p)
        self.assertEqual(path, [0,2,5])
        
        path = candidate.shortest_path(0, 6, p)
        self.assertEqual(path, [0,2,5,6])
        
        self.assertEqual(d, [0, 2, 1, 2, 3, 2, 3])
        self.assertEqual(p, [None, 0, 0, 0, 1, 2, 5])
        
    def test_3(self):
        G = [   {1:2, 2:1, 3:2, 6:4},
            {4:1},
            {4:4, 5:1, 0:6},
            {5:1},
            {},
            {6:1},
            {}
        ]
        
        d,p = candidate.dijkstra_paths(G,2)
        
        path = candidate.shortest_path(2, 5, p)
        self.assertEqual(path, [2,5])
        
        path = candidate.shortest_path(2, 6, p)
        self.assertEqual(path, [2,5,6])
        
        self.assertEqual(d, [6, 8, 0, 8, 4, 1, 2])
        self.assertEqual(p, [2, 0, None, 0, 2, 2, 5])
        
    def test_4(self):
        G = [   {1:1, 2:2, 3:3, 6:9, 4:5},
            {6:7, 3:1},
            {5:3},
            {4:4},
            {},
            {6:1},
            {}
        ]
        
        d,p = candidate.dijkstra_paths(G,0)
        
        path = candidate.shortest_path(0, 4, p)
        self.assertEqual(path, [0,4])
        
        path = candidate.shortest_path(0, 3, p)
        self.assertEqual(path, [0,1,3])
        
        self.assertEqual(d, [0, 1, 2, 2, 5, 5, 6])
        self.assertEqual(p, [None, 0, 0, 1, 0, 2, 5])
        
    def test_5(self):
        G = [   {1:3, 2:5, 3:6},
            {0:3, 2:1, 3:2},
            {0:5, 1:1, 3:2},
            {0:6, 1:2, 2:2},
        ]
        
        d,p = candidate.dijkstra_paths(G,3)
        
        path = candidate.shortest_path(3, 0, p)
        self.assertEqual(path, [3,1,0])
        
        path = candidate.shortest_path(3, 2, p)
        self.assertEqual(path, [3,2])
        
        self.assertEqual(d, [5, 2, 2, 0])
        self.assertEqual(p, [1, 3, 3, None])
        
    def test_6(self):
        G = [   {1:3, 2:5, 3:6},
            {0:3, 2:1, 3:2},
            {0:5, 1:1, 3:2},
            {0:6, 1:2, 2:2},
        ]
        
        d,p = candidate.dijkstra_paths(G,0)
        
        path = candidate.shortest_path(0, 3, p)
        self.assertEqual(path, [0,1,3])
        
        path = candidate.shortest_path(0, 2, p)
        self.assertEqual(path, [0,1,2])
        
        path = candidate.shortest_path(0, 1, p)
        self.assertEqual(path, [0,1])
        
        self.assertEqual(d, [0, 3, 4, 5])
        self.assertEqual(p, [None, 0, 1, 1])
        
    def test_7(self):
        G = [{}]
        
        d,p = candidate.dijkstra_paths(G,0)
        
        path = candidate.shortest_path(0, 0, p)
        self.assertEqual(path, [0])
        
        self.assertEqual(d, [0])
        self.assertEqual(p, [None])
        
    def test_8(self):
        G = [{1:4, 2:3, 3:2},
             {},
             {},
             {}]
        
        d,p = candidate.dijkstra_paths(G,0)
        
        path = candidate.shortest_path(0, 1, p)
        self.assertEqual(path, [0,1])
        
        path = candidate.shortest_path(0, 2, p)
        self.assertEqual(path, [0,2])
        
        path = candidate.shortest_path(0, 3, p)
        self.assertEqual(path, [0,3])
        
        self.assertEqual(d, [0, 4, 3, 2])
        self.assertEqual(p, [None, 0, 0, 0])
        
    def test_9(self):
        G = [{1:1},
             {2:2},
             {3:3},
             {}]
        
        d,p = candidate.dijkstra_paths(G,0)
        
        path = candidate.shortest_path(0, 3, p)
        self.assertEqual(path, [0,1,2,3])
        
        path = candidate.shortest_path(0, 2, p)
        self.assertEqual(path, [0,1,2])
        
        path = candidate.shortest_path(0, 1, p)
        self.assertEqual(path, [0,1])
        
        path = candidate.shortest_path(0, 0, p)
        self.assertEqual(path, [0])
        
        self.assertEqual(d, [0, 1, 3, 6])
        self.assertEqual(p, [None, 0, 1, 2])

# Testausfuehrung via PyShell
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_dijkstra_paths)
# unittest.TextTestRunner(verbosity=2).run(suite)
