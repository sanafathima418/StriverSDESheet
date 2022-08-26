    # Time Complexity : O(2^N) 
    # Space Complexity : O(N)
    
def recur_sum(i, num, subset_list, sub_list, val):
    if(i == len(num) or num[i] > val or sum(sub_list) >= val):
        # 1. Base Case: Increment i till it reaches n and subsequence so far
        # Reached Leaf Node 
        if sum(sub_list) == val:
            subset_list.append(sub_list.copy())            
        return 
    
    # 2. Take current index for subsequence generation
    sub_list.append(num[i])
    recur_sum(i+1, num, subset_list, sub_list, val)  # Left sub-tree
        
    # 3. Dont take current index for subsequence generation
    sub_list.pop()
    # Look ahead and see next element is same as current, move pointer until value not same
    while i + 1 < len(num) and num[i] == num[i + 1]:
        i += 1
    recur_sum(i+1, num, subset_list, sub_list, val)  # Right sub-tree
  
def combinationSum2(arr, n, target):
    
    # Call_recursive function for every index in num
    subset_list = []
    arr.sort()
    recur_sum(0, arr, subset_list, [], target)

    return subset_list 
    


