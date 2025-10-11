class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Sort both arrays
        nums1.sort()
        nums2.sort()

        # Initialize two pointers
        N = len(nums1)
        M = len(nums2)
        p1 = 0
        p2 = 0

        # Create set that stores integers appearing in both arrays
        intersection = set()

        while p1 < N and p2 < M:
            # Add a value to the set if values at both pointers equal
            if nums1[p1] == nums2[p2]:
                intersection.add(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1

        # Convert intersection to an array
        result = []
        for x in intersection:
            result.append(x)

        # Return the result
        return result
