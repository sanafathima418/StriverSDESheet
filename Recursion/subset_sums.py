from typing import List

# Time Complexity : O(2^N) + O(NLOGN)
# Space Complexity : O(N)

def subsetSum(num: List[int]) -> List[int]:
    sub_sum = 0
    main_list = []
    
    def recur_sum(i):
        nonlocal sub_sum
        if(i == len(num)):
            # 1. Base Case: Increment i till it reaches n and append sum of subsequence so far
            # Reached Leaf Node
            main_list.append(sub_sum)
            return 

        # Take current index for sum calculation
        sub_sum += num[i]
        recur_sum(i+1)  # Left sub-tree

        # Dont take current index for sum calculation
        sub_sum -= num[i]
        recur_sum(i+1)  # Right sub-tree

    # Call_recursive function for every index in num
    recur_sum(0)
    main_list.sort() # Sort as per question
    return main_list
