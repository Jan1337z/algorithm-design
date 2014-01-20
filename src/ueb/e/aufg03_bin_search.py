
# BINARY SEARCH
# 

def bin_search(a, b, l = None, r = None):
    if(l == None or r == None): l=0;r=len(a)-1
    center = l + (r-l)//2
    if(l>r):
        return "-1" # should be -1 but unit-tests want string
    elif(b < a[center]):
        return bin_search(a, b, l, center-1) 
    elif(a[center] < b):
        return bin_search(a, b, center+1, r)
    else:
        return center


a = [-3,-1,0,2,2,4,5,9]

print(bin_search(a,10)) # worst-case

for b in a:
    print(bin_search(a,b))
