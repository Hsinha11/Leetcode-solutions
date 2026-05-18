class Solution:
    def minJumps(self, arr: List[int]) -> int:
        d= defaultdict(list)
        n = len(arr)
        if n==1:
            return 0
        for i in range(n):
            d[arr[i]].append(i)
        distance = 0
        q = deque()
        q.append(0)
        vis = [False]*n
        vis[0]=True
        ans = float('inf')
        while q:
            for i in range(len(q)):
                a = q.popleft()
                val = arr[a]
                neigh = d[val]+[a-1,a+1]
                for i in neigh:
                    if i==n-1:
                        return distance+1
                    if i in range(n) and vis[i]==False:
                        q.append(i)
                        vis[i]=True
            distance+=1
            del d[arr[a]]
        

