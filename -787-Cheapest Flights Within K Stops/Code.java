class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] it : flights)
            adj.get(it[0]).add(new int[]{it[1], it[2]});
        
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0, src});
        int[] dist = new int[n];
        Arrays.fill(dist, (int)1e9);
        dist[src] = 0;
        
        int stops = 0;
        while (!q.isEmpty() && stops <= k) {
            int size = q.size();
            while (size-- > 0) {
                int[] curr = q.poll();
                int dis = curr[0];
                int node = curr[1];
                for (int[] it : adj.get(node)) {
                    int adjNode = it[0];
                    int weight = it[1];
                    if (dis + weight < dist[adjNode]) {
                        dist[adjNode] = dis + weight;
                        q.add(new int[]{dis + weight, adjNode});
                    }
                }
            }
            stops++;
        }
        return dist[dst] == (int)1e9 ? -1 : dist[dst];
    }
}
