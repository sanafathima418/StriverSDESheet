from os import *
from sys import *
from collections import *
from math import *
import math

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


def getMaxPathSum(grid):
#         # Approach 1: Recursion/ Backtracking - TLE 
#         # TC: O(3^(N*M) as 3 possibilities
#         # SC: O(N) stack space
    
#         m = len(grid)
#         n = len(grid[0])
        
#         def recur_paths(i, j):
            
#             # 1. Base Case: end point(if any col in end row is reached)
#             if i == m-1:
#                 return grid[i][j]
            
#             # 2. Inductive Case: Recurse over 3 possibilities
#             down, down_right, down_left = -math.inf, -math.inf, -math.inf
#             down = recur_paths(i+1, j) + grid[i][j]
#             if j+1 < n:
#                 down_right = recur_paths(i+1, j+1) + grid[i][j]
#             if j-1 > -1:
#                 down_left = recur_paths(i+1, j-1) + grid[i][j]
#             return max(down, down_right, down_left)
        
#         # Go over all cols of first row as start points to calculate max obtained
#         max_res = -math.inf
#         for j in range(n):    
#             max_res = max(max_res, recur_paths(0,j)) # start points
#         return max_res
        
#         # Approach 2: DP Memoization
#         # TC: O(N^2) Traverse over matrix
#         # SC: O(N^2) for dp array
#         # DP array at any point will give the minimum path sum to end point from that point
        
#         m = len(grid)
#         n = len(grid[0])
#         dp = [[-1]*n for _ in range(m)]
        
#         def recur_paths(i, j):
            
#             # 1. Base Case: end point(if any col in end row is reached)
#             if i == m-1:
#                 return grid[i][j]
            
#             if dp[i][j] != -1:
#                 return dp[i][j]
            
#             # 2. Inductive Case: Recurse over 3 possibilities
#             down, down_right, down_left = -math.inf, -math.inf, -math.inf
#             down = recur_paths(i+1, j) + grid[i][j]
#             if j+1 < n:
#                 down_right = recur_paths(i+1, j+1) + grid[i][j]
#             if j-1 > -1:
#                 down_left = recur_paths(i+1, j-1) + grid[i][j]
            
#             dp[i][j] =  max(down, down_right, down_left)
#             return dp[i][j]
        
#         # Go over all cols of first row as start points to calculate max obtained
#         max_res = -math.inf
#         for j in range(n):    
#             max_res = max(max_res, recur_paths(0,j)) # start points
#         return max_res

#         # Approach 3: DP Tabulation - Top Down
#         # TC: O(N^2) Traverse over matrix
#         # SC: O(N^2) for dp array
        
        m = len(grid)
        n = len(grid[0])
    
        dp = [[0]*n for _ in range(m)]
        
        # 1. Initializing first row - base condition
        for j in range(n):
            dp[0][j] = grid[0][j]
            
        # 2. Inductive Case: Add the 3 possibilities
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                # 2.1 Initialization of last row - same as grid
                if i == m-1:
                    dp[i][j] = grid[i][j]
                else:
                    # 2.2 Compare down, down right and down left from dp array and add to current value in triangle
                    down, down_right, down_left = -math.inf, -math.inf, -math.inf
                    down = dp[i+1][j] + grid[i][j]
                    if j+1 < n:
                        down_right = dp[i+1][j+1] + grid[i][j]
                    if j-1 > -1:
                        down_left = dp[i+1][j-1] + grid[i][j]

                    dp[i][j] =  max(down, down_right, down_left)
        
        # 3. Return max of first column of dp
        return max(dp[0])







#   taking inpit using fast I/O
def takeInput() :
    n_x = stdin.readline().strip().split(" ")
    n = int(n_x[0].strip())
    m = int(n_x[1].strip())

    matrix=[list(map(int, stdin.readline().strip().split(" "))) for row in range(n)]

    return matrix, n, m


#   main
T = int(input())
while (T > 0):
    T -= 1
    matrix, n, m = takeInput()
    print(getMaxPathSum(matrix))
