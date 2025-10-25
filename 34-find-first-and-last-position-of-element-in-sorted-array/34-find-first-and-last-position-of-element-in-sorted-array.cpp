// LeetCode 34. Find First and Last Position of Element in Sorted Array
// Approach: Binary search twice to find leftmost and rightmost index of target.
// Time: O(log n), Space: O(1)

#include <vector>
using namespace std;

class Solution {
public:
    int findBound(const vector<int>& nums, int target, bool left) {
        int l = 0, r = nums.size() - 1, bound = -1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) {
                bound = mid;
                if (left) r = mid - 1;
                else l = mid + 1;
            } else if (nums[mid] < target) l = mid + 1;
            else r = mid - 1;
        }
        return bound;
    }

    vector<int> searchRange(vector<int>& nums, int target) {
        return {findBound(nums, target, true), findBound(nums, target, false)};
    }
};
