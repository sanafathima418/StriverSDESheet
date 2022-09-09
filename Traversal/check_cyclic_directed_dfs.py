from collections import defaultdict

# With DFS : If a node is visited, check if it was visited in current DFS cycle
# Time Complexity: O(V+E) for DFS traversal 
# Space Complexity: O(V) for adjacency list + O(V) for stack + O(2V) for 2 visited arrays

def detectCycleInDirectedGraph(n, edges):
    # Adjacency list to store Graph state
    adj_list = defaultdict(list)
    
    # Visited array
    visited = [0] * n
    
    # DFS Visited array: To check if node was visited in current DFS cycle
    dvisited = [0] * n
    
    # DFS Stack
    dfs_stack = []
    
    # Populate Adjacency list for all edges
    for i in range(len(edges)):
        adj_list[edges[i][0]].append(edges[i][1])
        
    # Add nodes that don't have 0 outdegree and indegree : no edges
    for i in range(1,n+1):
        if not adj_list[i]:
            adj_list[i] = []
    
    # DFS Traversal
    def dfs_traversal():
        # 1. Pop curr node from front of queue
        curr_node = dfs_stack.pop()
        
        # Mark visited and curr visited as 1
        visited[curr_node-1] = 1 
        dvisited[curr_node-1] = 1
        
        # 2. Loop over adj nodes
        for adj_node in adj_list[curr_node]:
            if visited[adj_node-1] == 0:
                # 3. If node not visited append to stack and recurse
                dfs_stack.append(adj_node)
                if dfs_traversal():
                    # 4. If while traversal we get 1, it means cycle exists so propagate that to caller
                    return 1
            elif dvisited[adj_node-1]: 
            # 5. If adj node is visited but was not visited in current DFS cycle then no cycle exists, else cycle exists
                return 1
        # 6. While going back reset as unvisited in current dfs visited array as we are retracing steps
        dvisited[curr_node-1] = 0
        return 0
    
    # Loop over all nodes to account for non-connected components
    for node in adj_list:
        # Start of every connected component
        if visited[node-1] == 0: 
            dfs_stack.append(node)
            # Connected Components will be taken care of in the dfs recursion
            if(dfs_traversal()):
                return 1
    return 0
    
    
    
    
