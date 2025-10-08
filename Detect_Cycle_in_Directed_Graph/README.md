# Detect Cycle in Directed Graph

## 🧠 Problem Statement
Given a directed graph, determine whether it contains a cycle.  
Return true if there is a cycle, otherwise false.

## 🪄 Approach
1. Use **Depth First Search (DFS)**.
2. Maintain two arrays:
   - **visited[]**: tracks visited nodes.
   - **recStack[]**: tracks nodes in the current recursion path.
3. If a node is visited again while still in recursion stack → cycle detected.

## 🧩 Test Cases
- Input:  
  n = 4, edges = [(0,1), (1,2), (2,3), (3,1)]  
  Output: true  
- Input:  
  n = 3, edges = [(0,1), (1,2)]  
  Output: false

## ⚙️ Edge Cases
- Empty graph  
- Single node with a self-loop  

## 🎯 Expected Outcome
Detects cycle correctly for any directed graph.

## 💻 C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool dfs(int node, vector<int> adj[], vector<int>& vis, vector<int>& rec) {
    vis[node] = 1;
    rec[node] = 1;
    for (int n : adj[node]) {
        if (!vis[n] && dfs(n, adj, vis, rec)) return true;
        else if (rec[n]) return true;
    }
    rec[node] = 0;
    return false;
}

bool isCyclic(int V, vector<int> adj[]) {
    vector<int> vis(V, 0), rec(V, 0);
    for (int i = 0; i < V; i++)
        if (!vis[i] && dfs(i, adj, vis, rec)) return true;
    return false;
}

int main() {
    int V = 4;
    vector<int> adj[V];
    adj[0].push_back(1);
    adj[1].push_back(2);
    adj[2].push_back(3);
    adj[3].push_back(1);
    cout << (isCyclic(V, adj) ? "Cycle Found" : "No Cycle");
}
```

## ☕ Java Solution
```java
import java.util.*;

class Main {
    static boolean dfs(int node, List<List<Integer>> adj, boolean[] vis, boolean[] rec) {
        vis[node] = true;
        rec[node] = true;
        for (int n : adj.get(node)) {
            if (!vis[n] && dfs(n, adj, vis, rec)) return true;
            else if (rec[n]) return true;
        }
        rec[node] = false;
        return false;
    }

    static boolean isCyclic(int V, List<List<Integer>> adj) {
        boolean[] vis = new boolean[V];
        boolean[] rec = new boolean[V];
        for (int i = 0; i < V; i++)
            if (!vis[i] && dfs(i, adj, vis, rec)) return true;
        return false;
    }

    public static void main(String[] args) {
        int V = 4;
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) adj.add(new ArrayList<>());
        adj.get(0).add(1);
        adj.get(1).add(2);
        adj.get(2).add(3);
        adj.get(3).add(1);
        System.out.println(isCyclic(V, adj) ? "Cycle Found" : "No Cycle");
    }
}
```
