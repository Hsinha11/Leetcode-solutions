
# 3. Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s`, find the length of the **longest substring** without repeating characters.

---

### Example 1:
**Input:**  
```

s = "abcabcbb"

```
**Output:**  
```

3

```
**Explanation:** The answer is `"abc"`, with the length of 3.

---

### Example 2:
**Input:**  
```

s = "bbbbb"

```
**Output:**  
```

1

```
**Explanation:** The answer is `"b"`, with the length of 1.

---

### Example 3:
**Input:**  
```

s = "pwwkew"

```
**Output:**  
```

3

````
**Explanation:** The answer is `"wke"`, with the length of 3.  
Note: `"pwke"` is a subsequence, not a substring.

---

## Constraints:
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

---

## Edge Cases:
1. `s = ""` → Output should be `0` (empty string).  
2. `s = "a"` → Output should be `1` (single character).  
3. `s = "au"` → Output should be `2` (two unique characters).  
4. `s = "abba"` → Output should be `2` (substring `"ab"` or `"ba"`).

---

## Approach
We use the **Sliding Window Technique** with a HashMap (or HashSet):  

1. Use two pointers (`left`, `right`) to represent the current window.  
2. Expand `right` and add characters into a set.  
3. If a duplicate is found, shrink the window by moving `left` until the substring is valid.  
4. Track the maximum window size.  

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(min(n, charset_size))`

---

## Implementation

### C++ Code
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> set;
        int left = 0, maxLength = 0;

        for (int right = 0; right < s.size(); right++) {
            while (set.find(s[right]) != set.end()) {
                set.erase(s[left]);
                left++;
            }
            set.insert(s[right]);
            maxLength = max(maxLength, right - left + 1);
        }
        return maxLength;
    }
};
````

---

### Java Code

```java
import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<>();
        int left = 0, maxLength = 0;

        for (int right = 0; right < s.length(); right++) {
            while (set.contains(s.charAt(right))) {
                set.remove(s.charAt(left));
                left++;
            }
            set.add(s.charAt(right));
            maxLength = Math.max(maxLength, right - left + 1);
        }
        return maxLength;
    }
}
```

---

### Python Code

```python
from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen_index_by_char: Dict[str, int] = {}
        window_start_index: int = 0
        max_window_length: int = 0

        for window_end_index, current_char in enumerate(s):
            if current_char in last_seen_index_by_char:
                previous_index: int = last_seen_index_by_char[current_char]
                if previous_index >= window_start_index:
                    window_start_index = previous_index + 1

            last_seen_index_by_char[current_char] = window_end_index
            current_window_length: int = window_end_index - window_start_index + 1
            if current_window_length > max_window_length:
                max_window_length = current_window_length

        return max_window_length


if __name__ == "__main__":
    solver = Solution()
    print(solver.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(solver.lengthOfLongestSubstring("bbbbb"))     # 1
    print(solver.lengthOfLongestSubstring("pwwkew"))    # 3
```
