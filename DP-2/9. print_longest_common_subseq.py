class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # Printing longest common substring
        # Approach 1: Reconstruction from DP array

        i = len(text1)
        j = len(text2)

        lcs = ""

        while(i and j):
            if text1[i] == text2[j]:
                lcs += text1[i]
                i -= 1
                j -= 1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    i -= 1
                else:
                    j -= 1
         print(lcs)
    
        # Approach 2: Recursion
    
        def recur_subseq(i, j):
            
            # 1. Base Case
            if i >= len(text1) or j >= len(text2):
                return ''
            
            # 2. Recurrence
            # If the indexes match, then go back on both
            if text1[i] == text2[j]:
                # Increase length of subsequence by 1 by adding 1
                return text1[i] + recur_subseq(i+1, j+1)
            
            # If no match - take max of the two possibilties
            # Poss 1 - move back i and keep j constant
            # Poss 2 - move back j and keep i constant
            # Do not increase length of subsequence as no match, so add 0
            poss1 = recur_subseq(i+1, j)
            poss2 = recur_subseq(i, j+1)
            if len(poss1) > len(poss2):
                return poss1
            else:
                return poss2
        
        print(recur_subseq(0, 0))
        return 1
    
        # Approach 3: DP Memoization
        m = len(text1)
        n = len(text2)
        dp = [[-1 for i in range(n)] for j in range(m)]
        
        def recur_subseq(i, j):
            
            # 1. Base Case
            if i >= m or j >= n:
                return ''
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            # 2. Recurrence
            # If the indexes match, then go back on both
            if text1[i] == text2[j]:
                # Increase length of subsequence by 1 by adding 1
                dp[i][j] = text1[i] + recur_subseq(i+1, j+1)
            else:
                # If no match - take max of the two possibilties
                # Poss 1 - move back i and keep j constant
                # Poss 2 - move back j and keep i constant
                # Do not increase length of subsequence as no match, so add 0
                poss1 = recur_subseq(i+1, j)
                poss2 = recur_subseq(i, j+1)
                if len(poss1) > len(poss2):
                    dp[i][j] = poss1
                else:
                    dp[i][j] = poss2
            return dp[i][j]
        
        print(recur_subseq(0, 0))
        return 1

        # Approach 4: DP Tabultion
    
        m = len(text1)
        n = len(text2)
        
        dp = [['' for i in range(n+1)] for j in range(m+1)]
            
        # 1. Initialization
        # Already done
            
        # 2. Recurrence
        for i in range(1, m+1):
            for j in range(1, n+1):
                # If the indexes match, then go back on both
                if text1[i-1] == text2[j-1]:
                    dp[i][j] =  text1[i-1] + dp[i-1][j-1]
                else:
                    # If no match - take max of the two possibilties
                    # Poss 1 - move back i and keep j constant
                    # Poss 2 - move back j and keep i constant
                    if len(dp[i-1][j]) > len(dp[i][j-1]):
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-1]
        
        print(dp[m][n][::-1])
        return 1