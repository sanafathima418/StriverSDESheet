from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Approach: Topo Sort BFS - Kahn's Algorithm
        # TC: O(V+E) for traversing all edges and vertices
        # SC: O(V) for queue, indegree, adj_list
        
        adj_list = defaultdict(list)
        indegree = [0] * numCourses
        bfs_queue = []
        traversal_count = 0
        
        # 1. Populate adj list with all edges and update indegree array
        for i in range(len(prerequisites)):
            adj_list[prerequisites[i][1]].append(prerequisites[i][0])
            indegree[prerequisites[i][0]] += 1  # this depends on the representation in edges(prereq) array
            
        # 2. Add nodes that have an outdegree and indegree of 0 : no edges
        for i in range(numCourses):
            if i not in adj_list:
                adj_list[i] = []
        
        # 3. Loop over all nodes to check for start points
        for i in range(numCourses):
            if not indegree[i]:
                bfs_queue.append(i)
        
        # 4. BFS Traversal
        while(bfs_queue):
            curr_node = bfs_queue.pop(0)
            traversal_count += 1
            # 4.1 Traverse over adj nodes
            for adj_node in adj_list[curr_node]:
                # 4.2 Reduce indegree count
                indegree[adj_node] -= 1
                # 4.3 If indegree has reduced to zero then push to queue
                if not indegree[adj_node]: 
                    bfs_queue.append(adj_node)

        # 5. If all nodes traversed then no cycle so possible to complete all courses
        if traversal_count == numCourses:
            return True
        return False
            
                
            