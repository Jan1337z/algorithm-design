
# Adjazenzmengen nach Adjazenzmatrix in O(m^2)=O(|Ausgabe|) 
def to_matrix(G):
    A = []
    # todo
    return A

# Adjazenzmatrix nach Adjazenzmengen in O(m^2)=O(n)  
def from_matrix(A):
    G = []
    # todo
    return G

# Graph als Adjazenzmatrix
def define_G_matrix():
    A = []
    A.append([0,1,1,0,0])
    A.append([1,0,1,1,1])
    A.append([1,1,0,1,1])
    A.append([0,1,1,0,1])
    A.append([0,1,1,1,0])
    return A


A = define_G_matrix()
print('A:',A)
G = from_matrix(A)
print('G:',G)
B = to_matrix(G)
print('B:',B)
print(A == B)

