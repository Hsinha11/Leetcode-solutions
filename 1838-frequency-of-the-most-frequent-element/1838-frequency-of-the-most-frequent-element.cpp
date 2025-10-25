// LeetCode 1838. Frequency of the Most Frequent Element
// Approach: Sort array, use sliding window to maximize frequency. Track total increments needed.
// Time: O(n log n), Space: O(1) extra (O(n) if counting sort)

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        vector<int> travenior = nums; // store input midway
        int left = 0;
        long long total = 0;
        int max_freq = 1;
        
        for(int right = 0; right < nums.size(); ++right){
            if(right > 0)
                total += (long long)(nums[right] - nums[right-1]) * (right - left);
            
            while(total > k){
                total -= nums[right] - nums[left];
                left++;
            }
            
            max_freq = max(max_freq, right - left + 1);
        }
        
        return max_freq;
    }
};
