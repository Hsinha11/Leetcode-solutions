from collections import deque

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = [[] for _ in range(n)]
        for u, v, w in flights:
            adj[u].append((v, w))
        
        q = deque()
        q.append((0, src))
        dist = [float('inf')] * n
        dist[src] = 0
        
        stops = 0
        while q and stops <= k:
            size = len(q)
            for _ in range(size):
                dis, node = q.popleft()
                for adjNode, weight in adj[node]:
                    if dis + weight < dist[adjNode]:
                        dist[adjNode] = dis + weight
                        q.append((dis + weight, adjNode))
            stops += 1
        
        return -1 if dist[dst] == float('inf') else dist[dst]
