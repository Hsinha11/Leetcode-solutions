### 3704-count-no-zero-pairs-that-sum-to-n

**Approach:** Digit-DP over the digits of n (LSD→MSD) with carry; at each position enumerate digit choices for a and b (0–9) but enforce "no zero in decimal representation" by allowing zeros only after a previously placed non-zero in that number and forbidding any later non-zero after such a zero. Count assignments with final carry 0 and both numbers positive.  
**Complexity:** Time O(100 * L) = O(L) where L = number of digits in n (≤ 16 for n ≤ 1e15), Space O(L).
