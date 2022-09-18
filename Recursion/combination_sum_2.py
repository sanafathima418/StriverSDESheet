# Time Complexity : O(2^N) 
# Space Complexity : O(N)
    
def combinationSum2(arr, n, target):
    main_list = []
    sub_list = []
    
    def recur_sum(i):
        if(i == len(arr) or arr[i] > target or sum(sub_list) >= target):
            # 1. Base Case: Increment i till it reaches n and subsequence so far
            # Reached Leaf Node 
            if sum(sub_list) == target:
                main_list.append(sub_list.copy())            
            return 

        # 2. Take current index for subsequence generation
        sub_list.append(arr[i])
        recur_sum(i+1)  # Left sub-tree

        # 3. Dont take current index for subsequence generation
        sub_list.pop()
        # Look ahead and see next element is same as current, move pointer until value not same
        while i + 1 < len(arr) and arr[i] == arr[i + 1]:
            i += 1
        recur_sum(i+1)  # Right sub-tree
    
    # Call_recursive function for every index in num
    arr.sort()
    recur_sum(0)
    return main_list 
    

 
    


