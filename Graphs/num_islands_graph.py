class Solution:
    
    # Approach: DFS Traversal over grid
    # TC: O(M*N)
    # SC: O(M*N) for visited array, OPTIMIZATION to O(1): Replace grid arr to reflect visited
    
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        dirs = [[-1,0], [1,0], [0,-1], [0, 1]] # Possible Directions
            
        def dfs(i,j,visited):
            # 1. Mark current node as visited
            visited[i][j] = 1
            # 2. Check all possibilities
            for k in range(4):
                # 3. Check if i and j are within grid
                if i+dirs[k][0] > -1 and i+dirs[k][0] < len(grid) and j+dirs[k][1] > -1 and j+dirs[k][1] < len(grid[0]):
                    # 4. Check if node is 1 and not visited and call dfs
                    if int(grid[i+dirs[k][0]][j+dirs[k][1]]) == 1 and not visited[i+dirs[k][0]][j+dirs[k][1]]:
                        dfs(i+dirs[k][0], j+dirs[k][1], visited)
        
        # Loop over grid and identify start points of DFS traversal
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if int(grid[i][j]) == 1 and not visited[i][j]:
                    dfs(i,j, visited)
                    num_islands += 1
                    
        return num_islands