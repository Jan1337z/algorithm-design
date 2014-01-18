import ueb.e.aufg03_bin_search as candidate
import unittest

# Testfaelle BINARY SEARCH
class Test_bin_search(unittest.TestCase):
    
    # ungerade
    def test_1(self):
        L = [-4,7,9,12,34,68,345,511,512]
        self.assertEqual(candidate.bin_search(L,511), 7)
    
    def test_2(self):
        L = [-4,7,9,12,34,68,345,511,512]
        self.assertTrue(type(candidate.bin_search(L,513)) == type(""))
    
    def test_3(self):
        L = [-4,7,9,12,34,68,345,511,512]
        self.assertEqual(candidate.bin_search(L,-4), 0)
    
    def test_4(self):
        L = [-4,7,9,12,34,68,345,511,512]
        self.assertEqual(candidate.bin_search(L,345), 6)
    
    def test_5(self):
        L = [-4,7,9,12,34,68,345,511,512]
        self.assertTrue(type(candidate.bin_search(L,-5)) == type(""))
    
    def test_6(self):
        L = [-4,7,9,12,34,68,345,511,512]
        self.assertTrue(type(candidate.bin_search(L,69)) == type(""))
    
    def test_7(self):
        L = [-4,7,9,12,34,68,345,511,512]
        self.assertTrue(type(candidate.bin_search(L,8)) == type(""))
    
    #gerade
    def test_8(self):
        L = [-4,7,9,12,34,68]
        self.assertEqual(candidate.bin_search(L,68), 5)
    
    def test_9(self):
        L = [-4,7,9,12,34,68]
        self.assertTrue(type(candidate.bin_search(L,69)) == type(""))
    
    def test_10(self):
        L = [-4,7,9,12,34,68]
        self.assertEqual(candidate.bin_search(L,7), 1)
    
    def test_11(self):
        L = [-4,7,9,12,34,68]
        self.assertEqual(candidate.bin_search(L,9), 2)
    
    def test_12(self):
        L = [-4,7,9,12,34,68]
        self.assertTrue(type(candidate.bin_search(L,-5)) == type(""))
    
    def test_13(self):
        L = [-4,7,9,12,34,68]
        self.assertTrue(type(candidate.bin_search(L,35)) == type(""))
    
    def test_14(self):
        L = [-4,7,9,12,34,68]
        self.assertTrue(type(candidate.bin_search(L,8)) == type(""))
    
    #2er-Potenz
    def test_15(self):
        L = [-4,7,9,12,34,68,88,120]
        self.assertEqual(candidate.bin_search(L,68), 5)
    
    def test_16(self):
        L = [-4,7,9,12,34,68,88,120]
        self.assertTrue(type(candidate.bin_search(L,69)) == type(""))
    
    def test_17(self):
        L = [-4,7,9,12,34,68,88,120]
        self.assertEqual(candidate.bin_search(L,7), 1)
    
    def test_18(self):
        L = [-4,7,9,12,34,68,88,120]
        self.assertEqual(candidate.bin_search(L,9), 2)
    
    def test_19(self):
        L = [-4,7,9,12,34,68,88,120]
        self.assertTrue(type(candidate.bin_search(L,-5)) == type(""))
    
    def test_20(self):
        L = [-4,7,9,12,34,68,88,120]
        self.assertTrue(type(candidate.bin_search(L,35)) == type(""))
    
    def test_21(self):
        L = [-4,7,9,12,34,68,88,120]
        self.assertTrue(type(candidate.bin_search(L,8)) == type(""))

# Testausfuehrung via PyShell
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_bin_search)
# unittest.TextTestRunner(verbosity=2).run(suite)
