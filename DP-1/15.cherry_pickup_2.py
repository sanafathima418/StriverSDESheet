class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
#         Intuition - Cannot find all by R1 and R2 and sum as it wont be optimal with little effort
#         Both R1 and R2 are to be moved SIMULTANEOUSLY
        
#         Approach 1: Backtracking 3D - TLE
#         TC: O(9^(N*M)) as there are 9 possibilities (3*3- nested loop)
#         SC: O(N) stack space
        
#         m = len(grid)
#         n = len(grid[0])
        
#         def recur_cherry(i, j1, j2):
            
#             # 1.1. Base Case 1 - boundary
#             if j1 < 0 or j2 < 0 or j1 >= n or j2 >= n:
#                 return float('-inf')
             
#             # 1.2. Base Case 2 - Destination reached
#             if i == m-1:
#                 # 1.2.1 If R1 and R2 reach same destination, add only once
#                 if j1 == j2:
#                     return grid[i][j1]
#                 # 1.2.2 If two different destinations reached then add twice
#                 else:
#                     return grid[i][j1]+ grid[i][j2]
            
#             # 2. Inductive Case
#             max_res = float('-inf')
#             changes = [-1, 0, 1]
#             for change_r1 in changes:
#                 for change_r2 in changes:
#                     if j1 == j2:
#                         max_res = max(max_res, grid[i][j1] + recur_cherry(i+1, j1 + change_r1, j2 + change_r2))
#                     else:
#                         max_res = max(max_res, grid[i][j1] + grid[i][j2] + recur_cherry(i+1, j1 + change_r1, j2 + change_r2))
            
#             return max_res
        
#         return recur_cherry(0,0,n-1)
    
        # Approach 2: DP Memoization - Top Down
        # TC: O(M*N^2)) for 3D array traversal
        # SC: O(N*N^2) for 3D array
        
        m = len(grid)
        n = len(grid[0])
        
        # 3D DP Array
        dp=[[[-1 for _ in range(n)] for _ in range(n)] for _ in range(m)]
        
        def recur_cherry(i, j1, j2):
            
            # 1.1. Base Case 1 - boundary
            if j1 < 0 or j2 < 0 or j1 >= n or j2 >= n:
                return float('-inf')
             
            # 1.2. Base Case 2 - Destination reached
            if i == m-1:
                # 1.2.1 If R1 and R2 reach same destination, add only once
                if j1 == j2:
                    return grid[i][j1]
                # 1.2.2 If two different destinations reached then add twice
                else:
                    return grid[i][j1]+ grid[i][j2]
            
            if dp[i][j1][j2] != -1:
                return dp[i][j1][j2]
            
            # 2. Inductive Case
            max_res = float('-inf')
            changes = [-1, 0, 1]
            for change_r1 in changes:
                for change_r2 in changes:
                    if j1 == j2:
                        max_res = max(max_res, grid[i][j1] + recur_cherry(i+1, j1 + change_r1, j2 + change_r2))
                    else:
                        max_res = max(max_res, grid[i][j1] + grid[i][j2] + recur_cherry(i+1, j1 + change_r1, j2 + change_r2))
            
            dp[i][j1][j2] = max_res
            return dp[i][j1][j2] 
        
        return recur_cherry(0,0,n-1)
        
        