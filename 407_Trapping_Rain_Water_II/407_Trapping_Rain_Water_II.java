import java.util.*;

class Solution {
    public int trapRainWater(int[][] heightMap) {
        if (heightMap == null || heightMap.length == 0 || heightMap[0].length == 0) return 0;
        int m = heightMap.length, n = heightMap[0].length;
        if (m < 3 || n < 3) return 0;

        boolean[][] visited = new boolean[m][n];
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));

        // Push all boundary cells into min-heap
        for (int i = 0; i < m; i++) {
            pq.offer(new int[]{heightMap[i][0], i, 0}); visited[i][0] = true;
            pq.offer(new int[]{heightMap[i][n-1], i, n-1}); visited[i][n-1] = true;
        }
        for (int j = 0; j < n; j++) {
            if (!visited[0][j]) { pq.offer(new int[]{heightMap[0][j], 0, j}); visited[0][j] = true; }
            if (!visited[m-1][j]) { pq.offer(new int[]{heightMap[m-1][j], m-1, j}); visited[m-1][j] = true; }
        }

        int res = 0;
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};

        while (!pq.isEmpty()) {
            int[] cell = pq.poll();
            int h = cell[0], r = cell[1], c = cell[2];
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || visited[nr][nc]) continue;
                visited[nr][nc] = true;
                int nh = heightMap[nr][nc];
                if (nh < h) res += h - nh;
                pq.offer(new int[]{Math.max(nh, h), nr, nc});
            }
        }

        return res;
    }
}
