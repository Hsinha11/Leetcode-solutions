import heapq                # Import heapq module for heap (priority queue) operations
from collections import Counter  # Import Counter to count word frequencies

class Solution(object):
    def topKFrequent(self, words, k):
        # Step 1: Count the frequency of each word in the input list 'words'
        count = Counter(words)
        
        # Step 2: Create a heap (min-heap in Python)
        # We use (-freq, word) so that the most frequent words come first.
        # Negative frequency ensures that higher frequency has higher priority
        # If two words have the same frequency, Python will compare them lexicographically (alphabetically)
        heap = [(-freq, word) for word, freq in count.items()]

        # Step 3: Convert the list into a heap (in-place)
        heapq.heapify(heap)
        # Now the heap is organized so that the smallest (most negative) freq is at the top,
        # which corresponds to the most frequent word.

        # Step 4: Pop the top 'k' elements from the heap (most frequent words)
        # Each pop removes the most frequent word (or alphabetically smallest in case of tie)
        return [heapq.heappop(heap)[1] for _ in range(k)]
        # We only take the word (index 1 of tuple), ignoring the frequency


# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Example from LeetCode
    words1 = ["i", "love", "leetcode", "i", "love", "coding"]
    k1 = 2
    result1 = solution.topKFrequent(words1, k1)
    print(f"Input: words = {words1}, k = {k1}")
    print(f"Output: {result1}")
    print(f"Expected: ['i', 'love']")
    print()
    
    # Test case 2: Different frequencies
    words2 = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k2 = 4
    result2 = solution.topKFrequent(words2, k2)
    print(f"Input: words = {words2}, k = {k2}")
    print(f"Output: {result2}")
    print(f"Expected: ['the', 'is', 'sunny', 'day']")
    print()
    
    # Test case 3: Single word
    words3 = ["word"]
    k3 = 1
    result3 = solution.topKFrequent(words3, k3)
    print(f"Input: words = {words3}, k = {k3}")
    print(f"Output: {result3}")
    print(f"Expected: ['word']")
