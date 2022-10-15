from os import *
from sys import *
from collections import *
from math import *

def minHeap(N: int, Q: [[]]) -> []:
    heap = []
    return_list = []
    
    def swap(i,j):
        tmp = heap[i]
        heap[i] = heap[j]
        heap[j] = tmp
    
    def heapify(i):
        # Push Up: If the element at pointer i is less than parent, swap and heapify on parent pointer
        if i > 0 and heap[i] < heap[(i-1)//2]:
            swap(i,(i-1)//2)
            heapify((i-1)//2)
        
    def insert(item):
        # Nothing to do here, just append to end of array 
        # As max heap(multiply -1) to work like min heap
        heap.append(item * -1)
        heapify(len(heap)-1) 
    
    def bubble_down(): 
        # Push down: If element at i is greater than children, bubble down (always choose the path along smaller child to swap)
        # If children exist loop
        i = 0
        idx = (2*i) + 1
        # Left child exists take care by loop
        while(idx < len(heap)):
            # If right child exists, check which is it is smaller and reassign idx
            if idx + 1 < len(heap) and heap[idx+1] < heap[idx]:
                idx += 1
            # If parent is greater than child, swap
            if heap[i] > heap[idx]:
                swap(i,idx)
            # Update indices
            i = idx
            idx = (2*i) + 1

    def extract_min():
        # Get min element
        min_ele = heap[0]
        swap(0,-1)
        heap.pop()
        # Call bubble down
        bubble_down()
        return min_ele
    
    for inner_list in Q:
        if inner_list[0] == 0:
            insert(inner_list[1])
        else:
            # As max heap, multiply min element by -1 to render original element
            return_list.append(extract_min() * -1) 
                                          
    return return_list
            

