import collections

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        # Result list to store the maximum of each sliding window
        output = []
        
        # Deque to store indices of useful elements in the current window
        # The deque will always be in decreasing order of their values in nums
        q = collections.deque()
        
        # Left (l) and right (r) pointers for the sliding window
        l = r = 0

        # Iterate until the right pointer reaches the end of the array
        while r < len(nums):
            # Remove elements smaller than the current element nums[r]
            # from the back of the deque, since they can’t be maximum anymore
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # Add the current index to the deque
            q.append(r)

            # Remove indices from the front of the deque that are out of the current window
            if l > q[0]:
                q.popleft()

            # If the window has reached size k, start adding maximums to output
            if (r + 1) >= k:
                # The element at the front of the deque is the maximum for this window
                output.append(nums[q[0]])
                # Move the left boundary to slide the window forward
                l += 1

            # Move the right boundary to expand the window
            r += 1

        # Return the list of maximums for each window
        return output


# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Example from LeetCode
    nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
    k1 = 3
    result1 = solution.maxSlidingWindow(nums1, k1)
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output: {result1}")
    print(f"Expected: [3, 3, 5, 5, 6, 7]")
    print()
    
    # Test case 2: Single element
    nums2 = [1]
    k2 = 1
    result2 = solution.maxSlidingWindow(nums2, k2)
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output: {result2}")
    print(f"Expected: [1]")
    print()
    
    # Test case 3: All same elements
    nums3 = [1, 1, 1, 1]
    k3 = 2
    result3 = solution.maxSlidingWindow(nums3, k3)
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Output: {result3}")
    print(f"Expected: [1, 1, 1]")
