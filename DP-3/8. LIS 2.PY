class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        
        # Approach 1: DP Tabulation - TLE
        # TC: O(N^2)
        # SC: O(N)
        # Intuition: Same as Approach 1 from LIS
        
        # 1. Initialization
#         n = len(nums)
#         dp = [1]*n # least length of subsequence is (the number itself)
#         max_len = 1
        
#         # 2. Recurrence
#         for i in range(1, n):
#             # 2.1 Check from 1 to n
#             for j in range(i):
#                 # 2.2 Check from 0 to i for numbers lesser than i and update dp[i]
#                 if nums[i] > nums[j] and nums[i] - nums[j] <= k:
#                     # 2.3 Additional condition to check for k
#                     dp[i] = max(dp[i], 1 + dp[j])
#                     max_len = max(max_len, dp[i])
        
#         return max_len
    
        # Approach 2: DP Binary Search also TLE 
        # Approach 3: Use Segment Trees

        






