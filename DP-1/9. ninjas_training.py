from typing import *
  
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    
#     # Approach 1: Top Down Recursion - TLE
#     # TC: O(3^N) as there are 2-3 possibilities for each recursion step
#     # SC: O(1) as no extra space
    
#     def recur_ninjas(i, prev_act):
#         # 1. Base Case
#         if i == n:
#             return 0
        
#         # 2. Inductive Case: Traverse over 3 possibilities
#         l_energy = 0
#         for j in range(3):
#             if j == prev_act:
#                 # 2.1 If same as prev act, skip
#                 continue
#             # Compare against previous values of same parent
#             # Important to add here
#             l_energy = max(l_energy, recur_ninjas(i+1, j) + points[i][j])
#         return l_energy
    
#     return recur_ninjas(0,-1)

#     # Approach 2: DP Memoization
#     # TC: O(N^3) as there are 2-3 possibilities for each recursion step
#     # SC: O(N^2) for dp array
    
#     dp = [[-1]*3 for i in range(n)]
    
#     def recur_ninjas(i, prev_act):
#         # 1. Base Case
#         if i == n:
#             print("return")
#             return 0
#         print(i, prev_act)
#         if dp[i][prev_act] != -1:
#             # 2.2 Check if entry exists in dp array
#             return dp[i][prev_act]
        
#         # 2. Inductive Case: Traverse over 3 possibilities
#         l_energy = 0
#         for j in range(3):
#             if j == prev_act:
#                 # 2.1 If same as prev act, skip
#                 continue
                
#             # 2.2 Compare against previous values of same parent
#             # Important to add here as you take current day and go down
#             l_energy = max(l_energy, recur_ninjas(i+1, j) + points[i][j])
        
#         dp[i][prev_act] = l_energy
#         return l_energy
    
#     return recur_ninjas(0,-1)

    # Approach 3: DP Tabulation - Bottom up
    # TC: O(N^3) as there are 2-3 possibilities for each recursion step
    # SC: O(N^2) for dp array
    
    # 1. Base Case
    dp = [[0]*3 for _ in range(n)]
    dp[0][0], dp[0][1], dp[0][2] = points[0][0], points[0][1], points[0][2]
    
    # 2. Inductive Case: Traverse over all days
    for i in range(1, n):
        # 2.1 Traverse over 3 possibilities of activities for current activity
        for j in range(3):
            # 2.2 Traverse over 3 possibilities of previous activities
            for k in range(3):
                if j == k:
                    # 2.3 If same as prev act, skip
                    continue
                dp[i][j] = max(dp[i][j], dp[i-1][k] + points[i][j])
     
    # 3. Get max of last row
    return max(dp[-1])


        
