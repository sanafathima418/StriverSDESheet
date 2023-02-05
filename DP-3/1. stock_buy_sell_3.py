class Solution:
    def maxProfit(self, prices: List[int]) -> int:       
        
        # Approach: Recursion - TLE
        # TC: O(2^N)
        # SC: O(1)
        # Do not think like stock 1 and 2 probs of comparing current day price
        # Intuition: 4 transaction possible in total
        # In a day, can buy, sell or rest
        
#         n = len(prices)
        
#         def recur_profit(i, max_t):
#             # 1. Base Case
#             # 1.1 If array traversed
#             if i == n:
#                 return 0
            
#             # 1.2 If 2 buy and 2 sell done
#             if max_t == 0:
#                 return 0
            
#             # 2. Recurrence
#             # 2.1 Rest - Don't do anything for the day
#             not_take = recur_profit(i+1, max_t)
            
#             # 2.2 Buy or Sell on that day
#             take = 0
#             # 2.2.1 Can buy only if nothing bought i.e transaction after 0 or 2
#             if not max_t % 2:
#                 # Buy - will need to find sell price so current day price is subtracted (sell-buy)
#                 take = -prices[i] + recur_profit(i+1, max_t - 1)
#             else:
#                 # Sell
#                 take = prices[i] + recur_profit(i+1, max_t - 1)
            
#             return max(not_take, take)
                
#         return recur_profit(0, 4)
    
#         # Approach: DP Memoization
#         # TC: O(N^2)
#         # SC: O(1)
        
#         n = len(prices)
#         dp = [[-1 for i in range(5)] for j in range(n)]
        
#         def recur_profit(i, max_t):
#             # 1. Base Case
#             # 1.1 If array traversed
#             if i == n:
#                 return 0
            
#             # 1.2 If 2 buy and 2 sell done
#             if max_t == 0:
#                 return 0
            
#             if dp[i][max_t] != -1:
#                 return dp[i][max_t]
            
#             # 2. Recurrence
#             # 2.1 Rest - Don't do anything for the day
#             not_take = recur_profit(i+1, max_t)
            
#             # 2.2 Buy or Sell on that day
#             take = 0
#             # 2.2.1 Can buy only if nothing bought i.e transaction after 0 or 2
#             if not max_t % 2:
#                 # Buy - will need to find sell price so current day price is subtracted (sell-buy)
#                 take = -prices[i] + recur_profit(i+1, max_t - 1)
#             else:
#                 # Sell
#                 take = prices[i] + recur_profit(i+1, max_t - 1)
            
#             dp[i][max_t] = max(not_take, take)
#             return dp[i][max_t]
                
#         return recur_profit(0, 4)

        # Approach: DP Tabulation
        # TC: O(N)
        # SC: O(1)
        
        n = len(prices)
        dp = [[0 for i in range(5)] for j in range(n+1)]
        
        # Going to start working from top right corner
        for i in range(n-1, -1, -1):
            for j in range(1,5):
                # 2. Recurrence
                # 2.1 Rest - Don't do anything for the day
                not_take = dp[i+1][j]

                # 2.2 Buy or Sell on that day
                take = 0
                # 2.2.1 Can buy only if nothing bought i.e transaction after 0 or 2
                if not j % 2:
                    # Buy - will need to find sell price so current day price is subtracted (sell-buy)
                    take = -prices[i] + dp[i+1][j-1]
                else:
                    # Sell
                    take = prices[i] + dp[i+1][j-1]

                dp[i][j] = max(not_take, take)
        
        return dp[0][4]

        