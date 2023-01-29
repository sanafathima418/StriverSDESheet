from os import *
from sys import *
from collections import *
from math import *

def lcs(str1, str2):
    # Approach: DP Tabulation
    # TC: O(N^2) to traverse over 2D array
    # SC: O(N^2) for 2D array

    m = len(str1)
    n = len(str2)

    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    max_len = 0
            
    # 1. Initialization
    # Already done - technically first row and col to be initialized to 0
            
    # 2. Recurrence
    for i in range(1, m+1):
        for j in range(1, n+1):
            # If the indexes match, then go back on both
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                max_len = max(max_len , dp[i][j])
            else:
                # No match so drop the sequence and assign 0
                dp[i][j] = 0 
    
    return max_len
            

