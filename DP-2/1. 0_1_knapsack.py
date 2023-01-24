from os import *
from sys import *
from collections import *
from math import *
import math

## Read input as specified in the question.
## Print output as specified in the question.

def knapsack(n, w, v, max_w):
    # # Approach 1: Recursion - TLE
    # # TC: O(2^N) for 2 possibilities
    # # SC: O(N) for stack space

    # def recur_knapsack(i, curr_w):
    #     if i < 0 or curr_w == 0:
    #         return 0

    #     not_pick = 0 + recur_knapsack(i-1, curr_w)
    #     pick = 0
    #     if w[i] <= curr_w:
    #         pick = v[i] + recur_knapsack(i-1, curr_w - w[i])

    #     return max(not_pick, pick)
        
    # return recur_knapsack(n-1, max_w)

    # # Approach 2: DP Memoization
    # # TC: O(N^2) for traversing 2D array
    # # SC: O(N^2) for 2D array

    # dp = [[-1 for i in range(max_w+1)] for j in range(n+1)]

    # def recur_knapsack(i, curr_w):
    #     if i < 0 or curr_w == 0:
    #         return 0

    #     if dp[i][curr_w] != -1:
    #         return dp[i][curr_w]

    #     not_pick = 0 + recur_knapsack(i-1, curr_w)
    #     pick = 0
    #     if w[i] <= curr_w:
    #         pick = v[i] + recur_knapsack(i-1, curr_w - w[i])

    #     dp[i][curr_w] = max(not_pick, pick)
    #     return dp[i][curr_w]
        
    # return recur_knapsack(n-1, max_w)

    # Approach 3: DP Tabulation
    # TC: O(N^2) for traversing 2D array
    # SC: O(N^2) for 2D array

    dp = [[0 for i in range(max_w+1)] for j in range(n)]

    for i in range(w[0], max_w+1):
        dp[0][i] = v[0]

    for i in range(1, n):
        for j in range(max_w+1):
            not_pick = 0 + dp[i-1][j]
            pick = -math.inf
            if w[i] <= j:
                pick = v[i] + dp[i-1][j - w[i]]

            dp[i][j] = max(not_pick, pick)

    return dp[n-1][max_w]

n_t = int(input())
for i in range(n_t):
    n = int(input())
    w = [int(x) for x in input().split()]
    v = [int(x) for x in input().split()]
    max_w = int(input())

    print(knapsack(n, w, v, max_w))
