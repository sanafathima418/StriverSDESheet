class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # Approach 1: Same as Approach 4 of LIS
        # TC: O(N^2)
        # SC: O(N)
        # Intuition:

        n = len(nums)
        # 1. Initialization
        dp = [1] * n
        count = [1] * n # count array with count[i] indicating max possible lis from 0-i
        maxi = 1

        # 2. Recurrence
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    # 2.1 If a new element added to lis, then propagate the count as this length is seen for the first time
                    count[i] = count[j]
                elif nums[i] > nums[j] and 1 + dp[j] == dp[i]:
                    # 2.2 If equal, it means the current i is being hit twice so add up the count and assign to current
                    count[i] += count[j]
            maxi = max(maxi, dp[i])

        # 3. Sum up all numbers in count with max_len lis as this is the number of lis
        max_lis = 0
        for i in range(n):
            if dp[i] == maxi:
                max_lis += count[i]
        return max_lis

        