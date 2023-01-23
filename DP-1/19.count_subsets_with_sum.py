from os import *
from sys import *
from collections import *
from math import *

from typing import List

def findWays(arr: List[int], k: int) -> int:
    
#     # Approach 1 - Recursion - TLE
#     # TC: O(2^N) for 2 possibilities
#     # SC: O(N) for stack space
#     num_subsets = 0
    
#     def recur_ways(i, subsum):
#         nonlocal num_subsets
        
#         if subsum == 0:
#             num_subsets += 1
#             return
        
#         if(i < 0): return 

#         recur_ways(i-1, subsum)  # Not Take
#         recur_ways(i-1, subsum - arr[i])  # Take
    
#     n = len(arr)
#     recur_ways(n-1,k)
#     return num_subsets

    # Approach 2 - DP Memoization
    # TC: O(N^2) for going over array
    # SC: O(N^2) for dp array
#     n = len(arr)
#     dp = [[-1 for i in range(k+1)] for j in range(n)]
    
#     def recur_ways(i, subsum):
#         # 1. Base Case
#         if i < 0: 
#             if subsum == 0: return 1
#             else: return 0
        
#         # 2. DP array check
#         if dp[i][subsum] != -1:
#             return dp[i][subsum]
        
#         # 3. Not Take
#         not_take = recur_ways(i-1, subsum)  
        
#         # 4. Take
#         take = 0
#         if arr[i] <= subsum:
#             take = recur_ways(i-1, subsum - arr[i]) 
        
#         # 5. Count Calculate
#         dp[i][subsum] = take + not_take
#         return dp[i][subsum]
    
#     return recur_ways(n-1,k)

    # Approach 3 - DP Tabulation
    # TC: O(N^2) for going over array
    # SC: O(N^2) for dp array
    
    n = len(arr)
    dp = [[0 for i in range(k+1)] for j in range(n)]
    
    # 1. Initialization
    for i in range(n):
        dp[i][0] = 1
        
    if arr[0] <= k:
        dp[0][arr[0]] = 1
    
    # This is some unique stuff - picked from YT comments but works
    # It probably means if the number is 0 then there are two ways of picking 0, i.e, taking or not taking
    if(arr[0] == 0): dp[0][0] = 2
        
    # 2. Recurrence
    for i in range(1,n):
        for j in range(k+1):
            # 3. Not Take
            not_take = dp[i-1][j]  

            # 4. Take
            take = 0
            if arr[i] <= j:
                take = dp[i-1][j - arr[i]]  

            # 5. Count Calculate
            dp[i][j] = take + not_take
    
    return dp[n-1][k]
    


    