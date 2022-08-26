    # Time Complexity : O(2^N) 
    # Space Complexity : O(N)
    
def recur_sum(i, num, subset_list, sub_list, val):
    if(i == len(num)):
        # 1. Base Case: Increment i till it reaches n and subsequence so far
        if sum(sub_list) == val:
            subset_list.append(sub_list.copy())
        return 

    # Take current index for subsequence generation
    sub_list.append(num[i])
    recur_sum(i+1, num, subset_list, sub_list, val)  # Left sub-tree
        
    # Dont take current index for subsequence generation
    sub_list.pop()
    recur_sum(i+1, num, subset_list, sub_list, val)  # Right sub-tree
  
def findSubsetsThatSumToK(arr, n, k):
    
    # Call_recursive function for every index in num
    subset_list = []
    recur_sum(0, arr, subset_list, [], k)

    return subset_list 
    

