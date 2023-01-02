# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Approach: Use 1 minheap
        # TC: O(NLOGK) where n is the number of nodes and k is the number of lists
        # SC: O(N) for linkedlist and heap
        
        min_heap = []  # Min Heap
        head = curr = ListNode()  # New list: head points to start, curr to traverse over new list
        
        # 1. Initialization of min heap with first elements of all lists
        for i,list_head in enumerate(lists):
            if list_head:
                # Push value and list number
                heapq.heappush(min_heap,(list_head.val,i))
            
        # Add subsequent elements and build sorted linkedlist
        while(min_heap):
            # 2. Pop min element which is at top and add to sorted list along with the list it belongs to
            val, i = heapq.heappop(min_heap)
            
            curr.next = ListNode(val)  # Create new node and attach to curr
            curr = curr.next # Move pointer forward
            
            # 3. Add next elements after popped element into heap
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(min_heap,(lists[i].val, i))
                          
        return head.next
            
            
            
        