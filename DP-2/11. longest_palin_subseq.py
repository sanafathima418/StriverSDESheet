class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        # Can be easily done using string and its reverse an employing lcs
        # This is a different approach which reduces space complexity by O(N) - Frankly not worth it
#         # Approach 1: Recursion - TLE
#         # TC: >>> O(2^N) for atleast 2 possibilities
#         # SC: O(N) for stack space
        
#         def recur_palin(i,j):
#             # 1. Base Case
#             if i > j:
#                 # 1.1 The indexes have gone over so return 
#                 return 0
            
#             if i == j:
#                 # 1.2 Edge Case: comparing a character against itself so every character in itself forms a palindrome of len 1
#                 return 1
            
#             # 2. Recurrence
#             if s[i] == s[j]:
#                 # 2.1 Add 2 because we are moving on from the palin part of string where we compare 2 different chars
#                 return 2 + recur_palin(i+1, j-1)
#             else:
#                 # 2.2 Check the possibilities (same as lcs)
#                 return max(recur_palin(i+1,j), recur_palin(i, j-1))
        
#         return recur_palin(0, len(s)-1)
        
        # Approach 2: DP Memoization
        # TC: O(N^2) for traversing 2D array
        # SC: O(N^2) for 2D array
        
#         n = len(s)
        
#         dp = [[-1 for i in range(n+1)] for j in range(n+1)]
        
#         def recur_palin(i,j):
#             # 1. Base Case
#             if i > j:
#                 # 1.1 The indexes have gone over so return 
#                 return 0
            
#             if i == j:
#                 # 1.2 Edge Case: comparing a character against itself so every character in itself forms a palindrome of len 1
#                 return 1
            
#             if dp[i][j] != -1:
#                 return dp[i][j]
            
#             # 2. Recurrence
#             if s[i] == s[j]:
#                 # 2.1 Add 2 because we are moving on from the palin part of string where we compare 2 different chars
#                 dp[i][j] = 2 + recur_palin(i+1, j-1)
#             else:
#                 # 2.2 Check the possibilities (same as lcs)
#                 dp[i][j] = max(recur_palin(i+1,j), recur_palin(i, j-1))
            
#             return dp[i][j]
        
#         return recur_palin(0, len(s)-1)
    
        # Approach 3: DP Tabulation - using 2 strings(original and reverse) and lcs technique instead of above technique
        # TC: O(N^2) for traversing 2D array
        # SC: O(N^2) for 2D array
        
        n = len(s)
        
        dp = [[0 for i in range(n+1)] for j in range(n+1)]
        
        # 1. Initialization
        # Already done when dp array assigned to 0
        
        # 2. Recurrence
        # Only values on upper half of diagonal are filled
        r = s[::-1]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == r[j-1]:
                    # 2.1 Add 2 because we are moving on from the palin part of string where we compare 2 different chars
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    # 2.2 Check the possibilities (same as lcs)
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[n][n]