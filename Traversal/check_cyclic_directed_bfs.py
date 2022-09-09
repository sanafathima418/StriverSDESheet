from collections import defaultdict

# With BFS : Using Kahn's Algorithm: Check if atleast 1 node has indegree of 0
# Time Complexity: O(V+E) for BFS traversal 
# Space Complexity: O(V) for adjacency list + O(V) for Indegree array

def detectCycleInDirectedGraph(n, edges):
    # Adjacency list to store Graph state
    adj_list = defaultdict(list)
    
    # Indegree array
    indegree = [0] * n
    
    # BFS Queue
    bfs_queue = []
    
    # Traversal Count variable instead of Topo Sort Order Array (Same purpose as we only need length)
    traversal_count = 0
    
    # Populate Adjacency list for all edges
    for i in range(len(edges)):
        adj_list[edges[i][0]].append(edges[i][1])
        # Update Indegree while creating adj list
        indegree[edges[i][1] - 1] += 1
        
     # Add nodes that don't have 0 outdegree and indegree : no edges
    for i in range(n):
        if not adj_list[i]:
            adj_list[i] = []
        
    # BFS Traversal
    def bfs_traversal():
        nonlocal traversal_count
        
        # 1. While queue not empty, process all nodes
        while(bfs_queue):
            # 2. Pop from Queue and increment traversal count
            curr_node = bfs_queue.pop(0)
            traversal_count += 1
            # 3. For every node adjacent to current node
            for adj_node in adj_list[curr_node]:
                # 4. Reduce Indegree
                indegree[adj_node - 1] -= 1
                if indegree[adj_node - 1] == 0:
                    # 5. If indegree == 0 or less, Push to Queue
                    bfs_queue.append(adj_node)
        
    # Start Point: Get nodes with indegree = 0 
    for i in range(n):
        if indegree[i - 1] == 0:
            # Append to Queue
            bfs_queue.append(i)
    
    bfs_traversal() 
    
    # If topo sort happens for all nodes then no cycle exists, else cycle exists 
    if traversal_count == n:
        return 0
    return 1
    
    
    
    
