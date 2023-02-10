class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Approach 1: Recursion - TLE
        # TC: O(2^N)
        # SC: O(N)
        # Intuition: f(i, prev) means by taking index at prev and i when i>prev, max length of taking and not taking i
        
        # n = len(nums) 

        # def recur_lis(i, prev):
        #     # 1. Base Case, no more elements so 0
        #     if i == n:
        #         return 0

        #     # 2. Recurrence
        #     # not take
        #     not_take = 0 + recur_lis(i+1, prev)

        #     # take
        #     take = 0
        #     # 2.1 If no element taken earlier or current is greater than previous, take and add 1
        #     if prev == -1 or nums[i] > nums[prev]:
        #         take = 1 + recur_lis(i+1, i)

        #     return max(take, not_take)

        # return recur_lis(0, -1)

        # Approach 2: DP Memoization - TLE (huge inputs)
        # TC: O(N^2)
        # SC: O(N^2)
        # Intuition: f(i, prev) means by taking index at prev and i when i>prev, max length of taking and not taking i
        
        # n = len(nums) 
        # dp = [[-1 for i in range(n+1)] for j in range(n)]

        # def recur_lis(i, prev):
        #     # 1. Base Case
        #     if i == n:
        #         return 0

        #     if dp[i][prev+1] != -1:
        #         return dp[i][prev+1]

        #     # 2. Recurrence
        #     # not take
        #     not_take = 0 + recur_lis(i+1, prev)

        #     # take
        #     take = 0
        #     if prev == -1 or nums[i] > nums[prev]:
        #         take = 1 + recur_lis(i+1, i)

        #     dp[i][prev+1] = max(take, not_take)
        #     return dp[i][prev+1]

        # return recur_lis(0, -1)

        # Approach 3: DP Tabultion - TLE
        # TC: O(N^2)
        # SC: O(N^2)
        # Intuition: f(i, prev) means by taking index at prev and i when i>prev, max length of taking and not taking i
        
        # n = len(nums) 
        # dp = [[0 for i in range(n+1)] for j in range(n+1)]
        # # 1. Initialization
        # dp[n-1][n] = 0

        # # 2. Recurrence
        # for i in range(n-1, -1, -1):
        #     for j in range(i-1, -2, -1):
        #         # not take
        #         not_take = 0 + dp[i+1][j+1]

        #         # take
        #         take = 0
        #         if j == -1 or nums[i] > nums[j]:
        #             take = 1 + dp[i+1][i+1]

        #         dp[i][j+1] = max(take, not_take)

        # return dp[0][0]

        # Leetcode Alternate Approach - not very intuitive
        # Approach 4: DP Tabulation + Recontruction
        # TC: O(N^2)
        # SC: O(N)
        # Intuition: f(i) - max length of substring from 0-i
        # This approach works here cause max length of input is 2500
        # Same doesn't for LIS 2 as the limit is 10^5
        
        # 1. Initialization
        # n = len(nums)
        # dp = [1] * n # least length of subsequence is (the number itself)
        
        # # For Reconstruction
        # hashr = [0] * n # array that consists of indexes of lis ending at last_idx
        # maxi = 1 # max length of lis
        # last_idx = 0 # last index of lis
        
        # # 2. Recurrence
        # for i in range(n):
        #     hashr[i] = i # points to same index
        #     for j in range(i):
        #         if nums[i] > nums[j] and 1 + dp[j] > dp[i]:
        #             # Similar to dp[i] = max(dp[i], 1 + dp[j])
        #             dp[i] = 1 + dp[j]
        #             hashr[i] = j # update best idx to go back to for recon
        #     if dp[i] > maxi:
        #         maxi = dp[i]
        #         last_idx = i # To get start point of lis(/end point- will be reversed)
        
        # # 3. Reconstruction
        # lis = []
        # lis.append(nums[last_idx])
        # while(hashr[last_idx] != last_idx):
        #     last_idx = hashr[last_idx]
        #     lis.append(nums[last_idx])
        # print(lis[::-1])
        # return max(dp)
    
        # Approach 5: Slightly better way of building subsequence (not DP) - Linear Search
        # TC: O(N^2)
        # SC: O(N)
        
        # # 1. Initialization
        # subseq = [nums[0]] 
        # n = len(nums)
        
        # # 2. Recurrence
        # for i in range(1, n):
        #     # 2.1 If current element is greater than element seen at end of subseq, append it 
        #     if nums[i] > subseq[-1]:
        #         subseq.append(nums[i])
        #     else:
        #         # 2.2 If it is lesser than last element seen, then find where in the subsequence it would fit
        #         # Could also end up fitting at start of subseq
        #         j = 0
        #         while(nums[i] > subseq[j]):
        #             j += 1
        #         subseq[j] = nums[i]
        
        # return len(subseq)
    
        # Approach 6: Use Binary Search to look for place to fit this number in else: V IMP
        # TC: O(NLOGN)
        # SC: O(N)  

        # 1. Initialization
        subseq = [nums[0]] 
        n = len(nums)

        def lower_bound(b, e, x):
            # Binary Search instead of Linear Search
            # 1. if x in array then return its index
            # 2. if not there then return the first index after x
            while(b < e):
                m = (b + e) // 2
                if x <= subseq[m]:
                    e = m
                else:
                    b = m + 1
            return b
        
        # 2. Recurrence
        for i in range(1, n):
            # 2.1 If current element is greater than element seen at end of subseq, append it 
            if nums[i] > subseq[-1]:
                subseq.append(nums[i])
            else:
                # 2.2 If it is lesser than last element seen, then find where in the subsequence it would fit
                # This is done using lower bound function
                j = lower_bound(0, len(subseq), nums[i]) - 0 # search start at 0 and end at end of subseq
                subseq[j] = nums[i]
        
        return len(subseq)
            
        
    
    
    

            