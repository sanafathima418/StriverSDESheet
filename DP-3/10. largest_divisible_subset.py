class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        # Approach 1: Same as Approach 4 of LIS with reconstruct, only change condition > to % and sort before starting
        # TC: O(N^2)
        # SC: O(N)

        # 1. Initialization
        n = len(nums)
        dp = [1] * n # least length of subsequence is (the number itself)
        
        # For Reconstruction
        hashr = [0] * n # array that consists of indexes of lis ending at last_idx
        maxi = 1 # max length of lis
        last_idx = 0 # last index of lis

        nums.sort()
        
        # 2. Recurrence
        for i in range(n):
            hashr[i] = i # points to same index
            for j in range(i):
                if nums[i] % nums[j] == 0 and 1 + dp[j] > dp[i]:
                    # Similar to dp[i] = max(dp[i], 1 + dp[j])
                    dp[i] = 1 + dp[j]
                    hashr[i] = j # update best idx to go back to for recon
            if dp[i] > maxi:
                maxi = dp[i]
                last_idx = i # To get start point of lis(/end point- will be reversed)
        
        # 3. Reconstruction
        lis = []
        lis.append(nums[last_idx])
        while(hashr[last_idx] != last_idx):
            last_idx = hashr[last_idx]
            lis.append(nums[last_idx])

        return lis[::-1]