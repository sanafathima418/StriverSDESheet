from collections import defaultdict

# With BFS : The trick is tracking parent of every node which is done by storing child and parent pairs in bfs queue.
# Time Complexity: O(V+E) for BFS traversal 
# Space Complexity: O(V) for adjacency list + O(V) for queue + O(V) for visited array

def cycleDetection(edges, n, m):
    
    # Adjacency list to store Graph state
    adj_list = defaultdict(list)
    
    # Visited array
    visited = [0] * n
    
    # BFS Queue
    bfs_queue = []
    
    # Populate Adjacency list for all edges
    for i in range(m):
        adj_list[edges[i][0]].append(edges[i][1])
        adj_list[edges[i][1]].append(edges[i][0])
        
    # Add nodes that don't have 0 outdegree and indegree : no edges
    for i in range(1,n+1):
        if not adj_list[i]:
            adj_list[i] = []
            
    # BFS Traversal
    def bfs_traversal():
        # 1. Loop for every node until queue is empty
        while(bfs_queue):
             # 2. Pop curr node from front of queue
            curr_node = bfs_queue.pop(0)
            parent_node = curr_node[1] # Get parent
            # 3. Loop over adj nodes and add all non-visited adj_node of curr node[0]:child /curr to queue
            # Mark added nodes as visited
            for adj_node in adj_list[curr_node[0]]:
                if visited[adj_node-1] == 0:
                    # Store [child/curr,parent]
                    bfs_queue.append([adj_node,curr_node[0]])
                    visited[adj_node-1] = 1
                elif adj_node !=  parent_node:
                    # 4. If adj node is visited but not a parent node then cycle exists
                    return 1
        return 0
    
    # Loop over all nodes to account for non-connected components
    for node in adj_list:
        # Start of every connected component
        if visited[node-1] == 0: 
            # Store [child/curr,parent]
            bfs_queue.append([node,-1])
            visited[node-1] = 1
            # Connected Components will be taken care of in the bfs traversal queue not empty 
            if(bfs_traversal()):
                return "Yes"
    return "No"
    
    
    
    
