// 3349. Adjacent Increasing Subarrays Detection I
// Easy
// Approach: Check each subarray of length k and its adjacent subarray. Return true if both strictly increasing.
// Time Complexity: O(n), Space Complexity: O(1)

#include <vector>
using namespace std;

class Solution {
public:
    bool checkAdjacentIncreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        auto is_increasing = [&](int start) {
            for (int i = start; i < start + k - 1; i++) {
                if (nums[i] >= nums[i + 1]) return false;
            }
            return true;
        };
        
        for (int i = 0; i <= n - 2 * k; i++) {
            if (is_increasing(i) && is_increasing(i + k)) return true;
        }
        return false;
    }
};
