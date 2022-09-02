from collections import defaultdict

# Time Complexity: O(V+E) for BFS traversal + O(NLOGN) for sorting
# Space Complexity: O(V) for adjacency list + O(V) for queue + O(V) for visited array

def BFS(vertex, edges):
    # Write your solution here
    # 'vertex' is the number of vertices present in the graph
    # 'edges' is a matrix of the set of edges between two given vertices in the graph 
    
    # Adjacency list to store Graph state
    adj_list = defaultdict(list)
    
    # Vistited array
    visited = [0] * vertex
    
    # BFS queue
    bfs_queue = []
    
    # Traversal result 
    bfs_result = []
    
    # Populate Adjacency list for all edges
    for i in range(len(edges[0])):
        adj_list[edges[0][i]].append(edges[1][i])
        adj_list[edges[1][i]].append(edges[0][i])
        
    # Add nodes that don't have 0 outdegree and indegree : no edges
    for i in range(vertex):
        if not adj_list[i]:
            adj_list[i] = []
    
    # BFS Traversal
    def bfs_traversal():
        
        # 1. Pop curr node from front of queue
        curr_node = bfs_queue.pop(0)
        # 2. Add curr node to traversal order list
        bfs_result.append(curr_node)
        
        # 3. Sort list of adj nodes as per question
        sorted_adj_list = sorted(adj_list[curr_node])
        
        # 4. Loop over adj nodes and add all non-visited adj_node of curr node to queue
        # Mark added nodes as visited
        for adj_node in sorted_adj_list:
            if visited[adj_node] == 0:
                bfs_queue.append(adj_node)
                visited[adj_node] = 1
                
        # 5. After adding adj nodes to queue, recurse for every node until queue is empty
        while(bfs_queue):
            bfs_traversal()     
                
    # Loop over all nodes to account for non-connected components
    for node in adj_list:
        # Start of every connected component
        if visited[node] == 0: 
            bfs_queue.append(node)
            visited[node] = 1
            # Connected Components will be taken care of in the recursion calls
            bfs_traversal()  

    return bfs_result
