#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        string current;
        current.reserve(2 * n);
        backtrack(n, 0, 0, current, result);
        return result;
    }
private:
    void backtrack(int n, int open, int close, string &current, vector<string> &result) {
        if ((int)current.size() == 2 * n) {
            result.push_back(current);
            return;
        }
        if (open < n) {
            current.push_back('(');
            backtrack(n, open + 1, close, current, result);
            current.pop_back();
        }
        if (close < open) {
            current.push_back(')');
            backtrack(n, open, close + 1, current, result);
            current.pop_back();
        }
    }
};

// Helper main for quick local testing
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    Solution sol;
    auto ans = sol.generateParenthesis(n);
    for (auto &s : ans) cout << s << "\n";
    return 0;
}


