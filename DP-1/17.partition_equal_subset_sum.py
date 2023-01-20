class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Approach 1: Backtracking- Take, not take - TLE
        # TC:O(2^N) for 2 possibilities
        # SC: O(N) for stack space
        # Good test case to think over - [2,2,3,9]
    
#         n = len(nums)
        
#         def recur_subsum(i, subsum):

#              # 1. Base Case 
#             if subsum == 0:
#                 return 1

#             if i == 0:
#                 return (nums[0] == subsum)

#             # 2. Not Take 
#             not_take = recur_subsum(i-1, subsum)

#             # 3. Take 
#             take = False
#             if nums[i] <= subsum: 
#                 take = recur_subsum(i-1, subsum - nums[i])

#             # 4. if either is true return true, else false
#             return not_take or take

#         # Total sum is odd and hence array cant be split
#         k = sum(nums)
#         if k % 2:
#             return False # odd sum cant be split

#         # If even set out to find the subset
#         return recur_subsum(n-1, k/2)
        
#         # Approach 2: DP Memoization 
#         # TC: O(k*N) for calcuating all index and subsum pairs
#         # SC: O(k*N) for dp array + O(N) for stack space
        
#         n = len(nums)
        
#         # Total sum is odd and hence array cant be split
#         k = sum(nums)
#         if k % 2:
#             return False # odd sum cant be split
        
#         # DP array for storing previous computations of an index and subsum pair
#         dp = [[-1 for i in range(k+1)] for j in range(n)]
        
#         def recur_subsum(i, subsum):

#              # 1. Base Case 
#             if subsum == 0:
#                 return 1

#             if i == 0:
#                 return (nums[0] == subsum)
            
#             # 2. DP array check
#             if dp[i][subsum] != -1:
#                 return dp[i][subsum]

#             # 3. Not Take 
#             not_take = recur_subsum(i-1, subsum)

#             # 4. Take 
#             take = False
#             if nums[i] <= subsum: 
#                 take = recur_subsum(i-1, subsum - nums[i])

#             # 5. if either is true return true, else false
#             dp[i][subsum] = not_take or take
#             return dp[i][subsum]

#         # If even set out to find the subset
#         return recur_subsum(n-1, int(k/2))

        # Approach 3: DP Tabulation - Bottom up
        # TC: O(k*N) for calcuating all index and subsum pairs
        # SC: O(k*N) for dp array
        
        def tabul_subset_sums(n,k):
            
            dp = [[False for i in range(k+1)] for j in range(n)]

            # 1. Initialization
           # 1.1 If target is 0, set true (subsum achieved) - if a sequence gets here it means it a valid one as per Appr 2
           # Rather, if a number is not taken then target sum of 0 can be achieved which is why this is true
            for i in range(n):
                dp[i][0] = True

            # 1.1 The 0th element alone "can" form target if less than k
            if nums[0] <= k:
                dp[0][nums[0]] = True

            # 2. Recurrence
            for i in range(1,n):
                for j in range(1,k+1):
                    not_take = dp[i-1][j]
                    take = False
                    if nums[i] <= j: 
                        take = dp[i-1][j-nums[i]]
                    dp[i][j] = take or not_take

            # 3. Return last element of array which indicates if a subset with all elements can sum to k
            return dp[n-1][k]
        
        # Total sum is odd and hence array cant be split
        k = sum(nums)
        if k % 2:
            return False # odd sum cant be split
        
        return tabul_subset_sums(len(nums),int(k/2))