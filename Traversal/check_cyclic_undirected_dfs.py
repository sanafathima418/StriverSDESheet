from collections import defaultdict

# With DFS : Check parent and propagate return value to caller by calling recur func within if condition and returning based on the value
# Time Complexity: O(V+E) for DFS traversal 
# Space Complexity: O(V) for adjacency list + O(V) for stack + O(V) for visited array

def cycleDetection(edges, n, m):
    
    # Adjacency list to store Graph state
    adj_list = defaultdict(list)
    
    # Visited array
    visited = [0] * n
    
    # DFS Stack
    dfs_stack = []
    
    # Populate Adjacency list for all edges
    for i in range(m):
        adj_list[edges[i][0]].append(edges[i][1])
        adj_list[edges[i][1]].append(edges[i][0])
        
    # Add nodes that don't have 0 outdegree and indegree : no edges
    for i in range(1,n+1):
        if not adj_list[i]:
            adj_list[i] = []
    
    # DFS Traversal
    def dfs_traversal():
        # 1. Pop curr node from front of queue
        curr_node = dfs_stack.pop()
        parent_node = curr_node[1] # Get parent
        
        # 2. Loop over adj nodes
        for adj_node in adj_list[curr_node[0]]:
            if visited[adj_node-1] == 0:
                # 3. If node not visited append to stack and recurse
                dfs_stack.append([adj_node,curr_node[0]])
                visited[adj_node-1] = 1 # Mark added node as visited
                if dfs_traversal():
                    # 4. If while traversal we get 1, it means cycle exists so propagate that to caller
                    return 1
            elif adj_node !=  parent_node: 
                # 5. If adj node is visited but not a parent node then cycle exists
                return 1
        return 0
    
    # Loop over all nodes to account for non-connected components
    for node in adj_list:
        # Start of every connected component
        if visited[node-1] == 0: 
            # Store [child/curr,parent]
            dfs_stack.append([node,-1])
            visited[node-1] = 1
            # Connected Components will be taken care of in the dfs recursion
            if(dfs_traversal()):
                return "Yes"
    return "No"
    
    
    
    
