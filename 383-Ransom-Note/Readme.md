<h2><a href="https://leetcode.com/problems/ransom-note">383. Ransom Note</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Easy-brightgreen" alt="Difficulty: Easy" />
<hr>

### 🧩 Problem Statement
Given two strings `ransomNote` and `magazine`, determine if `ransomNote` can be constructed from the letters of `magazine`.  
Each letter in `magazine` can only be used once in `ransomNote`.

---

### 💡 Approach
1️⃣ Iterate through each character in `ransomNote`.  
2️⃣ For each character, check if it exists in `magazine`.  
3️⃣ If it exists, remove one occurrence of that character from `magazine`.  
4️⃣ If any character is not found, return `False`.  
5️⃣ If the entire `ransomNote` can be formed, return `True`.

---

### ⏱️ Complexity Analysis
- **Time Complexity:** O(n × m) – where `n` is the length of `ransomNote` and `m` is the length of `magazine` (due to string replacement).  
- **Space Complexity:** O(1) – only uses constant extra space.

---

### 🧠 Intuition
You can think of `magazine` as a bag of letters.  
For every letter in `ransomNote`, try to pick it from the bag.  
If the bag runs out of any letter, construction fails.
