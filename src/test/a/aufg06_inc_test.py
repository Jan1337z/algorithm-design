
import unittest
import ueb.a.aufg06_inc as candidate

# Testfaelle für inc()
class Test_inc(unittest.TestCase):
        
    def test_1(self):
        a=[0,0,0,0,1]
        b=[0,0,0,1,0]
        candidate.inc(a)
        self.assertEqual(a, b)
    
    def test_2(self):
        a=[0,0,0,1,1]
        b=[0,0,1,0,0]
        candidate.inc(a)
        self.assertEqual(a, b)
        
    def test_3(self):
        a=[0,0,0,0,0]
        b=[0,0,0,0,1]
        candidate.inc(a)
        self.assertEqual(a, b)
        
    def test_4(self):
        a=[0,1,1,1,1]
        b=[1,0,0,0,0]
        candidate.inc(a)
        self.assertEqual(a, b)
        
    def test_5(self):
        a=[0,0,0,1,1]
        b=[0,0,1,0,0]
        candidate.inc(a)
        self.assertEqual(a, b)
        
    def test_6(self):
        a=[0,0,0]
        b=[0,0,1]
        candidate.inc(a)
        self.assertEqual(a, b)
        
    def test_7(self):
        a=[1,0,0,1,1]
        b=[1,0,1,0,0]
        candidate.inc(a)
        self.assertEqual(a, b)
        
    def test_8(self):
        a=[0,1,0,1,0]
        b=[0,1,0,1,1]
        candidate.inc(a)
        self.assertEqual(a, b)
        
    def test_9(self):
        a=[1,1,1,1,1]
        b=[0,0,0,0,0]
        candidate.inc(a)
        self.assertEqual(a, b)

# Testausfuehrung via PyShell
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_inc)
# unittest.TextTestRunner(verbosity=2).run(suite)
