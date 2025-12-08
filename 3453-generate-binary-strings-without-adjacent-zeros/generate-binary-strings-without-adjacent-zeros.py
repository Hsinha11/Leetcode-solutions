class Solution:
    def validStrings(self, n: int) -> List[str]:
        
        ans = []
        def dfs(i, res, last):
            if i==n:
                ans.append(res)
                return
            dfs(i+1,res+'1','1')
            if last!='0':
                dfs(i+1,res+'0','0')
        dfs(0,'',None)
        return ans
            