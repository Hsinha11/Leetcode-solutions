class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        q = deque([1])
        visited = {1}
        # print(q)
        maxdepth = -1
        while q:
            sz = len(q)
            for i in range(sz):
                cur = q.popleft()
                for v in adj[cur]:
                    if v not in visited:
                        visited.add(v)
                        q.append(v)
            maxdepth+=1
        return (2**(maxdepth-1))%(10**9 + 7)