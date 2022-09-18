# Time Complexity : O(2^N) 
# Space Complexity : O(N)
    
 def findSubsetsThatSumToK(arr, n, k) :
    main_list = []
    sub_list = []
    
    def recur_sum(i):
        if(i == n):
            # 1. Base Case: Increment i till it reaches n and subsequence so far
            if sum(sub_list) == k:
                main_list.append(sub_list.copy())
            return 

        # Take current index for subsequence generation
        sub_list.append(arr[i])
        recur_sum(i+1)  # Left sub-tree

        # Dont take current index for subsequence generation
        sub_list.pop()
        recur_sum(i+1)  # Right sub-tree
    
    # Call_recursive function for every index in num
    recur_sum(0)
    return main_list 
    

