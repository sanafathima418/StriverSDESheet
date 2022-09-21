from os import *
from sys import *
from collections import *
from math import *

# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getLeftView(root)->list:
# Approach: Use level order traversal and for every level, pop the leftmost(1st node) and append to traversal list and push children.
# For all other nodes of the level only pop and push children

# Time Complexity: O(N) for traversing all nodes of tree
# Space Complexity: O(N) for Queue

    traversal = []
    queue = [root]
    
    def BFS_traversal():
        while(queue):
            # Get length of queue that denotes number of nodes at current level
            curr_len = len(queue)
            # Pop leftmost node and append to traversal list
            curr_node = queue.pop(0)
            traversal.append(curr_node.data)
            # Push child nodes of popped node
            if curr_node.left: 
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
            curr_len -= 1
            # For all other nodes at current level, pop and append children until queue is empty (But DO NOT append to traversal list)
            while(curr_len):
                node = queue.pop(0)
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
                curr_len -= 1
            
    if root:        
        BFS_traversal()
    return traversal