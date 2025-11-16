// #DEFINE MOD = 1000000007;
class Solution {
public:
    int numSub(string s) {
        long long c = 0, group = 0;
        for (auto i : s) {
            if (i == '1') {

                group++;
            } else {
                c += (group * (group + 1)) / 2;
                group=0;
            }
        }
        c += (group * (group + 1)) / 2;
        return c%1000000007;
    }
};