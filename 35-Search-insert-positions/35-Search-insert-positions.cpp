#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = 0, r = nums.size()-1;
        int ceil = INT_MAX;
        while(l<=r){
            int mid = l + (r-l)/2;
            if(nums[mid] == target){
                return mid;
            }
            else if(nums[mid]>target){
                // ceil = min(ceil, mid);
                r = mid-1;
            }
            else{
                l = mid+1;
            }
        }

        return l;
    }
};