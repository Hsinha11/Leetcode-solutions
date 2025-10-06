# 4. Median of Two Sorted Arrays

> **Difficulty**: Hard  
> **Topics**: Array, Binary Search, Divide and Conquer  
> **Time Complexity**: O(log(min(m,n)))  
> **Space Complexity**: O(1)

## 📋 Problem Statement

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median of the two sorted arrays**.

The overall run time complexity should be **O(log (m+n))**.

### Examples

#### Example 1:
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

#### Example 2:
```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

### Constraints:
- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

---

## 🧠 Algorithm Explanation

### Core Concept: Binary Search on Partitions

The key insight is that we don't need to merge the arrays. Instead, we can use **binary search** to find the correct partition point where:

1. **Left partition** contains the smaller half of all elements
2. **Right partition** contains the larger half of all elements
3. **All elements in left ≤ all elements in right**

### Visual Representation

```
nums1: [1, 3] (cut1 = 1)
       [1 | 3]
       
nums2: [2] (cut2 = 1) 
       [2 | ]
       
Combined partitions:
Left:  [1, 2]  (size = 2)
Right: [3]     (size = 1)
Median = max(1, 2) = 2
```

### Algorithm Steps

1. **Ensure smaller array first**: Make `nums1` the smaller array for efficiency
2. **Binary search on cuts**: Search for the right partition in `nums1`
3. **Calculate corresponding cut**: Determine cut position in `nums2`
4. **Check partition validity**: Verify left elements ≤ right elements
5. **Calculate median**: Based on total length (odd/even)

---

## 💻 Implementation

```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // Ensure nums1 is the smaller array for binary search efficiency
        if (nums1.size() > nums2.size()) return findMedianSortedArrays(nums2, nums1);
        
        int n1 = nums1.size(), n2 = nums2.size();
        int low = 0, high = n1;

        while (low <= high) {
            int cut1 = (low + high) / 2;
            int cut2 = (n1 + n2 + 1) / 2 - cut1;

            int left1  = (cut1 == 0) ? INT_MIN : nums1[cut1 - 1];
            int left2  = (cut2 == 0) ? INT_MIN : nums2[cut2 - 1];
            int right1 = (cut1 == n1) ? INT_MAX : nums1[cut1];
            int right2 = (cut2 == n2) ? INT_MAX : nums2[cut2];

            if (left1 <= right2 && left2 <= right1) {
                if ((n1 + n2) % 2 == 0)
                    return (max(left1, left2) + min(right1, right2)) / 2.0;
                else
                    return max(left1, left2);
            } 
            else if (left1 > right2)
                high = cut1 - 1;
            else
                low = cut1 + 1;
        }
        return 0.0; // Should never reach here
    }
};

int main() {
    Solution sol;
    int m, n;
    cout << "Enter size of nums1: ";
    cin >> m;
    vector<int> nums1(m);
    cout << "Enter elements of nums1 (sorted): ";
    for (int i = 0; i < m; i++) cin >> nums1[i];

    cout << "Enter size of nums2: ";
    cin >> n;
    vector<int> nums2(n);
    cout << "Enter elements of nums2 (sorted): ";
    for (int i = 0; i < n; i++) cin >> nums2[i];

    double ans = sol.findMedianSortedArrays(nums1, nums2);
    cout << "Median: " << fixed << setprecision(5) << ans << endl;
    return 0;
}
```

---

## 🔍 Step-by-Step Walkthrough

### Example: nums1 = [1,3], nums2 = [2]

| Step | cut1 | cut2 | left1 | left2 | right1 | right2 | Valid? | Action |
|------|------|------|-------|-------|--------|--------|--------|--------|
| 1 | 1 | 1 | 1 | 2 | 3 | INT_MAX | ✅ | Found! |

**Result**: Since total length is odd (3), median = max(1, 2) = **2**

### Example: nums1 = [1,2], nums2 = [3,4]

| Step | cut1 | cut2 | left1 | left2 | right1 | right2 | Valid? | Action |
|------|------|------|-------|-------|--------|--------|--------|--------|
| 1 | 1 | 1 | 1 | 3 | 2 | 4 | ❌ | left2 > right1 |
| 2 | 2 | 0 | 2 | INT_MIN | INT_MAX | 3 | ✅ | Found! |

**Result**: Since total length is even (4), median = (max(2, INT_MIN) + min(INT_MAX, 3)) / 2 = **(2 + 3) / 2 = 2.5**

---

## 🎯 Key Insights

### 1. **Why Binary Search Works**
- We're searching for the correct partition, not individual elements
- Each comparison eliminates half the search space
- Time complexity: O(log(min(m,n)))

### 2. **Partition Logic**
```cpp
cut2 = (n1 + n2 + 1) / 2 - cut1
```
- Ensures left partition has ⌈(total)/2⌉ elements
- The `+1` handles both odd and even cases elegantly

### 3. **Boundary Conditions**
- `INT_MIN` for empty left partitions
- `INT_MAX` for empty right partitions
- Handles edge cases gracefully

### 4. **Median Calculation**
```cpp
// Even total length
median = (max(left1, left2) + min(right1, right2)) / 2.0

