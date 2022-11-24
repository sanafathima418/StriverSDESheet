from os import *
from sys import *
from collections import *
from math import *

# Approach: Pop unsorted, Sort, Push back
# TC: O(N^2)
# SC: O(N)
        
def sortStack(stack):
    
    def sortInsert(stack, element):
        if not stack or stack[-1] < element:
            # Base Case: If nothing on stack or top is lesser than element, append
            stack.append(element)
        else:
            # Remove from top and recurse
            popped_ele = stack.pop()
            sortInsert(stack, element)

            # Put back element
            stack.append(popped_ele)
    
    if stack:
        # Pop element one by one and sort remaining elements
        popped_ele = stack.pop()
        sortStack(stack)
        
        # Push the popped element back into sorted stack
        sortInsert(stack, popped_ele)
    return stack