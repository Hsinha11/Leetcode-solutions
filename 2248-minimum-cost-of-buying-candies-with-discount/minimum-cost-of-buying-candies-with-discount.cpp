class Solution {
public:
    int minimumCost(vector<int>& cost) {
        sort(cost.begin(),cost.end(),greater<int>{});
        int ans = 0,x=0;
        for (auto i:cost){
            if (x==2){
                x =0;
                continue;
            }
            ans+=i;
            x++;
        }
        return ans;
    }
};