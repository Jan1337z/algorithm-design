import ueb.f.aufg06_min_ed_dp as candidate
import unittest

# Testfaelle fuer min_ed_dp

class Test_min_ed_dp(unittest.TestCase):
    
    def test_1(self):
        a = 'apfel'
        b = 'pferd'
        d = 3
        
        self.assertEqual(candidate.min_ed_dp(a, b), d)
        
    def test_2(self):
        a = 'abc'
        b = 'cd'
        d = 3
        
        self.assertEqual(candidate.min_ed_dp(a, b), d)
        
    def test_3(self):
        a = ''
        b = '123'
        d = 3
        
        self.assertEqual(candidate.min_ed_dp(a, b), d)
        
    def test_4(self):
        a = 'hallo'
        b = 'halo'
        d = 1
        
        self.assertEqual(candidate.min_ed_dp(a, b), d)
        
    def test_5(self):
        a = '123'
        b = '321'
        d = 2
        
        self.assertEqual(candidate.min_ed_dp(a, b), d)
        
    def test_6(self):
        a = ''
        b = ''
        d = 0
        
        self.assertEqual(candidate.min_ed_dp(a, b), d)
        
    def test_7(self):
        a = 'abcdef'
        b = '123'
        d = 6
        
        self.assertEqual(candidate.min_ed_dp(a, b), d)
        
    def test_8(self):
        a = 'expect'
        b = 'respect'
        d = 2
        
        self.assertEqual(candidate.min_ed_dp(a, b), d)
        
    def test_9(self):
        a = ''
        b = '1'
        d = 1
        
        self.assertEqual(candidate.min_ed_dp(a, b), d)
        
    def test_10(self):
        a = '1'
        b = ''
        d = 1
        
        self.assertEqual(candidate.min_ed_dp(a, b), d)
        
# Testausfuehrung via PyShell
# if __name__ == "__main__":
#     suite = unittest.TestLoader().loadTestsFromTestCase(Test_min_ed_dp)
#     unittest.TextTestRunner(verbosity=2).run(suite)
