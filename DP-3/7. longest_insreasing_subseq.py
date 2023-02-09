class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Approach: DP Tabulation
        # TC: O(N^2)
        # SC: O(N)
        # Intuition: f(i) - max length of substring from 0-i
        
#         # 1. Initialization
#         n = len(nums)
#         dp = [1]*n # least length of subsequence is (the number itself)
        
#         # 2. Recurrence
#         for i in range(1, n):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], 1 + dp[j])

#         return max(dp)
    
        # Approach: Slightly better way of building subsequence (not DP) which allows reconstruction
        # TC: O(N^2)
        # SC: O(N)
        
        # 1. Initialization
        subseq = [nums[0]] 
        n = len(nums)
        
        # 2. Recurrence
        for i in range(1, n):
            # 2.1 If current element is greater than element seen at end of subseq, append it 
            if nums[i] > subseq[-1]:
                subseq.append(nums[i])
            else:
                # 2.2 If it is lesser than last element seen, then find where in the subsequence it would fit
                # Could also end up fitting at start of subseq
                j = 0
                while(nums[i] > subseq[j]):
                    j += 1
                subseq[j] = nums[i]
        
        return len(subseq)
    
        # Approach 3 : Use Binary Search to look for place to fit this number in else
                    
            
        
    
    
    

            