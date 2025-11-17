class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        found=False
        c=0
        for i in nums:
            if i==1:
                if found==False:
                    found=True
                else:
                    if c<k:
                        return False
                    else:
                        c=0
            else:
                if found==True:
                    c+=1
                else:
                    continue
        return True