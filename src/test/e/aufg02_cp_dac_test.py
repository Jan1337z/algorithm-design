from vl.lek08.cp_all_pairs import cp_all_pairs, rand_set

import ueb.e.aufg02_cp_dac as candidate
import unittest
import timeit

def exec_helper_cp(U):
    return candidate.cp(U)

def exec_helper_cp_all_pairs(U):
    return cp_all_pairs(U)

class Test_cp_dac(unittest.TestCase):
    
    def test_1(self):
        U = {(12,4),(2,17),(3,3)}
        self.assertEqual(candidate.cp(U), cp_all_pairs(U))
        
    def test_2(self):
        U = {(2,2), (3,4), (5,4)}
        self.assertEqual(candidate.cp(U), cp_all_pairs(U))
        
    def test_3(self):
        U = {(2, 3), (7, 15), (9, 2), (11, 12)}
        self.assertEqual(candidate.cp(U), cp_all_pairs(U))
        
    def test_4(self):
        U = {(3, 24), (13, 6), (5, 20), (0, 0), (27, 25)}
        self.assertEqual(candidate.cp(U), cp_all_pairs(U))
        
    def test_5(self):
        for _ in range(100):
            for j in range(3,20):
                U = rand_set(j)
                if len(U) >= 3:
                    self.assertEqual(candidate.cp(U), cp_all_pairs(U))
                    
    def test_6(self):
        print('Laufzeit-Vergleich')
        for i in range(1,6):
            U = rand_set(i*500)
            
            T0 = timeit.Timer('exec_helper_cp(' + str(U) + ')', 'from aufg02_cp_dac_test import exec_helper_cp')
            T1 = timeit.Timer('exec_helper_cp_all_pairs(' + str(U) + ')', 'from aufg02_cp_dac_test import exec_helper_cp_all_pairs')
       
            t0 = T0.repeat(1,1)  
            t1 = T1.repeat(1,1)  
            print('cp           mit #U =',len(U),'Dauer in sec : ', t0)
            print('cp_all_pairs mit #U =',len(U),'Dauer in sec : ', t1)
            print('------------------------------------------------')

# Testausfuehrung via PyShell
# if __name__ == "__main__":
#     suite = unittest.TestLoader().loadTestsFromTestCase(Test_cp_dac)
#     unittest.TextTestRunner(verbosity=2).run(suite)