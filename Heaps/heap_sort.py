from os import *
from sys import *
from collections import *
from math import *
import heapq

# Time Complexity: O(nlogn) to go over elements and do heap operations
# Space Compelxity: O(n) for heap

# Min Heap: Sorts in decreasing order
# Max Heap: Sorts in increasing order

def heapSort(arr, n):
    
    min_heap = []
    
    def swap(i,j):
        tmp = min_heap[i]
        min_heap[i] = min_heap[j]
        min_heap[j] = tmp
    
    def heapify(i):
       # Push Up: If the element at pointer i is more than parent, swap and heapify on parent pointer
       if i > 0 and min_heap[i] < min_heap[(i-1)//2]:
            swap(i, (i-1)//2) 
            heapify((i-1)//2)
            
    def bubble_down(m): 
        # Push down: If element at i is greater than children, bubble down (always choose the path along smaller child to swap)
        # If children exist loop
        i = 0
        idx = (2*i) + 1
        # Left child exists take care by loop
        while(idx < m):
            # If right child exists, check which is it is smaller and reassign idx
            if idx + 1 < m and min_heap[idx+1] < min_heap[idx]:
                idx += 1
            # If parent is smaller than child, swap
            if min_heap[i] > min_heap[idx]:
                swap(i,idx)
            # Update indices
            i = idx
            idx = (2*i) + 1
    
    # 1. Transform into max heap
    for i in range(n):
        min_heap.append(arr[i])
        heapify(i)
    
    # 2. In place sort: Remove from heap and store in end
    for i in range(n-1,-1,-1):
        min_ele = min_heap[0]
        swap(0,i)
        bubble_down(i)
        
    return min_heap[::-1] 
    