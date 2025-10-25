// LeetCode 194. Transpose File
// Approach: Read each line into a 2D vector, then swap rows and columns.
// Time Complexity: O(m*n), Space Complexity: O(m*n)

#include <bits/stdc++.h>
using namespace std;

int main() {
    string line;
    vector<vector<string>> matrix;
    
    while (getline(cin, line)) {
        istringstream iss(line);
        string word;
        vector<string> row;
        while (iss >> word) row.push_back(word);
        matrix.push_back(row);
    }
    
    if (matrix.empty()) return 0;
    int rows = matrix.size(), cols = matrix[0].size();
    
    for (int c = 0; c < cols; ++c) {
        for (int r = 0; r < rows; ++r) {
            cout << matrix[r][c];
            if (r != rows - 1) cout << " ";
        }
        cout << "\n";
    }
    
    return 0;
}
