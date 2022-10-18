import heapq

# Standard Technique

# Time Complexity: O(logn) for all heap operations + O(1) for getting median
# Space Complexity: O(n) for min and max heap

class MedianFinder:
    # Intuition: Max Heap is 1 more than Min Heap Size

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        
    def addNum(self, num: int) -> None:
        # 1. By Default add to max heap
        heapq.heappush(self.max_heap, -num) 
        
        # 1. Balance 1: To account for auto add to max heap in Step 1: Transfer from max heap to min heap  
        curr = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, curr*-1)     
        
        # 2. Balance 2: If min size more than max, Transfer from min heap to max heap  
        if len(self.min_heap) > len(self.max_heap):
            curr = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, curr*-1)
        
        
    def findMedian(self) -> float:
        # 3. Find median as usual
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]*-1
        else:
            return (self.max_heap[0]*-1 + self.min_heap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# Non Standard Technique
# Time Complexity: O(logn) for all heap operations + O(1) for getting median
# Space Complexity: O(n) for min and max heap

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        
    def addNum(self, num: int) -> None:
        # Intuition: Max Heap size >= Min Heap Size
        
        # 1. Add to Max Heap: If first element ever or num < top of max heap
        # 2. Else add to Min Heap
        if (not self.max_heap) or (num < (self.max_heap[0]*-1)):
            heapq.heappush(self.max_heap, num*-1) 
        else:
            heapq.heappush(self.min_heap, num)     
        
        # 3. If Min heap is greater then move from min to max
        if len(self.min_heap) > len(self.max_heap):
            curr = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, curr*-1)
        elif (len(self.max_heap) - len(self.min_heap)) > 1:
            # 4. If max heap size is 1 greater than min heap size as per intuition, 
            # Move from max to min
            curr = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, curr*-1)
        
        
    def findMedian(self) -> float:
        # Calculate median (Only Max heap can have more elements of the two so if odd median is available there)
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]*-1
        else:
            # Means equal number of elements on both so fetch top from each
            return (self.max_heap[0]*-1 + self.min_heap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()