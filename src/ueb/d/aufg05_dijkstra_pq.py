
# (SINGLE-SOURCE) SHORTEST PATH

# Verbesserung von dijkstra mittels MinPrioQueue
from heapq import heappush, heappop
import heapq

def dijkstra_pq(G,s):
    m = len(G)
    d = [None]*m 
    p = [None]*m            
    d[s] = 0     
    Q = [(0,s)]
    
    while Q:
        c,v = heappop(Q) 
        for u in G[v]:
            alt = d[v] + G[v][u]
            if d[u]==None or alt < d[u]:
                d[u] = alt
                heappush(Q, (alt,u))
    return d
      

# G aus VL
from vl.lek06.dijkstra import G
dijkstra_pq(G,0)
