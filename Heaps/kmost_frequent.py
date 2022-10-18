import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Time Complexity: O(n) for traversing over input array + O(logn) for heap operations (heappop)
        # Space Complexity: O(n) for min heap
        
        # 1. Calculate frequencies of all elements
        freq_map = {}
        for ele in nums:
            if ele in freq_map:
                freq_map[ele] += 1
            else:
                freq_map[ele] = 1
                
        # 2. Construct max heap of tuple: (occurance,element) so we can pop from it k times based on occurance
        # Occurance is first element of tuple so heap auto sorts based on that instead the element
        max_heap = [(v*-1, k) for k, v in freq_map.items()]
        heapq.heapify(max_heap)
            
        # 3. HeapPop k times to get k most frequent (similar to functionality of heapq.nlargest)
        kfreq_list = []
        for _ in range(k):
            kfreq_list.append(heapq.heappop(max_heap)[1])
        
        return kfreq_list
        
                
                