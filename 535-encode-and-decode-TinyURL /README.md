<h2><a href="https://leetcode.com/problems/encode-and-decode-tinyurl">535. Encode and Decode TinyURL</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />
<hr>

### 🧩 Problem Statement
Design a class (`Codec`) to implement a URL shortening service.
The class must provide two methods:
1.  `String encode(String longUrl)`: Returns a shortened URL (e.g., `http://tinyurl.com/4e9iAk`) for the given `longUrl`.
2.  `String decode(String shortUrl)`: Returns the original `longUrl` for the given `shortUrl`.

The algorithm must ensure that any encoded URL can be accurately decoded back to its original value.

---

### 💡 Approach
1️⃣ Use two **HashMaps** for bi-directional mapping: one to map the short key to the long URL (`mapShortToLong`) and one for the reverse (`mapLongToShort`).

2️⃣ **Encoding**:
* Check if the `longUrl` is already present in the map. If so, return the existing short URL, ensuring **idempotency**.
* If new, generate a **unique 6-character alphanumeric key** (e.g., "4e9iAk").
* Store the key-value pairs in both HashMaps.

3️⃣ **Decoding**:
* Extract the short key from the `shortUrl` by removing the base prefix (`http://tinyurl.com/`).
* Use the key to look up and return the original `longUrl`.

---

### 🧠 Intuition
In a real-world URL shortener, the mapping must be persistent. In this implementation, the **HashMaps** serve as the highly efficient in-memory storage layer.

By using a **fixed-length random key** (e.g., 6 characters from 62 possible alphanumeric characters), we create an extremely large address space ($62^6 \approx 56.8$ billion unique keys). This massive key space minimizes collisions and allows both encoding and decoding to perform in near-instantaneous **constant time** $O(1)$.

---

### ⏱️ Complexity Analysis
* **Time Complexity:** $O(1)$ — Hash map operations (lookup and insertion) take constant time on average.
* **Space Complexity:** $O(N)$ — where $N$ is the number of URLs encoded, as all mappings must be stored.

---

### 📘 Example
```
Input: url = "https://leetcode.com/problems/design-tinyurl"
Output (Encoded Example): "http://tinyurl.com/A7fFz0"
Output (Decoded): "https://leetcode.com/problems/design-tinyurl"
```