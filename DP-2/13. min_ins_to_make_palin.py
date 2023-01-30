class Solution:
    def minInsertions(self, s: str) -> int:
        
        # Approach 1: Recursion - TLE
        # TC: >> O(2^N) 
        # SC: O(N)
        # Intuition: Use LPS and subtract n from it 
        
#         def recur_min(i ,j):
#             if i < 0 or j < 0:
#                 return 0
            
#             if s[i] == r[j]:
#                 return 1 + recur_min(i-1, j-1)
#             else:
#                 return max(recur_min(i-1, j), recur_min(i, j-1))
        
#         n = len(s)
#         r = s[::-1]
        
#         # Find length of longest palindromic subsequence
#         # That minus the length of the string is the min insertions needed to make string palindromic)
#         return (n - recur_min(n-1, n-1))
    
#         # Approach 2: DP Memoization
#         # TC: O(N^2) 
#         # SC: O(N^2)
#         # Intuition: Use LPS and subtract n from it
        
#         n = len(s)
#         dp = [[-1 for i in range(n)] for j in range(n)]
        
#         def recur_min(i ,j):
#             if i < 0 or j < 0:
#                 return 0
            
#             if dp[i][j] != -1:
#                 return dp[i][j]
            
#             if s[i] == r[j]:
#                 dp[i][j] = 1 + recur_min(i-1, j-1)
#             else:
#                 dp[i][j] = max(recur_min(i-1, j), recur_min(i, j-1))
#             return dp[i][j]
        
#         r = s[::-1]
        
#         # Find length of longest palindromic subsequence
#         # That minus the length of the string is the min insertions needed to make string palindromic)
#         return (n - recur_min(n-1, n-1))
        
        # Approach 3: DP Tabultion
        # TC: O(N^2) 
        # SC: O(N^2)
        # Intuition: Use LPS and subtract n from it
        
        n = len(s)
        dp = [[0 for i in range(n+1)] for j in range(n+1)]
        r = s[::-1]
        
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == r[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # Find length of longest palindromic subsequence
        # That minus the length of the string is the min insertions needed to make string palindromic)
        return (n - dp[n][n])