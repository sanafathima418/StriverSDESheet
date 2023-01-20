from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):
    
    # Approach 1: Backtracking- Take, not take - TLE
    # TC:O(2^N) for 2 possibilities
    # SC: O(N) for stack space
    
#     def recur_subsum(i, subsum):
        
#          # 1. Base Case - is sum is achieved - true or reached end of array - false
#         if subsum == k:
#             return 1
        
#         if i == n:
#             return 0
        
#         # 2. Not Take 
#         not_take = recur_subsum(i+1, subsum)
        
#         # 3. Take 
#         if (subsum + arr[i]) <= k: # if subsum goes above k then no point in proceeding here
#             take = recur_subsum(i+1, subsum + arr[i])
        
#         # 4. if either is true return true, else false
#         return not_take or take
    
#     return recur_subsum(0,0)
        
    # Approach 2: DP Memoization 
    # TC: O(k*N) for calcuating all index and subsum pairs
    # SC: O(k*N) for dp array + O(N) for stack space
    
    # DP array for storing previous computations of an index and subsum pair
#     dp = [[-1 for i in range(k+1)] for j in range(n)]
    
#     def recur_subsum(i, subsum):
        
#         # 1. Base Case - is sum is achieved - true or reached end of array - false
#         if subsum == k:
#             return True
        
#         if i == n:
#             return False
        
#         # 2. Check dp array
#         if dp[i][subsum] != -1:
#             return dp[i][subsum]
        
#         # 3. Not Take 
#         not_take = recur_subsum(i+1, subsum)

#         # 4. Take 
#         take = False
#         if (subsum + arr[i]) <= k: # if subsum goes above k then no point in proceeding here
#             take = recur_subsum(i+1, subsum + arr[i])
        
#         # 5. if either is true return true, else false
#         dp[i][subsum] = not_take or take
#         return dp[i][subsum]
       
#     return recur_subsum(0,0)

    # Approach 3: DP Tabulation - Bottom up
    # TC: O(k*N) for calcuating all index and subsum pairs
    # SC: O(k*N) for dp array
    
    dp = [[False for i in range(k+1)] for j in range(n)]
    
    # 1. Initialization
   # 1.1 If target is 0, set true (subsum achieved) - if a sequence gets here it means it a valid one as per Appr 2 (refer top down instead of the bottom up above)
    for i in range(n):
        dp[i][0] = True
            
    # 1.1 The 0th element alone "can" form target if less than k
    if arr[0] <= k:
        dp[0][arr[0]] = True
    
    # 2. Recurrence
    for i in range(1,n):
        for j in range(1,k+1):
            not_take = dp[i-1][j]
            take = False
            if arr[i] <= j: 
                take = dp[i-1][j-arr[i]]
            dp[i][j] = take or not_take
    
    # 3. Return last element of array which indicates if a subset with all elements can sum to k
    return dp[n-1][k]
            
    
    
    

