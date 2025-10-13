# Problem: Length of Last Word

## Original Problem Statement
Given a string `s` consisting of words and spaces, return **the length of the last word** in the string.
A **word** is a maximal substring consisting of non-space characters only.

### Example
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

---

## Approach 
1. **Skip trailing spaces:**  
   - Start from the end of the string and move left until you find a non-space character.
   - This ensures trailing spaces don’t affect the count.

2. **Count the last word’s length:**  
   - From the first non-space character (from the end), count characters until you reach another space or the start of the string.
   - Keep a counter to record the length.

3. **Return the counter value.**

This approach efficiently avoids using string split or extra arrays.

---

## Example
**Input:**  
- s = "   Fly me   to   the moon  "

**Steps:**  
- Ignore trailing spaces → last non-space char is `'n'`.  
- Count backwards until a space → `'moon'` has 4 letters.  

**Output:**  
- 4

---

## Time and Space Complexity

| Complexity | Description |
|-------------|--------------|
| **Time**    | `O(n)` — We traverse the string once from the end. |
| **Space**   | `O(1)` — Only a few variables are used; no extra data structures. |

---

## Example Test Cases

| Input | Output | Explanation |
|--------|---------|-------------|
| `"Hello World"` | `5` | Last word = “World” |
| `"a"` | `1` | Single letter word |
| `"   fly me   to   the moon  "` | `4` | Last word = “moon” |
| `"luffy is still joyboy"` | `6` | Last word = “joyboy” |

---


