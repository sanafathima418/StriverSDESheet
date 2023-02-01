from os import *
from sys import *
from collections import *
from math import *

def canYouMake(s: str, p: str) -> int:

    # # Approach 1: Recursion - TLE
    # # TC: >> O(2^N)
    # # SC: O(N)
    # # Intuition: Same as LCS except for final return 

    # m = len(s)
    # n = len(p)

    # def recur_palin(i, j):
    #     if i < 0 or j < 0:
    #         return 0
        
    #     if s[i] == p[j]:
    #         return 1 + recur_palin(i-1, j-1)
    #     else:
    #         return max(recur_palin(i-1, j), recur_palin(i, j-1))

    # # Add both strings and subtract 2 times the lowest common substring
    # return (m + n) - (2 * recur_palin(m-1, n-1))

    # # Approach 2: DP Memoization
    # # TC: O(N^2)
    # # SC: O(N^2)
    # # Intuition: Same as LCS except for final return 

    # m = len(s)
    # n = len(p)

    # dp = [[-1 for i in range(n)] for j in range(m)]

    # def recur_palin(i, j):
    #     if i < 0 or j < 0:
    #         return 0
        
    #     if dp[i][j] != -1:
    #         return dp[i][j]
        
    #     if s[i] == p[j]:
    #         dp[i][j] = 1 + recur_palin(i-1, j-1)
    #     else:
    #         dp[i][j] = max(recur_palin(i-1, j), recur_palin(i, j-1))
        
    #     return dp[i][j]

    # # Add both strings and subtract 2 times the lowest common substring
    # return (m + n) - (2 * recur_palin(m-1, n-1))
    
    # Approach 3: DP Tabulation
    # TC: O(N^2)
    # SC: O(N^2)
    # Intuition: Same as LCS except for final return 

    m = len(s)
    n = len(p)

    dp = [[0 for i in range(n+1)] for j in range(m+1)]

    # 1. Initialization
    # Already handled in L63
    
    # 2. Recurrence
    for i in range(1, m+1):
        for j in range(1, n+1):    
            if s[i-1] == p[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Add both strings and subtract 2 times the lowest common substring
    return (m + n) - (2 * dp[m][n])