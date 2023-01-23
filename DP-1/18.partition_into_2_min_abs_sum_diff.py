from os import *
from sys import *
from collections import *
from math import *
import math

from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10 ** 7)

def minSubsetSumDifference(arr, n):
        # Approach 3: DP Tabulation - Bottom up - taken from prob 17.
        # TC: O(k*N) for calcuating all index and subsum pairs
        # SC: O(k*N) for dp array
        
        def tabul_subset_sums(n,k):
            
            dp = [[False for i in range(k+1)] for j in range(n)]

            # 1. Initialization
           # 1.1 If target is 0, set true (subsum achieved) - if a sequence gets here it means it a valid one as per Appr 2
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
                    dp[i][j] = max(not_take, take) 

            # 3. Return last element of array which indicates if a subset with all elements can sum to k
            return dp

        k = sum(arr)
        
        dp = tabul_subset_sums(len(arr),k)
        min_abs = math.inf
        
        # Go over success subsums of last row in dp array and calculate minima
        for i, val in enumerate(dp[n-1]):
            if val:
                s1 = i
                s2 = k - i
                min_abs = min(min_abs, abs(s1-s2))
        
        return min_abs











# Taking input using fast I/0.
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return N, arr


tc = int(input())
while tc > 0:
    N, arr = takeInput()
    ans = minSubsetSumDifference(arr, N)
    stdout.write(str(ans) + "\n")
    tc -= 1
