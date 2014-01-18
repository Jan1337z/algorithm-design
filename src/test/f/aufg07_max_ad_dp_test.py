import ueb.f.aufg07_max_ad_dp as candidate
import unittest

# Testfaelle fuer max_ap_dp

class Test_max_ad_dp(unittest.TestCase):
    
    def test_1(self):
        s = [6,7,12,14]
        r = [5,6,5,1]
        G = 10
        
        self.assertEqual(candidate.max_ap_dp(s, r), G)
        
    def test_2(self):
        s = [4,9,24,25,30]
        r = [1,1,4,5,1]
        G = 6
        
        self.assertEqual(candidate.max_ap_dp(s, r), G)
        
    def test_3(self):
        s = [3,9,24,25,31]
        r = [1,1,4,5,1]
        G = 8
        
        self.assertEqual(candidate.max_ap_dp(s, r), G)
        
    def test_4(self):
        s = [3,9,20,25,31]
        r = [1,1,4,5,1]
        G = 8
        
        self.assertEqual(candidate.max_ap_dp(s, r), G)
        
    def test_5(self):
        s = [3,9,19,25,31]
        r = [1,1,4,5,1]
        G = 12
        
        self.assertEqual(candidate.max_ap_dp(s, r), G)
        
    def test_6(self):
        s = [3,8,9,25,31]
        r = [1,2,2,5,1]
        G = 9
        
        self.assertEqual(candidate.max_ap_dp(s, r), G)
        
    def test_7(self):
        s = [8,9,24,25,31,36,41,46]
        r = [1,2,4,5,1,2,3,8]
        G = 17
        
        self.assertEqual(candidate.max_ap_dp(s, r), G)
        
    def test_8(self):
        s = [3]
        r = [1]
        G = 1
        
        self.assertEqual(candidate.max_ap_dp(s, r), G)
        
    def test_9(self):
        s = []
        r = []
        G = 0
        
        self.assertEqual(candidate.max_ap_dp(s, r), G)
        
# Testausfuehrung via PyShell
# if __name__ == "__main__":
#     suite = unittest.TestLoader().loadTestsFromTestCase(Test_max_ad_dp)
#     unittest.TextTestRunner(verbosity=2).run(suite)
