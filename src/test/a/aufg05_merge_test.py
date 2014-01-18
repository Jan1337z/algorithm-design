
import unittest
import ueb.a.aufg05_merge as candidate

# Testfaelle fuer merge()
class Test_merge(unittest.TestCase):
    
    # a laenger als b
    def test_1(self):
        a=[-3,0,1,4,7]
        b=[-2,5,25]
        self.assertEqual(candidate.merge(a,b), [-3,-2,0,1,4,5,7,25])
        self.assertTrue(a == [-3,0,1,4,7], 'a geaendert')
        self.assertTrue(b == [-2,5,25], 'b geaendert')
    
    # b laenger als a
    def test_2(self):
        b=[-3,0,1,4,7]
        a=[-2,5,25]
        self.assertEqual(candidate.merge(a,b), [-3,-2,0,1,4,5,7,25])
        self.assertTrue(b == [-3,0,1,4,7], 'b geaendert')
        self.assertTrue(a == [-2,5,25], 'a geaendert')
    
    # b leer
    def test_3(self):
        a=[-3,0,1,4,7]
        b=[]
        self.assertEqual(candidate.merge(a,b), [-3,0,1,4,7])
        self.assertTrue(a == [-3,0,1,4,7], 'a geaendert')
        self.assertTrue(b == [], 'b geaendert')
    
    # a leer
    def test_4(self):
        a=[]
        b=[-2,5,25]
        self.assertEqual(candidate.merge(a,b), [-2,5,25])
        self.assertTrue(a == [], 'a geaendert')
        self.assertTrue(b == [-2,5,25], 'b geaendert')
    
    # a,b leer
    def test_5(self):
        a=[]
        b=[]
        self.assertEqual(candidate.merge(a,b), [])
        self.assertTrue(a == [], 'a geaendert')
        self.assertTrue(b == [], 'b geaendert')
    
    # letztes Element gleich
    def test_6(self):
        a=[-3,0,1,4,7,25]
        b=[-2,5,25]
        self.assertEqual(candidate.merge(a,b), [-3,-2,0,1,4,5,7,25,25])
        self.assertTrue(a == [-3,0,1,4,7,25], 'a geaendert')
        self.assertTrue(b == [-2,5,25], 'b geaendert')
    
    # a gleich b
    def test_7(self):
        a=[-3,0,1,4,7,25]
        b=[-3,0,1,4,7,25]
        self.assertEqual(candidate.merge(a,b), [-3,-3,0,0,1,1,4,4,7,7,25,25])
        self.assertTrue(a == [-3,0,1,4,7,25], 'a geaendert')
        self.assertTrue(b == [-3,0,1,4,7,25], 'b geaendert')


# Testausfuehrung via PyShell
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_merge)
# unittest.TextTestRunner(verbosity=2).run(suite)

