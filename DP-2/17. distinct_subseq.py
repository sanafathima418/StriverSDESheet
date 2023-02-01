class Solution:
    def numDistinct(self, s: str, p: str) -> int:
        
        # Approach 1: Recursion - TLE
        # TC:>> O(2^N)
        # SC: O(N)
        # Intuition: If match, take(go back on j) and not take(stay on j), if not match go back and search in i for char at j(stay on j)
        # f(i,j) - num of distinct subsequences in s[0-i] for p[0-j]
        
#         m = len(s)
#         n = len(p)
        
#         def recur_distinct(i, j):
#             # 1. Base Case
#             if j < 0:
#                 # All s2 matched so possible subseq
#                 return 1
#             if i < 0:
#                 # Some d2 not matched not not possible subseq
#                 return 0
            
#             # 2. Recurrence
#             if s[i] == p[j]:
#                 # 2.1 Take current i
#                 take = recur_distinct(i-1, j-1)
#                 # 2.2 Not Take current i
#                 not_take = recur_distinct(i-1, j)
                
#                 return take + not_take
            
#             else:
#                 return recur_distinct(i-1, j)
            
#         return recur_distinct(m-1, n-1)
    
#         # Approach 2: DP Memoization
#         # TC: O(N^2)
#         # SC: O(N^2)
        
#         m = len(s)
#         n = len(p)
#         dp = [[-1 for i in range(n+1)] for j in range(m+1)]
        
#         def recur_distinct(i, j):
#             # 1. Base Case
#             if j < 0:
#                 # All s2 matched so possible subseq
#                 return 1
#             if i < 0:
#                 # Some d2 not matched not not possible subseq
#                 return 0
            
#             if dp[i][j] != -1:
#                 return dp[i][j]
            
#             # 2. Recurrence
#             if s[i] == p[j]:
#                 # 2.1 Take current i
#                 take = recur_distinct(i-1, j-1)
#                 # 2.2 Not Take current i
#                 not_take =  recur_distinct(i-1, j)
#                 dp[i][j] = take + not_take
            
#             else:
#                 dp[i][j] = recur_distinct(i-1, j)
                
#             return dp[i][j]
            
#         return recur_distinct(m-1, n-1)

        # Approach 3: DP Tabulation
        # TC: O(N^2)
        # SC: O(N^2)
        
        m = len(s)
        n = len(p)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        
        # 1. Base Case
        # first column is 1 as with empty s, any p can be devised
        for i in range(m+1):
            dp[i][0] = 1
            
        # 2. Recurrence
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1]:
                    # 2.1 Take current i
                    take = dp[i-1][j-1]
                    # 2.2 Not Take current i
                    not_take =  dp[i-1][j]
                    dp[i][j] = take + not_take
                else:
                    dp[i][j] = dp[i-1][j]
            
        return dp[m][n]