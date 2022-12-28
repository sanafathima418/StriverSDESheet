class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Approach: Using Monotonic Stack which in in decreasing order
        # Front of Queue has max element, every time element is inserted into queue get max from front
        # Mono Stack will store indexes
        # TC: O(n) for traversing over input array
        # SC: O(n) for monotonic queue
        
        # NOTE: Mono Stack works same way as deque here (deque allows insertion and deletion from both ends)
        
        mono_stack = deque()
        res_arr = []
        
        for i,num in enumerate(nums):
            # 1. Remove out of bound elements
            while(mono_stack and mono_stack[0] == (i-k)):
                mono_stack.popleft()
            
            # 2. Pop from end to find best position to insert
            while(mono_stack and nums[mono_stack[-1]] < num):
                mono_stack.pop()
            
            # 3. Append to stack
            mono_stack.append(i)
            
            # 4. Add max of window to array
            if (i >= k-1):
                res_arr.append(nums[mono_stack[0]])
                
        return res_arr
                
                