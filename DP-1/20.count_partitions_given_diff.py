from os import *
from sys import *
from collections import *
from math import *

from typing import List


def countPartitions(n: int, d: int, arr: List[int]) -> int:
        
    # Approach 1 - Recursion - TLE
    # TC: O(2^N) for 2 possibilities
    # SC: O(N) for stack space
    
#     def recur_ways(i, subsum):
        
#         # 1. Base Case
#         if i < 0:
#             if subsum == 0: return 1
#             else: return 0
        
#         # 2. Not Take
#         not_take = recur_ways(i-1, subsum) 
        
#         # 3. Take
#         take = 0
#         if arr[i] <= subsum:
#             take = recur_ways(i-1, subsum - arr[i]) 
        
#         # 4. Count Calculate
#         return take + not_take
    
#     n = len(arr)
#     t = sum(arr)
#     if (d+t) % 2:
#         return 0
    
#     # Calculate the value of s1 to satisfy the conditions mentioned
#     # s1 >= s2 is always satisfied
#     s1 = (t+d)//2
#     return recur_ways(n-1,s1)

    # Approach 2 - DP Memoization
    # TC: O(N^2) for going over array
    # SC: O(N^2) for dp array
    
#     def recur_ways(i, subsum):
#         # 1. Base Case
#         if i < 0: 
#             if subsum == 0: return 1
#             return 0
        
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
    
#     n = len(arr)
#     t = sum(arr)
    
#     # Edge Case: If total sum is odd then cannot partition into 2 subsets
#     if d > t or (t + d) % 2:
#         return 0
    
#     # Calculate the value of s1 to satisfy the conditions mentioned
#     # s1 >= s2 is always satisfied
#     s1 = (t+d)//2
#     dp = [[-1 for i in range(s1+1)] for j in range(n)]
    
#     # Return answer mod thing else will not clear all test cases
#     return recur_ways(n-1,s1)%(10**9+7)

    # Approach 3 - DP Tabulation
    # TC: O(N^2) for going over array
    # SC: O(N^2) for dp array
    
    n = len(arr)
    t = sum(arr)
    
    # Edge Case: If total sum is odd then cannot partition into 2 subsets
    if d > t or (t + d) % 2:
        return 0
    
    # Calculate the value of s1 to satisfy the conditions mentioned
    # s1 >= s2 is always satisfied
    s1 = (t+d)//2
    dp = [[0 for i in range(s1+1)] for j in range(n)]
    
    # 1. Initialization
    # If sum is 0, then 1 way to achieved desired sum so set to 1
    for i in range(n):
        dp[i][0] = 1
    
    # If 1st element less than or equal to desired sum, then set the column of achieving that sum using the 1st number
    if arr[0] <= s1:
        dp[0][arr[0]] = 1
    
    # This is some unique stuff - picked from YT comments but works
    # It probably means if the 1st number is 0 then there are two ways of picking 0, i.e, taking or not taking
    if(arr[0] == 0): dp[0][0] = 2
        
    # 2. Recurrence
    for i in range(1,n):
        for j in range(s1+1):
            # 3. Not Take
            not_take = dp[i-1][j]  

            # 4. Take
            take = 0
            if arr[i] <= j:
                take = dp[i-1][j - arr[i]]  

            # 5. Count Calculate
            dp[i][j] = take + not_take
    
    return dp[n-1][s1]%(10**9+7)


    




    
