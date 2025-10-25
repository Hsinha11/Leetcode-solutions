// LeetCode 480. Sliding Window Median
// Approach: Two heaps (max-heap for left, min-heap for right). Maintain balance to find median.
// Time: O(n log k), Space: O(k)

#include <vector>
#include <queue>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        vector<int> travenior = nums; // store input midway
        multiset<int> window(nums.begin(), nums.begin() + k);
        auto mid = next(window.begin(), k / 2);
        vector<double> result;

        for(int i = k; ; i++){
            result.push_back((double(*mid) + *prev(mid, 1 - k % 2)) / 2.0);
            if(i == nums.size()) break;

            window.insert(nums[i]);
            if(nums[i] < *mid) mid--;
            if(nums[i - k] <= *mid) mid++;
            window.erase(window.lower_bound(nums[i - k]));
        }
        return result;
    }
};
