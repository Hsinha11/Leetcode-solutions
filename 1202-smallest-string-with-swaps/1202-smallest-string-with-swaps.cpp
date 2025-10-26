// 1202-smallest-string-with-swaps.cpp
// Approach: Use Union-Find (DSU) to group all indices that can be swapped with each other.
// For each connected component, collect characters and indices, sort them, 
// and place the smallest characters in the smallest indices.
// Time Complexity: O(n log n + m α(n)) where n = string length, m = number of pairs.
// Space Complexity: O(n)

#include <bits/stdc++.h>
using namespace std;

class DSU {
public:
    vector<int> parent, size;
    DSU(int n) {
        parent.resize(n);
        size.assign(n, 1);
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int x) {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    }
    void unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a != b) {
            if (size[a] < size[b]) swap(a, b);
            parent[b] = a;
            size[a] += size[b];
        }
    }
};

class Solution {
public:
    string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
        int n = s.size();
        DSU dsu(n);
        
        // Step 1: Union all index pairs
        for (auto &p : pairs) {
            dsu.unite(p[0], p[1]);
        }
        
        // Step 2: Group indices by their root parent
        unordered_map<int, vector<int>> components;
        for (int i = 0; i < n; i++) {
            components[dsu.find(i)].push_back(i);
        }
        
        // Step 3: For each component, sort indices and corresponding characters
        string result = s;
        for (auto &entry : components) {
            vector<int> indices = entry.second;
            string chars = "";
            for (int idx : indices) {
                chars.push_back(s[idx]);
            }
            sort(indices.begin(), indices.end());
            sort(chars.begin(), chars.end());
            for (int i = 0; i < indices.size(); i++) {
                result[indices[i]] = chars[i];
            }
        }
        return result;
    }
};
