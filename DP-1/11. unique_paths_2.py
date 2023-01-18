class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
#         # Approach 1: Recursion/ Backtracking - TLE 
#         # TC: O(2^(N*M) as 2 possibilities
#         # SC: O(N) stack space
#         Idea for counting ways: 
#         1. If success in base case return 1 else return 0
#         2. In the end return sum of all possibilities

#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])
        
#         def recur_paths(i, j):
            
#             # 1. Base Case: end point
#             if i == m-1 and j == n-1:
#                 return 1 # Success Case
            
#             if i > m-1 or j > n-1 or obstacleGrid[i][j] == 1:
#                 return 0 # Boundary Case
            
#             # 2. Inductive Case: Recurse over 2 possibilities
#             right = recur_paths(i, j+1)
#             down = recur_paths(i+1, j)
            
#             return right + down
        
#         # If obstacle at destination, return immediately
#         if obstacleGrid[m-1][n-1] == 1:
#             return 0
#         return recur_paths(0,0) # start point
    
#         # Approach 2: DP Memoization
#         # TC: O(N^2) Traverse over matrix
#         # SC: O(N^2) for dp array
#         # DP array at any point will give the number of ways to get to end point from that point

#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])
        
#         dp = [[-1]*n for _ in range(m)]
        
#         def recur_paths(i, j):
            
#             # 1. Base Case: end point
#             if i == m-1 and j == n-1:
#                 dp[i][j] = 1
#                 return 1 # Success Case
            
#             if i > m-1 or j > n-1 or obstacleGrid[i][j] == 1:
#                 return 0 # Boundary Case
            
#             if dp[i][j] != -1:
#                 return dp[i][j]
            
#             # 2. Inductive Case: Recurse over 2 possibilities
#             right = recur_paths(i, j+1)
#             down = recur_paths(i+1, j)
            
#             dp[i][j] = right + down
#             return dp[i][j]
        
#         If obstacle at destination, return immediately
#         if obstacleGrid[m-1][n-1] == 1:
#             return 0
#         return recur_paths(0,0) # start point

#         # Approach 3: DP Tabulation - Top Down
#         # TC: O(N^2) Traverse over matrix
#         # SC: O(N^2) for dp array
#         # Intuition: 
#         # 1. Initialize last row and col to 1 
#         # 2. Traverse from m-2,n-2 to 0,0 and add the value to its right and down to get current value
#         # 3. Final Value is available at 0,0
#         # This wont work if last row and col are initlaized before
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # If obstacle at destination, return immediately
        if obstacleGrid[m-1][n-1] == 1:
            return 0
    
        dp = [[0]*n for _ in range(m)]
        
        # 2. Inductive Case: Add the 2 possibilities
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                # 2.1 Check if obstacle, then dont add right and down at all
                if obstacleGrid[i][j] == 1:
                    continue
                # 2.2 Destination check
                elif i == m-1 and j == n-1:
                    dp[i][j] = 1
                # Add left and right if within boundary
                else:
                    right = 0
                    down = 0
                    if j < n-1:
                        right = dp[i][j+1] 
                    if i < m-1:
                        down = dp[i+1][j]
                    dp[i][j] = right + down
        
        return dp[0][0]