

# 
def insertion_sort(a):
    m = len(a)              
    for i in range(1,m):
        key = a[i]              # wird in a[0,..,i-1] einsortiert
        j = i
        while (j>0) and a[j-1]>key:
            a[j] = a[j-1]       # verschiebe Vorgaenger nach re.
            j -= 1
        a[j] = key              # a[0,..,i] ist sortiert
    return a

a = [53,24,-12,54,0,22,-12]
insertion_sort(a)   
print(a)


# Laufzeitanalyse
# def insertion_sort(a):
#     m = len(a)              # O(1)
#     for i in range(1,m):    # O(m-1)-oft
#         key = a[i]            # O(1)  
#         j = i                 # O(1)
#         while (j>0) and a[j-1]>key:   # hoechstens i-oft 
#             a[j] = a[j-1]             # O(1)
#             j -= 1                    # O(1)
#         a[j] = key            # O(1)
#     return a                # O(1)