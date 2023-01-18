class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
#         # Approach 1: Recursion/ Backtracking - TLE 
#         # TC: O(2^(N*M) as 2 possibilities
#         # SC: O(N) stack space
    
#         m = len(grid)
#         n = len(grid[0])
        
#         def recur_paths(i, j):
            
#             # 1. Base Case: end point
#             if i == m-1 and j == n-1:
#                 return grid[m-1][n-1]
            
#             # 2. Inductive Case: Recurse over 2 possibilities
#             right, down = math.inf, math.inf
#             if j+1 < n:
#                 right = recur_paths(i, j+1) + grid[i][j]
#             if i+1 < m:
#                 down = recur_paths(i+1, j) + grid[i][j]
            
#             return min(right, down)
        
#         return recur_paths(0,0) # start point
    
#         # Approach 2: DP Memoization
#         # TC: O(N^2) Traverse over matrix
#         # SC: O(N^2) for dp array
#         # DP array at any point will give the minimum path sum to end point from that point
        
#         m = len(grid)
#         n = len(grid[0])
#         dp = [[-1]*n for _ in range(m)]
        
#         def recur_paths(i, j):
            
#             # 1. Base Case: end point
#             if i == m-1 and j == n-1:
#                 dp[i][j] =  grid[m-1][n-1]
#                 return dp[i][j] # Success Case
            
#             if dp[i][j] != -1:
#                 return dp[i][j]
            
#             # 2. Inductive Case: Recurse over 2 possibilities
#             right, down = math.inf, math.inf
#             if j+1 < n:
#                 right = recur_paths(i, j+1) + grid[i][j]
#             if i+1 < m:
#                 down = recur_paths(i+1, j) + grid[i][j]

#             dp[i][j] = min(right, down)
#             return dp[i][j]
        
#         return recur_paths(0,0) # start point

#         # Approach 3: DP Tabulation - Top Down
#         # TC: O(N^2) Traverse over matrix
#         # SC: O(N^2) for dp array
        
        m = len(grid)
        n = len(grid[0])
    
        dp = [[0]*n for _ in range(m)]
        
        # 2. Inductive Case: Add the 2 possibilities
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                # 2.1 Destination check
                if i == m-1 and j == n-1:
                    dp[i][j] = grid[i][j]
                # Add right and down if within boundary
                else:
                    right, down = math.inf, math.inf
                    if j < n-1:
                        right = dp[i][j+1] + grid[i][j]
                    if i < m-1:
                        down = dp[i+1][j]  + grid[i][j]
                    dp[i][j] = min(right, down)
        
        return dp[0][0]
        
 
        
        