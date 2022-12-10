from typing import *
from collections import defaultdict

# Time Complexity: O(V+E) for DFS traversal + O(NLOGN) for sorting
# Space Complexity: O(V) for adjacency list + O(V) for stack + O(V) for visited array

def depthFirstSearch(V, E, s_edges):
    # Adjacency list to store Graph state
    adj_list = defaultdict(list)
    
    # Visited array
    visited = [0] * V
    
    # DFS Stack
    dfs_stack = []
    
    # Traversal result final
    main_list = []
    
    # Traversal result of every connected component
    sub_list = []
    
    # IGNORE: Input is taken incorrectly so tmp changes to convert object 
    # reference to list of edges
    edges = []
    for obj in s_edges:
        edges.append(list(map(int, obj)))
    
    # Populate Adjacency list for all edges
    for i in range(len(edges)):
        adj_list[edges[i][0]].append(edges[i][1])
        adj_list[edges[i][1]].append(edges[i][0])
        
    # Add nodes that don't have 0 outdegree and indegree : no edges
    for i in range(V):
        if not adj_list[i]:
            adj_list[i] = []
            
    # DFS Traversal
    def dfs_traversal():
        # 1. Pop from top of stack
        curr_node = dfs_stack.pop()
        
        # 2. Add popped node to traversal list
        sub_list.append(curr_node)
        
        # 3. For every node adjacent to current node, 
        # Call dfs traversal by marking as visited 
        # And adding to stack
        for adj_node in adj_list[curr_node]:
            if visited[adj_node] == 0:
                dfs_stack.append(adj_node)
                visited[adj_node] = 1
                dfs_traversal()
    
    # Loop over all nodes to account for non-connected components
    for node in adj_list:
        # Start of every connected component
        if visited[node] == 0: 
            dfs_stack.append(node)
            visited[node] = 1
            # Connected Components will be taken care of in the recursion calls
            sub_list = []  # Reinitialize for every non-connected component
            dfs_traversal()
            sub_list.sort()  # As required by problem 
            main_list.append(sub_list.copy()) # Append to main list of components
    
    main_list = sorted(main_list, key=lambda x: x[0])   # As required by problem 
    
    return main_list




