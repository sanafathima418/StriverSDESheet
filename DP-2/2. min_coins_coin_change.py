from os import *
from sys import *
from collections import *
from math import *
import math

from typing import List

def minimumElements(num: List[int], x: int) -> int:
    # Greedy Fails as no uniformity - should work similar to fractional knapsack
    # For test case {9,6,5,1} and tar 11, greedy fails as it finds min coins to be 
    # 3(9+1+1) while the expected answer is 2(6+5)
    # Concept of uniformity: difference between adjacent elements forming some order/equal

    # Approach 1: Recursion - TLE
    # TC: >>> O(2^N) Just exponential cause we can stand in same place for take
    # SC: O(N) for stack space
    # Intuition: Take stands at same index for infinity supply/ multiply use 
    # (to consider all possbilities of taking a particular coin) 
    # - instead of taking the max possible value of selecting the current coin

    # def recur_mincoins(i, x):
    #     # 1. Base Case
    #     if i == 0:
    #         if not x % num[0]:
    #             return x // num[0]
    #         return math.inf
        
    #     # 2. Recurrance
    #     # For not take, move back
    #     not_take = 0 + recur_mincoins(i-1, x)
    #     take = math.inf
    #     if num[i] <= x:
    #         # Stand at same index
    #         # Take one coin at a time so add 1 to recursion 
    #         take =  1 + recur_mincoins(i, x - num[i])

    #     # 3. Final Computation
    #     return min(take, not_take)
    
    # # If not possible to achieve target sum with the current denominations, return -1
    # ans = recur_mincoins(len(num)-1, x)
    # if ans >= math.inf:
    #     return -1
    # return ans

    # # Approach 2: DP Memoization
    # # TC:  O(N^2) for going over 2D array
    # # SC: O(N^2) for 2D array + O(N) for stack space
    
    # n = len(num)
    # dp = [[-1 for i in range(x+1)] for j in range(n)]

    # def recur_mincoins(i, x):
    #     # 1. Base Case
    #     if i == 0:
    #         if not x % num[0]:
    #             return x // num[0]
    #         return math.inf
        
    #     if dp[i][x] != -1:
    #         return dp[i][x]
        
    #     # 2. Recurrance
    #     # For not take, move back
    #     not_take = 0 + recur_mincoins(i-1, x)
    #     take = math.inf
    #     if num[i] <= x:
    #         # Stand at same index
    #         # Take one coin at a time so add 1 to recursion 
    #         take =  1 + recur_mincoins(i, x - num[i])

    #     # 3. Final Computation
    #     dp[i][x] = min(take, not_take)
    #     return dp[i][x]

    # # If not possible to achieve target sum with the current denominations, return -1
    # ans = recur_mincoins(n-1, x)
    # if ans >= math.inf:
    #     return -1
    # return ans

    # Approach 2: DP Tabulation
    # TC:  O(N^2) for going over 2D array
    # SC: O(N^2) for 2D array 
    
    n = len(num)
    dp = [[0 for i in range(x+1)] for j in range(n)]
    
    # 1. Base Case
    for j in range(x+1):
        if not j % num[0]:
            dp[0][j] = j // num[0]
        else:
            dp[0][j] = math.inf

    for i in range(1, n):
        for j in range(x+1):
            # 2. Recurrance
            not_take = 0 + dp[i-1][j]
            take = math.inf
            if num[i] <= j:
                # Stand at same index
                # Take one coin at a time so add 1 to recursion 
                take =  1 + dp[i][j - num[i]]

            # 3. Final Computation
            dp[i][j] = min(take, not_take)

    # If not possible to achieve target sum with the current denominations, return -1
    ans = dp[n-1][x]
    if ans >= math.inf:
        return -1
    return ans
            



