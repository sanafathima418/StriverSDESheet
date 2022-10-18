import heapq

# Time Complexity: O(log n) to heapify and pop + O(k) for getting largest element
# Space Complexity: O(1) as all in place operations

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert to max heap
        nums = [i*-1 for i in nums] 
        # Convert to heap
        heapq.heapify(nums)
        min_ele = nums[0]
        # Get k largest element
        for _ in range(k):
            # keep popping until k is reached
            min_ele = heapq.heappop(nums)
        # mutliply min_ele with -1 to return original kth largest element
        return min_ele * -1