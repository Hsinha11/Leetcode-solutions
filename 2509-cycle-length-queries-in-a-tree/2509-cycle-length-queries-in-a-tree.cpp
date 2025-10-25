// LeetCode 2509. Cycle Length Queries in a Tree
// Approach: Move both nodes up to their LCA, count steps, add 1 for the added edge
// Time Complexity: O(log n * m), Space Complexity: O(1) extra

#include <vector>
using namespace std;

class Solution {
public:
    vector<int> cycleLengthQueries(int n, vector<vector<int>>& queries) {
        vector<int> ans;
        for(auto &q : queries){
            int u = q[0], v = q[1];
            int length = 0;
            int a = u, b = v;
            while(a != b){
                if(a > b) a /= 2;
                else b /= 2;
                length++;
            }
            ans.push_back(length + 1);
        }
        return ans;
    }
};
