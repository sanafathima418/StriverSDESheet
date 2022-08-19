def maximumMeetings(start, end):
    
    # Time Complexity: O(N) + O(NLOGN) + O(N)
    # Space Complexity: O(N)
    
    tuple_list = []
    # 1. Create tuple list with (start_time, end_time, meeting_no)
    for i in range(len(start)):
        tuple_item = (start[i],end[i],i+1)
        tuple_list.append(tuple_item)
    
    # 2. Sort list of tuples by end_time
    tuple_list.sort(key = lambda x: x[1])
    
    # 3. Traverse to find meetings to organize
    curr_end = tuple_list[0][1]
    org_meets = [tuple_list[0][2]]
    for i in range(1,len(tuple_list)):
        if tuple_list[i][0] > curr_end:
            org_meets.append(tuple_list[i][2])
            curr_end = tuple_list[i][1]
    
    return org_meets
