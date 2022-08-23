def maximumValue(items, n, w):

	# Time Complexity: O(NLOGN) +O(N)
    # Space Complexity: O(1)
    
    #[weight,value]
    curr_w = w
    max_value = 0
    
   # 1. Sort based on val/wt
    items.sort(key = lambda x: x[1]/x[0], reverse = True)
    
    # 2. Calculate max value for knapsack
    for item in items:
        if(item[0] > curr_w):
            # Max Weight almost reached, hence partial addition
            max_value += ((curr_w * item[1])/item[0])
            break
        # Sufficient to accommodate whole item
        curr_w -= item[0]
        max_value += item[1]
        
    return max_value
    
    
