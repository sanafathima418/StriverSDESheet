class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
#         # Approach 1: Recursion/ Backtracking - TLE 
#         # TC: O(2^(N*M) as 2 possibilities
#         # SC: O(N) stack space
#         Idea for counting ways: 
#         1. If success in base case return 1 else return 0
#         2. In the end return sum of all possibilities
        
#         def recur_paths(i, j):
            
#             # 1. Base Case: end point
#             if i == m-1 and j == n-1:
#                 return 1 # Success Case
            
#             if i > m-1 or j > n-1:
#                 return 0 # Boundary Case
            
#             # 2. Inductive Case: Recurse over 2 possibilities
#             right = recur_paths(i, j+1)
#             down = recur_paths(i+1, j)
            
#             return right + down
        
#         return recur_paths(0,0) # start point
    
#         # Approach 2: DP Memoization
#         # TC: O(N^2) Traverse over matrix
#         # SC: O(N^2) for dp array
#         # DP array at any point will give the number of ways to get to end point from that point
        
#         dp = [[-1]*n for _ in range(m)]
        
#         def recur_paths(i, j):
            
#             # 1. Base Case: end point
#             if i == m-1 and j == n-1:
#                 dp[i][j] = 1
#                 return 1 # Success Case
            
#             if i > m-1 or j > n-1:
#                 return 0 # Boundary Case
            
#             if dp[i][j] != -1:
#                 return dp[i][j]
            
#             # 2. Inductive Case: Recurse over 2 possibilities
#             right = recur_paths(i, j+1)
#             down = recur_paths(i+1, j)
            
#             dp[i][j] = right + down
#             return dp[i][j]

#         return recur_paths(0,0) # start point

#         # Approach 3: DP Tabulation - Top Down
#         # TC: O(N^2) Traverse over matrix
#         # SC: O(N^2) for dp array
#         # Intuition: 
#         # 1. Initialize last row and col to 1 
#         # 2. Traverse from m-2,n-2 to 0,0 and add the value to its right and down to get current value
#         # 3. Final Value is available at 0,0
#         # Alternate way - go bottom up whose transposed matrix gives the same result as this solution(refer what dp array is in App. 2)
        
        dp = [[-1]*n for _ in range(m)]
        
        # 1. Initialization
        # 1.1 Set last row to 1
        for col in range(n):
            dp[m-1][col] = 1
        # 1.2 Set last column to 1
        for row in range(m):
            dp[row][n-1] = 1
        
        # 2. Inductive Case: Add the 2 possibilities
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[i][j] = dp[i][j+1] + dp[i+1][j]
        
        return dp[0][0]
        
 
        
        