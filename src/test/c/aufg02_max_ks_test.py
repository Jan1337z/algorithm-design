import unittest
import timeit
import ueb.c.aufg02_max_ks_exh as candidate_exh
import ueb.c.aufg02_max_ks_bt as candidate_bt
import ueb.c.aufg02_max_ks_bab as candidate_bab

def exec_helper_exh(s,v,S):
    candidate_exh.max_ks_exhaustive(s,v,S)

def exec_helper_bt(s,v,S):
    candidate_bt.max_ks_backtracking(s,v,S)

def exec_helper_bab(s,v,S):
    candidate_bab.max_ks_bab(s,v,S)

class Test_max_ks(unittest.TestCase):
    
    def test_1(self):
        s = [3,2,1,5]
        v = [3,1,1,4]
        S = 7
        opt = 5
        
        r_exh = candidate_exh.max_ks_exhaustive(s,v,S)
        r_bt = candidate_bt.max_ks_backtracking(s,v,S)
        r_bab = candidate_bab.max_ks_bab(s,v,S)
        
        self.assertEqual(r_exh, opt)
        self.assertEqual(r_bt, opt)
        self.assertEqual(r_bab, opt)
        
        num_of_execs = 5
        
        timer_exh = timeit.Timer('exec_helper_exh(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_exh')
        t_exh = timer_exh.timeit(num_of_execs)
        
        timer_bt = timeit.Timer('exec_helper_bt(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_bt')
        t_bt = timer_bt.timeit(num_of_execs)
        
        timer_bab = timeit.Timer('exec_helper_bab(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_bab')
        t_bab = timer_bab.timeit(num_of_execs)
        
        print('Test 1: 4 Gegenstände')
        print('Exhaustive Search:     ' + str(t_exh/num_of_execs) + ' Sek.')
        print('Backtracking:          ' + str(t_bt/num_of_execs) + ' Sek.')
        print('Branch&Bound:          ' + str(t_bab/num_of_execs) + ' Sek.')
        print('------------------------------------------------')
    
    def test_2(self):
        s = [3,2,1,5]
        v = [3,1,1,4]
        S = 8
        opt = 7
        
        r_exh = candidate_exh.max_ks_exhaustive(s,v,S)
        r_bt = candidate_bt.max_ks_backtracking(s,v,S)
        r_bab = candidate_bab.max_ks_bab(s,v,S)
        
        self.assertEqual(r_exh, opt)
        self.assertEqual(r_bt, opt)
        self.assertEqual(r_bab, opt)
        
        num_of_execs = 5
        
        timer_exh = timeit.Timer('exec_helper_exh(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_exh')
        t_exh = timer_exh.timeit(num_of_execs)
        
        timer_bt = timeit.Timer('exec_helper_bt(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_bt')
        t_bt = timer_bt.timeit(num_of_execs)
        
        timer_bab = timeit.Timer('exec_helper_bab(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_bab')
        t_bab = timer_bab.timeit(num_of_execs)
        
        print('Test 2: 4 Gegenstände')
        print('Exhaustive Search:     ' + str(t_exh/num_of_execs) + ' Sek.')
        print('Backtracking:          ' + str(t_bt/num_of_execs) + ' Sek.')
        print('Branch&Bound:          ' + str(t_bab/num_of_execs) + ' Sek.')
        print('------------------------------------------------')
        
    def test_3(self):
        s =  [3, 9, 10, 10, 1, 9, 10, 8, 10, 4]
        v =  [3, 5, 7, 1, 2, 6, 10, 1, 7, 4]
        S =  20
        opt = 19
        
        r_exh = candidate_exh.max_ks_exhaustive(s,v,S)
        r_bt = candidate_bt.max_ks_backtracking(s,v,S)
        r_bab = candidate_bab.max_ks_bab(s,v,S)
        
        self.assertEqual(r_exh, opt)
        self.assertEqual(r_bt, opt)
        self.assertEqual(r_bab, opt)
        
        num_of_execs = 5
        
        timer_exh = timeit.Timer('exec_helper_exh(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_exh')
        t_exh = timer_exh.timeit(num_of_execs)
        
        timer_bt = timeit.Timer('exec_helper_bt(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_bt')
        t_bt = timer_bt.timeit(num_of_execs)
        
        timer_bab = timeit.Timer('exec_helper_bab(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_bab')
        t_bab = timer_bab.timeit(num_of_execs)
        
        print('Test 3: 10 Gegenstände')
        print('Exhaustive Search:     ' + str(t_exh/num_of_execs) + ' Sek.')
        print('Backtracking:          ' + str(t_bt/num_of_execs) + ' Sek.')
        print('Branch&Bound:          ' + str(t_bab/num_of_execs) + ' Sek.')
        print('------------------------------------------------')
        
    def test_4(self):
        s =  [5, 4, 4, 8, 4, 6, 9, 10, 1, 1]
        v =  [9, 3, 5, 3, 1, 7, 3, 10, 4, 3]
        S =  20
        opt = 28
        
        r_exh = candidate_exh.max_ks_exhaustive(s,v,S)
        r_bt = candidate_bt.max_ks_backtracking(s,v,S)
        r_bab = candidate_bab.max_ks_bab(s,v,S)
        
        self.assertEqual(r_exh, opt)
        self.assertEqual(r_bt, opt)
        self.assertEqual(r_bab, opt)
        
        num_of_execs = 5
        
        timer_exh = timeit.Timer('exec_helper_exh(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_exh')
        t_exh = timer_exh.timeit(num_of_execs)
        
        timer_bt = timeit.Timer('exec_helper_bt(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_bt')
        t_bt = timer_bt.timeit(num_of_execs)
        
        timer_bab = timeit.Timer('exec_helper_bab(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_bab')
        t_bab = timer_bab.timeit(num_of_execs)
        
        print('Test 4: 10 Gegenstände')
        print('Exhaustive Search:     ' + str(t_exh/num_of_execs) + ' Sek.')
        print('Backtracking:          ' + str(t_bt/num_of_execs) + ' Sek.')
        print('Branch&Bound:          ' + str(t_bab/num_of_execs) + ' Sek.')
        print('------------------------------------------------')
        
    def test_5(self):
        s =  [2, 9, 18, 6, 1, 9, 12, 11, 7, 13, 7, 17, 9, 12, 8]
        v =  [5, 3, 11, 17, 20, 17, 1, 7, 17, 14, 12, 1, 2, 5, 15]
        S =  20
        opt = 59
        
        r_exh = candidate_exh.max_ks_exhaustive(s,v,S)
        r_bt = candidate_bt.max_ks_backtracking(s,v,S)
        r_bab = candidate_bab.max_ks_bab(s,v,S)
        
        self.assertEqual(r_exh, opt)
        self.assertEqual(r_bt, opt)
        self.assertEqual(r_bab, opt)
        
        num_of_execs = 5
        
        timer_exh = timeit.Timer('exec_helper_exh(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_exh')
        t_exh = timer_exh.timeit(num_of_execs)
        
        timer_bt = timeit.Timer('exec_helper_bt(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_bt')
        t_bt = timer_bt.timeit(num_of_execs)
        
        timer_bab = timeit.Timer('exec_helper_bab(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_bab')
        t_bab = timer_bab.timeit(num_of_execs)
        
        print('Test 5: 15 Gegenstände')
        print('Exhaustive Search:     ' + str(t_exh/num_of_execs) + ' Sek.')
        print('Backtracking:          ' + str(t_bt/num_of_execs) + ' Sek.')
        print('Branch&Bound:          ' + str(t_bab/num_of_execs) + ' Sek.')
        print('------------------------------------------------')
        
    def test_6(self):
        s =  [2, 18, 4, 7, 6, 13, 12, 19, 4, 1, 19, 9, 15, 13, 8, 6, 17, 10, 13, 7]
        v =  [5, 15, 1, 8, 10, 1, 2, 16, 1, 6, 2, 16, 8, 14, 20, 17, 20, 16, 8, 12]
        S =  30
        opt = 70
        
        r_exh = candidate_exh.max_ks_exhaustive(s,v,S)
        r_bt = candidate_bt.max_ks_backtracking(s,v,S)
        r_bab = candidate_bab.max_ks_bab(s,v,S)
        
        self.assertEqual(r_exh, opt)
        self.assertEqual(r_bt, opt)
        self.assertEqual(r_bab, opt)
        
        num_of_execs = 3
        
        timer_exh = timeit.Timer('exec_helper_exh(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_exh')
        t_exh = timer_exh.timeit(num_of_execs)
        
        timer_bt = timeit.Timer('exec_helper_bt(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_bt')
        t_bt = timer_bt.timeit(num_of_execs)
        
        timer_bab = timeit.Timer('exec_helper_bab(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_bab')
        t_bab = timer_bab.timeit(num_of_execs)
        
        print('Test 6: 20 Gegenstände')
        print('Exhaustive Search:     ' + str(t_exh/num_of_execs) + ' Sek.')
        print('Backtracking:          ' + str(t_bt/num_of_execs) + ' Sek.')
        print('Branch&Bound:          ' + str(t_bab/num_of_execs) + ' Sek.')
        print('------------------------------------------------')
        
    def test_7(self):
        s =  [32, 37, 24, 49, 28, 41, 32, 46, 45, 20, 31, 29, 13, 2, 21, 1, 31, 29, 10, 9, 34, 3, 33, 43, 50]
        v =  [48, 23, 4, 13, 10, 47, 5, 31, 23, 4, 30, 4, 38, 36, 22, 35, 21, 47, 5, 7, 12, 35, 41, 46, 16]
        S =  100
        opt =  251
        
        #r_exh = candidate_exh.max_ks_exhaustive(s,v,S)
        r_bt = candidate_bt.max_ks_backtracking(s,v,S)
        r_bab = candidate_bab.max_ks_bab(s,v,S)
        
        #self.assertEqual(r_exh, opt)
        self.assertEqual(r_bt, opt)
        self.assertEqual(r_bab, opt)
        
        num_of_execs = 3
        
        #timer_exh = timeit.Timer('exec_helper_exh(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_exh')
        #t_exh = timer_exh.timeit(num_of_execs)
        
        timer_bt = timeit.Timer('exec_helper_bt(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_bt')
        t_bt = timer_bt.timeit(num_of_execs)
        
        timer_bab = timeit.Timer('exec_helper_bab(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_bab')
        t_bab = timer_bab.timeit(num_of_execs)
        
        print('Test 7: 25 Gegenstände')
        print('Exhaustive Search:     Nicht ausgeführt.')
        print('Backtracking:          ' + str(t_bt/num_of_execs) + ' Sek.')
        print('Branch&Bound:          ' + str(t_bab/num_of_execs) + ' Sek.')
        print('------------------------------------------------')
        
    def test_8(self):
        s =  [26, 2, 6, 16, 42, 38, 34, 27, 47, 36, 48, 32, 40, 42, 32, 33, 25, 46, 34, 40, 18, 45, 15, 32, 21, 6, 25, 41, 16, 45]
        v =  [45, 21, 45, 9, 30, 25, 45, 39, 12, 39, 36, 29, 41, 21, 25, 3, 32, 37, 11, 9, 49, 18, 23, 48, 43, 44, 8, 1, 38, 8]
        S =  100
        opt =  285
        
        #r_exh = candidate_exh.max_ks_exhaustive(s,v,S)
        r_bt = candidate_bt.max_ks_backtracking(s,v,S)
        r_bab = candidate_bab.max_ks_bab(s,v,S)
        
        #self.assertEqual(r_exh, opt)
        self.assertEqual(r_bt, opt)
        self.assertEqual(r_bab, opt)
        
        num_of_execs = 3
        
        #timer_exh = timeit.Timer('exec_helper_exh(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_exh')
        #t_exh = timer_exh.timeit(num_of_execs)
        
        timer_bt = timeit.Timer('exec_helper_bt(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_bt')
        t_bt = timer_bt.timeit(num_of_execs)
        
        timer_bab = timeit.Timer('exec_helper_bab(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_bab')
        t_bab = timer_bab.timeit(num_of_execs)
        
        print('Test 8: 30 Gegenstände')
        print('Exhaustive Search:     Nicht ausgeführt.')
        print('Backtracking:          ' + str(t_bt/num_of_execs) + ' Sek.')
        print('Branch&Bound:          ' + str(t_bab/num_of_execs) + ' Sek.')
        print('------------------------------------------------')
        
    def test_9(self):
        s =  [29, 7, 38, 50, 3, 46, 1, 12, 47, 6, 48, 6, 41, 36, 19, 35, 50, 8, 18, 32, 13, 14, 34, 34, 38, 18, 12, 4, 16, 12, 7, 2, 29, 11, 8]
        v =  [34, 14, 37, 50, 48, 19, 23, 31, 10, 32, 3, 39, 3, 40, 20, 47, 43, 13, 50, 16, 35, 50, 12, 6, 24, 9, 15, 28, 9, 14, 20, 44, 22, 38, 29]
        S =  200
        opt =  591
        
        #r_exh = candidate_exh.max_ks_exhaustive(s,v,S)
        #r_bt = candidate_bt.max_ks_backtracking(s,v,S)
        r_bab = candidate_bab.max_ks_bab(s,v,S)
        
        #self.assertEqual(r_exh, opt)
        #self.assertEqual(r_bt, opt)
        self.assertEqual(r_bab, opt)
        
        num_of_execs = 1
        
        #timer_exh = timeit.Timer('exec_helper_exh(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_exh')
        #t_exh = timer_exh.timeit(num_of_execs)
        
        #timer_bt = timeit.Timer('exec_helper_bt(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_bt')
        #t_bt = timer_bt.timeit(num_of_execs)
        
        timer_bab = timeit.Timer('exec_helper_bab(' + str(s) + ',' + str(v) + ',' + str(S) + ')', 'from aufg02_max_ks_test import exec_helper_bab')
        t_bab = timer_bab.timeit(num_of_execs)
        
        print('Test 9: 35 Gegenstände')
        print('Exhaustive Search:     Nicht ausgeführt.')
        print('Backtracking:          Nicht ausgeführt.')
        print('Branch&Bound:          ' + str(t_bab/num_of_execs) + ' Sek.')
        print('------------------------------------------------')

# Testausfuehrung via PyShell
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_max_ks)
# unittest.TextTestRunner(verbosity=2).run(suite) 