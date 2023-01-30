class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # Crazy Problem 
        
#         # Approach: DP Tabulation - TLE 
#         # TC: O(N^2) to traverse over 2D array
#         # SC: O(N^2) for 2D array
#         # Same as LCS just add another check to see if the lcs candidate generated here is actually a palindrome

#         n = len(s)
#         r = s[::-1]

#         dp = [['' for i in range(n+1)] for j in range(n+1)]
#         longest_palin = ''

#         # 1. Initialization
#         # Already done - technically first row and col to be initialized to 0

#         # 2. Recurrence
#         for i in range(1, n+1):
#             for j in range(1, n+1):
#                 # If the indexes match, then go back on both
#                 if s[i-1] == r[j-1]:
#                     dp[i][j] = s[i-1] + dp[i-1][j-1]
#                     # Same as LCS just add another check to see if the lcs candidate generated here is actually a palindrome
#                     if len(dp[i][j]) > len(longest_palin):
#                         if dp[i][j] == dp[i][j][::-1]:
#                             longest_palin = dp[i][j]
#                 else:
#                     # No match so drop the sequence and assign 0
#                     dp[i][j] = '' 
        
#         return longest_palin

#         # Approach: DP Tabulation - TLE 
#         # TC: O(N^2) to traverse over 2D array
#         # SC: O(N^2) for 2D array
#         # Same as LCS just add another check to see if the lcs candidate generated here is actually a palindrome

        r = s[::-1]
        n = len(s)
        
        dp = [[0] * (n + 1) for i in range(n + 1)]
        maxlen = 0
        iPos = 0  # It is indicator to regenrate the lps in the end along with maxlen(end index of lps)

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == r[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if maxlen < dp[i][j]:
                        # if i - 1 == n - 1 - j - 1: - This wont work
                        if (i - 1) - dp[i][j] + 1 == n - 1 - (j - 1):
                            # This works as we consider the position we are at and go back to the start of palin of original string 
                            # and compare it against end of palin in reversed string
                            # For example - 'abbafgh' 
                            # a at index 6 in reversed string corresponds to a at index 0 in original string,
                            # but when we are at a6 in r, we are at a3 in o instead of a0
                            # this is why we go back in the original string by length of current lcs
                            maxlen = dp[i][j]
                            iPos = i
                # else:
                # Not actually needed as it is handled as a part of initialization
                #     dp[i][j] = 0
                
        return s[iPos - maxlen: iPos]

    
        