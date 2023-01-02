class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        # Concept: 2 coloring problem, recurive/backtracking solution same as m-coloring results in TLE
        # Approach: DFS Traversal and check if any of adj nodes have same color as current node if visited
        # If not visited assign alternate color
        # TC: O(V+E) for bfs traversal
        # SC: O(N) for visited array + O(N) for bfs queue
        
        dfs_stack = []
        visited = [-1] * len(graph) # Serves as color array too
        
        def dfs():
            # 1. Pop from top of stack
            curr_node = dfs_stack.pop()
            # 3. For every node adjacent to current node, 
            # Call dfs traversal by marking as visited 
            # And adding to stack
            for adj_node in graph[curr_node]:
                if visited[adj_node] == -1:
                    # 3. If not visited assign alternate color and append to stack
                    visited[adj_node] = ( visited[curr_node] + 1 ) % 2
                    dfs_stack.append(adj_node)
                    # 4. Traverse again and return if needed
                    if not dfs():
                        return False
                elif visited[adj_node] == visited[curr_node]:
                    # 5. If visited, check if color same as it's parent/origin and return immediately
                    return False
            return True

            
        # 1. Loop to go over all non connected components as well
        for i in range(len(graph)):
            # 2. For start of every connected component is node not visited, assign color 0 and push adj nodes
            if visited[i] == -1:
                dfs_stack.append(i)
                visited[i] = 0
                # 3. If in any connected component, 2 coloring not possible return immediately
                if not dfs():
                    return False
        # 4. If not returned from step 3, it means 2 coloring possible for the entire graph so return True
        return True
        
        