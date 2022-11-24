class Solution:
    def largestRectangleArea(self, height: List[int]) -> int: 
        # Approach: Use a monotonic stack that is increasing
        # Formula: (rse - lse + 1) * height[i]
        # Time Complexity: O(n)+O(n)+O(n) for 3 traversals
        # Space Complexity: O(n)+O(n)+O(n) for stack,lse,rse
        
        n = len(height)
        mono_stack = []
        lse = [0]*n
        rse = [0]*n
        final_res = -math.inf
        
        # Step 1: Find LSE
        for i in range(n):
            # 1. Pop Step
            while(mono_stack and height[mono_stack[-1]] >= height[i]):
                mono_stack.pop()
            
            # 2. Process Step: Pick from top of stack
            if mono_stack:
                lse[i] = mono_stack[-1]+1 # For left boundary do +1
            else:
                lse[i] = 0
                
            # 3. Push Step
            mono_stack.append(i)
        
        # Step 2: Find RSE
        mono_stack = []
        for i in range(n-1,-1,-1):
            # 1. Pop Step
            while(mono_stack and height[mono_stack[-1]] >= height[i]):
                mono_stack.pop()
            
            # 2. Process Step: Pick from top of stack
            if mono_stack:
                rse[i] = mono_stack[-1]-1  # For right boundary do -1
            else:
                rse[i] = n-1
                
            # 3. Push Step
            mono_stack.append(i)
        
        # Step 3: Apply Formula to generate max rectangle area
        for i in range(n):
            final_res = max(final_res, (rse[i] - lse[i] + 1) * height[i])

        return final_res
        