import ueb.e.aufg14_karatsuba as candidate
from vl.lek09.mult_naiv import mult_naiv
import unittest
import timeit
import random

# Testfaelle fuer karatsuba
def exec_helper_mult_naiv(x,y):
    return mult_naiv(x,y)

def exec_helper_karatsuba(x,y):
    return candidate.karatsuba(x, y)

class Test_karatsuba(unittest.TestCase):
    
    def test_1(self):
        x = 12
        y = 13
        r = 156
        self.assertEqual(candidate.karatsuba(x, y), r)
        
    def test_2(self):
        x = -12
        y = 13
        r = -156
        self.assertEqual(candidate.karatsuba(x, y), r)
        
    def test_3(self):
        x = 7
        y = 13
        r = 91
        self.assertEqual(candidate.karatsuba(x, y), r)
        
    def test_4(self):
        x = 12
        y = 7
        r = 84
        self.assertEqual(candidate.karatsuba(x, y), r)
        
    def test_5(self):
        x = 1
        y = 1
        r = 1
        self.assertEqual(candidate.karatsuba(x, y), r)
        
    def test_6(self):
        x = -3
        y = 13
        r = -39
        self.assertEqual(candidate.karatsuba(x, y), r)
        
    def test_7(self):
        x = -1
        y = -2
        r = 2
        self.assertEqual(candidate.karatsuba(x, y), r)
        
    def test_8(self):
        x = 0
        y = 13
        r = 0
        self.assertEqual(candidate.karatsuba(x, y), r)
        
    def test_9(self):
        x = -13
        y = 0
        r = 0
        self.assertEqual(candidate.karatsuba(x, y), r)
        
    def test_10(self):
        x = 100
        y = 15
        r = 1500
        self.assertEqual(candidate.karatsuba(x, y), r)
        
    # Laufzeitvergleich
    def test_11(self):
        a = 2
        b = 2
        
        for i in range(200,210):
            x = pow(a, i) + random.randrange(pow(a, i-1))
            y = pow(b, i) + random.randrange(pow(a, i-1))
            
            r = x * y
            
            T0 = timeit.Timer('exec_helper_mult_naiv(' + str(x) + ',' + str(y) + ')', 'from aufg14_karatsuba_test import exec_helper_mult_naiv')
            T1 = timeit.Timer('exec_helper_karatsuba(' + str(x) + ',' + str(y) + ')', 'from aufg14_karatsuba_test import exec_helper_karatsuba')
            
            t0 = T0.repeat(1,1)  
            t1 = T1.repeat(1,1)  
            print('mult_naiv(' + str(x) + ',' + str(y) + ') = ' + str(r) + ', Multiplikation in sec : ', t0)
            print('karatsuba(' + str(x) + ',' + str(y) + ') = ' + str(r) + ', Multiplikation in sec : ', t1)
            print('-------------------------------------------------------------------------------------------')

# Testausfuehrung via PyShell
# if __name__ == "__main__":
#     suite = unittest.TestLoader().loadTestsFromTestCase(Test_karatsuba)
#     unittest.TextTestRunner(verbosity=2).run(suite)
