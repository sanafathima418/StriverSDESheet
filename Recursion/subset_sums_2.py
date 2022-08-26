from typing import *

    # Time Complexity : O(2^N) + O(NLOGN)
    # Space Complexity : O(N)
    # Intuition: Dont process right subtree if you look ahead and see same element
    
def recur_subsequence(i, num, unique_list, sub_list):
    if(i == len(num)):
        # 1. Base Case: Increment i till it reaches n and subsequence so far
        # Reached Leaf Node
        unique_list.append(sub_list.copy())
        return 

    # Take current index for subsequence generation
    sub_list.append(num[i])
    recur_subsequence(i+1, num, unique_list, sub_list)  # Left sub-tree
        
    # Dont take current index for subsequence generation
    sub_list.pop()
    # Look ahead and see next element is same as current, move pointer until value not same
    while i + 1 < len(num) and num[i] == num[i + 1]:
        i += 1
    recur_subsequence(i+1, num, unique_list, sub_list)  # Right sub-tree
  
def uniqueSubsets(n :int,arr :List[int]) -> List[List[int]]:
    
    # Call_recursive function for every index in num
    unique_list = []
    arr.sort()
    recur_subsequence(0, arr, unique_list, [])

    return unique_list 
    

