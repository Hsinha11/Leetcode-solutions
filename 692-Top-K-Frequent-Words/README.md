# 🔤 Top K Frequent Words

## 📘 Problem Statement
Given an array of strings `words` and an integer `k`, return the `k` most frequent strings.

Return the answer **sorted by the frequency from highest to lowest**. Sort the words with the same frequency by their **lexicographical order**.

---

## 💡 Approach — Using Heap (Priority Queue)

**Key Strategy**: Use `Counter` to count frequencies, then use a heap with negative frequencies to simulate max-heap behavior.

### Algorithm Steps:
1. **Count frequencies** using `Counter(words)`
2. **Create heap** with `(-freq, word)` tuples (negative freq converts min-heap to max-heap)
3. **Heapify** the list to create proper heap structure
4. **Extract top K** elements using `heappop()`

---

## 🧾 Code Implementation
```python
import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):
        # Count word frequencies
        count = Counter(words)
        
        # Create heap with (-freq, word) tuples
        # Negative frequency ensures most frequent words come first
        # Tuple comparison handles lexicographical tie-breaking
        heap = [(-freq, word) for word, freq in count.items()]
        
        # Convert to heap and extract top K
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
```

---

## ⏱️ Time & Space Complexity

### Time Complexity: **O(n + k log n)**
- **Frequency Counting**: O(n) - iterate through all words
- **Heap Creation**: O(n) - create tuples for unique words  
- **Heapify**: O(n) - convert list to heap structure
- **Extract Top K**: O(k log n) - pop k elements from heap

### Space Complexity: **O(n)**
- **Counter**: O(n) - stores frequency of each unique word
- **Heap**: O(n) - stores all unique words
- **Result**: O(k) - stores top k words

---

## 🔍 Why This Works

### **Negative Frequencies Strategy:**
```python
# Python's heapq is a MIN-HEAP, but we want MAX-HEAP behavior
heap = [(-3, "love"), (-2, "i")]   # Negative frequencies
# Min-heap puts (-3, "love") at top ✅ (most frequent)
```

### **Tuple Comparison for Tie-Breaking:**
```python
# When frequencies are equal, Python compares words lexicographically
(-2, "apple") vs (-2, "banana") → "apple" comes first ✅
```

---

## ✅ Test Cases
```python
# Test 1: words = ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]

# Test 2: words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4  
# Output: ["the", "is", "sunny", "day"]
```

---

## 🏆 Key Points
- **Optimal when k << n** (better than O(n log n) sorting approach)
- **Clean implementation** using Python's built-in data structures
- **Elegant tie-breaking** through tuple comparison
- **Heap + Counter** is a powerful combination for top-K problems