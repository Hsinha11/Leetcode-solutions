#include <vector>
#include <unordered_map>

using namespace std;
class Solution {
public:
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        // Key insight: exactly(K) = atMost(K) - atMost(K-1)
        return atMostKDistinct(nums, k) - atMostKDistinct(nums, k - 1);
    }
    
private:
    // Helper function: count subarrays with at most K distinct integers
    int atMostKDistinct(vector<int>& nums, int k) {
        if (k == 0) return 0;
        
        unordered_map<int, int> freq;
        int left = 0, result = 0;
        
        for (int right = 0; right < nums.size(); right++) {
            // Expand window: add nums[right]
            freq[nums[right]]++;
            
            // Shrink window: while we have more than k distinct integers
            while (freq.size() > k) {
                freq[nums[left]]--;
                if (freq[nums[left]] == 0) {
                    freq.erase(nums[left]);
                }
                left++;
            }
            
            // Count all subarrays ending at 'right' with at most k distinct
            // All subarrays from [left, right], [left+1, right], ..., [right, right]
            result += right - left + 1;
        }
        
        return result;
    }
};