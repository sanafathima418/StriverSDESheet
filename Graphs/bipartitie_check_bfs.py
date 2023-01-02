class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        # Concept: 2 coloring problem, recurive/backtracking solution same as m-coloring results in TLE
        # Approach: BFS Traversal and check if any of adj nodes have same color as current node if visited
        # If not visited assign alternate color
        # TC: O(V+E) for bfs traversal
        # SC: O(N) for visited array + O(N) for bfs queue
        
        bfs_queue = []
        visited = [-1] * len(graph) # Serves as color array too
        
        def bfs():
            while(bfs_queue):
                # 1. Get current node
                curr_node = bfs_queue.pop(0)
                # 2. Traverse over adj nodes
                for adj_node in graph[curr_node]:
                    if visited[adj_node] == -1:
                        # 3. If not visited assign alternate color
                        visited[adj_node] = ( visited[curr_node] + 1 ) % 2
                        bfs_queue.append(adj_node)
                    elif visited[adj_node] == visited[curr_node]:
                        # 4. If visited, check if color same as it's parent/origin and return immediately
                        return False
            # 5. If all is good then return True as 2 coloring possible for this connected component
            return True
            
        # 1. Loop to go over all non connected components as well
        for i in range(len(graph)):
            # 2. For start of every connected component is node not visited, assign color 0 and push adj nodes
            if visited[i] == -1:
                bfs_queue.append(i)
                visited[i] = 0
                # 3. If in any connected component, 2 coloring not possible return immediately
                if not bfs():
                    return False
        # 4. If not returned from step 3, it means 2 coloring possible for the entire graph so return True
        return True
        