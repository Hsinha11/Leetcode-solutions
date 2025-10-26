// LeetCode 2310. Sum of Numbers With Units Digit K
// Medium
// Approach: Try set sizes from 1 to 10; check if sum - k*size is divisible by 10.
// Time: O(1), Space: O(1)

class Solution {
public:
    int minimumNumbers(int num, int k) {
        if(num == 0) return 0;
        for(int size = 1; size <= 10; ++size) {
            if(k * size <= num && (num - k * size) % 10 == 0)
                return size;
        }
        return -1;
    }
};
