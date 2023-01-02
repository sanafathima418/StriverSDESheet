class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Approach 1: Using 2 arrays and sorting them
        # TC: O(NLOGN) for traversing and sorting
        # SC: O(N+N) for storing start and end times

        start_times = [time[0] for time in intervals]
        end_times = [time[1] for time in intervals]

        start_times.sort()
        end_times.sort()

        j = 0
        min_rooms = 0

        # 1. Traverse over start times
        for i in range(len(start_times)):
            # 2. If start time is lesser then increment min rooms
            if start_times[i] < end_times[j]:
                min_rooms += 1
            else:
                # 3. If end time is lesser then check next end time with the next start
                j += 1
        
        return min_rooms

        # Approach 2: Using minheap for end time
        # Use heap to get min end time as we traverse over array
        # if current start is greater than min end in heap then meeting ended so pop
        # push current end to minheap
        # TC: O(NLOGN) for traversing, heapify and sort
        # SC: O(N) for storing end times
        import heapq
        minheap = []
        intervals.sort() # wont work without sort

        # 1. Traverse over start times
        for i in range(len(intervals)):
            # 2. If start time is greater or equal, pop end time to heap
            if minheap and intervals[i][0] >= minheap[0]:
                heapq.heappop(minheap)
            # 3. Push current end time to heapq for later use
            heapq.heappush(minheap, intervals[i][1])
        
        # 4. The end times left in the heap after processing all starts is the number of rooms needed
        return len(minheap)

        # Apporach 3: Can also be done using fast and slow pointer- same as min platforms
