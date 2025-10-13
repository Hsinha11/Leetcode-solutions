from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def backtrack(ind,prev,value,exp):
            if ind == len(num):
                if value == target:
                    res.append(exp)
                return

            for i in range(ind,len(num)):
                if i>ind and num[ind]=='0':
                    break
                cur_str = num[ind:i+1]
                cur_num = int(cur_str)

                if ind == 0:
                     backtrack(i + 1, cur_num, cur_num, cur_str)
                else:
                    backtrack(i+1,cur_num,value+cur_num,exp+'+'+cur_str)
                    backtrack(i+1,-cur_num,value-cur_num,exp+'-'+cur_str)
                    backtrack(i+1,prev*cur_num,value - prev + (prev * cur_num),exp+'*'+cur_str)

        backtrack(0, 0, 0, "")
        return res
