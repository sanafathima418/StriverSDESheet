class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
#         # Approach 1: Recursion - TLE
#         # TC: O(2^N) for the 2 possibilties of every number
#         # SC: O(N) for stack space
        
#         n = len(nums)
        
#         def recur_target(i, subsum):
#             # 1. Base Case
#             if i < 0:
#                 if subsum == 0:
#                     return 1
#                 else:
#                     return 0
            
#             # 2. Recurrance
#             positive = recur_target(i-1, subsum + nums[i])
#             negative = recur_target(i-1, subsum - nums[i])
            
#             return positive + negative
        
#         return recur_target(n-1, target)
    
        # Approach 2: DP Memoization 
        # TC: O(N^2) for the going over 2D array
        # SC: O(N^2) for the 2D array
        # Keep an eye out for negative target - hence cant use same technique as App 1
        # This problem is same as count partitions with given diff (DP1 - 20)
        
#         def recur_ways(i, subsum):
#             # 1. Base Case
#             if i < 0: 
#                 if subsum == 0: return 1
#                 return 0

#             # 2. DP array check
#             if dp[i][subsum] != -1:
#                 return dp[i][subsum]

#             # 3. Not Take
#             not_take = recur_ways(i-1, subsum)  

#             # 4. Take
#             take = 0
#             if nums[i] <= subsum:
#                 take = recur_ways(i-1, subsum - nums[i]) 

#             # 5. Count Calculate
#             dp[i][subsum] = take + not_take
#             return dp[i][subsum]

#         n = len(nums)
#         total_sum = sum(nums)

#         # Edge Case: If total sum is odd then cannot partition into 2 subsets
#         if target > total_sum or (target - total_sum) % 2:
#             return 0
        
#         # Weird edge case
#         if(target not in range(-1 * total_sum, total_sum + 1) ): return 0

#         # Calculate the value of s1 to satisfy the conditions mentioned
#         # s1 >= s2 is always satisfied
#         s1 = (target + total_sum)//2
#         dp = [[-1 for i in range(s1+1)] for j in range(n)]

#         # Return answer mod thing else will not clear all test cases
#         return recur_ways(n-1,s1)

        # Approach 3 - DP Tabulation
        # TC: O(N^2) for going over array
        # SC: O(N^2) for dp array
    
        n = len(nums)
        total_sum = sum(nums)

        # Edge Case: If total sum is odd then cannot partition into 2 subsets
        if target > total_sum or (target - total_sum) % 2:
            return 0

        # Weird edge case
        if(target not in range(-1 * total_sum, total_sum + 1) ): return 0

        # Calculate the value of s1 to satisfy the conditions mentioned
        # s1 >= s2 is always satisfied
        s1 = (target + total_sum) // 2
        dp = [[0 for i in range(s1+1)] for j in range(n)]

        # 1. Initialization
        # If sum is 0, then 1 way to achieved desired sum so set to 1
        for i in range(n):
            dp[i][0] = 1

        # If 1st element less than or equal to desired sum, then set the column of achieving that sum using the 1st number
        if nums[0] <= s1:
            dp[0][nums[0]] = 1

        # This is some unique stuff - picked from YT comments but works
        # It probably means if the 1st number is 0 then there are two ways of picking 0, i.e, taking or not taking
        if(nums[0] == 0): dp[0][0] = 2

        # 2. Recurrence
        for i in range(1,n):
            for j in range(s1+1):
                # 3. Not Take
                not_take = dp[i-1][j]  

                # 4. Take
                take = 0
                if nums[i] <= j:
                    take = dp[i-1][j - nums[i]]  

                # 5. Count Calculate
                dp[i][j] = take + not_take

        return dp[n-1][s1]
            

        
