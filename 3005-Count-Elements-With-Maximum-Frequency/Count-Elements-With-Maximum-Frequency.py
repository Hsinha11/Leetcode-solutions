from collections import Counter
from typing import List
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_freq = max(counts.values())
        return sum(freq for freq in counts.values() if freq == max_freq)
        