class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # Approach 1: Recursion - TLE
        # TC: O(2^N *2^M) for generating subsequences for 2 different strings
        # SC: O(N) for stack space
        
#         def recur_subseq(i, j):
            
#             # 1. Base Case
#             if i < 0 or j < 0:
#                 return 0
            
#             # 2. Recurrence
#             # If the indexes match, then go back on both
#             if text1[i] == text2[j]:
#                 # Increase length of subsequence by 1 by adding 1
#                 return 1 + recur_subseq(i-1, j-1)
            
#             # If no match - take max of the two possibilties
#             # Poss 1 - move back i and keep j constant
#             # Poss 2 - move back j and keep i constant
#             # Do not increase length of subsequence as no match, so add 0
#             return max(0 + recur_subseq(i-1, j), 0 + recur_subseq(i, j-1))
        
#         return recur_subseq(len(text1) - 1, len(text2) - 1)
    
        # Approach 2: DP Memoization 
        # TC: O(N^2) for traversing the dp array
        # SC: O(N^2) for dp array
        
#         dp = [[-1 for i in range(len(text2))] for j in range(len(text1))]
        
#         def recur_subseq(i, j):
            
#             # 1. Base Case
#             if i < 0 or j < 0:
#                 return 0
            
#             # 2. DP array check
#             if dp[i][j] != -1:
#                 return dp[i][j]
            
#             # 3. Recurrence
#             # If the indexes match, then go back on both
#             if text1[i] == text2[j]:
#                 dp[i][j] =  1 + recur_subseq(i-1, j-1)
#             else:
#                 # If no match - take max of the two possibilties
#                 # Poss 1 - move back i and keep j constant
#                 # Poss 2 - move back j and keep i constant
#                 dp[i][j] = max(0 + recur_subseq(i-1, j), 0 + recur_subseq(i, j-1))
            
#             return dp[i][j]     
        
#         return recur_subseq(len(text1) - 1, len(text2) - 1)
    
        # Approach 3: DP Tabulation
        # TC: O(N^2) for traversing the dp array
        # SC: O(N^2) for dp array
        
        m = len(text1)
        n = len(text2)
        
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
            
        # 1. Initialization
        # Already done
            
        # 2. Recurrence
        for i in range(1, m+1):
            for j in range(1, n+1):
                # If the indexes match, then go back on both
                if text1[i-1] == text2[j-1]:
                    dp[i][j] =  1 + dp[i-1][j-1]
                else:
                    # If no match - take max of the two possibilties
                    # Poss 1 - move back i and keep j constant
                    # Poss 2 - move back j and keep i constant
                    dp[i][j] = max(0 + dp[i-1][j], 0 + dp[i][j-1])  
        
        return dp[m][n]
            