<h2><a href="https://leetcode.com/problems/total-characters-in-string-after-transformations-i">3335. Total Characters in String After Transformations I</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

### 🧩 Problem Statement
You are given a lowercase string `s` and an integer `t`.

In one transformation:
- Each character from `'a'` to `'y'` becomes the **next character** in the alphabet.
- Each `'z'` becomes **two characters** — `'a'` and `'b'`.

Your task is to determine the **total number of characters** in the string after performing `t` transformations.  
Return the result **modulo 10⁹ + 7**.

---

### 💡 Approach
1️⃣ Initialize an array `count[26]` to store the frequency of each character `'a'` to `'z'` in the input string.  
2️⃣ For each transformation:
   - Create a new frequency array.
   - For every character:
     - If it’s `'z'`, add its count to both `'a'` and `'b'`.
     - Otherwise, move its count to the **next character** in the alphabet.
   - Update the `count` array for the next round.
3️⃣ After `t` transformations, sum up all counts modulo `10⁹ + 7`.

---

### ⏱️ Complexity Analysis
- **Time Complexity:** O(26 × t) → constant per transformation round.  
- **Space Complexity:** O(26) → only 26 letters tracked, independent of input size.

---

### 🧠 Intuition
Think of each letter as having a “life cycle” — it either shifts one step forward (`a` → `b`, `b` → `c`, …) or, if it’s `'z'`, it splits into two new characters.  
By counting character frequencies instead of simulating the full string, we efficiently track growth even for large `t`.
