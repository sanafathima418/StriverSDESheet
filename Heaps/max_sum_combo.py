# from os import *
# from sys import *
# from collections import *
# from math import *
# import heapq

# def kMaxSumCombination(a, b, n, k):

#     # Brute Force: Find all sum combos and get k largest
#     # Time Complexity: O(N^2) + O(LOGN)
#     # Space Complexity: O(N)

#     heap_list = []
    
#     for i in range(len(a)):
#         for j in range(len(b)):
#             heap_list.append(a[i] + b[j])
    
#     return heapq.nlargest(k, heap_list)

#     # Optimized: Reduce search space
#     # Time Complexity: O(NLOGN)
#     # Space Complexity: O(N)

from os import *
from sys import *
from collections import *
from math import *
import heapq

# Time Complexity: O(nlogn) - to sort + O(klogn) heapify and traverse over k times
# Space Compexity: O(N) for heap,visited_array and return list of k max sums

def kMaxSumCombination(a, b, n, k):
    # 1. Sort both arrays
    a.sort(reverse = True)
    b.sort(reverse = True)
    
    max_heap = []
    visited_arr = []
    sum_list = []
    
    # 2. Initialization: Push first element sums into heap and indices into visited array
    heapq.heappush(max_heap,((a[0]+b[0])*-1,(0,0)))
    visited_arr.append((0,0))
    
    # 3. Find k sums
    for _ in range(k):
        # 4. Pop element from heap
        curr_element = heapq.heappop(max_heap)
        sum_list.append(curr_element[0] * -1)  # Store in sum_list
        i, j = curr_element[1]
        
        if i+1 < n and j+1 < n:
            if not (i+1,j) in visited_arr:
                # 5. Push a[i+1]+b[j] if not visited
                heapq.heappush(max_heap,((a[i+1]+b[j])*-1,(i+1,j)))
                visited_arr.append((i+1,j))
            if not (i,j+1) in visited_arr:
                # 6. Push a[i]+b[j+1] if not visited
                heapq.heappush(max_heap,((a[i]+b[j+1])*-1,(i,j+1)))
                visited_arr.append((i,j+1))
        
    return sum_list
        
        
        