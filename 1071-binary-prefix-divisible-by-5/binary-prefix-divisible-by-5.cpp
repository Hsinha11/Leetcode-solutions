class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& nums) {
        vector<bool> l(nums.size());
        long long int k=0;
        for (int i =0; i<nums.size();i++){
            k = ((k<<1) | nums[i])%5;
            l[i] =(k==0);
        }
        return l;
    }
};