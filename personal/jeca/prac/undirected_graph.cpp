#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

class Graph {
private:
    int V; // Number of vertices
    vector<vector<int>> adj; // 2D adjacency list

    void dfs(int node, vector<int> &vis, vector<int> &result) {
        vis[node] = 1;
        result.push_back(node);
        for(auto it : adj[node]) {
            if(!vis[it]) {
                dfs(it, vis, result);
            }
        }
    }

public:
    // Create: Initialize graph with vertices
    Graph(int vertices) : V(vertices) {
        adj.resize(V);
    }

    // Create: Add undirected edge
    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // Read: Check if edge exists
    bool hasEdge(int u, int v) {
        auto& neighbors = adj[u];
        return find(neighbors.begin(), neighbors.end(), v) != neighbors.end();
    }

    // Update: Replace connection (remove old, add new)
    void updateEdge(int u, int oldV, int newV) {
        removeEdge(u, oldV);
        addEdge(u, newV);
    }

    // Delete: Remove undirected edge
    void removeEdge(int u, int v) {
        // Remove v from u's neighbors
        auto& u_neighbors = adj[u];
        u_neighbors.erase(remove(u_neighbors.begin(), u_neighbors.end(), v), u_neighbors.end());
        
        // Remove u from v's neighbors
        auto& v_neighbors = adj[v];
        v_neighbors.erase(remove(v_neighbors.begin(), v_neighbors.end(), u), v_neighbors.end());
    }

    // Read: Print adjacency list
    void printGraph() {
        for (int i = 0; i < V; ++i) {
            cout << i << " -> ";
            for (int neighbor : adj[i]) {
                cout << neighbor << " ";
            }
            cout << endl;
        }
    }

    vector<int> dfsOfGraph() {
        int n = adj.size();
        vector<int> res, vis(n, 0);
        int start = 0;
        dfs(start, vis, res);

        return res;
    }

    vector<int> bfsOfGraph() {
        int n = adj.size();
        vector<int> bfs, vis(n ,0);
        queue<int> q;
        q.push(0);
        vis[0] = 1;

        while (!q.empty()) {
            int node = q.front();
            q.pop();
            bfs.push_back(node);

            for (auto it : adj[node]) {
                if (!vis[it]) {
                    vis[it] = 1;
                    q.push(it);
                }
            }
        }

        return bfs;
    }
};


int main() {
    Graph g(5); // Create graph with 4 vertices

    // Add edges
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(0, 3);
    g.addEdge(2, 4);

    // Check edge
    // cout << "Edge 1-3 exists? " << g.hasEdge(1, 3) << endl; // 1 (true)

    // Update edge: change 0-2 to 0-3
    // g.updateEdge(0, 2, 3);

    // Remove edge
    // g.removeEdge(1, 3);

    // Print final graph
    // g.printGraph();

    vector<int> dfs = g.dfsOfGraph();
    for(const auto& number : dfs) {
        cout << number << " ";
    }
    cout << endl;

    vector<int> bfs = g.bfsOfGraph();
    for(const auto& number : bfs) {
        cout << number << " ";
    }
    cout << endl;

    return 0;
}
