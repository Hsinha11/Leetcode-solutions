#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        // Assuming lowercase English letters per problem constraints
        array<int, 26> freq{};
        for (char c : s) freq[c - 'a']++;
        for (char c : t) {
            int idx = c - 'a';
            if (--freq[idx] < 0) return false;
        }
        return true;
    }
};

// Helper main for quick local testing
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Input:
    // s t (as two tokens)
    // Example: anagram nagaram
    string s, t;
    if (!(cin >> s >> t)) return 0;
    Solution sol;
    cout << (sol.isAnagram(s, t) ? "true" : "false") << "\n";
    return 0;
}


