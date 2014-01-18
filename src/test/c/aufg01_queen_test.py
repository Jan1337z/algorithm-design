import unittest
import ueb.c.aufg01_queen_bt_all as candidate

class Test_queen_bt_all(unittest.TestCase):
    
    def test_1(self):
        m = 2
        r = candidate.queen_backtracking_all(m)
        self.assertEqual(len(r), 0)
    
    def test_2(self):
        m = 3
        r = candidate.queen_backtracking_all(m)
        self.assertEqual(len(r), 0)
    
    def test_3(self):
        m = 4
        r = candidate.queen_backtracking_all(m)
        self.assertEqual(len(r), 2)
    
    def test_4(self):
        m = 5
        r = candidate.queen_backtracking_all(m)
        self.assertEqual(len(r), 10)
    
    def test_5(self):
        m = 6
        r = candidate.queen_backtracking_all(m)
        self.assertEqual(len(r), 4)
    
    def test_6(self):
        m = 7
        r = candidate.queen_backtracking_all(m)
        self.assertEqual(len(r), 40)
    
    def test_7(self):
        m = 8
        r = candidate.queen_backtracking_all(m)
        self.assertEqual(len(r), 92)
    
    def test_8(self):
        m = 9
        r = candidate.queen_backtracking_all(m)
        self.assertEqual(len(r), 352)
    
    def test_9(self):
        m = 10
        r = candidate.queen_backtracking_all(m)
        self.assertEqual(len(r), 724)
    
    def test_10(self):
        m = 11
        r = candidate.queen_backtracking_all(m)
        self.assertEqual(len(r), 2680)

# Testausfuehrung via PyShell
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_queen_bt_all)
# unittest.TextTestRunner(verbosity=2).run(suite)
