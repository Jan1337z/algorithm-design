
# UnionFind-Datenstruktur als oo-Klasse
class UnionFind():
    
    # Konstruktor makeUnionFind(m)
    def __init__(self, m):
        self.sets = [{j} for j in range(m)]             # O(m)
        self.set_containing = [ i for i in range(m)]    # O(m)
    
    def find(self,i):
        return self.set_containing[i]                   # O(1)
    
    def union(self, A, B):
        if len(self.sets[A]) > len(self.sets[B]):       # O(1)
            A,B = B,A       # A ist nicht die groessere Menge
        # Elemente aus A gehoeren zu B
        for i in self.sets[A]:                          # O(#A)
            self.set_containing[i] = B                  # O(1)
        # Mengen vereinigen
        self.sets[B] |= self.sets[A]                    # O(#A)
        self.sets[A] = set()                            # O(1)


# Verwendung:
# Instanz mit m=5 erzeugen
uf = UnionFind(5) # __init__ wird ausgefuehrt

uf.sets           # Instanzvars sind public 
uf.set_containing

# in welcher Menge ist 3?
uf.find(3)

# vereinige die Mengen die 2 bzw. 3 enthalten
uf.union(uf.find(2),uf.find(3))
uf.sets
uf.set_containing


# vereinige die Mengen die 2 bzw. 4 enthalten 
uf.union(uf.find(2),uf.find(4))
uf.sets
uf.set_containing

# restliche Vereinigungen
uf.union(uf.find(0),uf.find(1))
uf.union(uf.find(1),uf.find(4))
uf.sets
uf.set_containing
