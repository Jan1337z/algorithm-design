

# Vorbedingung: a und b aufsteigend sortiert
# liefert neue Liste
def merge(a,b):
    
    a_i, b_i = 0,0
    result_list = []
    
    while a_i != len(a) and b_i != len(b):
        if(a[a_i]<=b[b_i]):
            result_list.append(a[a_i])
            a_i += 1 
        elif(b[b_i]<a[a_i]): 
            result_list.append(b[b_i])
            b_i += 1
            
    result_list += a[a_i:] 
    result_list += b[b_i:]
    return result_list


# r=[-3,0,1,4,7]
# s=[-2,5,25]
# print(merge(r,s))

# Laufzeit, m=len(a), k=len(b)
# to do 