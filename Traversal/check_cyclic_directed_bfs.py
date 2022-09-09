from collections import defaultdict

# With BFS : Using Kahn's Algorithm: Check if atleast 1 node has indegree of 0
# Time Complexity: O(V+E) for BFS traversal 
# Space Complexity: O(V) for adjacency list + O(V) for Indegree array

def detectCycleInDirectedGraph(n, edges):
    # Adjacency list to store Graph state
    adj_list = defaultdict(list)
    
    # Indegree array
    indegree = [0] * n
    
    # Populate Adjacency list for all edges
    for i in range(len(edges)):
        adj_list[edges[i][0]].append(edges[i][1])
        # Update Indegree while creating adj list
        indegree[edges[i][1] - 1] += 1
        
    # Add nodes that don't have 0 outdegree and indegree : no edges
    for i in range(n):
        if not adj_list[i]:
            adj_list[i] = []
    
    # Start Point: Get nodes with indegree = 0 
    for i in range(1,n):
        if indegree[i-1] == 0:
            return 0
    return 1
    
    
    
    
