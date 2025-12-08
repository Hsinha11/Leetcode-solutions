class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        piv = []
        for i in nums:
            if i<pivot:
                left.append(i)
            elif i>pivot:
                right.append(i)
            else:
                piv.append(i)
        # right.sort( )
        left.extend(piv)
        left.extend(right)
        return left
