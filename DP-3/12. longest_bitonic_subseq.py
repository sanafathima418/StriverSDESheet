from os import *
from sys import *
from collections import *
from math import *

def longestBitonicSequence(arr, n):

    # Approach 1: Same as Approach 4 of LIS, check condition differs
    # TC: O(N^2) + O(N^2) + O(N)
    # SC: O(N) + O(N)
    # Intuition for Bitonic:
    # 1. If first increasing then decreasing
    # 2. Only increasing, no decreasing
    # 3. No Increasing, only decreasing
    
    dp1 = [1] * n
    dp2 = [1] * n

    # 1. Increasing
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and 1 + dp1[j] > dp1[i]:
                dp1[i] = 1 + dp1[j]

    # 2. Decreasing
    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            if arr[j] < arr[i] and 1 + dp2[j] > dp2[i]:
                dp2[i] = 1 + dp2[j]
    
    # 3. length of LBS
    maxi = 0
    for i in range(n):
        maxi = max(maxi, dp1[i] + dp2[i] - 1)
    
    return maxi

