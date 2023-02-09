class Solution:
    def isMatch(self, s: str, p: str) -> bool:
#         # Approach - Recursion - Suprisingly no TLE with this
#         # TC: >> O(2^N)
#         # SC: O(N)
        
#         # DO NOT REFER TO SOLUTION IN LC - it is highly confusing
#         # Can be easily converted to Memoization
        
#         m = len(s)
#         n = len(p)
        
#         def recur_regex(i, j):
            
#             # 1. Base Case
#             if i < 0 and j < 0:
#                 # 1.1 If both reached then return True
#                 return 1
            
#             if j < 0 or (i < 0 and p[j] != '*'):
#                 # 1.2 If j reaches end or i reaches end and pattern is not * ("aaa" and "aaaa")
#                 return 0
            
#             if i < 0 and p[j] == "*":
#                 # 1.3 If i reaches end and pattern to be traversed with * (move back 2 steps and re-check)
#                 return recur_regex(i, j-2)
            
#             # 2. Recurrence
#             if s[i] == p[j] or p[j] == '.':
#                 # 2.1 If match, move both
#                 return recur_regex(i-1, j-1)
            
#             if p[j] == '*':
#                 # 2.2 Zero or more occurences so not take and take
#                 not_take = recur_regex(i, j-2)
#                 take = 0
#                 if j > 0 and s[i] == p[j-1] or p[j-1] == '.':
#                     # 2.2.1 Check if the previous character is same or . and check the previous characters in input string 
#                     take = recur_regex(i-1,j)
#                 return take or not_take
            
#             # 2.3 No match, so return 0 immediately
#             return 0
        
#         return recur_regex(m-1, n-1)

#         # Approach 2 - Memoization
#         # TC: O(N^2)
#         # SC: O(N^2)
        
#         m = len(s)
#         n = len(p)
        
#         dp = [[-1 for i in range(n+1)] for j in range(m+1)]
        
#         def recur_regex(i, j):
            
#             # 1. Base Case
#             if i < 0 and j < 0:
#                 # 1.1 If both reached then return True
#                 return 1
            
#             if j < 0 or (i < 0 and p[j] != '*'):
#                 # 1.2 If j reaches end or i reaches end and pattern is not * ("aaa" and "aaaa")
#                 return 0
            
#             if i < 0 and p[j] == "*":
#                 # 1.3 If i reaches end and pattern to be traversed with * (move back 2 steps and re-check)
#                 return recur_regex(i, j-2)
            
#             else:
#                 if dp[i][j] != -1:
#                     return dp[i][j]
                
#                 # 2. Recurrence
#                 if s[i] == p[j] or p[j] == '.':
#                     # 2.1 If match, move both
#                     dp[i][j] = recur_regex(i-1, j-1)


#                 elif p[j] == '*':
#                     # 2.2 Zero or more occurences so not take and take
#                     not_take = recur_regex(i, j-2)
#                     take = 0
#                     if j > 0 and s[i] == p[j-1] or p[j-1] == '.':
#                         # 2.2.1 Check if the previous character is same or . and check the previous characters in input string 
#                         take = recur_regex(i-1,j)
#                     dp[i][j] = take or not_take

#                 # 2.3 No match, so return 0 immediately
#                 else:
#                     dp[i][j] = 0
#             return dp[i][j]
        
#         return recur_regex(m-1, n-1)


        # Approach 3 - Tabulation
        # TC: O(N^2)
        # SC: O(N^2)

        m = len(s)
        n = len(p)
        
        dp = [[False for i in range(n+1)] for j in range(m+1)]
        
        dp[0][0] = True
        
        for i in range(1, n+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if j > 0 and (s[i-1] == p[j-2] or p[j-2] == '.'):
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                else:
                    dp[i][j] = False
        
        return dp[m][n]
