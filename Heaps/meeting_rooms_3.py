class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        # Approach: Using 2 minheaps
        # Heap1: To get min end time as we traverse over array
        # Heap2: To store available rooms
        # TC: O(NLOGN) for traversing, heapify and sort
        # SC: O(N) for heaps and room count
        
        import heapq
        minheap1 = []
        minheap2 = [i for i in range(n)]
        heapq.heapify(minheap2)
        
        meetings.sort() # sorted by start time
        rooms = [0] * n 

        # 1. Traverse over meeting time
        for i in range(len(meetings)):
            # 2. Pop meetings that have ended before current start time and update available rooms
            while(minheap1 and meetings[i][0] >= minheap1[0][0]):
                _, free_room  = heapq.heappop(minheap1)
                heapq.heappush(minheap2, free_room)
                    
            # 3.If available rooms get lowest available and assign same time as delay
            if minheap2:
                free_room  = heapq.heappop(minheap2)
                delay = meetings[i][0]
            else:
                # 4. Pop top from end time heap and update delay of this meeting with popped end time
                # Use soonest ending meeting here 
                delay, free_room = heapq.heappop(minheap1)
                
            # 5. Push current meeting end time and room assigned
            heapq.heappush(minheap1, (delay + meetings[i][1] - meetings[i][0], free_room))
            rooms[free_room] += 1
            
        
        # 4. Get lowest index of max occupied rooms 
        return rooms.index(max(rooms))