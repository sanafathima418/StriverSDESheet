class Solution:
    def climbStairs(self, n: int) -> int:

        # Same as Fibonacci except for an additional initialization i.e, n=2 instead of only 1 and 2
        # The below code calculates fib of n+1 which works just fine

#         # Approach 1: 1D Memoization DP
#         # TC: O(N) as we calculate nth fib num only once making traversal linear
#         # SC: O(N)+O(N) for dp array and recursion stack space
        
#         # 1. Initialize dp array
#         dp_array = [-1]*(n+2)
        
#         def f(m):
#             # 2.1 Base Case
#             if m <= 1:
#                 return m
            
#             # 2.2 Check if subproblem already solved and return 
#             if dp_array[m] != -1:
#                 return dp_array[m]
            
#             # 2.3 Solve new subproblem and update in dp_array
#             dp_array[m] = f(m-1) + f(m-2)
            
#             # 2.4 Return the solved problem value as the prev problem is expecting this value to calculate sum
#             return dp_array[m] 
        
#         # 3. Call recursive function which will return the nth fib num
#         return f(n+1)  
        
#         # Approach 2: 1D Tabulation DP
#         # TC: O(N) for going over all fib numbers from 0-n
#         # SC: O(N) for dp array alone
        
#         # 1. Initialize dp array
#         dp_array = [0]*(n+2)
        
#         # 2. Initialization: Set up Base Case or return if needed
#         if n <= 1:
#             return n
#         dp_array[1] = 1
        
#         # 3. Inductive Case: Traverse for all other cases and update dp array
#         for i in range(2,n+2):
#             dp_array[i] = dp_array[i-1] + dp_array[i-2]
        
#         # Return final value
#         return dp_array[-1]

        # Approach: 1D Tabulation DP with Space Optimization
        # TC: O(N) for going over all fib numbers from 0-n
        # SC: O(1) 
        
        # 1. Initialization: Set up Base Case or return if needed
        if n <= 1:
            return n
        curr = 0
        prev2 = 0
        prev1 = 1
        
        # 2. Inductive Case: Traverse for all other cases and update pointers
        for i in range(2,n+2):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr # In next step this curr will become prev1 so duplicate it here
        
        # Return final value
        return curr