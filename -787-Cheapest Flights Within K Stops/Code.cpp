class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst,
                          int k) {
        vector<vector<pair<int, int>>> adj(n);
        for (auto it : flights)
            adj[it[0]].push_back({it[1], it[2]});
        queue<pair<int, int>> q;
        q.push({0, src});
        vector<int> dist(n, 1e9);
        dist[src] = 0;
        int stops = 0;
        while (!q.empty() && stops <= k) {
            int size = q.size();
            while (size--) {
                int dis = q.front().first;
                int node = q.front().second;
                q.pop();
                for (auto it : adj[node]) {
                    int adjNode = it.first;
                    int weight = it.second;
                    if (dis + weight < dist[adjNode]) {
                        dist[adjNode] = dis + weight;
                        q.push({dis + weight, adjNode});
                    }
                }
            }
            stops++;
        }
        if(dist[dst] == 1e9)    return -1;
        return dist[dst];
    }
};
