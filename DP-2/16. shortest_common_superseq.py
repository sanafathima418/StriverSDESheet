class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Approach: DP Tabulation
        # TC: O(N^2) to traverse over 2D array
        # SC: O(N^2) for 2D array
        # Intuition - LCS reconstucted. + other chars in str1 + other chars in str2

        m = len(str1)
        n = len(str2)

        dp = [[0 for i in range(n+1)] for j in range(m+1)]

        # 1. Initialization
        # Already done - technically first row and col to be initialized to 0

        # 2. Recurrence
        for i in range(1, m+1):
            for j in range(1, n+1):
                # If the indexes match, then go back on both
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    # No match so drop the sequence and assign 0
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        lcs = ""
        i = m
        j = n
        
        # 3. LCS Reconstruction- exception being we take chars even when they are not equal
        while(i and j):
            if str1[i-1] == str2[j-1]:
                lcs += str1[i-1]
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                lcs += str1[i-1] # Unique to SCS (take whatever is more)
                i -= 1
            else:
                lcs += str2[j-1] # Unique to SCS 
                j -= 1
        
        # 4. Take remaining chars in str1
        while(i > 0):
            lcs += str1[i-1]
            i -= 1
        
        # 5. Take remaining chars in str2
        while(j > 0):
            lcs += str2[j-1]
            j -= 1
        
        # 6. As we traverse dp array in reverse, need to reverse it back to obtain actual answer
        return lcs[::-1]

                
            