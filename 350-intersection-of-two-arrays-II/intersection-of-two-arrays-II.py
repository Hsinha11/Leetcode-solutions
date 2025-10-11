from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Step 1: Sort both arrays to make comparison easier
        nums1.sort()
        nums2.sort()
        
        ans = []          # Result list to store intersection elements
        i = j = 0         # Two pointers for nums1 and nums2

        # Step 2: Traverse both arrays using two pointers
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                # Move i forward if nums1 element is smaller
                i += 1
            elif nums1[i] > nums2[j]:
                # Move j forward if nums2 element is smaller
                j += 1
            else:
                # Elements match — add to result and move both pointers
                ans.append(nums1[i])
                i += 1
                j += 1

        # Step 3: Return the intersection list
        return ans
    
    
