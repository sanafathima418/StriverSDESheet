# https://www.youtube.com/watch?v=3jvWodd7ht0

from sys import stdin
import json

# Time Complexity : O(2^N) 
# Space Complexity : O(N)

def check_palin(s,i,j):
    while(i < j):
        if(s[i] != s[j]):
            return False
        i, j = i+1, j-1
    return True

def partition(s):
    
    partition_list = []
    sub_list = []
    
    def recur_partition(i):
        if i >= len(s):  # Base Case
            partition_list.append(list(sub_list))
            return 
        
        # At each level(in recursion tree), Partition every string after every character
        for j in range(i,len(s)):
            if check_palin(s,i,j):
                # Append to path list for the palindrome part
                sub_list.append(s[i:j+1])
                # Recurse for remaining string
                recur_partition(j+1) 
                # Backtrack
                sub_list.pop()

    recur_partition(0) 
    return partition_list

s=stdin.readline().rstrip()

final=partition(s)

for ele in final:
    ele = sorted(ele)
    print(json.dumps(ele))

