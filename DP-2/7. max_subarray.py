class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Approach 1: DP Tabulation
        # Employ Kadane's Algorithm here 
        # Pick not pick wont work for contigious subarrays
        # TC: O(N) for going over array
        # SC: O(1)
        
        n = len(nums)
        
        # 1. Initialization of local max and min
        local_min, local_max = nums[0], nums[0]
        # Need a separate variable for result so result so far
        result = local_max
        
        for i in range(1, n):
            # Calculate temp max(cant use local max as it will get updated disrupting results for calculating local min) 
            # Temp max first cause local min, local max doesnt get updated before this iteration is complete
            
            temp_max = max(nums[i], nums[i] + local_min, nums[i] + local_max)
            local_min = min(nums[i], nums[i] + local_min, nums[i] + local_max)
            
            local_max = temp_max
            
            result = max(result, local_max)
            
        return result