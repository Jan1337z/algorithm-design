import unittest
import timeit
import ueb.c.aufg03_min_tsp_exh as candidate_exh
import ueb.c.aufg03_min_tsp_bab as candidate_bab

# Testfaelle fuer
# min_tsp_exhaustive
# min_tsp_bab

def exec_helper_exh(D):
    candidate_exh.min_tsp_exhaustive(D)

def exec_helper_bab(D):
    candidate_bab.min_tsp_bab(D)

class Test_min_tsp(unittest.TestCase):
    
    def test_1(self):
        D = [[0,1,1],[1,0,1],[1,1,0]]
        opt = 3
        
        r_exh = candidate_exh.min_tsp_exhaustive(D)
        r_bab = candidate_bab.min_tsp_bab(D)
        self.assertEqual(opt, r_exh)
        self.assertEqual(opt, r_bab)
        
        num_of_execs = 5
        
        timer_exh = timeit.Timer('exec_helper_exh(' + str(D) + ')', 'from aufg03_min_tsp_test import exec_helper_exh')
        t_exh = timer_exh.timeit(num_of_execs)
        
        timer_bab = timeit.Timer('exec_helper_bab(' + str(D) + ')', 'from aufg03_min_tsp_test import exec_helper_bab')
        t_bab = timer_bab.timeit(num_of_execs)
        
        print('Test 1: 3 Städte')
        print('Exhaustive Search:     ' + str(t_exh/num_of_execs) + ' Sek.')
        print('Branch&Bound:          ' + str(t_bab/num_of_execs) + ' Sek.')
        print('------------------------------------------------')
        
    def test_2(self):
        D = [[0,13,2],[7,0,2],[3,8,0]]
        opt = 17
        
        r_exh = candidate_exh.min_tsp_exhaustive(D)
        r_bab = candidate_bab.min_tsp_bab(D)
        self.assertEqual(opt, r_exh)
        self.assertEqual(opt, r_bab)
        
        num_of_execs = 5
        
        timer_exh = timeit.Timer('exec_helper_exh(' + str(D) + ')', 'from aufg03_min_tsp_test import exec_helper_exh')
        t_exh = timer_exh.timeit(num_of_execs)
        
        timer_bab = timeit.Timer('exec_helper_bab(' + str(D) + ')', 'from aufg03_min_tsp_test import exec_helper_bab')
        t_bab = timer_bab.timeit(num_of_execs)
        
        print('Test 2: 3 Städte')
        print('Exhaustive Search:     ' + str(t_exh/num_of_execs) + ' Sek.')
        print('Branch&Bound:          ' + str(t_bab/num_of_execs) + ' Sek.')
        print('------------------------------------------------')
        
    def test_3(self):
        D = [[0,13,2],[7,0,2],[1,8,0]]
        opt = 16
        
        r_exh = candidate_exh.min_tsp_exhaustive(D)
        r_bab = candidate_bab.min_tsp_bab(D)
        self.assertEqual(opt, r_exh)
        self.assertEqual(opt, r_bab)
        
        num_of_execs = 5
        
        timer_exh = timeit.Timer('exec_helper_exh(' + str(D) + ')', 'from aufg03_min_tsp_test import exec_helper_exh')
        t_exh = timer_exh.timeit(num_of_execs)
        
        timer_bab = timeit.Timer('exec_helper_bab(' + str(D) + ')', 'from aufg03_min_tsp_test import exec_helper_bab')
        t_bab = timer_bab.timeit(num_of_execs)
        
        print('Test 3: 3 Städte')
        print('Exhaustive Search:     ' + str(t_exh/num_of_execs) + ' Sek.')
        print('Branch&Bound:          ' + str(t_bab/num_of_execs) + ' Sek.')
        print('------------------------------------------------')
        
    def test_4(self):
        D = [[0, 5, 10, 9, 5], [5, 0, 9, 7, 4], [8, 2, 0, 3, 6], [7, 10, 4, 0, 3], [9, 2, 9, 1, 0]]
        opt =  17
        
        r_exh = candidate_exh.min_tsp_exhaustive(D)
        r_bab = candidate_bab.min_tsp_bab(D)
        self.assertEqual(opt, r_exh)
        self.assertEqual(opt, r_bab)
        
        num_of_execs = 5
        
        timer_exh = timeit.Timer('exec_helper_exh(' + str(D) + ')', 'from aufg03_min_tsp_test import exec_helper_exh')
        t_exh = timer_exh.timeit(num_of_execs)
        
        timer_bab = timeit.Timer('exec_helper_bab(' + str(D) + ')', 'from aufg03_min_tsp_test import exec_helper_bab')
        t_bab = timer_bab.timeit(num_of_execs)
        
        print('Test 4: 5 Städte')
        print('Exhaustive Search:     ' + str(t_exh/num_of_execs) + ' Sek.')
        print('Branch&Bound:          ' + str(t_bab/num_of_execs) + ' Sek.')
        print('------------------------------------------------')
        
    def test_5(self):
        D =  [[0, 18, 10, 20, 4, 17, 8, 2], [15, 0, 3, 16, 12, 19, 17, 16], [11, 5, 0, 11, 4, 3, 18, 18], [14, 19, 10, 0, 20, 14, 8, 11], [11, 18, 5, 8, 0, 17, 12, 16], [15, 12, 18, 15, 8, 0, 17, 5], [3, 10, 5, 10, 18, 11, 0, 14], [16, 8, 6, 2, 19, 1, 18, 0]]
        opt =  41
        
        r_exh = candidate_exh.min_tsp_exhaustive(D)
        r_bab = candidate_bab.min_tsp_bab(D)
        self.assertEqual(opt, r_exh)
        self.assertEqual(opt, r_bab)
        
        num_of_execs = 5
        
        timer_exh = timeit.Timer('exec_helper_exh(' + str(D) + ')', 'from aufg03_min_tsp_test import exec_helper_exh')
        t_exh = timer_exh.timeit(num_of_execs)
        
        timer_bab = timeit.Timer('exec_helper_bab(' + str(D) + ')', 'from aufg03_min_tsp_test import exec_helper_bab')
        t_bab = timer_bab.timeit(num_of_execs)
        
        print('Test 5: 8 Städte')
        print('Exhaustive Search:     ' + str(t_exh/num_of_execs) + ' Sek.')
        print('Branch&Bound:          ' + str(t_bab/num_of_execs) + ' Sek.')
        print('------------------------------------------------')
        
    def test_6(self):
        D =  [[0, 20, 9, 20, 17, 5, 8, 18, 16, 10], [15, 0, 1, 6, 2, 2, 20, 17, 12, 18], [20, 8, 0, 6, 4, 12, 17, 12, 19, 2], [6, 5, 6, 0, 10, 2, 15, 20, 4, 18], [6, 8, 8, 18, 0, 5, 20, 1, 20, 15], [5, 3, 8, 19, 1, 0, 2, 3, 7, 9], [7, 8, 5, 13, 6, 6, 0, 1, 8, 20], [10, 20, 17, 18, 19, 14, 17, 0, 19, 1], [9, 15, 7, 13, 18, 3, 9, 17, 0, 8], [9, 18, 8, 16, 3, 6, 16, 4, 9, 0]]
        opt =  39
        
        r_exh = candidate_exh.min_tsp_exhaustive(D)
        r_bab = candidate_bab.min_tsp_bab(D)
        self.assertEqual(opt, r_exh)
        self.assertEqual(opt, r_bab)
        
        num_of_execs = 1
        
        timer_exh = timeit.Timer('exec_helper_exh(' + str(D) + ')', 'from aufg03_min_tsp_test import exec_helper_exh')
        t_exh = timer_exh.timeit(num_of_execs)
        
        timer_bab = timeit.Timer('exec_helper_bab(' + str(D) + ')', 'from aufg03_min_tsp_test import exec_helper_bab')
        t_bab = timer_bab.timeit(num_of_execs)
        
        print('Test 6: 10 Städte')
        print('Exhaustive Search:     ' + str(t_exh/num_of_execs) + ' Sek.')
        print('Branch&Bound:          ' + str(t_bab/num_of_execs) + ' Sek.')
        print('------------------------------------------------')
        
    def test_7(self):
        D =  [[0, 16, 1, 15, 10, 1, 14, 10, 5, 1, 1], [13, 0, 11, 9, 10, 6, 2, 10, 13, 1, 4], [10, 7, 0, 17, 12, 16, 13, 7, 7, 10, 15], [4, 18, 10, 0, 17, 13, 5, 8, 6, 11, 14], [16, 6, 2, 17, 0, 11, 19, 16, 8, 4, 1], [8, 20, 7, 12, 15, 0, 6, 13, 6, 18, 8], [15, 8, 12, 12, 8, 2, 0, 11, 5, 4, 11], [10, 19, 2, 6, 8, 9, 18, 0, 14, 14, 17], [8, 12, 17, 8, 5, 5, 8, 12, 0, 15, 7], [17, 18, 5, 20, 4, 3, 12, 11, 7, 0, 17], [8, 9, 1, 12, 1, 11, 4, 3, 19, 13, 0]]
        opt =  40
        
        #r_exh = candidate_exh.min_tsp_exhaustive(D)
        r_bab = candidate_bab.min_tsp_bab(D)
        #self.assertEqual(opt, r_exh)
        self.assertEqual(opt, r_bab)
        
        num_of_execs = 1
        
        #timer_exh = timeit.Timer('exec_helper_exh(' + str(D) + ')', 'from aufg03_min_tsp_test import exec_helper_exh')
        #t_exh = timer_exh.timeit(num_of_execs)
        
        timer_bab = timeit.Timer('exec_helper_bab(' + str(D) + ')', 'from aufg03_min_tsp_test import exec_helper_bab')
        t_bab = timer_bab.timeit(num_of_execs)
        
        print('Test 7: 11 Städte')
        print('Exhaustive Search:     Nicht ausgeführt.')
        print('Branch&Bound:          ' + str(t_bab/num_of_execs) + ' Sek.')
        print('------------------------------------------------')

# Testausfuehrung via PyShell
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_min_tsp)
# unittest.TextTestRunner(verbosity=2).run(suite)
