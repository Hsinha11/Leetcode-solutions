# 🏙️ Maximize the Minimum Powered City (LeetCode 2528)

**Difficulty:** Hard  
**Languages:** Python, C++  
**Topic Tags:** Binary Search, Greedy, Prefix Sum, Difference Array, Sliding Window  

---

## 🧩 Problem Statement

Alice is managing a line of cities. Each city can have multiple **power stations**, and each station provides power to all cities within a fixed **range** `r`.  
We are given:
- An array `stations[i]`, representing the number of power stations in the `i-th` city.
- Two integers `r` and `k` where:
  - Each existing power station powers all cities within distance `r`.
  - We can build **k new power stations** anywhere.

The **power** of a city = total number of stations that supply it (from nearby cities within distance `r`).

We need to **maximize the minimum power** across all cities after placing up to `k` new stations optimally.

---

## 🧠 Example

### Example 1
**Input**
stations = [1, 2, 4, 5, 0]
r = 1
k = 2

**Output**
5

**Explanation**
- Place both new stations at city `1`.
- New configuration: `[1, 4, 4, 5, 0]`
- City powers become:
  - City 0 → 1 + 4 = **5**
  - City 1 → 1 + 4 + 4 = **9**
  - City 2 → 4 + 4 + 5 = **13**
  - City 3 → 5 + 4 = **9**
  - City 4 → 5 + 0 = **5**
- The minimum power = **5**.

No better configuration exists.

---

## 🚀 Solution Approach

### Algorithm
1. **Compute Initial Power**: Use prefix sums to calculate each city's initial power in O(n)
2. **Binary Search**: Search for the maximum feasible minimum power value
3. **Greedy Validation**: For each candidate value, use difference array technique to simulate adding stations optimally
4. **Range Updates**: When adding stations at position i, they affect cities from i to i+2r

### Key Techniques
- **Prefix Sum**: O(1) range sum queries for initial power calculation
- **Difference Array**: Efficient range updates for simulating station additions
- **Binary Search**: Find maximum feasible minimum power value
- **Greedy Strategy**: Always add stations to the leftmost city that needs them

### Complexity Analysis
- **Time Complexity**: O(n log(max_power + k))
- **Space Complexity**: O(n)

## 📁 Solution Files
- `2528-Maximize-the-Minimum-Powered-City.py` - Python implementation
- `2528-Maximize-the-Minimum-Powered-City.cpp` - C++ implementation with test cases