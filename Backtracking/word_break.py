def wordBreak(arr, n, target):
    
    # With Backtracking we get TLE for some test cases - To be redone using DP
    # Time Complexity: O(4^N) - 4 possibilities for every word in dict
    # Space Complexity: O(N) for sub list
    
    sub_list = []
    
    def backtrack(j):
        
        nonlocal sub_list
        new_str = ''.join(sub_list)
        if len(new_str) >= len(target):           
            if new_str == target:
                return 1
            else:
                return 0
        
        for i in range(n):
            sub_list.append(arr[i])
            if backtrack(j+1):
                return 1
            sub_list.pop()
        return 0
            
    return backtrack(0)
    
            
    
        
            
