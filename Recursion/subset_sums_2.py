from typing import *
     # Intuition: Dont process right subtree if you look ahead and see same element
    # Time Complexity : O(2^N) + O(NLOGN)
    # Space Complexity : O(N)
def uniqueSubsets(n :int,arr :List[int]) -> List[List[int]]:
    
    main_list = []
    sub_list = []
    
    def recur_subsequence(i):
        if(i == n):
            # 1. Base Case: Increment i till it reaches n and subsequence so far
            # Reached Leaf Node
            main_list.append(sub_list.copy())
            return 

        sub_list.append(arr[i]) # Take current index for subsequence generation
        recur_subsequence(i+1)  # Left sub-tree

        sub_list.pop() # Dont take current index for subsequence generation
        
        # Look ahead and see next element is same as current, move pointer until value not same
        while i + 1 < n and arr[i] == arr[i + 1]:
            i += 1
        recur_subsequence(i+1)  # Right sub-tree
    
    # Call_recursive function for every index in arr
    arr.sort()
    recur_subsequence(0)
    return main_list 
    

