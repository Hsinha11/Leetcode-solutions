class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v,dist in roads:
            graph[u].append((v,dist))
            graph[v].append((u,dist))
        ans = float('inf')
        q = deque([(1)])
        visited = set()
        while q:
            u = q.popleft()
            for v,dist in graph[u]:
                ans = min(ans,dist)
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        return ans
