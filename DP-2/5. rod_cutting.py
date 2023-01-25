from sys import stdin
import sys

def cutRod(price, n):
    # Approach 1: Recursion - TLE
    # TC: >>> O(2^N) for 2 possibilities taken x times
    # SC: O(N) for stack space

    # def recur_cut(i, curr_len):
    #     # 1. Base Case
    #     if i == 0:
    #         # Take 1st index, curr_len times as length of 1st rod is 1 and multiply by its price
    #         return curr_len * price[0]
        
    #     # 2. Recurrance
    #     not_take = 0 + recur_cut(i-1, curr_len)
    #     take = 0
    #     # 2.1 rod length is i+1 - as 1 based indexing
    #     if (i+1) <= curr_len:
    #         # 2.2 subtract curr len by rod length times(i+1)
    #         take = price[i] + recur_cut(i, curr_len - (i+1))

    #     return max(not_take, take)

    # return recur_cut(n-1, n)

    # Approach 2: DP Memoization 
    # TC: >>> O(N^2) for traversing over 2D array
    # SC: O(N^2) for 2D array + O(N) for stack space

    # dp = [[-1 for i in range(n+1)] for j in range(n)]

    # def recur_cut(i, curr_len):
    #     # 1. Base Case
    #     if i == 0:
    #         # Take 1st index, curr_len times as length of 1st rod is 1 and multiply by its price
    #         return curr_len * price[0]
        
    #     if dp[i][curr_len] != -1:
    #         return dp[i][curr_len]
        
    #     # 2. Recurrance
    #     not_take = 0 + recur_cut(i-1, curr_len)
    #     take = 0
    #     # 2.1 rod length is i+1 - as 1 based indexing
    #     if (i+1) <= curr_len:
    #         # 2.2 subtract curr len by rod length times(i+1)
    #         take = price[i] + recur_cut(i, curr_len - (i+1))

    #     dp[i][curr_len] = max(not_take, take)
    #     return dp[i][curr_len]

    # return recur_cut(n-1, n)

    # Approach 3: DP Tabulation 
    # TC: >>> O(N^2) for traversing over 2D array
    # SC: O(N^2) for 2D array

    dp = [[0 for i in range(n+1)] for j in range(n)]

    # 1. Initialization
    for i in range(n+1):
        dp[0][i] = i * price[0]
        
    for i in range(n):
        for j in range(n+1):
            # 2. Recurrance
            not_take = 0 + dp[i-1][j]
            take = 0
            # 2.1 rod length is i+1 - as 1 based indexing
            if (i+1) <= j:
                # 2.2 subtract curr len by rod length times(i+1)
                take = price[i] + dp[i][j - (i+1)]

            dp[i][j] = max(not_take, take)

    return dp[n-1][n]
    
















# Taking input using fast I/O.
def takeInput():
    n = int(input())

    price = list(map(int, input().strip().split(" ")))

    return price, n


# Main.
t = int(input())
while t:
    price, n = takeInput()
    print(cutRod(price, n))
    t = t-1
