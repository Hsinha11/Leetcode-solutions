#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size(), n = heights[0].size();
        vector<vector<bool>> pacific(m, vector<bool>(n, false));
        vector<vector<bool>> atlantic(m, vector<bool>(n, false));
        
        for (int i = 0; i < m; i++) {
            pacific[i][0] = true;
            atlantic[i][n-1] = true;
        }
        for (int j = 0; j < n; j++) {
            pacific[0][j] = true;
            atlantic[m-1][j] = true;
        }
        
        bool updated = true;
        while(updated) {
            updated = false;
            for(int i=0;i<m;i++){
                for(int j=0;j<n;j++){
                    if(!pacific[i][j]){
                        if(i>0 && pacific[i-1][j] && heights[i][j] >= heights[i-1][j]){
                            pacific[i][j] = true; updated = true;
                        } else if(i<m-1 && pacific[i+1][j] && heights[i][j] >= heights[i+1][j]){
                            pacific[i][j] = true; updated = true;
                        } else if(j>0 && pacific[i][j-1] && heights[i][j] >= heights[i][j-1]){
                            pacific[i][j] = true; updated = true;
                        } else if(j<n-1 && pacific[i][j+1] && heights[i][j] >= heights[i][j+1]){
                            pacific[i][j] = true; updated = true;
                        }
                    }
                    if(!atlantic[i][j]){
                        if(i>0 && atlantic[i-1][j] && heights[i][j] >= heights[i-1][j]){
                            atlantic[i][j] = true; updated = true;
                        } else if(i<m-1 && atlantic[i+1][j] && heights[i][j] >= heights[i+1][j]){
                            atlantic[i][j] = true; updated = true;
                        } else if(j>0 && atlantic[i][j-1] && heights[i][j] >= heights[i][j-1]){
                            atlantic[i][j] = true; updated = true;
                        } else if(j<n-1 && atlantic[i][j+1] && heights[i][j] >= heights[i][j+1]){
                            atlantic[i][j] = true; updated = true;
                        }
                    }
                }
            }
        }
        
        vector<vector<int>> result;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(pacific[i][j] && atlantic[i][j])
                    result.push_back({i,j});
            }
        }
        return result;
    }
};

int main(){
    Solution sol;
    vector<vector<int>> heights = {{1,2,2,3,5},
                                   {3,2,3,4,4},
                                   {2,4,5,3,1},
                                   {6,7,1,4,5},
                                   {5,1,1,2,4}};
    vector<vector<int>> ans = sol.pacificAtlantic(heights);
    for(auto &v: ans){
        cout << "[" << v[0] << "," << v[1] << "] ";
    }
    cout << endl;
    return 0;
}
