import heapq

# Time Complexity: O(n) to go over all elements + O(logk) for all heap operations + O(nk) to remove elements
# Space Complexity: O(n) for min and max heap

# This is my technique, as per leetcode solutions, there is another technique using lazy removal technique  
# which brings down complexity of removal step to O(1) - I find this v complicated

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap = []
        min_heap = []
        median_list = []
        i = 0 # To move window
        j = i # To expand window upto k
        
        while(j<len(nums)):
             # 1. Add: By Default add to max heap
            heapq.heappush(max_heap, nums[j]*-1) 

            # 1. Balance 1: To account for auto add to max heap in Step 1: Transfer from max heap to min heap  
            curr = heapq.heappop(max_heap)
            heapq.heappush(min_heap, curr*-1)     

            # 2. Balance 2: If min size more than max, Transfer from min heap to max heap  
            if len(min_heap) > len(max_heap):
                curr = heapq.heappop(min_heap)
                heapq.heappush(max_heap, curr*-1)
                
            j += 1 # Expand window
                        
            # 3. Find median of window
            if (j-i) == k:
                if len(max_heap) > len(min_heap):
                    median_list.append(max_heap[0]*-1)
                else:
                    median_list.append((max_heap[0]*-1 + min_heap[0]) / 2)
                
                # 4. Remove element at local start(i) from max or min heap
                if nums[i] <= max_heap[0]*-1:
                    max_heap.remove(nums[i]*-1)
                    heapq.heapify(max_heap)
                else:
                    min_heap.remove(nums[i])
                    heapq.heapify(min_heap)
                i += 1  # Time to move window
                
        return median_list
            
            
            
                