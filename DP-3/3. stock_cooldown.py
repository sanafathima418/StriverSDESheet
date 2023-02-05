class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Approach: Recursion - TLE
        # TC: O(2^N)
        # SC: O(1)
        # Same as buy sell 3, but add a variable indicating whether or not you can buy on a day
        
#         n = len(prices)
        
#         def recur_profit(i, buy):
#             # 1. Base Case
#             # 1.1 If array traversed
#             if i == n:
#                 return 0
            
#             # 2. Recurrence
#             # 2.1 Rest - Don't do anything for the day
#             not_take = recur_profit(i+1, buy)
            
#             # 2.2 Buy or Sell on that day
#             take = 0
#             # 2.2.1 Can buy only if nothing bought i.e transaction after 0 or k
#             if buy:
#                 # Buy - will need to find sell price so current day price is subtracted (sell-buy)
#                 take = -prices[i] + recur_profit(i+1, 0)
#             else:
#                 # Sell - after sell, move date by 2
#                 take = prices[i] + recur_profit(i+2, 1)
            
#             return max(not_take, take)
        
#          # 3. Can buy on 0th day
#          return recur_profit(0, 1)
    
#         # Approach: DP Memoization
#         # TC: O(N^2)
#         # SC: O(N^2)
        
#         n = len(prices)
#         dp = [[-1 for i in range(2)] for j in range(n+2)]
        
#         def recur_profit(i, buy):
#             # 1. Base Case
#             # 1.1 If array traversed
#             if i >= n:
#                 return 0
            
#             if dp[i][buy] != -1:
#                 return dp[i][buy]
            
#             # 2. Recurrence
#             # 2.1 Rest - Don't do anything for the day
#             not_take = recur_profit(i+1, buy)
            
#             # 2.2 Buy or Sell on that day
#             take = 0
#             # 2.2.1 Can buy only if nothing bought i.e transaction after 0 or 2
#             if buy:
#                 # Buy - will need to find sell price so current day price is subtracted (sell-buy)
#                 take = -prices[i] + recur_profit(i+1, 0)
#             else:
#                  # Sell - after sell, move date by 2
#                 take = prices[i] + recur_profit(i+2, 1)
            
#             dp[i][buy] = max(not_take, take)
#             return dp[i][buy]
                
#         return recur_profit(0, 1)

#        # Approach: DP Tabulation
#         # SC: O(N^2)
#         # SC: O(N^2)
        
        n = len(prices)
        dp = [[0 for i in range(2)] for j in range(n+2)]
        
        # Going to start working from last day
        for i in range(n-1, -1, -1):
            for j in range(2):
                # 2. Recurrence
                # 2.1 Rest - Don't do anything for the day
                not_take = dp[i+1][j]

                # 2.2 Buy or Sell on that day
                take = 0
                # 2.2.1 Can buy only if nothing bought i.e transaction after 0 or 2
                if j:
                    # Buy - will need to find sell price so current day price is subtracted (sell-buy)
                    take = -prices[i] + dp[i+1][0]
                else:
                    # Sell
                    take = prices[i] + dp[i+2][1]

                dp[i][j] = max(not_take, take)
        
        return dp[0][1]

            