class Solution {
public:
    int minimumSumSubarray(vector<int>& nums, int l, int r) {
        int ans = INT_MAX;
        int n = nums.size();
        for (int i =0 ; i <n;i++){
            int curr = 0;
            for (int j=i;j<n;j++){
                curr+=nums[j];
                int length = j - i + 1;
                if (length>=l && length<=r){
                    if (curr>0){
                        ans = min(ans,curr);
                    }
                }
                else if(length>r){
                    break;
                }
            }
        }
        return (ans==INT_MAX)?-1:ans;
    }
};