from collections import defaultdict

# Time Complexity: O(V+E) for DFS traversal 
# Space Complexity: O(V) for adjacency list + O(V) for stack + O(V) for visited array
    
def topologicalSort(adj, v, e):

    # Adjacency list to store Graph state
    adj_list = defaultdict(list)
    
    # Visited array
    visited = [0] * v
    
    # DFS Stack
    dfs_stack = []
    
    # Populate Adjacency list for all edges
    for i in range(e):
        adj_list[adj[i][0]].append(adj[i][1])
        
    # Add nodes that don't have 0 outdegree and indegree : no edges
    for i in range(v):
        if not adj_list[i]:
            adj_list[i] = []
            
    # DFS Traversal
    def dfs_traversal(node):
        # 1. For every node adjacent to current node, 
        # Call dfs traversal by marking as visited 
        for adj_node in adj_list[node]:
            if visited[adj_node] == 0:
                visited[adj_node] = 1
                dfs_traversal(adj_node)
        # 2. Append to Stack for topo sort order after traversal of current node
        dfs_stack.append(node)
    
     # Loop over all nodes to account for non-connected components
    for node in adj_list:
        # Start of every connected component
        if visited[node] == 0: 
            visited[node] = 1
            # Connected Components will be taken care of in the recursion calls
            dfs_traversal(node)
    
    # Stack contains elements with v in the end and u at top so reverse
    return dfs_stack[::-1]
