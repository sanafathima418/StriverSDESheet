class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # Approach - Recursion - Suprisingly no TLE with this
        # TC: >> O(2^N)
        # SC: O(N)
        
        # DO NOT REFER TO SOLUTION IN LC - it is highly confusing
        # Can be easily converted to Memoization
        
        m = len(s)
        n = len(p)
        
        def recur_regex(i, j):
            
            # 1. Base Case
            if i < 0 and j < 0:
                # 1.1 If both reached then return True
                return 1
            
            if j < 0 or (i < 0 and p[j] != '*'):
                # 1.2 If j reaches end or i reaches end and pattern is not * ("aaa" and "aaaa")
                return 0
            
            if i < 0 and p[j] == "*":
                # 1.3 If i reaches end and pattern to be traversed with * (move back 2 steps and re-check)
                return recur_regex(i, j-2)
            
            # 2. Recurrence
            if s[i] == p[j] or p[j] == '.':
                # 2.1 If match, move both
                return recur_regex(i-1, j-1)
            
            if p[j] == '*':
                # 2.2 Zero or more occurences so not take and take
                not_take = recur_regex(i, j-2)
                take = 0
                if j > 0 and s[i] == p[j-1] or p[j-1] == '.':
                    # 2.2.1 Check if the previous character is same or . and check the previous characters in input string 
                    take = recur_regex(i-1,j)
                return take or not_take
            
            # 2.3 No match, so return 0 immediately
            return 0
        
        return recur_regex(m-1, n-1)