from typing import List

# Time Complexity : O(2^N) + O(NLOGN)
# Space Complexity : O(N)

def recur_sum(i, sub_sum, num, sum_list):
    if(i == len(num)):
        # 1. Base Case: Increment i till it reaches n and append sum of subsequence so far
        # Reached Leaf Node
        sum_list.append(sub_sum)
        return 
    
    # Take current index for sum calculation
    sub_sum += num[i]
    recur_sum(i+1, sub_sum, num, sum_list)  # Left sub-tree
        
    # Dont take current index for sum calculation
    sub_sum -= num[i]
    recur_sum(i+1, sub_sum, num, sum_list)  # Roght sub-tree

def subsetSum(num: List[int]) -> List[int]:
    
    # Call_recursive function for every index in num
    sum_list = []
    recur_sum(0, 0, num, sum_list)
    
    # Sort as per question
    sum_list.sort()
    return sum_list
