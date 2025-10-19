# 🧾 Text Justification

## 📘 Problem Statement
Given an array of words and a maximum width `maxWidth`, format the text such that each line has **exactly maxWidth characters** and is **fully (left and right) justified**.

- Words should be packed greedily — i.e., as many words as fit in a line.
- Extra spaces should be distributed as evenly as possible between words.
- If the number of spaces does not divide evenly, the **leftmost gaps get more spaces**.
- The last line should be **left-justified**, and no extra space should be inserted between words.

🔗 **Problem Link:** [LeetCode 68 — Text Justification](https://leetcode.com/problems/text-justification/)

---

## 💡 Example
**Input:**
words = ["This", "is", "an", "example", "of", "text"]
maxWidth = 16

**Output:**
["This is an",
"example of text"]


---

## 🧭 Approach (Greedy Line Formation)

1. **Greedy Line Selection:**  
   Start from the first word, keep adding words to the current line until adding another would exceed `maxWidth`.

2. **Compute Space Distribution:**  
   - If it's the **last line** or there is **only one word**, left justify (add remaining spaces at the end).  
   - Otherwise, distribute spaces evenly:
     - `spaces = (maxWidth - totalChars) / gaps`
     - `extra = (maxWidth - totalChars) % gaps`  
       → Extra spaces go to the leftmost gaps.

3. **Build the Line:**  
   Concatenate words with the calculated number of spaces.

4. **Repeat** for all lines.

---

## ⏱️ Time Complexity
- **O(N)** where N = total number of words.  
  Each word is processed once to determine its line placement.

## 💾 Space Complexity
- **O(1)** (excluding the output list).  
  Only a few variables are used for tracking indices and spacing.

---

## 🖥️ Supported Implementations
✅ **C++**  
✅ **Java**  
✅ **Python**  
All versions include **runtime user input** for easy testing and demonstration.
