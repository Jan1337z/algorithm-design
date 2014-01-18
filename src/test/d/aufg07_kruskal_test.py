import unittest
import ueb.d.aufg07_kruskal as candidate

class Test_kruskal(unittest.TestCase):
    
    def test_1(self):
        G = [   {1:1, 4:4, 2:3},
            {0:1, 3:3, 4:1},
            {0:3, 4:2, 5:3},
            {1:3, 4:1},
            {0:4, 1:1, 2:2, 3:1, 5:2},
            {2:3, 4:2}
        ]
        
        T,c = candidate.kruskal(G)
        
        self.assertEqual(T, {frozenset((0,1)), frozenset((2,4)), frozenset((4,1)), frozenset((4,5)), frozenset((3,4))})
        self.assertEqual(c, 7)
        
    def test_2(self):
        G = [   {1:2, 2:3, 3:1},
            {0:2, 2:1, 3:4},
            {0:3, 1:1, 3:4},
            {0:1, 1:4, 2:4},
        ]
        
        T,c = candidate.kruskal(G)
        
        self.assertEqual(T, {frozenset((0,3)), frozenset((1,0)), frozenset((1,2))})
        self.assertEqual(c, 4)
        
    def test_3(self):
        G = [   {1:1},
            {0:1,2:1},
            {1:1,3:1},
            {2:1,4:1},
            {3:1}
        ]
        
        T,c = candidate.kruskal(G)
        
        self.assertEqual(T, {frozenset((0,1)), frozenset((1,2)), frozenset((2,3)), frozenset((3,4))})
        self.assertEqual(c, 4)
        
    def test_4(self):
        G = [   {1:5, 2:5, 3:10, 4:10},
            {0:5},
            {0:5},
            {0:10},
            {0:10}
        ]
        
        T,c = candidate.kruskal(G)
        
        self.assertEqual(T, {frozenset((0,1)), frozenset((0,2)), frozenset((0,3)), frozenset((0,4))})
        self.assertEqual(c, 30)
        
    def test_5(self):
        G = [   {}
        ]
        
        T,c = candidate.kruskal(G)
        
        self.assertEqual(T, set())
        self.assertEqual(c, 0)
        
    def test_6(self):
        G = [   {2:3},
                {5:1},
                {0:3, 5:3, 4:1, 3:3},
                {2:3, 6:4},
                {2:1, 5:1, 6:5},
                {1:1, 2:3, 4:1},
                {3:4, 4:5}
        ]
        
        T,c = candidate.kruskal(G)
        
        self.assertEqual(T, {frozenset((1,5)), frozenset((4,5)), frozenset((2,4)), frozenset((0,2)), frozenset((2,3)), frozenset((3,6))})
        self.assertEqual(c, 13)
        
    def test_7(self):
        G = [   {2:3, 7:4},
                {5:1},
                {0:3, 5:3, 4:1, 3:3},
                {2:3, 6:4, 7:2},
                {2:1, 5:1, 6:5},
                {1:1, 2:3, 4:1},
                {3:4, 4:5, 7:1},
                {3:2, 0:4, 6:1}
        ]
        
        T,c = candidate.kruskal(G)
        
        self.assertEqual(T, {frozenset((1,5)), frozenset((4,5)), frozenset((2,4)), frozenset((0,2)), frozenset((2,3)), frozenset((3,7)), frozenset((7,6))})
        self.assertEqual(c, 12)
        
    def test_8(self):
        G = [   {1:2, 2:7, 3:10},   # s 
                {0:2, 2:8},         # a
                {0:7, 1:8},         # b
                {0:10, 4:1, 7:9},   # c
                {3:1, 5:3, 6:4},    # d  
                {4:3, 6:5, 7:6},    # e  
                {4:4, 5:5},         # f
                {3:9, 5:6}          # g
        ]
        
        T,c = candidate.kruskal(G)
        
        self.assertEqual(T, {frozenset({5, 7}), frozenset({3, 4}), frozenset({0, 2}), frozenset({4, 6}), frozenset({0, 1}), frozenset({0, 3}), frozenset({4, 5})})
        self.assertEqual(c, 33)

# Testausfuehrung via PyShell
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_kruskal)
# unittest.TextTestRunner(verbosity=2).run(suite)
