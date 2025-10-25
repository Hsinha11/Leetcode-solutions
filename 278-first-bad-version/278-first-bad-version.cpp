// LeetCode 278. First Bad Version
// Approach: Binary Search to minimize API calls.
// Time: O(log n), Space: O(1)

bool isBadVersion(int version); // Provided by the problem

class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1, right = n;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid))
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }
};
