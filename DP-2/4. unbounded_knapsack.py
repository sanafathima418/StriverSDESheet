from os import *
from sys import *
from collections import *
from math import *

def unboundedKnapsack(n, w, profit, weight):
    # Approach 1: Recursion. - TLE
    # TC: O(2^N) for 2 possibilities
    # SC: O(N) for stack space

    # def recur_unbounded(i,curr_w):
    #     # 1. Base Case
    #     if i < 0 or curr_w == 0: 
    #         return 0
        
    #     # 2. Recurrence
    #     not_take = 0 + recur_unbounded(i-1, curr_w)
    #     take = 0
    #     if weight[i] <= curr_w:
    #         take = profit[i] + recur_unbounded(i, curr_w - weight[i])

    #     return max(not_take, take)
    
    # return recur_unbounded(n-1, w)

    # Approach 2: DP Memoization
    # TC: O(N^2) for traversing over 2d array
    # SC: O(N^2) for 2d array + O(N) for stack space

    # dp = [[-1 for j in range(w+1)] for i in range(n)]

    # def recur_unbounded(i,curr_w):
    #     # 1. Base Case
    #     if i < 0 or curr_w == 0: 
    #         return 0
        
    #     if dp[i][curr_w] != -1:
    #         return dp[i][curr_w]
        
    #     # 2. Recurrence
    #     not_take = 0 + recur_unbounded(i-1, curr_w)
    #     take = 0
    #     if weight[i] <= curr_w:
    #         take = profit[i] + recur_unbounded(i, curr_w - weight[i])

    #     dp[i][curr_w] = max(not_take, take)
    #     return dp[i][curr_w]
    
    # return recur_unbounded(n-1, w)

    # Approach 3: DP Tabulation
    # TC: O(N^2) for traversing over 2d array
    # SC: O(N^2) for 2d array

    # DP array represents max profit by choosing items of different weights to achieve a total weight of curr_w
    dp = [[0 for j in range(w+1)] for i in range(n)]

    # 1. Initialization
    for j in range(w+1):
        # Initialize first row with the current weight of entire capacity/ 1st item weight and its value 
        dp[0][j] =  (j // weight[0]) * profit[0]

    # 2. Recurrence    
    for i in range(1, n):
        for j in range(w+1):
            not_take = 0 + dp[i-1][j]
            take = 0
            if weight[i] <= j:
                # Infinite supply of items - hence stand in same place for take
                take = profit[i] + dp[i][j - weight[i]]

            dp[i][j] = max(not_take, take)
    
    return dp[n-1][w]
