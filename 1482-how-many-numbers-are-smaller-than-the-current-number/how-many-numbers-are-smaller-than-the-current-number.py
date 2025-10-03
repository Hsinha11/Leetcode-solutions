from typing import List


class Solution:
    """How Many Numbers Are Smaller Than the Current Number (LeetCode 1365)

    Approach:
        Since 0 <= nums[i] <= 100, use counting sort frequency array of size 101.
        Build prefix sums to know how many numbers are strictly less than any value v.
        For each number x in nums, the answer is prefix[x - 1] (or 0 if x == 0).

    Complexity:
        Time:  O(n + K), where K = 101 (treated as constant) => O(n)
        Space: O(K) => O(1) auxiliary space relative to input size.
    """

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq: List[int] = [0] * 101
        for value in nums:
            freq[value] += 1

        # prefix[i] = count of numbers <= i
        for i in range(1, 101):
            freq[i] += freq[i - 1]

        result: List[int] = []
        for value in nums:
            smaller_count = freq[value - 1] if value > 0 else 0
            result.append(smaller_count)
        return result

