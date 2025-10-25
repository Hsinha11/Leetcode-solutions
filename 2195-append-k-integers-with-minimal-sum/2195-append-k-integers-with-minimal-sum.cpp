// LeetCode 2195. Append K Integers With Minimal Sum
// Approach: Add smallest missing positive integers not in nums until k numbers are added
// Time Complexity: O(n + k), Space Complexity: O(n)

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long minimalKSum(vector<int>& nums, int k) {
        unordered_set<int> s(nums.begin(), nums.end());
        long long added_sum = 0;
        long long current = 1;
        while(k > 0) {
            if(s.find(current) == s.end()) {
                added_sum += current;
                k--;
            }
            current++;
        }
        return added_sum;
    }
};
