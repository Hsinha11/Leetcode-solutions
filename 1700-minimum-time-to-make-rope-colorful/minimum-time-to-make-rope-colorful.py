class Solution:
    def minCost(self, colors: str, n: List[int]) -> int:
        stack= []
        ans = 0
        for i in range(len(colors)):
            if stack and colors[stack[-1]]==colors[i]:
                if n[stack[-1]]>n[i]:
                    ans+=n[i]
                    continue
                else:
                    ans+=n[stack.pop()]
            stack.append(i)
        return ans