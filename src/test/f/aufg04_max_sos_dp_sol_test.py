import ueb.f.aufg04_max_sos_dp_sol as candidate
import unittest

# Testfaelle fuer max_sos_dp_sol
# bei Mehrdeutigkeit wird Geg. nicht hinzugenommen, 
# daher ist auch opt. Lsg eindeutig

class Test_max_sos_dp_sol(unittest.TestCase):
    
    def test_1(self):
        s = [6,3,5,8]
        S = 12
        R = {0,2}
        
        self.assertEqual(candidate.max_sos_dp_sol(s, S), R)
        
    def test_2(self):
        s = [6,3,5,8,14,10,2]
        S = 20
        R = {0,4}
        
        self.assertEqual(candidate.max_sos_dp_sol(s, S), R)
        
    def test_3(self):
        s = [1,1,1,1,1,1,1]
        S = 4
        R = {0,1,2,3}
        
        self.assertEqual(candidate.max_sos_dp_sol(s, S), R)
        
    def test_4(self):
        s = [3,4,8,3]
        S = 11
        R = {0,2}
        
        self.assertEqual(candidate.max_sos_dp_sol(s, S), R)
        
    def test_5(self):
        s = [3,4,8,20]
        S = 19
        R = {0,1,2}
        
        self.assertEqual(candidate.max_sos_dp_sol(s, S), R)
        
    def test_6(self):
        s = [6,3,5,8,5,45,8,2,3,7,5,63,8,8,2,8,9,4,52,9,58,4,95,19,8,78,62,7]
        S = 100
        R = {0, 1, 2, 3, 4, 6, 7, 11}
        
        self.assertEqual(candidate.max_sos_dp_sol(s, S), R)
        
    def test_7(self):
        s = [0,0,0,8,2]
        S = 10
        R = {3, 4}
        
        self.assertEqual(candidate.max_sos_dp_sol(s, S), R)
        
    def test_8(self):
        s = [5]
        S = 10
        R = {0}
        
        self.assertEqual(candidate.max_sos_dp_sol(s, S), R)
        
    def test_9(self):
        s = [0]
        S = 0
        R = set()
        
        self.assertEqual(candidate.max_sos_dp_sol(s, S), R)

# Testausfuehrung via PyShell
# if __name__ == "__main__":
#     suite = unittest.TestLoader().loadTestsFromTestCase(Test_max_sos_dp_sol)
#     unittest.TextTestRunner(verbosity=2).run(suite)