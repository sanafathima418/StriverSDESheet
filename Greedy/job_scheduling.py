def jobScheduling(jobs):
    
    # Time Complexity: O(NLOGN) + O(N*M)
    # Space Complexity: O(N)
    
    max_deadline = max(jobs,key=lambda x:x[0])
    time_jobs = [-1] * max_deadline[0]
    
    # 1. Sort jobs based on profit  
    jobs.sort(key = lambda x:x[1], reverse = True)
    
    # 2. Perform job on the last "available" day
    max_profit = 0
    # Process all jobs
    for j,job in enumerate(jobs):
        i = job[0]-1
        # For every job search from deadline to 0th interval to see if free
        while(i > -1):
            if(time_jobs[i] == -1):
                # Free interval found
                break
            i -= 1
        if i > -1:
            # If free interval found - i will be > -1(else would have reached 0 and decremented)
            time_jobs[i] = j  # dummy assignment to show interval taken
            max_profit += job[1] # Sum Profit
    
    return max_profit
