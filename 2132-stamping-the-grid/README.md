### 2132-stamping-the-grid

**Approach:** Use 2D prefix sums to detect all top-left positions where a stamp can be placed (submatrix sum == 0). Use a 2D difference array to apply all such stamps efficiently, rebuild coverage via prefix sums, and verify every empty cell is covered.

**Complexity:** Time O(m * n), Space O(m * n)
