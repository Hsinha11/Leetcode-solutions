#include <bits/stdc++.h>
using namespace std;

class Solution {

public:
    // Returns True if the position of fresh oranges is within the grid
    bool inBounds(int r, int c, int rows, int cols)
    {
        return r >= 0 && c >= 0 && r < rows && c < cols; 
    }
    
    int orangesRotting(vector<vector<int>>& grid) {

        int rows = grid.size(), cols = grid[0].size();
            
        // Directions for up, down, left and right
            
        vector <vector<int>> directions = { {0,1}, {1,0}, {-1,0}, {0,-1} };
            
        queue <pair<int,int>> q;
            
        int freshOranges = 0;
            
        for(int r = 0; r < rows; r++)
        {
            for(int c = 0; c < cols; c++)
            {
                if(grid[r][c] == 2) q.push({r, c});  // positions of the rotten oranges
                    
                else if(grid[r][c] == 1) freshOranges++;    // count fresh oranges
            }  
        }
            
        // if no fresh oranges present, no time is needed
            
        if (freshOranges == 0) return 0;
            
        int minutes = -1;
            
        while(!q.empty()){
            
            int size = q.size();

            minutes++;
                    
            while(size--){
                    
            auto[r, c] = q.front();
                        
            q.pop();
                    
            // check for 4 directions with the current rotten orange location
                        
            for(auto &dir : directions) {
                        
            int x = r + dir[0];
            int y = c + dir[1];
                            
                            
            // check if the adjacent oranges are within grid bounds and they are fresh
                            
            if( inBounds(x, y, rows, cols) && grid[x][y] == 1 ){
                            
                grid[x][y] = 2;   // make it rotten
                                    
                freshOranges -= 1;  // decrement count of fresh oranges
                                    
                q.push( {x,y} );  // push in queue
                    
            }                 
         }   
       }       
    } 
    
    // if no fresh oranges present, all are rotten and return minutes else 0
    return (freshOranges == 0) ? minutes : -1;  
  
    }
};


int main() {
    
    Solution solution;
    vector<vector<int>> grid = {
        {2,1,1},
        {1,1,0},
        {0,1,1}
    };

    cout << "Minutes until all oranges rot: " << solution.orangesRotting(grid) << "\n"; // output : 4

    return 0;
}


