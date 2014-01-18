import ueb.f.aufg05_min_cs_dp_sol as candidate
import unittest

# Testfaelle fuer min_cs_dp_sol
# bei Mehrdeutigkeit wird aktuelles Lager beibehalten und im letzten Lager t bevorzugt
# daher ist auch opt. Lsg eindeutig

class Test_min_cs_dp_sol(unittest.TestCase):
    
    def test_1(self):
        c = [{'t':1,'l':50}, {'t':3,'l':20}, {'t':20,'l':2}, {'t':30,'l':4}]
        u = 10
        r = ['t', 't', 'l', 'l']
        
        self.assertEqual(candidate.min_cs_dp_sol(c, u), r)
        
    def test_2(self):
        c = [{'t':30,'l':10}, {'t':20,'l':40}, {'t':50,'l':10}, {'t':20,'l':30}, {'t':30,'l':70}, {'t':40,'l':40}, {'t':50,'l':40}]
        u = 10
        r = ['t', 't', 'l', 't', 't', 't', 't']
        
        self.assertEqual(candidate.min_cs_dp_sol(c, u), r)
        
    def test_3(self):
        c = [{'t':30,'l':10}, {'t':20,'l':40}, {'t':50,'l':10}, {'t':20,'l':30}, {'t':30,'l':70}, {'t':40,'l':40}, {'t':50,'l':10}]
        u = 10
        r = ['t', 't', 'l', 't', 't', 'l', 'l']
        
        self.assertEqual(candidate.min_cs_dp_sol(c, u), r)
        
    def test_4(self):
        c = [{'t':30,'l':10}, {'t':20,'l':40}]
        u = 10
        r = ['t', 't']
        
        self.assertEqual(candidate.min_cs_dp_sol(c, u), r)
        
    def test_5(self):
        c = [{'t':80,'l':10}, {'t':30,'l':10}, {'t':10,'l':40}]
        u = 5
        r = ['t','l','t']
        
        self.assertEqual(candidate.min_cs_dp_sol(c, u), r)
        
    def test_6(self):
        c = [{'t':80,'l':10}, {'t':30,'l':10}]
        u = 20
        r = ['t','t']
        
        self.assertEqual(candidate.min_cs_dp_sol(c, u), r)
        
    def test_7(self):
        c = [{'t':80,'l':10}]
        u = 20
        r = ['t']
        
        self.assertEqual(candidate.min_cs_dp_sol(c, u), r)
        
    def test_8(self):
        c = [{'t':20,'l':10}, {'t':30,'l':10}, {'t':30,'l':10}]
        u = 10
        r = ['t','l', 'l']
        
        self.assertEqual(candidate.min_cs_dp_sol(c, u), r)

# Testausfuehrung via PyShell
# if __name__ == "__main__":
#    suite = unittest.TestLoader().loadTestsFromTestCase(Test_min_cs_dp_sol)
#    unittest.TextTestRunner(verbosity=2).run(suite)