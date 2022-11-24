class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Approach: Use a monotonic stack that is decreasing
        # Time Complexity: O(n) for traversing 
        # Space Complexity: O(n) for stack
        
        n = len(nums)
        mono_stack = []
        next_greater_list = [0]*n
        
        # Reverse Traverse over array twice to account for cyclic
        for i in range((2*n)-1,-1,-1):
            # 1. Pop Step
            while(mono_stack and mono_stack[-1] <= nums[i%n]):
                mono_stack.pop()
            
            # 2. Process Step: Pick from top of stack
            if(i < n):
                if mono_stack:
                    next_greater_list[i] = mono_stack[-1]
                else:
                    next_greater_list[i] = -1
                
            # 3. Push Step
            mono_stack.append(nums[i%n])
        
        return next_greater_list