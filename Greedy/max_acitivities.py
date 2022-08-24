def maximumActivities(start, finish):
    
    # 1. Create list of tuples of (start,finish) to process together
    activity_times = []
    for i in range(len(start)):
        activity_times.append((start[i],finish[i]))
    
    # 2. Sort based on finish time in asc order
    activity_times.sort(key = lambda x:x[1])
    
    # 3. Process activities one by one
    max_activities = 1
    curr_end = activity_times[0][1]
    for i in range(1,len(activity_times)):
        if activity_times[i][0] >= curr_end:
            max_activities += 1
            curr_end = activity_times[i][1]
            
    return max_activities
    