// Odd total length  
median = max(left1, left2)
```

---

## 📊 Complexity Analysis

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| **Binary Search** | **O(log(min(m,n)))** | **O(1)** | Optimal solution |
| Merge Arrays | O(m + n) | O(m + n) | Simple but not optimal |
| Sort Combined | O((m+n)log(m+n)) | O(m + n) | Naive approach |

---

## 🧪 Test Cases

### Basic Cases
```cpp
// Test 1: Simple case
nums1 = [1,3], nums2 = [2]
Expected: 2.0

// Test 2: Even length
nums1 = [1,2], nums2 = [3,4]  
Expected: 2.5
```

### Edge Cases
```cpp
// Test 3: Empty array
nums1 = [], nums2 = [1]
Expected: 1.0

// Test 4: Single elements
nums1 = [1], nums2 = [2]
Expected: 1.5

// Test 5: Different sizes
nums1 = [1,3], nums2 = [2,4,5,6]
Expected: 3.5
```

### Advanced Cases  
```cpp
// Test 6: Negative numbers
nums1 = [-5,-3,-1], nums2 = [1,3]
Expected: -1.0

// Test 7: Large difference
nums1 = [1,2], nums2 = [1000000]
Expected: 2.0
```

---

## 🚀 How to Run

### Compilation
```bash
g++ -o solution median_solution.cpp
```

### Execution
```bash
./solution
```

### Sample Input/Output
```
Enter size of nums1: 2
Enter elements of nums1 (sorted): 1 3
Enter size of nums2: 1  
Enter elements of nums2 (sorted): 2
Median: 2.00000
```

---

## 🔧 Alternative Approaches

### 1. **Merge Two Arrays** (O(m+n))
```cpp
double findMedianMerge(vector<int>& nums1, vector<int>& nums2) {
    vector<int> merged;
    int i = 0, j = 0;
    
    while (i < nums1.size() && j < nums2.size()) {
        if (nums1[i] <= nums2[j]) merged.push_back(nums1[i++]);
        else merged.push_back(nums2[j++]);
    }
    
    while (i < nums1.size()) merged.push_back(nums1[i++]);
    while (j < nums2.size()) merged.push_back(nums2[j++]);
    
    int n = merged.size();
    return n % 2 ? merged[n/2] : (merged[n/2-1] + merged[n/2]) / 2.0;
}
```

### 2. **Two Pointers** (O(m+n), Space O(1))
```cpp
double findMedianTwoPointers(vector<int>& nums1, vector<int>& nums2) {
    int total = nums1.size() + nums2.size();
    int target = total / 2;
    int i = 0, j = 0, count = 0;
    int prev = 0, curr = 0;
    
    while (count <= target) {
        prev = curr;
        if (i < nums1.size() && (j >= nums2.size() || nums1[i] <= nums2[j])) {
            curr = nums1[i++];
        } else {
            curr = nums2[j++];
        }
        count++;
    }
    
    return total % 2 ? curr : (prev + curr) / 2.0;
}
```

---

## 📚 Related Problems

- **[Kth Smallest Element in Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)**
- **[Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance/)**
- **[Median of Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)**

---

## 💡 Tips for Interview

### Key Points to Mention:
1. **Time complexity requirement**: O(log(m+n)) suggests binary search
2. **Partition strategy**: Focus on partitioning, not merging
3. **Edge cases**: Handle empty arrays and boundary conditions
4. **Integer overflow**: Use appropriate data types for calculations

### Common Mistakes:
- Forgetting to ensure `nums1` is the smaller array
- Incorrect partition size calculation
- Not handling boundary conditions (empty partitions)
- Using wrong median formula for odd/even cases

---

## 🏆 Optimization Notes

1. **Always make `nums1` smaller**: Reduces binary search space
2. **Use `(n1 + n2 + 1) / 2`**: Elegant way to handle odd/even cases
3. **INT_MIN/INT_MAX for boundaries**: Simplifies edge case handling
4. **Early termination**: Algorithm guarantees finding solution

---

## 📖 Additional Resources

- **LeetCode Problem**: [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
- **Time Complexity**: O(log(min(m,n)))
- **Space Complexity**: O(1)
- **Difficulty**: Hard
- **Category**: Binary Search, Array

---

*This solution demonstrates advanced binary search techniques and optimal space-time complexity for a classic algorithmic problem.*
