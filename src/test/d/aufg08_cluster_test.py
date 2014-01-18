import unittest
import ueb.d.aufg08_cluster as candidate

class Test_cluster(unittest.TestCase):
    
    def test_1(self):
        m = 5
        
        d = {}
        d[0,0]= 0
        d[0,1]= 11
        d[0,2]= 7
        d[0,3]= 15
        d[0,4]= 8
        d[1,0]= 11
        d[1,1]= 0
        d[1,2]= 12
        d[1,3]= 9
        d[1,4]= 2
        d[2,0]= 7
        d[2,1]= 12
        d[2,2]= 0
        d[2,3]= 13
        d[2,4]= 14
        d[3,0]= 15
        d[3,1]= 9
        d[3,2]= 13
        d[3,3]= 0
        d[3,4]= 6
        d[4,0]= 8
        d[4,1]= 2
        d[4,2]= 14
        d[4,3]= 6
        d[4,4]= 0
        
        for l in range(1,m+1):
            A = candidate.cluster(m, d, l)
            self.assertEqual(len(A), l)
        
        A = candidate.cluster(m, d, 1)
        self.assertEqual(A, [{0, 1, 2, 3, 4}])
        
        A = candidate.cluster(m, d, 2)
        self.assertEqual(A, [{0, 2}, {1, 3, 4}])
        
        A = candidate.cluster(m, d, 3)
        self.assertEqual(A, [{0}, {1, 3, 4}, {2}])
        
        A = candidate.cluster(m, d, 4)
        self.assertEqual(A, [{0}, {1, 4}, {2}, {3}])
        
        A = candidate.cluster(m, d, 5)
        self.assertEqual(A, [{0}, {1}, {2}, {3}, {4}])
        
    def test_2(self):
        m = 6
        
        d = {}
        d[0,0]= 0
        d[0,1]= 11
        d[0,2]= 7
        d[0,3]= 15
        d[0,4]= 8
        d[0,5]= 8
        d[1,0]= 11
        d[1,1]= 0
        d[1,2]= 12
        d[1,3]= 9
        d[1,4]= 2
        d[1,5]= 4
        d[2,0]= 7
        d[2,1]= 12
        d[2,2]= 0
        d[2,3]= 13
        d[2,4]= 14
        d[2,5]= 6
        d[3,0]= 15
        d[3,1]= 9
        d[3,2]= 13
        d[3,3]= 0
        d[3,4]= 6
        d[3,5]= 2
        d[4,0]= 8
        d[4,1]= 2
        d[4,2]= 14
        d[4,3]= 6
        d[4,4]= 0
        d[4,5]= 9
        d[5,0]= 8
        d[5,1]= 4
        d[5,2]= 6
        d[5,3]= 2
        d[5,4]= 9
        d[5,5]= 0
        
        for l in range(1,m+1):
            A = candidate.cluster(m, d, l)
            self.assertEqual(len(A), l)
        
        A = candidate.cluster(m, d, 1)
        self.assertEqual(A, [{0, 1, 2, 3, 4, 5}])
        
        A = candidate.cluster(m, d, 2)
        self.assertEqual(A, [{0}, {1, 2, 3, 4, 5}])
        
        A = candidate.cluster(m, d, 3)
        self.assertEqual(A, [{0}, {1, 3, 4, 5}, {2}])
        
        A = candidate.cluster(m, d, 4)
        self.assertEqual(A, [{0}, {1, 4}, {2}, {3, 5}])
        
        A = candidate.cluster(m, d, 5)
        self.assertEqual(A, [{0}, {1, 4}, {2}, {3}, {5}])
        
        A = candidate.cluster(m, d, 6)
        self.assertEqual(A, [{0}, {1}, {2}, {3}, {4}, {5}])
        
    def test_3(self):
        m = 3
        
        d = {}
        d[0,0]= 0
        d[0,1]= 11
        d[0,2]= 4
        d[1,0]= 11
        d[1,1]= 0
        d[1,2]= 12
        d[2,0]= 4
        d[2,1]= 12
        d[2,2]= 0
        
        for l in range(1,m+1):
            A = candidate.cluster(m, d, l)
            self.assertEqual(len(A), l)
        
        A = candidate.cluster(m, d, 1)
        self.assertEqual(A, [{0, 1, 2}])
        
        A = candidate.cluster(m, d, 2)
        self.assertEqual(A, [{0, 2}, {1}])
        
        A = candidate.cluster(m, d, 3)
        self.assertEqual(A, [{0}, {1}, {2}])
        
    def test_4(self):
        m = 1
        
        d = {}
        d[0,0]= 0
        
        for l in range(1,m+1):
            A = candidate.cluster(m, d, l)
            self.assertEqual(len(A), l)
        
        A = candidate.cluster(m, d, 1)
        self.assertEqual(A, [{0}])
        
    def test_5(self):
        m = 2
        
        d = {}
        d[0,0]= 0
        d[0,1]= 4
        d[1,0]= 4
        d[1,1]= 0
        
        for l in range(1,m+1):
            A = candidate.cluster(m, d, l)
            self.assertEqual(len(A), l)
        
        A = candidate.cluster(m, d, 1)
        self.assertEqual(A, [{0,1}])
        
        A = candidate.cluster(m, d, 2)
        self.assertEqual(A, [{0},{1}])

# Testausfuehrung via PyShell
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_cluster)
# unittest.TextTestRunner(verbosity=2).run(suite)
