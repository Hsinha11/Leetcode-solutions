<h2><a href="https://leetcode.com/problems/powx-n">50. Pow(x, n)</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

### 🧩 Problem Statement
Implement the function `pow(x, n)` that calculates **x raised to the power n** (`xⁿ`).

You must not use built-in functions like `pow()` or the exponentiation operator `**`.

---

### 💡 Approach
1️⃣ Use **fast exponentiation (binary exponentiation)** to efficiently compute powers.  
2️⃣ The idea:
   - Split the exponent `n` into halves recursively.
   - Compute `x^(n/2)` once, square it, and multiply by `x` again if `n` is odd.  
3️⃣ Handle negative exponents by computing the reciprocal:  
   `xⁿ = 1 / x⁻ⁿ` when `n < 0`.

---

### 🧠 Intuition
Instead of multiplying `x` by itself `n` times (which is slow),  
we reduce the number of multiplications by half at each recursive step.  
This makes the algorithm **logarithmic** instead of linear in time.

---

### ⏱️ Complexity Analysis
- **Time Complexity:** O(log n) — due to recursive halving of the exponent.  
- **Space Complexity:** O(log n) — recursion stack depth proportional to `log n`.

---

### 📘 Example
Input: x = 2.00000, n = 10
Output: 1024.00000

Input: x = 2.00000, n = -2
Output: 0.25000