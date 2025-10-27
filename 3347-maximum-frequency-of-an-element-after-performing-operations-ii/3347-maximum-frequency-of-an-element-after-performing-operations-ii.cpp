// 3347-maximum-frequency-of-an-element-after-performing-operations-ii.cpp
// LeetCode 3347. Maximum Frequency of an Element After Performing Operations II
//
// Approach:
//   Sort the array. For each distinct value v, compute the number of elements inside
//   [v-k, v+k] using binary searches. Let cnt be total in that interval and eq be
//   number already equal to v. We can increase frequency to eq + min(numOperations, cnt - eq).
//   Track maximum over v.
// Time: O(n log n) (sorting + binary searches). Space: O(1) extra (besides sorted array).

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxFrequency(vector<long long>& nums, long long k, int numOperations) {
        int n = nums.size();
        if (n == 0) return 0;
        sort(nums.begin(), nums.end());
        int ans = 1;

        for (int i = 0; i < n; ) {
            long long v = nums[i];
            long long left = v - k;
            long long right = v + k;
            auto lo_it = lower_bound(nums.begin(), nums.end(), left);
            auto hi_it = upper_bound(nums.begin(), nums.end(), right);
            int lo = (int)(lo_it - nums.begin());
            int hi = (int)(hi_it - nums.begin()); // exclusive
            int cnt = hi - lo;

            auto eq_hi_it = upper_bound(nums.begin() + i, nums.end(), v);
            int eq_hi = (int)(eq_hi_it - nums.begin());
            int eq = eq_hi - i;

            int possible = eq + min((int)numOperations, cnt - eq);
            ans = max(ans, possible);

            i = eq_hi; // skip duplicates
        }

        return min(ans, n);
    }
};

// local test
int main() {
    Solution s;
    vector<long long> a1 = {1,4,5};
    cout << s.maxFrequency(a1, 1, 2) << "\n"; // 2

    vector<long long> a2 = {5,11,20,20};
    cout << s.maxFrequency(a2, 5, 1) << "\n"; // 2
    return 0;
}
