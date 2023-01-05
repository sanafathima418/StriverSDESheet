from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

def maximumNonAdjacentSum(nums):  
#     # Approach 1: Recursion TLE
#     # TC: 0(2^N)
#     # SC: O(N) 
#     def recur_nums(i):
#         # 1. Base Case
#         if i == 0:
#             return nums[i]
#         if i < 0:
#             return 0
#         
#         # 2. Inductive Case
#         # 2.1 If going to pick then go back 2 steps
#         pick = nums[i] + recur_nums(i-2)
#         # 2.2 If not going to pick then go back 1 step
#         not_pick = 0 + recur_nums(i-1)
#         # 2.3 return max
#         return max(pick, not_pick)
    
#     return recur_nums(len(nums)-1)
    
#     # Approach 2: DP Memoization
#     # TC: 0(N) for going over array
#     # SC: O(N) for recursion + O(N) for dp array
#     def recur_nums(i):
#         # 1. Base Case
#         if i == 0:
#             return nums[i]
#         if i < 0:
#             return 0
        
#         # 2. Memoization Check
#         if dp_array[i] != -1:
#             return dp_array[i]
        
#         # 3. Inductive Case
#         pick = nums[i] + recur_nums(i-2)
#         not_pick = 0 + recur_nums(i-1)
        
#         dp_array[i] = max(pick, not_pick)
#         return dp_array[i]
    
#     dp_array = [-1] * len(nums)
#     return recur_nums(len(nums)-1)

    # Approach 3: DP Tabulation
    # TC: 0(N) for going over array
    # SC: O(N) for dp array
        
        # 1. Initialization
        n = len(nums)
        dp_array = [0] * n
        # 1.1 Base Case
        dp_array[0] = nums[0]
        
        # 3. Recurrence - Traverse from 1-n as 0 is base case
        for i in range(1, n):
            # 3.1 Pick is always the number
            pick = nums[i]
            if i > 1:
                # 3.2 Go back only if index exists to make sure no negative indices happen
                pick += dp_array[i-2]
            not_pick = 0 + dp_array[i-1]
            dp_array[i] = max(pick, not_pick)
        
        # 4. Return max sum available in last position of dp array
        return dp_array[-1]

    # Approach 4: DP Tabulation - Space Optimization
    # TC: 0(N) for going over array
    # SC: O(1) for curr, prev1 and prev2 
    # Can be done!

# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1