from os import *
from sys import *
from collections import *
from math import *

from typing import *

# Problem Link : https://atcoder.jp/contests/dp/tasks/dp_b (Code not there)
  
def frogJump(n: int, heights: List[int], k: int) -> int:
    
#     # Approach 1: Recursion, lead to TLE
#     # TC: O(k^N) for traversing left and right subtrees
#     # SC: O(N) for stack space
    
    # def recur_frog(i):
    #     # 1. Base Case
    #     if i == 0:
    #         return 0

    #     min_energy = -math.inf
    #     # 2. Inductive Case
    #     for j in range(1, k+1):
    #         if (j-i) >= 0:
    #             jump = recur_frog(j-i) + abs(heights[i] - heights[i-j]) 
    #             min_energy = min(min_energy, jump)
    #     return min_energy
        
    # return recur_frog(n-1)

#     # Approach 2: DP Memoization
#     # TC: O(N) for checking all steps on staircase
#     # SC: O(N) for dp array

    # dp_array = [-1] * n
    
    # def recur_frog(i):
    #     # 1. Base Case
    #     if i == 0:
    #         return 0

    #     # 2. Inductive Case
    #     # 2.1 Check if subproblem already solved
    #     if dp_array[i] != -1:
    #         return dp_array[i]

    #     # 2.2 Solve subproblem is not solved and update dp array
    #     min_energy = -math.inf
    #     for j in range(1, k+1):
    #         if (j-i) >= 0:
    #             jump = recur_frog(j-i) + abs(heights[i] - heights[i-j]) 
    #             min_energy = min(min_energy, jump)
    #     
    #     dp_array[i] =  min_energy
    #     return dp_array[i]
    
    # return recur_frog(n-1)
    
    # Approach 3: DP Tabulation
    # TC: O(N) for checking all steps on staircase
    # SC: O(N) for dp array
    
        dp_array = [0]*n
        # 1. Base Case
        if n == 0:
            return 0
        
        dp_array[0] = 0
            
        # 2.2 Solve subproblem is not solved and update dp array
        for i in range(1, n):
            min_energy = -math.inf
            for j in range(1, k+1):
                if (j-i) >= 0:
                    jump = dp_array[j-i] + abs(heights[i] - heights[i-j]) 
                    min_energy = min(min_energy, jump)
            
            dp_array[i] =  min_energy
        
        return dp_array[-1]

    # Approach 4: DP Tabulation Space Optimization
    # TC: O(N) for checking all steps on staircase
    # SC: O(k) for dp array
    # Maintain a linked list of size k,
    # for every movement of a window delete first element and append curr element to end of list
