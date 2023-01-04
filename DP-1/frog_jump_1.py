from os import *
from sys import *
from collections import *
from math import *

from typing import *

# Problem Link : https://www.codingninjas.com/codestudio/problems/frog-jump_3621012
  
def frogJump(n: int, heights: List[int]) -> int:
    
#     # Approach 1: Recursion, lead to TLE
#     # TC: O(2^N) for traversing left and right subtrees
#     # SC: O(N) for stack space
    
#     def recur_frog(i):
#         # 1. Base Case
#         if i == 0:
#             return 0
        
#         # 2. Inductive Case
#         left = recur_frog(i-1) + abs(heights[i] - heights[i-1]) 
#         if i > 1:
#             # Right jump only possible if i is more than 1
#             right = recur_frog(i-2) + abs(heights[i] - heights[i-2]) 
#             return min(left,right)
#         return left
        
#     return recur_frog(n-1)

#     # Approach 2: DP Memoization
#     # TC: O(N) for checking all steps on staircase
#     # SC: O(N) for dp array
    
#     def recur_frog(i, dp_array):
#         # 1. Base Case
#         if i == 0:
#             return 0
        
#         # 2. Inductive Case
#         # 2.1 Check if subproblem already solved
#         if dp_array[i] != -1:
#             return dp_array[i]
        
#         # 2.2 Solve subproblem is not solved and update dp array
#         left = recur_frog(i-1, dp_array) + abs(heights[i] - heights[i-1]) 
#         if i > 1:
#             # Right jump only possible if i is more than 1
#             right = recur_frog(i-2, dp_array) + abs(heights[i] - heights[i-2]) 
#             dp_array[i] = min(left,right)
#         else:
#             dp_array[i] = left
#         return dp_array[i]
   
#     return recur_frog(n-1,[-1]*n)
    
#     # Approach 3: DP Tabulation
#     # TC: O(N) for checking all steps on staircase
#     # SC: O(N) for dp array
    
#     dp_array = [0]*n
#     # 1. Base Case
#     if n == 0:
#         return 0
        
#     # 2. Inductive Case: Traverse over other cases
#     for i in range(1,n):
#         left = dp_array[i-1] + abs(heights[i] - heights[i-1]) 
#         if i > 1:
#             right = dp_array[i-2] + abs(heights[i] - heights[i-2]) 
#             dp_array[i] = min(left,right)
#         else:
#             dp_array[i] = left
   
#     return dp_array[-1]

    # Approach 4: DP Tabulation Space Optimization
    # TC: O(N) for checking all steps on staircase
    # SC: O(N) for dp array
    
    # 1. Base Case
    if n == 0:
        return 0
    curr = 0
    prev1 = 0 # dont use left and right here instead as left and right are different from prev values as only one of them is taken
    prev2 = 0
        
    # 2. Inductive Case: Traverse over other cases
    for i in range(1,n):
        left = prev1 + abs(heights[i] - heights[i-1]) 
        if i > 1:
            right = prev2 + abs(heights[i] - heights[i-2]) 
            curr = min(left,right)
        else:
            curr = left
        prev2 = prev1
        prev1 = curr
   
    return curr