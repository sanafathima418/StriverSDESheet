from collections import defaultdict

# Topo Sort works only for DAG
# BFS topo using Kahn's Algorithms: Use Indegree array 
# Time Complexity: O(V+E) for BFS traversal 
# Space Complexity: O(V) for adjacency list + O(V) for queue + O(V) for indegree array
    
def topologicalSort(adj, v, e):

    # Adjacency list to store Graph state
    adj_list = defaultdict(list)
    
    # Indegree array
    indegree = [0] * v
    
    # BFS Queue
    bfs_queue = []
    
    # Topo Sort Order Array
    topo_sort = []
    
    # Populate Adjacency list for all edges
    for i in range(e):
        adj_list[adj[i][0]].append(adj[i][1])
        # Update Indegree while creating adj list
        indegree[adj[i][1]] += 1
        
    # Add nodes that don't have 0 outdegree and indegree : no edges
    for i in range(v):
        if not adj_list[i]:
            adj_list[i] = []
    
    # BFS Traversal
    def bfs_traversal():
        
        # 1. While queue not empty, process all nodes
        while(bfs_queue):
            # 2. Pop from Queue and add to topo sort array
            curr_node = bfs_queue.pop(0)
            topo_sort.append(curr_node)
            # 3. For every node adjacent to current node
            for adj_node in adj_list[curr_node]:
                # 4. Reduce Indegree
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    # 5. If indegree == 0 or less, Push to Queue
                    bfs_queue.append(adj_node)
    
    # Start Point: Get nodes with indegree = 0 
    for i in range(v):
        if indegree[i] == 0:
            # Append to Queue
            bfs_queue.append(i)
    # Queue always contains elements to process here at start as it is a DAG
    bfs_traversal() 
    
    return topo_sort
