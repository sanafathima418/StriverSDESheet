class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
#         # Approach 1: Recursion/ Backtracking - TLE 
#         # TC: O(2^(N*M) as 2 possibilities
#         # SC: O(N) stack space
    
#         m = len(triangle)
#         n = len(triangle[-1])
        
#         def recur_paths(i, j):
            
#             # 1. Base Case: end point
#             if i == m-1:
#                 return triangle[i][j]
            
#             # 2. Inductive Case: Recurse over 2 possibilities
#             right, down = math.inf, math.inf
#             if j+1 < n:
#                 right = recur_paths(i+1, j) + triangle[i][j]
#             if i+1 < m:
#                 down = recur_paths(i+1, j+1) + triangle[i][j]
            
#             return min(right, down)
        
#         return recur_paths(0,0) # start point
    
#         # Approach 2: DP Memoization
#         # TC: O(N^2) Traverse over matrix
#         # SC: O(N^2) for dp array
#         # DP array at any point will give the minimum path sum to end point from that point
        
#         m = len(triangle)
#         n = len(triangle[-1])
        
#         dp = [[-1]*n for _ in range(m)]
        
#         def recur_paths(i, j):
            
#             # 1. Base Case: end point
#             if i == m-1:
#                 return triangle[i][j]
            
#             if dp[i][j] != -1:
#                 return dp[i][j]
            
#             # 2. Inductive Case: Recurse over 2 possibilities
#             right, down = math.inf, math.inf
#             if j+1 < n:
#                 right = recur_paths(i+1, j) + triangle[i][j]
#             if i+1 < m:
#                 down = recur_paths(i+1, j+1) + triangle[i][j]
            
#             dp[i][j] = min(right, down)
#             return dp[i][j]
        
#         return  recur_paths(0,0) # start point

#         # Approach 3: DP Tabulation - Top Down
#         # TC: O(N^2) Traverse over matrix
#         # SC: O(N^2) for dp array
        
        m = len(triangle)
        n = len(triangle[-1])
        k = n
        
        dp = [[0]*n for _ in range(m)]
        
        # 2. Inductive Case: Compare the 2 possibilities and add to current
        for i in range(m-1,-1,-1):
            for j in range(k-1,-1,-1):
                # 2.1 Initialization of last row - same as triangle
                if i == m-1:
                    dp[i][j] = triangle[i][j]
                else:
                    # 2.2 Compare down and down right from dp array and add to current value in triangle
                    down, d_right = math.inf, math.inf
                    down = dp[i+1][j] + triangle[i][j]
                    if i+1 < m:
                        d_right = dp[i+1][j+1] + triangle[i][j]
                    dp[i][j] = min(down, d_right)
            # 2.3 k decrements after a row as triangle becomes slimmer as we go up
            k -= 1

        return dp[0][0] 
        
 
        
        