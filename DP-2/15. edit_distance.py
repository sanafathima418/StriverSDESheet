class Solution:
    def minDistance(self, s: str, p: str) -> int:
        # Approach 1: Recursion - TLE
        # TC: >> O(2^N)
        # SC: O(N + M)
        # Intuition: Same as LCS - Min ins and del except for final return and base case

#         m = len(s)
#         n = len(p)

#         def recur_palin(i, j):
            
#             # 1. Base Case
#             if i < 0:
#                 # If i has reached end, word2 could have some words or not so return it
#                 return j + 1 # 'length' of remaining chars
#             if j < 0:
#                 # If j has reached end, word1 could have some words or not so return it
#                 return i + 1 # 'length' of remaining chars

#             # 2. Recurrence
#             # 2.1 If same - do nothing but explore the next chars in both
#             if s[i] == p[j]:
#                 return recur_palin(i-1, j-1)
#             else:
#                 # 2.2 If not same - Explore all possibilities of moving from those indexes and add 1 as the operation needed
#                 # i-1, j-1 needed here too as <>
#                 # Min of all shrinked string possibilities as follows:
#                 # 1. (i, j-1) - Insert in str1
#                 # 2. (i-1, j) - Delete in str1
#                 # 3. (i-1, j-1) - Replace in str1
#                 return 1 + min(recur_palin(i-1, j-1), recur_palin(i-1, j), recur_palin(i, j-1))

#         # Add both strings and subtract 2 times the lowest common substring
#         # f(i,j) signifies - min possible ops to convert s1[0-i] to s2[0-j]
        
#         # Start checking from back, but will be updated from base case 0
#         return recur_palin(m-1, n-1)

        # # Approach 2: DP Memoization
        # # TC: O(N^2)
        # # SC: O(N^2)

#         m = len(s)
#         n = len(p)
#         dp = [[-1 for i in range(n+1)] for j in range(m+1)]

#         def recur_palin(i, j):
            
#             # 1. Base Case
#             if i < 0:
#                 # If i has reached end, word2 could have some words or not so return it
#                 return j + 1 # 'length' of remaining chars
#             if j < 0:
#                 # If j has reached end, word1 could have some words or not so return it
#                 return i + 1 # 'length' of remaining chars
            
#             if dp[i][j] != -1:
#                 return dp[i][j]
            
#             # 2. Recurrence
#             # 2.1 If same - do nothing but explore the next chars in both
#             if s[i] == p[j]:
#                 dp[i][j] = recur_palin(i-1, j-1)
#             else:
#                 # 2.2 If not same - Explore all possibilities of moving from those indexes and add 1 as the operation needed
#                 # i-1, j-1 needed here too as <>
#                 # Min of all shrinked string possibilities as follows:
#                 # 1. (i, j-1) - Insert in str1
#                 # 2. (i-1, j) - Delete in str1
#                 # 3. (i-1, j-1) - Replace in str1
#                 dp[i][j] = 1 + min(recur_palin(i-1, j-1), recur_palin(i-1, j), recur_palin(i, j-1))
            
#             return dp[i][j]

#         # Add both strings and subtract 2 times the lowest common substring
#         # f(i,j) signifies - min possible ops to convert s1[0-i] to s2[0-j]
        
#         # Start checking from back, but will be updated from base case 0
#         return recur_palin(m-1, n-1)

        # Approach 3: DP Tabulation
        # TC: O(N^2)
        # SC: O(N^2)

        m = len(s)
        n = len(p)
        # one additional row and column for empty string
        dp = [[0 for i in range(n+1)] for j in range(m+1)]

        # 1. Initialization
        # for 1st col/row - whose str1 is "" and str2 is one char added at a time to str2 and vice versa
        for i in range(m+1):
            dp[i][0] = i
        
        for j in range(n+1):
            dp[0][j] = j

        # 2. Recurrence
        for i in range(1, m+1):
            for j in range(1, n+1):    
                if s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

        return dp[m][n]