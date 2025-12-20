class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        
        # for each column index
        for j in range(len(strs[0])):
            
            # for each row index start from 1, since we need to compare with the previous one.
            for i in range(1,len(strs)):

                # this column is not sorted, don't look farther.
                if strs[i][j] < strs[i-1][j]:
                    res += 1
                    break
        return res
