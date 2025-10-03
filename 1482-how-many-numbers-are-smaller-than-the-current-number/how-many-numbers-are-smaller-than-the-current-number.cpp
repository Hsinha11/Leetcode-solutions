// Approach: Copy and sort the array. For each value, its first index in the
// sorted array equals the count of elements strictly smaller than it.
// Time: O(n log n), Space: O(n). (Alternative O(n) counting sort uses value range 0..100)
class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> c =nums;
        sort(c.begin(),c.end());
        vector<int> res;

        for(auto i :nums){
            auto it = find(c.begin(),c.end(),i);
            int ind = distance(c.begin(),it);
            res.push_back(ind);
        }
        return res;
    }
};