class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # Hard Problem
        
        # Approach 1: Recursion - TLE
        # TC: >> O(2^N)
        # SC: O(N)
        # f(i,j) represents if s[0-i] == p[0-j]
        
#         m = len(s)
#         n = len(p)

#         def recur_wildcard(i, j):
#             # 1. Base Case
#             if i < 0 and j < 0:
#                 # 1.1 If both are less than 0, both strings parsed successfully
#                 return 1
            
#             if j < 0:
#                 # 1.2 If 2nd string parsed and i is still left then False
#                 return 0
            
#             if i < 0:
#                 # 1.3 If 1st string parsed and j is still left, parse rest of j and check if it is *
#                 while j >= 0 and p[j] == '*':
#                     j -= 1
#                 # 1.4 If j is fully parsed then True, else False
#                 if j < 0:
#                     return 1
#                 return 0

#             # 2. Recurrence
#             if s[i] == p[j] or p[j] == '?':
#                 # 2.1 If equal or single character match, check other chars
#                 return recur_wildcard(i-1, j-1) 
#             else:
#                 if p[j] == '*':
#                     # 2.2 If multi match, then check possibilities of moving from that index
#                     return recur_wildcard(i, j-1) or recur_wildcard(i-1, j)
#                 else:
#                     # 2.3 Character mis-match so return false immediately 
#                     return 0 

#         return recur_wildcard(m-1, n-1)
    
        # Approach 3: DP Memoization
        # TC: O(N^2)
        # SC: O(N^2)
        # f(i,j) represents if s[0-i] == p[0-j]
        
#         m = len(s)
#         n = len(p)
        
#         dp = [[-1 for i in range(n)] for j in range(m)]

#         def recur_wildcard(i, j):
#             # 1. Base Case
#             if i < 0 and j < 0:
#                 # 1.1 If both are less than 0, both strings parsed successfully
#                 return 1
            
#             if j < 0:
#                 # 1.2 If 2nd string parsed and i is still left then False
#                 return 0
            
#             if i < 0:
#                 # 1.3 If 1st string parsed and j is still left, parse rest of j and check if it is *
#                 while j >= 0 and p[j] == '*':
#                     j -= 1
#                 # 1.4 If j is fully parsed then True, else False
#                 if j < 0:
#                     return 1
#                 return 0
            
#             if dp[i][j] != -1:
#                 return dp[i][j]

#             # 2. Recurrence
#             if s[i] == p[j] or p[j] == '?':
#                 # 2.1 If equal or single character match, check other chars
#                 dp[i][j] = recur_wildcard(i-1, j-1) 
#             else:
#                 if p[j] == '*':
#                     # 2.2 If multi match, then check possibilities of moving from that index
#                     dp[i][j] = recur_wildcard(i, j-1) or recur_wildcard(i-1, j)
#                 else:
#                     # 2.3 Character mis-match so return false immediately 
#                     dp[i][j] = 0 
            
#             return dp[i][j]

#         return recur_wildcard(m-1, n-1)
    
        # Approach 3: DP Tabultion
        # TC: O(N^2)
        # SC: O(N^2)
        # f(i,j) represents if s[0-i] == p[0-j]
        
        m = len(s)
        n = len(p)
        
        dp = [[0 for i in range(n+1)] for j in range(m+1)]

        # 1. Base Case
        # 1.1 Null and null string match
        dp[0][0] = 1
        
        # 1.2 Different from Approach 1 and 2 - Null string with * 
        for j in range(1, n+1):
            if p[j-1] == '*':
                # 1.2.1 For first row('') - Propagate the value of prev of the col to the col with * 
                dp[0][j] = dp[0][j-1]
            
        # 2. Recurrence
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    # 2.1 If equal or single character match, check other chars
                    dp[i][j] = dp[i-1][j-1] 
                else:
                    if p[j-1] == '*':
                        # 2.2 If multi match, then check possibilities of moving from that index
                        dp[i][j] = dp[i][j-1] or dp[i-1][j]
            
        return dp[m][n]