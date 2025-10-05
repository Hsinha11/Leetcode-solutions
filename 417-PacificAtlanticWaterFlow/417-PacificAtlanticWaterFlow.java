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
