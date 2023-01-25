class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Approach: Array Traversal to find minima and maxima in one pass such that maxima occurs after minima
        # TC: O(N)
        # SC: O(1)
        # Kadane's Algorithm
        
        # Store maxima, minima and profit
        max_min_set = [prices[0]]*2
        profit = 0
        
        # Traverse over prices array
        for i in range(1,len(prices)):
            if prices[i] < max_min_set[0]:
                # 1. If minima, update max and min
                 max_min_set = [prices[i]]*2
            elif prices[i] > max_min_set[1]:
                # 2. If current price is greater than max, update only max
                max_min_set[1] = prices[i]
            # Update profit nonetheless
            profit = max(profit, max_min_set[1] - max_min_set[0])
        
        return profit