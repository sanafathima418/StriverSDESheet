class Solution:
    def rob(self, nums: List[int]) -> int:
    
    # Approach 1: DP Tabulation
    # Call rob1 twice with two different arrays and the answer is the max of the 2
    # 1. nums with elements from 0->n-1
    # 2. nums with elements from 1->n
    # TC: 0(N) for going over array
    # SC: O(N) for dp array
        
        # House Robber 1 module
        def rob1(nums):
            # 1. Initialization
            n = len(nums)
            dp_array = [0] * n
            # 1.1 Base Case
            dp_array[0] = nums[0]

            # 3. Recurrence - Traverse from 1-n as 0 is base case
            for i in range(1, n):
                # 3.1 Pick is always the number
                pick = nums[i]
                if i > 1:
                    # 3.2 Go back only if index exists to make sure no negative indices happen
                    pick += dp_array[i-2]
                not_pick = 0 + dp_array[i-1]
                dp_array[i] = max(pick, not_pick)

            # 4. Return max sum available in last position of dp array
            return dp_array[-1]
        
        # Edge Cases similar to base case
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        
        # Intuition 
        return max(rob1(nums[:-1]), rob1(nums[1:]))
        
        
        