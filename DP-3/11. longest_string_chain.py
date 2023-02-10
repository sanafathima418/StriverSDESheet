class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Approach 1: Most Intuitive - severe TLE
        # Combine LCS + word length check bw worda and wordb and then apply Approach 4 of lIS
        # TC: O(N^2)+O(N^2) for lcs find and reconstruct + O(N^2) for LIS
        # SC: O(N^2) for dp of lcs + O(N) for aux space of lcs + O(N) for aux space of word len + O(N) for dp of LIS
        
        # Intuition
        # 1. Get LCS of 2 words and check if == prev word
        # 2. If yes, check for length diff == 1
        # 3. In LIS, update dp[i] based on max value

        # def lcs(text1, text2):
        # # lowest common subseq
        #     m = len(text1)
        #     n = len(text2)
            
        #     dp = [[0 for i in range(n+1)] for j in range(m+1)]
                
        #     # 1. Initialization
        #     # Already done
                
        #     # 2. Recurrence
        #     for i in range(1, m+1):
        #         for j in range(1, n+1):
        #             # If the indexes match, then go back on both
        #             if text1[i-1] == text2[j-1]:
        #                 dp[i][j] =  1 + dp[i-1][j-1]
        #             else:
        #                 # If no match - take max of the two possibilties
        #                 # Poss 1 - move back i and keep j constant
        #                 # Poss 2 - move back j and keep i constant
        #                 dp[i][j] = max(0 + dp[i-1][j], 0 + dp[i][j-1]) 
            
        #     # 3. Reconstruction
        #     i = len(text1)
        #     j = len(text2)

        #     lcs_str = ""
        #     while(i and j):
        #         if text1[i-1] == text2[j-1]:
        #             lcs_str += text1[i-1]
        #             i -= 1
        #             j -= 1
        #         else:
        #             if dp[i-1][j] > dp[i][j-1]:
        #                 i -= 1
        #             else:
        #                 j -= 1
        #     return lcs_str[::-1]

        # def check_pred(i, j):
        #     lcs_str = lcs(words[i], words[j])
        #     if lcs_str == words[j] and len(words[i]) - len(words[j]) == 1:
        #         return 1
        #     return 0
        
        # n = len(words)
        # dp = [1] * n
        # words.sort(key = len)

        # for i in range(n):
        #     for j in range(i):
        #         if check_pred(i, j) and 1 + dp[j] > dp[i]:
        #             dp[i] = 1 + dp[j]
        
        # return max(dp)

        # Approach 2: No need to do lcs, just check for existence of all characters of 2nd string in 1st
        # TC: O(N^2 * L)
        # SC: O(N)

        # Intuition:
        # 1. Sort word array based on length
        # 2. Check for length of str1 > length of str2 +1  
        # 3. Compare characters in both

        def check_pred(word1, word2):
            # 1. If 
            if len(word1) != len(word2) + 1:
                return 0
            
            w_i = 0
            w_j = 0
            while(w_i < len(word1)):
                if w_j < len(word2) and word1[w_i] == word2[w_j]:
                    w_i += 1
                    w_j += 1
                else:
                    w_i += 1
            
            if w_i == len(word1) and w_j == len(word2):
                return 1
            return 0

        n = len(words)
        dp = [1] * n
        words.sort(key = len)
        maxi = 1

        for i in range(n):
            for j in range(i):
                if check_pred(words[i], words[j]) and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    maxi = max(maxi, dp[i])
        
        return maxi