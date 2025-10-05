// 217-contains-duplicate.cpp
// LeetCode Problem 217 - Contains Duplicate
// Author: Shiwans Kumar Yadav
// Approach: Use unordered_set to check for duplicates efficiently.
// Time Complexity: O(n)
// Space Complexity: O(n)

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for (int num : nums) {
            if (seen.count(num)) return true; // Duplicate found
            seen.insert(num);
        }
        return false; // No duplicates found
    }
};

// Example test
int main() {
    Solution s;
    vector<int> nums = {1,2,3,1};
    cout << (s.containsDuplicate(nums) ? "True" : "False") << endl; // Output: True
    return 0;
}
