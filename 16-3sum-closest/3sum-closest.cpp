class Solution {
public:
    int threeSumClosest(vector<int>& num, int target) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        int n = num.size();
        sort(num.begin(), num.end());
        int mini = num[0]+num[1]+num[2];
        for (int i = 0; i < n; i++) {
            if (i > 0 && num[i] == num[i - 1])
                continue;
            int j = i + 1;
            int k = n - 1;
            while (j < k) {
                int sum = num[i] + num[j] + num[k];
                if (abs(target-sum)<abs(target-mini)){
                    mini = sum;
                }
                if (sum < target) {
                    // mini = min(sum, mini);
                    j++;
                } else if (sum > target) {
                    // mini = max(sum, mini);
                    k--;
                } else {
                   return sum;
                }
            }
        }
        return mini;
    }
};