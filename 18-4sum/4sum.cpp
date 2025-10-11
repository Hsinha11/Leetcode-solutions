#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> result;
        int n = (int)nums.size();
        sort(nums.begin(), nums.end());
        for (int i = 0; i < n; ++i) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            for (int j = i + 1; j < n; ++j) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;
                long long remaining = (long long)target - nums[i] - nums[j];
                int l = j + 1, r = n - 1;
                while (l < r) {
                    long long two = (long long)nums[l] + nums[r];
                    if (two == remaining) {
                        result.push_back({nums[i], nums[j], nums[l], nums[r]});
                        int leftVal = nums[l], rightVal = nums[r];
                        while (l < r && nums[l] == leftVal) ++l;
                        while (l < r && nums[r] == rightVal) --r;
                    } else if (two < remaining) {
                        ++l;
                    } else {
                        --r;
                    }
                }
            }
        }
        return result;
    }
};

// Helper main for quick local testing
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, target;
    if (!(cin >> n)) return 0;
    vector<int> nums(n);
    for (int i = 0; i < n; ++i) cin >> nums[i];
    cin >> target;
    Solution sol;
    auto ans = sol.fourSum(nums, target);
    for (auto &q : ans) {
        for (int i = 0; i < (int)q.size(); ++i) {
            if (i) cout << ' ';
            cout << q[i];
        }
        cout << "\n";
    }
    return 0;
}


