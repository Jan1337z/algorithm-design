from ueb.d.aufg01_min_intpart_exh import compatible, m_min_intpart

# MINIMUM INTERVAL PARTITIONING


# Enwurfsmuster Greedy
def min_intpart_greedy(L):
    m = len(L)            
    # create m resources
    R = [set() for _ in range(m)]
    for i,_ in enumerate(L):
        for r in R:
            # if current resource intersected with new
            # element is compatible -> add it
            # else try next resource
            if(compatible(L, r | {i})): 
                r.add(i)
                break;
            
    return m_min_intpart(L, R)


# Bsp
# L = [(0,3),(0,12),(0,4),(4,6),(5,7),(8,10),(9,13),(14,17),(15,16)]
# print(min_intpart_greedy(L))
# print(min_intpart_greedy([(0,2),(0,3),(1,3),(2,4)]))
# print(min_intpart_greedy([(0,3),(0,2),(2,3),(3,4)]))


# Laufzeit
#

