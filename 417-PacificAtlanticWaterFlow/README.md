# 417. Pacific Atlantic Water Flow (POTD 5 Oct)

## Problem Statement

You are given an `m x n` matrix `heights` representing the height of each cell of an island. The island borders the **Pacific Ocean** on the left and top edges, and the **Atlantic Ocean** on the right and bottom edges.

Water can flow from a cell to its neighboring cell (north, south, east, west) if the neighboring cell's height is **less than or equal** to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a list of all coordinates `[r, c]` where water can flow to **both the Pacific and Atlantic oceans**.

---

## Examples

**Example 1:**

```

Input: heights = [[1,2,2,3,5],
[3,2,3,4,4],
[2,4,5,3,1],
[6,7,1,4,5],
[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

```

**Example 2:**

```

Input: heights = [[1]]
Output: [[0,0]]

```

---

## Constraints

- `m == heights.length`
- `n == heights[r].length`
- `1 <= m, n <= 200`
- `0 <= heights[r][c] <= 10^5`

---

## Approach

1. Use two boolean matrices `pacific` and `atlantic` to track which cells can reach each ocean.
2. Initialize cells touching oceans as `true`.
3. Iteratively update cells if water can flow from them to a cell that can reach the ocean.
4. After stabilization, return cells which can reach **both** oceans.

This is effectively a **reverse BFS/DFS problem**.

---

## Time Complexity

- `O(m * n)` — Each cell is visited multiple times until convergence.

## Space Complexity

- `O(m * n)` — For the two boolean matrices.
```

---

**417-PacificAtlanticWaterFlow.cpp**:

```cpp
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
```

---

**417-PacificAtlanticWaterFlow.java**:

```java
import java.util.*;

class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int m = heights.length, n = heights[0].length;
        boolean[][] pacific = new boolean[m][n];
        boolean[][] atlantic = new boolean[m][n];
        
        for(int i=0;i<m;i++){
            pacific[i][0] = true;
            atlantic[i][n-1] = true;
        }
        for(int j=0;j<n;j++){
            pacific[0][j] = true;
            atlantic[m-1][j] = true;
        }
        
        boolean updated = true;
        while(updated){
            updated = false;
            for(int i=0;i<m;i++){
                for(int j=0;j<n;j++){
                    if(!pacific[i][j]){
                        if(i>0 && pacific[i-1][j] && heights[i][j]>=heights[i-1][j]){
                            pacific[i][j]=true; updated=true;
                        } else if(i<m-1 && pacific[i+1][j] && heights[i][j]>=heights[i+1][j]){
                            pacific[i][j]=true; updated=true;
                        } else if(j>0 && pacific[i][j-1] && heights[i][j]>=heights[i][j-1]){
                            pacific[i][j]=true; updated=true;
                        } else if(j<n-1 && pacific[i][j+1] && heights[i][j]>=heights[i][j+1]){
                            pacific[i][j]=true; updated=true;
                        }
                    }
                    if(!atlantic[i][j]){
                        if(i>0 && atlantic[i-1][j] && heights[i][j]>=heights[i-1][j]){
                            atlantic[i][j]=true; updated=true;
                        } else if(i<m-1 && atlantic[i+1][j] && heights[i][j]>=heights[i+1][j]){
                            atlantic[i][j]=true; updated=true;
                        } else if(j>0 && atlantic[i][j-1] && heights[i][j]>=heights[i][j-1]){
                            atlantic[i][j]=true; updated=true;
                        } else if(j<n-1 && atlantic[i][j+1] && heights[i][j]>=heights[i][j+1]){
                            atlantic[i][j]=true; updated=true;
                        }
                    }
                }
            }
        }
        
        List<List<Integer>> result = new ArrayList<>();
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(pacific[i][j] && atlantic[i][j]){
                    result.add(Arrays.asList(i,j));
                }
            }
        }
        return result;
    }

    public static void main(String[] args){
        Solution sol = new Solution();
        int[][] heights = {{1,2,2,3,5},
                           {3,2,3,4,4},
                           {2,4,5,3,1},
                           {6,7,1,4,5},
                           {5,1,1,2,4}};
        List<List<Integer>> ans = sol.pacificAtlantic(heights);
        for(List<Integer> v: ans){
            System.out.println(v);
        }
    }
}
```


