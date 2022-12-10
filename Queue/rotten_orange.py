from collections import defaultdict

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Approach: BFS (In place grid updation after every minute)
        # TC: O(M*N) for traversing over grid
        # SC: O(M*N) for visited array and bfs queue
        
        dRow = [-1,0,1,0]
        dCol = [0,1,0,-1]
        
        visited = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        
        bfs_queue = []
        good_o = 0
            
        # Loop over all nodes to account for non-connected components
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Start of every connected component: start at rotten oranges
                if visited[i][j] == 0 and grid[i][j] == 2:
                    # Append index and time 
                    bfs_queue.append((i,j,0))
                    visited[i][j] = 1
                elif grid[i][j] == 1:
                    good_o += 1
        
        # Return if no good oranges found at time 0
        if not good_o:
            return 0
         
        # BFS Traversal
        while(bfs_queue):
            # 1. Pop curr node from front of queue
            c_i, c_j, t = bfs_queue.pop(0)

            # 2. Loop over adj nodes and add all non-visited adj_node of curr node to queue
            # Mark added nodes as visited
            for i in range(4):
                n_i, n_j = c_i + dRow[i], c_j + dCol[i]
                if n_i < len(grid) and n_i > -1 and n_j < len(grid[0]) and n_j > -1:
                    # 3. If orange exists in cell and not visited, add to queue, mark as visited and update grid
                    if visited[n_i][n_j] == 0:
                        if grid[n_i][n_j] != 0:
                            bfs_queue.append((n_i, n_j, t+1))
                            grid[n_i][n_j] = 2
                        visited[n_i][n_j] = 1
        
        # Check if any good oranges left
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        # Return last time stamp
        return t