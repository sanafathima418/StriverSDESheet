class Solution:
    def change(self, x: int, num: List[int]) -> int:
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

#         def recur_mincoins(i, x):
#             # 1. Base Case
#             if i == 0:
#                 if not x % num[0]:
#                     return 1
#                 return 0

#             # 2. Recurrance
#             # For not take, move back
#             not_take = recur_mincoins(i-1, x)
#             take = 0
#             if num[i] <= x:
#                 # Stand at same index
#                 take =  recur_mincoins(i, x - num[i])

#             # 3. Final Computation
#             return take + not_take

#         return recur_mincoins(len(num)-1, x)


            # # Approach 2: DP Memoization
            # # TC:  O(N^2) for going over 2D array
            # # SC: O(N^2) for 2D array + O(N) for stack space
    
#         n = len(num)
#         dp = [[-1 for i in range(x+1)] for j in range(n)]

#         def recur_mincoins(i, x):
#             # 1. Base Case
#             if i == 0:
#                 if not x % num[0]:
#                     return 1
#                 return 0

#             if dp[i][x] != -1:
#                 return dp[i][x]

#             # 2. Recurrance
#             # For not take, move back
#             not_take = recur_mincoins(i-1, x)
#             take = 0
#             if num[i] <= x:
#                 # Stand at same index
#                 take =  recur_mincoins(i, x - num[i])

#             # 3. Final Computation
#             dp[i][x] = take + not_take
#             return dp[i][x]

#         return recur_mincoins(n-1, x)

            # Approach 2: DP Tabulation
            # TC:  O(N^2) for going over 2D array
            # SC: O(N^2) for 2D array 
    
            n = len(num)
            dp = [[0 for i in range(x+1)] for j in range(n)]

            # 1. Base Case
            for j in range(x+1):
                if not j % num[0]:
                    dp[0][j] = 1
                else:
                    dp[0][j] = 0

            for i in range(1, n):
                for j in range(x+1):
                    # 2. Recurrance
                    not_take = dp[i-1][j]
                    take = 0
                    if num[i] <= j:
                        # Stand at same index
                        take =  dp[i][j - num[i]]

                    # 3. Final Computation
                    dp[i][j] = take + not_take

                    
            return dp[n-1][x]

            



